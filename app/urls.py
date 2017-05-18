from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
   
#restaurant urls 
    	# url(r'^$', views.RestaurantIndexView.as_view(),name="restaurant-index"),
    	url(r'^$', login_required(views.RestaurantIndexView.as_view()) ,name="restaurant-index"),
		
		url(r'^add/$',views.RestaurantCreate.as_view(),name='restaurant-add'),
		
		
		url(r'^(?P<pk>[0-9]+)/$', views.RestaurantDetailView.as_view(),name="restaurant-detail"),

		url(r'^(?P<pk>[0-9]+)/delete/$', views.RestaurantDelete.as_view(),name="restaurant-delete"),

    	url(r'^(?P<pk>[0-9]+)/update/', views.RestaurantUpdate.as_view(),name="restaurant-update"),



# item urls
    	url(r'^item/$',login_required(views.ItemIndexView.as_view()) ,name="item-index"),
		
		url(r'^item/add/$',views.ItemCreate.as_view(),name='item-add'),
		
		
		url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(),name="item-detail"),

		url(r'^item/(?P<pk>[0-9]+)/delete/$', views.ItemDelete.as_view(),name="item-delete"),

    	url(r'^item/(?P<pk>[0-9]+)/update/', views.ItemUpdate.as_view(),name="item-update"),



    	 url(r'^register', views.UserFormView.as_view(),name="register"),
   		 url(r'^login/$', auth_views.login, name='login'),
  		 url(r'^logout/$', auth_views.logout, {'next_page': 'app:restaurant-index'}, name='logout'),

  		 url(r'^item_search', views.itemsearch,name="item_search"),
  		 
 
]