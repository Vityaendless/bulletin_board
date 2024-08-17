from rest_framework.permissions import BasePermission, IsAuthenticated


class IsModeratorPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user.has_perm('webapp.see_no_moderate_ads'):
            return False
        return True


class IsAuthorPermission(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return request.method in ['DELETE'] and obj.author == request.user
