import json

from channels.generic.websocket import AsyncWebsocketConsumer


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
