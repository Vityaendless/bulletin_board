import json
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from webapp.models import Ad
from .permissions import IsModeratorPermission
from .serializers import AdSerializer


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ModerationView(APIView):
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
