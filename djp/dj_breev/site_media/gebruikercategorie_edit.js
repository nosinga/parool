function gebruikercategorie_edit() {
  var item = $(this).parent();    
  var categorie = item.find(".categorie").attr("href");
  item.load(
    "/gebruikercategoriesave/?ajax&categorie=" + encodeURIComponent(categorie),
    null,
    function () {
      $("#save-form").submit(gebruikercategorie_save);
    }
  );
  return false;
}

$(document).ready(function () {
  $("ul.gebruikercategories .edit").click(gebruikercategorie_edit);
});

function gebruikercategorie_save() {
  var item = $(this).parent();
  var data = {
    categorie: item.find("#id_categorie").val(),
    volgorde: item.find("#id_volgorde").val(),
    aantal_artikelen: item.find("#id_aantal_artikelen").val()
  };
  $.post("/gebruikercategoriesave/?ajax", data , function (result) {
    if (result != "failure") {
      item.before($("li", result).get(0));
      item.remove();
      $("ul.gebruikercategories .edit").click(gebruikercategorie_edit);
    }
    else {
      alert("Valideren gebruikercategorie bij bewaren is niet gelukt.");
    }
  });
  return false;
}
