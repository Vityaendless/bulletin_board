from rest_framework.permissions import IsAuthenticated


class IsModeratorPermission(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if not request.user.has_perm('webapp.see_no_moderate_ads'):
            return False
        return True
