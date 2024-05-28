from rest_framework import serializers
from apps.contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ["id", "title", "first_name", "last_name", "phone_number", "email", "address", "date_created", "last_modified", "owner"]