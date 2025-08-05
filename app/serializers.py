from rest_framework import serializers
from .models import (
    Announcement,
    Club,
    ClubMember,
    UnionMember,
    MediaGallery
)
from django.contrib.auth import authenticate

# Announcement Serializer
class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


# Club Serializer
class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


# Club Member Serializer
class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMember
        fields = '__all__'


# Union Member Serializer
class UnionMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnionMember
        fields = '__all__'


# Media Gallery Serializer
class MediaGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaGallery
        fields = '__all__'


class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user and user.is_active and user.is_superuser:
                data['user'] = user
            else:
                raise serializers.ValidationError("Invalid credentials or not an admin.")
        else:
            raise serializers.ValidationError("Both username and password are required.")
        return data