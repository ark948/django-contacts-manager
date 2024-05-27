from rest_framework import serializers
from apps.contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id", 
            "title",
            "owner",
        )
        model = Contact