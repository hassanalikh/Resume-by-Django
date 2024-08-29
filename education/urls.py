from django.urls import path
from . import views
urlpatterns = [
    path('skills/', views.education, name='skils')
]
