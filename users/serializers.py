from django.contrib.auth.models import User, Group
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import exceptions, serializers

class CustomUserCreateSerializer(UserCreateSerializer):
    is_doctor = serializers.BooleanField(style={"input_type": "bool"}, write_only=True, default=False)


    class Meta(UserCreateSerializer.Meta):
        # model= User
        fields = (*UserCreateSerializer.Meta.fields, "is_doctor")

    def validate(self, attrs):
        is_doctor = attrs.pop("is_doctor")
        attrs = super().validate(attrs=attrs)
        
        attrs["is_doctor"] = is_doctor
        return attrs
        

    def create(self, validated_data):
        is_doctor = validated_data.pop("is_doctor")
        user = super().create(validated_data=validated_data)
        
        if is_doctor:
            user.groups.add(Group.objects.get(name="doctor"))
        else:
            user.groups.add(Group.objects.get(name="patient"))

        user.save()
        return user


