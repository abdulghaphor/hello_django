from django.urls import path
from . import views as _

urlpatterns = [
	path('create/', _.UserCreateAPIView.as_view()),
	path('edit/', _.UpdateUser.as_view()),
	path('users/', _.ViewUser.as_view()),
	path('login/', _.LoginUser.as_view()),	
]