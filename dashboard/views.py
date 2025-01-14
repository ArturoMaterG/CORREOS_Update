from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,View, UpdateView
from newsletters.models import Newsletter
from newsletters.forms import NewsletterCreationForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
class DashboardHomeView(TemplateView):
    template_name="dashboard/index.html"

class NewslettersDashboardHomeView(View):
    
    def get(self, request, *args, **kwargs):
        newsletter=Newsletter.objects.all()
        context={
            'newsletters':newsletter
        }
        return render(request, 'dashboard/list.html', context)
    

class NewslettersCreatedViews(TemplateView):


    def get(self, request, *args, **kwargs):

        form=NewsletterCreationForm()
        context={
            'form':form

        }
        return render(request, 'dashboard/create.html', context)
    
    def post(self, request, *args, **kwargs):
        


        if request.method=="POST":

            form=NewsletterCreationForm(request.POST or None)
            if form.is_valid():

                instance=form.save()
                newsletter=Newsletter.objects.get(id=instance.id)

                if newsletter.status=="Published":

                    subject=newsletter.subject
                    body=newsletter.body
                    from_email=settings.EMAIL_HOST_USER

                    for email in newsletter.email.all():
                        send_mail(subject=subject, from_email=from_email, recipient_list=[email],message=body, fail_silently=True)

                return redirect('dashboard:list')

        context={
            
            'form':form

        }
        return render(request, 'dashboard/create.html', context)
    
    
class NewslettersDetailViews(View):
    def get(self, request, pk, *args, **kwargs):
        
        newsletter=get_object_or_404(Newsletter,pk=pk)
        
        context={
            'newsletter':newsletter
            
        }
        
        
        return render(request, 'dashboard/detail.html', context)
    
    
class NewslettersUpdateViews(UpdateView):

    model=Newsletter
    form_class=NewsletterCreationForm
    template_name='dashboard/update.html'
    success_url="dashboard/detail/2/"
    
    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)
        
        context.update({
            'view_type':'update'
        })
        return context
    
    
    
    def post(self, request, pk, *args, **kwargs):
        
        newsletter=get_object_or_404(Newsletter, pk=pk)

        if request.method=="POST":
            
            form=NewsletterCreationForm(request.POST or None)
            if form.is_valid():

                instance=form.save()
                newsletter=Newsletter.objects.get(id=instance.id)

                if newsletter.status=="Published":

                    subject=newsletter.subject
                    body=newsletter.body
                    from_email=settings.EMAIL_HOST_USER

                    for email in newsletter.email.all():
                        send_mail(subject=subject, from_email=from_email, recipient_list=[email],message=body, fail_silently=True)

                return redirect('dashboard:detail',pk=newsletter.id)
            return redirect('dashboard:detail',pk=newsletter.id)
        else:
            form=NewsletterCreationForm(instance=newsletter)

        context={
            
            'form':form

        }
        return render(request, 'dashboard/update.html', context)
    

    