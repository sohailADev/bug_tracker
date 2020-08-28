from django.urls import path
from bug_tracker_app import views

urlpatterns = [
    path('',views.index_view,name='home_page'),
    path('login/',views.login_view,name='login_page'),
    path('add_ticket/',views.add_ticket_view,name='add_ticket_page'),
    path('edit_ticket/<int:ticket_id>',views.edit_ticket_view,name='edit_ticket_page'),
    path('complete_ticket/<int:ticket_id>',views.complete_ticket_view,name='complete_ticket_page'),
    path('retunr_ticket/<int:ticket_id>',views.return_ticket_view,name='return_ticket_page'),
    path('assign_me/<int:ticket_id>',views.assign_me_view,name='assign_me_page'),
    path('invalid/<int:ticket_id>',views.invalid_ticket_view,name='invalid_ticket_page'),
    path('user/<str:user_name>',views.user_detail_view,name='user_detail_page'),
    path('ticket/<int:ticket_id>',views.ticket_detail_view,name='ticket_detail_page'),
    path('logout/',views.logout_view,name='logout_page'),
]
