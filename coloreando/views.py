from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from form import LoginForm
from models import Users


class LandingView(TemplateView):
    template_name = "landing.html"

    def get(self, request):
        return super(LandingView, self).get(request)

class CanvasView(TemplateView):
    template_name = "dashboard.html"

    def get(self, request):
        return super(CanvasView, self).get(request)        


class LoginView(TemplateView):

    login = LoginForm
    initial = {'key': 'value'}
    template_name = 'landing.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.login(request.POST)
        if form.is_valid():
            new_user = Users(form.cleaned_data['username'],
                             form.cleaned_data['color'])
            new_user.save()
            check_user = Users.objects.get(username__exact=new_user.username)
            if check_user is not None:
                return HttpResponseRedirect('/canvas')

        return render(request, self.template_name, {'form':form})