from rest_framework import (
    mixins,
    viewsets,
)

from campaignerapi.models import Messages
from campaignerapi.serializers import MessagesSerializer


class MessagesViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,):

    serializer_class = MessagesSerializer
    queryset = Messages.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Create a comment for an episode
        """
        self.event = "CREATE_MESSAGES"
        return super().create(request, *args, **kwargs)