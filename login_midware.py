from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,render,HttpResponse,HttpResponseRedirect
class Login_test(MiddlewareMixin):
    def process_request(self,request):
        need_login = ['/app_login2/home/',]
        print(request.path,'path!!!!!!!1')
        islogin = request.session.get('islogin')
        if request.path in need_login:
            if islogin:
                print('ok')
            else:
                return HttpResponseRedirect('/app_login2/login/')

