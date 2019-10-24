from rest_framework.permissions import BasePermission

class IsItemOwnerOrStaff(BasePermission):
	message = "You must be he owner or a staff member"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True
		else:
			return False