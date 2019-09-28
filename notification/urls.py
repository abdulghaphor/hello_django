from django.urls import path
from .views import *

app_name = 'notification'

urlpatterns = [
	path('', NotificationHandler.as_view(),name='handler'),
]
