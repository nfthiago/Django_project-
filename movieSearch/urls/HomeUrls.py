from django.urls import path 
from movieSearch.views.HomeView import home_view

#method path imported from path
urlpatterns = [
    #first parameter = string (url address), second parameter = calling method view
    path("", home_view),
]