from . import views
from django.urls import path

urlpatterns= [
    path("", views.age_page, name = "age_html")
]