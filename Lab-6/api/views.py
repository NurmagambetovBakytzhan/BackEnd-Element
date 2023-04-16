from django.db.models import Max
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models, serializers


# Create your views here.
class CompanyViewSet(ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanyModelSerializer

    @action(detail=True, methods=['GET'], url_path='vacancies')
    def get_vacancies(self, request, *args, **kwargs):
        vacancies = models.Vacancy.objects.filter(company_id=kwargs['pk'])

        serializer = serializers.VacancyModelSerializer(vacancies, many=True).data
        return Response(serializer)


class VacancyViewSet(ModelViewSet):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancyModelSerializer

    @action(detail=False, methods=['GET'])
    def top_ten(self, request):
        top_ten = self.get_queryset().annotate(max_salary=Max('salary')).order_by('-max_salary')[:10]
        print(str(top_ten.query))
        print(top_ten)
        serializer = serializers.VacancyModelSerializer(top_ten, many=True).data
        return Response(serializer)
