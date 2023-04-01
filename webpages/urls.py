from django.urls import path
from .views import LandingPageView, HistoryView, LodgeOfficersView, ContactUsView, SuccessView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('history/', HistoryView.as_view(), name='history'),
    path('lodge-officers/', LodgeOfficersView.as_view(), name='lodge_officers'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('send_email/', ContactUsView.as_view(), name='send_email'),
    path('success/', SuccessView.as_view(), name='success'),
]