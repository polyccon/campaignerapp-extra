from rest_framework.serializers import ModelSerializer

from campaignerapi.models import Messages

class MessagesSerializer(ModelSerializer):
    class Meta:
        model = Messages
        fields = (
            "subject", "body", "user", "sending_datetime", "created_at",
            "updated_at"
        )