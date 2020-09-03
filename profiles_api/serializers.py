from rest_framework import serializers

from profiles_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'profile_image', 'phone', 'event_description', 'event_date',
                  'event_guest_count', 'event_type', 'event_postcode', 'event_address', 'event_cancelled', 'event_budget', 'event_dietary')
        # make password write only
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            profile_image=validated_data['profile_image'],
            phone=validated_data['phone'],
            event_description=validated_data['event_description'],
            event_date=validated_data['event_date'],
            event_guest_count=validated_data['event_guest_count'],
            event_type=validated_data['event_type'],
            event_postcode=validated_data['event_postcode'],
            event_address=validated_data['event_address'],
            event_cancelled=validated_data['event_cancelled'],
            event_budget=validated_data['event_budget'],
            event_dietary=validated_data['event_dietary']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeeItemSerializer(serializers.ModelSerializer):
    """Serializes a profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
