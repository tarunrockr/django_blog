from django.urls import path 
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('add/', views.AddPost.as_view(), name='add_post'),
	path('edit/', views.EditPost.as_view(), name='edit_post'),
	path('edit/<int:id>/', views.EditPost.as_view(), name='edit_get'),
	path('show/<int:id>', views.show_post, name='show_post'),
]