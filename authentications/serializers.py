""" DJango DRF Serializers """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from authentications.models import CustomUser


class UserGroupsSerializers(serializers.ModelSerializer):
    """Groups User Serializers"""

    class Meta:
        """Groups User Fields"""

        model = Group
        fields = ("id", "name")


class UserSigInUpSerializers(serializers.ModelSerializer):
    """Serializers"""
    avatar = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        allow_null=False,
        use_url=False,
        required=False,
    )
    username = serializers.CharField(
        max_length=255,
        min_length=5,
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            'email',
            "password",
            "avatar",
            "password2",
            "groups",
        ]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data['email'],
        )
        user.set_password(validated_data["password"])
        for i in validated_data.pop("groups"):
            user.groups.add(i)

        user.avatar = self.context.get("avatar")
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        if self.context.get("avatar") == None:
            instance.avatar = instance.avatar
        else:
            instance.avatar = self.context.get("avatar")
        instance.save()
        return instance


class UserSigInInSerializers(serializers.ModelSerializer):
    """Serializers"""

    username = serializers.CharField(max_length=50, min_length=2)
    password = serializers.CharField(max_length=50, min_length=1)

    class Meta:
        model = CustomUser
        fields = ["username", "password"]
        read_only_fields = ("username",)


class UserInformationSerializers(serializers.ModelSerializer):
    """User Profiles Serializers"""

    groups = UserGroupsSerializers(read_only=True, many=True)

    class Meta:
        """User Model Fileds"""

        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "groups"]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
