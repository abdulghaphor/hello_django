from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
	# path('add/', _.Add.as_view(),name='add'),
	# path('delete/', _.Delete.as_view(),name='delete'),
	# path('edit/', _.Edit.as_view(),name='edit'),
	# path('list/', _.List.as_view(),name='list'),
	path('', CartHandler.as_view(),name='handler'),
	path('checkout/', Checkout.as_view(),name='checkout'),
	path('history/', History.as_view(),name='history'),
]
