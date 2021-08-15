from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='home_page'),
    path('post/create/', views.BlogCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='detail_page'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),

    path('', views.home_page, name='home_page'),
    # path('post/create/', views.create_post, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='detail_page'),
]