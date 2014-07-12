from core.models import Report, Species, Photo
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail', read_only=True)

    class Meta:
        model = Photo
        fields = ('photo', 'thumbnail')


class SpeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = ('id', 'name', 'guid', 'occurrenceCount')


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    photos = PhotoSerializer(many=True, read_only=False, required=True)
    species = SpeciesSerializer(many=False, read_only=True)
    user = serializers.RelatedField(many=False)

    class Meta:
        model = Report
        fields = ('id', 'user', 'name', 'description', 'creationTime', 'photos')