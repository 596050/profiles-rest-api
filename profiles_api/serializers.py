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

# {
#         "id": 1,
#         "email": "phil_apple@gmail.co.fi",
#         "name": "Phil Apple",
#         "profile_image": "https://s3.amazonaws.com/uifaces/faces/twitter/sur4dye/128.jpg",
#         "phone": "07172837467",
#         "event_description": "I am hosting a boys night and would like pizza and beer",
#         "event_date": "2021-10-25",
#         "event_guest_count": 7,
#         "event_type": "Party",
#         "event_postcode": "WF9 3NY",
#         "event_address": "8 Park Estate",
#         "event_cancelled": false,
#         "event_budget": 300,
#         "event_dietary": null
#     },
#     {
#         "id": 2,
#         "email": "martyn_banana@gmail.co.fi",
#         "name": "Martyn Banana",
#         "profile_image": "https://s3.amazonaws.com/uifaces/faces/twitter/atariboy/128.jpg",
#         "phone": "07656462636",
#         "event_description": "For my wedding I would like to have something classy. Must be veggie.",
#         "event_date": "2021-02-17",
#         "event_guest_count": 300,
#         "event_type": "Wedding",
#         "event_postcode": "NG2 5FQ",
#         "event_address": "Rosebery Avenue",
#         "event_cancelled": false,
#         "event_budget": 5000,
#         "event_dietary": "vegetarian"
#     }


# steve_carrot@gmail.co.fi
# https: // s3.amazonaws.com/uifaces/faces/twitter/BillSKenney/128.jpg
# Steve Carrot
# 07263545162
# Office Christmas Party. Finger Foods. Drinks
# 05/12/2021
# 35
# Corporate
# E1 1EW
# 20-30 Whitechapel Rd
# TRUE
# 3000
# vegetarian, vegan, nut free,
