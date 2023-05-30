from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('adminindex',views.adminindex,name='adminindex'),
    path('store',views.store,name='store'),
    path('contact',views.contact,name='contact'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addevent',views.addevent,name='addevent'),
    path('showevent',views.showevent,name='showevent'),
    path('editdetails/<int:pk>',views.editdetails,name='editdetails'),
    path('deletedetails/<int:pk>',views.deletedetails,name='deletedetails'),
    path('logout',views.logout,name='logout'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('signup',views.signup,name='signup'),
    path('login_user',views.login_user,name='login_user'),
    path('eventitem/<int:pk>/<int:k>/',views. eventitem,name='eventitem'),
    path('loadeventitems/<int:pk>',views.loadeventitems,name='loadeventitems'),
    path('details/<int:pk>/<int:k>/',views.details,name='details'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('showuser',views.showuser,name='showuser'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('eventitems',views.eventitems,name='eventitems'),
    path('deleteitem/<int:pk>',views.deleteitem,name='deleteitem')


]