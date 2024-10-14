from django.urls import path
from .views import newletter_signup, newsletter_unsubscribe


app_name="newsletters"

urlpatterns = [
    path('entrenamiento/', newletter_signup, name='option'),
    path('unsubscribe/', newsletter_unsubscribe, name='unsubscribe'),
]


