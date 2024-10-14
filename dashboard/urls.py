from django.urls import path
from .views import DashboardHomeView,NewslettersDashboardHomeView, NewslettersCreatedViews, NewslettersDetailViews, NewslettersUpdateViews


app_name= "dashboard"

urlpatterns = [
    path('',DashboardHomeView.as_view(),name='home'),
    path('list/',NewslettersDashboardHomeView.as_view(),name='list'),
    path('create/',NewslettersCreatedViews.as_view(),name='create'),
    path('detail/<int:pk>',NewslettersDetailViews.as_view(),name='detail'),
    path('update/<int:pk>',NewslettersUpdateViews.as_view(),name='update'),
]
