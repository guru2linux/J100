from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


# Create your views here.
def landing_page(request):
    return render(request, 'webpages/landing_page.html')

def about_us(request):
    return render(request, 'webpages/about_us.html')

def lodge_officers(request):
    return render(request, 'webpages/lodge_officers.html')

def contact_us(request):
    form = ContactForm()
    return render(request, 'webpages/contact_us.html', {'form':form})

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Message from {} ({})'.format(name, email)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'dulcio.lee@gmail.com' 
            send_mail(subject, message, from_email, [to_email])
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'webpages/contact_us.html', {'form': form})

def success(request):
    return render(request, 'webpages/success.html')

    return redirect('landing_page')