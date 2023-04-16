from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/vacancies/<int:id>/', consumers.VacancyConsumer.as_asgi()),
    path('ws/vacancies/<int:id>/submit/', consumers.NotificationConsumer.as_asgi()),

]