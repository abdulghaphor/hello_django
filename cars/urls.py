from django.urls import path
from . import views as _

urlpatterns = [
	path('list/', _.CarList.as_view()),
]
