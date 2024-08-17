import json
from datetime import datetime
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from webapp.models import Ad, Comment
from .permissions import IsModeratorPermission
from .serializers import CommentModelSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ModerationView(APIView):
    permission_classes = [IsModeratorPermission]

    def put(self, request, *args, **kwargs):
        if request.body:
            ad = get_object_or_404(Ad, pk=kwargs.get('pk'))
            if ad.status == '1':
                data = json.loads(request.body)
                if data['action'] == 'approve':
                    ad.status = 2
                    ad.published_at = datetime.now()
                elif data['action'] == 'reject':
                    ad.status = 3
                ad.save()
                return Response({'id': ad.id, 'published_at': ad.published_at, 'status': ad.status}, status=201)
            else:
                return Response({'error': 'Object is not in moderation'}, status=400)
        else:
            return Response({'error': 'No correct data'}, status=400)


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    permission_classes = [IsAuthenticated]
