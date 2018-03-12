from rest_framework import serializers

from contacts.models import Contact


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'mobile', 'age', 'bio', 'created_at', 'updated_at')
