from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="lista"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detalle"),
]