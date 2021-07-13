from rest_framework import serializers
from measurements.models import Measurement, Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', 'latitude', 'longitude', 'created_at', 'updated_at')


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('value', 'project', 'created_at', 'updated_at')
