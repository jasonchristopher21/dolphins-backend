from api import views
from django.urls import path

urlpatterns = [
    path("parse", views.ParserView.as_view()),
]