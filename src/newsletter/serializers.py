from rest_framework import serializers
from .models import Newsletter,ContactForm


class CreateNewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['email', 'interests', 'location']

    def create(self, validated_data):
        return Newsletter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.interests = validated_data.get('interests', instance.interests)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance



class CreateContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['contact_email','title', 'message', 'location']

    def create(self, validated_data):
        return ContactForm.objects.create(**validated_data)