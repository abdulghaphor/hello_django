from django.urls import path
from . import views as _

app_name = 'cart'

urlpatterns = [
	# path('add/', _.Add.as_view(),name='add'),
	# path('delete/', _.Delete.as_view(),name='delete'),
	# path('edit/', _.Edit.as_view(),name='edit'),
	# path('list/', _.List.as_view(),name='list'),
	path('', _.CartHandler.as_view(),name='cart-handler'),
]
