import json
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from webapp.models import Ad
from .permissions import IsModeratorPermission


class ModerationView(APIView):
    def get_permissions(self):
        return [IsModeratorPermission()]

    def put(self, request, *args, **kwargs):
        if request.body:
            data = json.loads(request.body)
            ad = get_object_or_404(Ad, pk=kwargs.get('pk'))
            if data['action'] == 'approve':
                ad.status = 2
            elif data['action'] == 'reject':
                ad.status = 3
            ad.save()
            return Response({'id': ad.id, 'published_at': ad.published_at, 'status': ad.status}, status=201)
        else:
            return Response({'error': 'No correct data'}, status=400)

