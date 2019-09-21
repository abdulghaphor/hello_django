from django.urls import path
from . import views as _

app_name = 'products'

urlpatterns = [
	path('list/', _.List.as_view(),name='list'),
	path('details/<int:pk>/',_.Details.as_view(),name='detail')
]
