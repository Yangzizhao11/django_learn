from django.urls import path
from . import views
from django.urls import path


app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('upload/image/', views.uploadView, name= 'upload_image'),
    path('image/list', views.ImageView.as_view(), name= 'image_list')
]