import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.vacancy_id = self.scope['url_route']['kwargs']['id']
        self.room_group_name = f'vacancy_{self.vacancy_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def application_notification(self, event):
        message = event['message']

        await self.send(text_data=message)

class VacancyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.vacancy_id = str(self.scope['url_route']['kwargs']['id'])
        await self.channel_layer.group_add(
            self.vacancy_id, self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.vacancy_id, self.channel_name
        )

    async def send_notification(self, event: dict):
        await self.send(text_data=json.dumps(event))
