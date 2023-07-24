from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from .models import ugol 

@receiver(post_save, sender=ugol)  # Replace YourModel with your actual model class
def on_new_entry(sender, instance, **kwargs):
    # Notify the group when a new entry is added
    from channels.layers import get_channel_layer
    data = ugol.objects.all().values('value', 'timestamp')
    graph_data = [
        {'value': entry['value'], 'timestamp': entry['timestamp']}
        for entry in data
    ]
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'graph_updates',
        {
            'type': 'send_update',
            'data': graph_data,  # You can send specific data related to the new entry here
        }
    )
