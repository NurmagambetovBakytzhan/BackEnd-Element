from rest_framework import serializers
from . import models


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class VacancyModelSerializer(serializers.ModelSerializer):
    company = CompanyModelSerializer()

    class Meta:
        model = models.Vacancy
        fields = '__all__'
