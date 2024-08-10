from rest_framework.permissions import BasePermission


class IsModeratorPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user.has_perm('webapp.see_no_moderate_ads'):
            return False
        return True
