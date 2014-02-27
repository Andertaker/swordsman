

from django.contrib.auth.views import logout
from django.http import HttpResponse
from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register



@dajaxice_register(name='ajax_login')
def ajax_login(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    return simplejson.dumps({'message':'Hello World'})
    dajax = Dajax()
    result = 3 * 5
    dajax.assign('#result','value',str(result))
    return dajax.json()





def user_logout(request, next_page):
    return logout(request, next_page)
