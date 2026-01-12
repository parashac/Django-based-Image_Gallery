from gallery_app import views
from django.urls import path
urlpatterns =[
    path("",views.gallery,name="gallery"),
    path('upload/', views.upload_image, name='upload_image'),
    path('delete/<int:id>/', views.delete_image, name='delete_image'),
]