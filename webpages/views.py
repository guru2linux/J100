from django.views import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage


class LandingPageView(View):
    def get(self, request):
        return render(request, 'webpages/landing_page.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'webpages/about_us.html')


class LodgeOfficersView(View):
    def get(self, request):
        return render(request, 'webpages/lodge_officers.html')


class ContactUsView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'webpages/contact_us.html', {'form':form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Message from {} ({})'.format(name, email)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'dulcio.lee@gmail.com'
            send_mail(subject, message, from_email, [to_email])
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect('success')
        return render(request, 'webpages/contact_us.html', {'form': form})


class SuccessView(View):
    def get(self, request):
        return render(request, 'webpages/success.html')
    
    def post(self, request):
        return redirect('landing_page')