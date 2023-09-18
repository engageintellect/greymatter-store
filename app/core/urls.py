from django.urls import path
from core.views import layout, store, signup, myaccount, edit_myaccount, about
from django.contrib.auth import views
from product.views import product


urlpatterns = [
	path('', layout, name='layout'),
	path('signup/', signup, name='signup'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
	path('myaccount/', myaccount, name='myaccount'),
	path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
	path('store/', store, name='store'),
	path('about/', about, name='about'),
	path('store/<slug:slug>/', product, name='product'),
]