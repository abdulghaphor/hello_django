from django.urls import path
from . import views as _

app_name = 'accounts'

urlpatterns = [
	path('', _.Details.as_view(), name="details"),
	path('edit/', _.Edit.as_view(), name="edit"),
	path('delete/', _.Delete.as_view(),name="delete"),
	path('changepassword/', _.ChangePassword.as_view(),name="delete"),
	path('register/', _.Register.as_view(),name="register"),
	path('login/', _.Login.as_view(),name="login"),
	path('list/', _.List.as_view(),name="list"),
]