from django.urls import path
from .views import *
urlpatterns = [
    path('login/', login_view, name='login'),
    path('get-banner/',get_banner_view),
    path('get-about/',get_about_view),
    path('get-univs/',get_univs_view),
    path('get-facs/',get_facs_view),
    path('get-student/',get_student_view),
    path('get-comms/', get_comms_view),
    path('get-unidetails/', get_unidetails_view),
    path('get-profile/', get_profile_view),
    path('get-punivs/', get_punivs_view),
    path('get-assistent/', get_assistent_view),
    path('get-econtract/', get_econtract_view),
    path('get-statistics/', get_statistics_view),
    path('get-univcab/', get_univcab_view),
    path('search/', search, name='search'),
]
