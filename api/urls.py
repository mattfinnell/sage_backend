from django.urls import path
from api.example import ExampleDetailView, ExampleListView

urlpatterns = [
    path("examples/", ExampleListView.as_view()),
    path("examples/<int:pk>", ExampleDetailView.as_view()),
]
