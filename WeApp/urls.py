from django.urls import path
from . import views

urlpatterns = [
    path("", views.WeApp, name='WeApp'),
    path("RSVP", views.RSVP, name="RSVP"),
    path("itenary", views.itenary, name="itenary"),
    path("FAQ", views.FAQ, name="FAQ"),
    path('save/', views.FAQ, name='save_data'),
    path('Travel', views.Travel, name='Travel'),

]