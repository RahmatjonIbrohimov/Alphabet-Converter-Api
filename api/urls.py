from django.urls import pathfrom . import viewsurlpatterns = [    path('', views.home),    path('api/', views.HomeViews.as_view(), name='api'),    path('api/text/add/', views.AddTextView.as_view(), name='add-text'),    path('api/file/add/', views.AddFileView.as_view(), name='add-file'),]