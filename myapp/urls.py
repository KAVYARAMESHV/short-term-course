from django.urls import path
from . import views



urlpatterns = [

    path('login/', views.login_page),
    path('login_post/', views.login_post),
    path('home/', views.home),

    path('add_course/', views.add_course),
    path('add_coursepost/', views.addcourse_post),
    path('view_course/', views.view_course),
    # path('courseview/<str:id>', views.courseactive),
    path('delete_course/<str:id>', views.deletecourse),
    path('edit_course/<str:id>', views.edit_course),
    path('edit_coursepost/', views.edit_coursepost),

    path('setinactive/<str:id>', views.courseactive),
    path('setactive/<str:id>', views.courseainctive),


    path('viewprofile/', views.viewprofile),
    path('changepswrd_post/', views.changepswrd_post),


    path('searchh/<str:a>', views.searchcourse),
    path('AjaxDelete/<str:id>', views.AjaxDelete),

    path('ajaxview/',views.jqry_dataview),
    path('demoviiew/',views.demoview),


    #################

]