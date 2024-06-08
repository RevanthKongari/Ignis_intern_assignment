
from django.urls import path
from . import views

urlpatterns = [
    path('start_scraping/', views.Start_Scraping.as_view(), name='start_scraping'),
    path('scraping_status/<str:job_id>/', views.Scraping_Status.as_view(), name='scraping_status'),
]
