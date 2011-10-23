import sys
import vktrouw_search
reload(vktrouw_search)
e=vktrouw_search.searcher()
if len(sys.argv) > 1 :
  q = str(sys.argv[1])
else :
  q = 'morgen'     
print "e.query('" + q + "')"
e.query(q)
