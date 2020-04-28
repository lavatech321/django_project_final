from django.urls import path
from . import views

urlpatterns = [
    path('page1/', views.page1 , name='page1'),
    path('page2/<teamname>', views.page2 , name='page2'),
    path('page3/<tname>', views.page3 , name='page3'),
    path('page4/<teamname>/<topic>', views.page4 , name='page4'),
    path('page5/team/<teamname>/topic/<topic>', views.page5 , name='page5'),

    path('signup/', views.signup , name='signup'),
    path('add_comment/<tname>/<topic>', views.add_comment , name='add_comment'),
]
