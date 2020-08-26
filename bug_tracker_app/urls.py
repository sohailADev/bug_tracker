from django.urls import path
from bug_tracker_app import views

urlpatterns = [
    path('',views.index_view,name='home_page'),
    path('login/',views.login_view,name='login_page'),
]
