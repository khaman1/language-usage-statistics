from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import re

class PageRender:
    request     = 0
    context     = {}
    template_url= ''

    def __init__(self,request=0,template_url='',check_login=False):
        self.template_url       = template_url

        ## If required to login
        if check_login:
            if not self.is_authenticated():
                return JsonResponse('You need to log in!', safe=False)

        ##
        if request:         
            self.request        = request
            self.process_request()

    def mobile(request):
        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

        try:
            if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
                return True
            else:
                return False
        except:
            return False

    def is_authenticated(self):
        if not self.request.user.is_authenticated:
            False
        else:
            True

    def process_request(self):
        pass

    def exec(self):
        return self

    def render(self):
        return render(self.request, self.template_url, self.context)