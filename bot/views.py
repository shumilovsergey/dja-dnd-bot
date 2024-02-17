from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import telegram_format
from .keyboards import keyboard_test
import random
import requests
import json
from server.const import TOKEN

@api_view(['POST'])
def getMessage(request):
    message = telegram_format(request.data)

    if message.error:
        # serializer = JSONSerializer.serialize(message)
        return Response("ok", status=200)
    
    if message.text:
        print("ok")
        # message.sendMessage(text="Бросить кубик:", keyboard=keyboard_test)
        # send()

    if message.callback == "del":
        message.deleteMessage()

    if message.callback == "d1":
        # message.deleteMessage()
        random_number = random.randint(1, 6)
        message.sendMessage(text=str(random_number), chat_id="-4156846227")




    return Response("ok", status=200)

def send():
    data = { 
        "chat_id": "-1002087646322",
        "text": "test",
        "reply_markup" : json.dumps(keyboard_test)
    }
    response = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data)
    return response