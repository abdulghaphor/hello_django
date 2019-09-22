from django.urls import path
from . import views as _

app_name = 'payment'

urlpatterns = [
	path('successful/',_.Successful.as_view(),name='successful'),
	path('failed/',_.Failed.as_view(),name='failed'),
	path('',_.Generate.as_view(),name='generate'),
	# path('add/', _.Add.as_view(),name='add'),
	# path('delete/', _.Delete.as_view(),name='delete'),
	# path('edit/', _.Edit.as_view(),name='edit'),
	# path('list/', _.List.as_view(),name='list'),
	# path('', _.CartHandler.as_view(),name='cart-handler'),
]
