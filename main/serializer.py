from rest_framework import serializers
from .models import *

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class UniversitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = '__all__'


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class UniDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uni_Details
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class PUniversitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = P_Universities
        fields = '__all__'


class AssistentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistent
        fields = '__all__'

class EcontractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Econtract
        fields = '__all__'


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'


class UnivCabSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnivCab
        fields = '__all__'
