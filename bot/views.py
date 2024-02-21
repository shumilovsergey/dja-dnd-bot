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
    
    if message.text == "бросай" or message.text == "Бросай":

        message.sendMessage(text="Бросить кубик:", keyboard=keyboard_test)
        message.deleteMessage()
        # send()

    if message.callback == "del":
        message.deleteMessage()

    if message.callback == "d1":
        random_number = random.randint(1, 6)
        message.sendMessage(text=f"На кубике выпало -  {random_number}")
        message.deleteMessage()




    return Response("ok", status=200)

