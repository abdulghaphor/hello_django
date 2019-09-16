from rest_framework.permissions import BasePermission

class TestPerm(BasePermission):
	message = "Permission Denied."

	def object_has_permission(self, request, view,obj):
	# 	print("x",obj.email)
		if request.user.is_staff or (obj.email == request.user):

			return True
		else:
			print('hello',request.user)
			return True