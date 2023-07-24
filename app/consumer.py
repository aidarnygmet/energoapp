import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add necessary authentication or permission checks here if required
        print("connection ok")
        await self.channel_layer.group_add('graph_updates', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Perform any necessary clean-up on disconnect
        await self.channel_layer.group_discard('graph_updates', self.channel_name)

    async def send_update(self, event):
        # This method receives real-time updates from the server
        # and sends them to the connected WebSocket clients
        data = event['data']
        for item in data:
            item['timestamp'] = item['timestamp'].isoformat()
        await self.send(json.dumps(data))

    