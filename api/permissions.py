from rest_framework.permissions import BasePermission

class IsStaffOrOwner(BasePermission):
	message = "Sir!! You are not the one who added this item; therefore TURN BACK!"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or obj.name == request.user:
			return True
		return False