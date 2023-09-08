from api import views
from django.urls import path

urlpatterns = [
    path("process", views.ProcessFilesView.as_view()),
]