from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.http import  HttpResponse, HttpResponseRedirect, Http404 
from django.template import  Context, RequestContext
from django.template.loader import  get_template
from django.contrib.auth import logout, authenticate
from django.contrib.auth.views  import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction
from breev.forms import *
from breev.models import *

from datetime import datetime

from utils_sql import *

##
##
## Utils voor loging en voting
##
def log_action(request,article):
  user        = request.user
  session_key = request.session.session_key
  now         = datetime.now()
  previous_action = list(LogAction.objects.filter(usr=user,session_key=session_key).exclude(art=article).order_by('id'))
  if previous_action :
     previous_action = previous_action[-1]
     log = LogAction.objects.get(id = previous_action.id )
     log.spent_time = (now - previous_action.last_action_time).seconds
     if log.spent_time > 300 :
        log.spent_time = 300
     log.save()

  current_action, created = LogAction.objects.get_or_create(
          usr=user
        , art=article
        , session_key = session_key
        , action = 'read'
        , defaults = {'last_action_time' : now}
        )
        
  current_action.last_action_time = now
  current_action.save()      
##
def vote_action(request, article, score_change) :
  user        = request.user
  new_score, created = Vote.objects.get_or_create(
          usr=user
        , art=article
        , defaults = { 'score' : 0 }
        )
  if new_score.score < 3 and new_score.score > -3 :     
     new_score.score = new_score.score + score_change
     
  if new_score.score == 3 and score_change == -1:
     new_score.score =  2

  if new_score.score == -3 and score_change == 1:
     new_score.score =  -2
        
  new_score.save()        
##
##

def main_page(request) :
  user = request.user
  if len(user.username) > 0 :
    ranked_articles = AukArtikelRankVw.objects.raw(
      get_sql('main_page','user_ranked_articles'),[user.username]
    )[:150]     
  else :
    ranked_articles = AukArtikelRankVw.objects.raw(
      get_sql('main_page','ranked_articles')
    )[:150]     
  for ranked_article in ranked_articles :
      sqlstatement = get_sql('main_page','krantnaam_bij_artikel')
      colnames, kranten = get_sqlrecordset_with_columnnames(sqlstatement,[ranked_article.artikel_id])
      krantnaam = ''
      for krant in kranten :
        krantnaam = krantnaam + ' | ' + krant['naam']
      krantnaam = krantnaam[1:]
      ranked_article.krant = krantnaam    
      
  variables = RequestContext(request, {
    'ranked_articles' : ranked_articles
  })
  return render_to_response(
   'main_page.html', variables)

def article_page(request,article_id) :
  article = get_object_or_404 (
    AukArtikel,
    id = article_id
  )
  if len(request.user.username) > 0 :
     log_action(request,article=article)
  variables = RequestContext(request, {
    'article' : article
  })
  return render_to_response('article_page.html', variables)


def article_vote_plus_page(request, article_id) :
  article = get_object_or_404 (
    AukArtikel,
    id = article_id
  )
  vote_action(request, article, 1)
  return article_page(request, article_id)

def article_vote_min_page(request, article_id) :
  article = get_object_or_404 (
    AukArtikel,
    id = article_id
  )
  vote_action(request, article, -1)
  return article_page(request, article_id)


def logout_page(request) :
  logout(request)
  return HttpResponseRedirect('/')
  
def register_page(request) :
  if request.method == 'POST' :
    form = RegistrationForm(request.POST)
    if form.is_valid() :
      user = User.objects.create_user(
        username = form.cleaned_data['username'],
        password = form.cleaned_data['password1'],
        email = form.cleaned_data['username']
        )
      # aanmaken default profile
      categories = Categorie.objects.all()
      for categorie in categories :
        GebruikerCategorie.objects.create(
          usr=user, cat=categorie, volgorde = categorie.volgorde, aantal_artikelen=5
        )
      return HttpResponseRedirect('/register/success/')
  else :
    form = RegistrationForm()
  variables = RequestContext(request, {
      'form' : form
      })
  return render_to_response(
      'registration/register.html',
      variables
      )
       
def user_preference_page(request, user_id) :
  user = get_object_or_404(User, id=user_id)

  if user.username == request.user.username :
    sqlstatement = get_sql('user_preference_page','gebruikercategories',)
    gebruikercategories_cn = get_sqlrecordset_with_columnnames(sqlstatement,[user.id])

    variables = RequestContext (request,{
     'gebruikercategories' : gebruikercategories_cn,
     'username' : user.username,
#     'show_tags' : True,
     'show_edit' : user.username == request.user.username,
      })
    return render_to_response('user_preferences_page.html',variables)
  else :
    return main_page(request)

def _gebruikerCategorie_save(request, form) :
  # create or get categorie
  categorie, dummy = Categorie.objects.get_or_create(
    naam = form.cleaned_data['categorie']
  )
  # create or get gebruikerCategorie
  gebruikerCategorie, created = GebruikerCategorie.objects.get_or_create(
    usr = request.user,
    cat = categorie
  )
  # Update gebruikerCategorie
  gebruikerCategorie.volgorde         = form.cleaned_data['volgorde']
  gebruikerCategorie.aantal_artikelen = form.cleaned_data['aantal_artikelen']
  gebruikerCategorie.save()
  # ugly hack, noodzakelijk vanwege gebruikercategories_cn gebruik
  gebruikerCategorie.categorie = categorie.naam
  return gebruikerCategorie

@login_required
@csrf_exempt
def gebruikerCategorie_save_page(request) :
  ajax = 'ajax' in request.GET
  if request.method == 'POST' :
    form = GebruikerCategorieSaveForm(request.POST)

    if form.is_valid() :
      gebruikerCategorie = _gebruikerCategorie_save(request, form)
      if ajax :
        variables = RequestContext(request, {
          'gebruikercategories' : [gebruikerCategorie] ,
          'show_edit' : True,
        })
        return render_to_response(
          'gebruikercategorie_list.html' , variables
        )
      else :
        return HttpResponseRedirect(
          '/instellingen/user/%s/' % request.user.username
        )      
    else :
     if ajax :
        return HttpResponse(u'failure') 
  elif 'categorie' in request.GET :
    categorienaam = request.GET['categorie']
    try :
      categorie = Categorie.objects.get(naam = categorienaam)
      gebruikerCategorie = GebruikerCategorie.objects.get(
        usr = request.user,
        cat = categorie
      )
      volgorde         = gebruikerCategorie.volgorde  
      aantal_artikelen = gebruikerCategorie.aantal_artikelen
    except ( GebruikerCategorie.DoesNotExist) :
      pass
    form = GebruikerCategorieSaveForm({
      'categorie' : categorie ,
      'volgorde'  : volgorde ,
      'aantal_artikelen' : aantal_artikelen ,  
      })

  else :
    form = GebruikerCategorieSaveForm()
  variables = RequestContext(request, {
    'form': form
  })
  if ajax :
    return render_to_response('gebruikercategorie_save_form.html', variables)
  else :
    return render_to_response('gebruikercategorie_save.html', variables)

def search_page(request) :
  form = SearchForm()
  ranked_articles = []
  show_results = False
  if 'query' in request.GET :
    show_results = True
    query = request.GET['query'].strip()
    if query :
      form = SearchForm({'query' : query })
      query = '%' + query.lower() + '%'
      ranked_articles = AukArtikelRankVw.objects.raw(
        get_sql('search_page','search_ranked_articles'),[query,query]
       )[:50]
      print len(ranked_articles)       
  variables = RequestContext(request, {
      'form' : form,
      'ranked_articles' : ranked_articles,
      'show_results' : True,
      'show_user' : True  
  })
  return render_to_response('search.html', variables)
