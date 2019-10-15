from basicApp import views
from django.urls import path


''' This app_name is used in html pages in href. Html page checks this app_name for the url.'''

app_name = 'basicApp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),

]
