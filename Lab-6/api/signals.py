from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.JobApplication)
def notify_application(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"vacancy_{instance.vacancy.id}",
            {"type": "application_notification", "message": "New application received"}
        )


@receiver(post_save, sender=models.Vacancy)
def send_notification(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        str(instance.id),
        {
            'type': 'send_notification',
            'company': instance.company
            # 'status': instance.status
        }
    )
