from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import Student_Model,Student_Form
from django.views.generic.base import RedirectView, TemplateView
from django.views import View
# from django.http import HttpRequestRedirect

# Create your views here.
class UserAddShowView(TemplateView):
    template_name = 'enroll/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        sf = Student_Form()        
        sm = Student_Model.objects.all()
        context = {
            'sf': sf,
            'sm': sm,
        }
        return context

    def post(self, request):
        sf = Student_Form(request.POST)
        if sf.is_valid():
            na = sf.cleaned_data['name']
            em = sf.cleaned_data['email']
            pw = sf.cleaned_data['password']
            sm_obj = Student_Model(name=na, email=em, password=pw)
            sm_obj.save()
            return HttpResponseRedirect('/')

class UserDeleteView(RedirectView):
    url = "/"
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Student_Model.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class UserUpdateView(View):
    def get(self, request, id):
        pi = Student_Model.objects.get(pk=id)
        sf = Student_Form(instance=pi)
        return render(request, "enroll/update.html",{'form':sf})

    def post(self, request, id):
        pi = Student_Model.objects.get(pk=id)
        sf = Student_Form(request.POST, instance=pi)
        if sf.is_valid():
            sf.save()
        return render(request, "enroll/update.html",{'form':sf})

