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

    if message.callback == "del":
        message.deleteMessage()

    if message.callback == "D4":
        random_number = random.randint(1, 4)
        message.sendMessage(text=f"На кубике выпало -  {random_number}")
        message.deleteMessage()

    if message.callback == "D6":
        random_number = random.randint(1, 6)
        message.sendMessage(text=f"На кубике выпало -  {random_number}")
        message.deleteMessage()

    if message.callback == "D8":
        random_number = random.randint(1, 8)
        message.sendMessage(text=f"На кубике выпало -  {random_number}")
        message.deleteMessage()

    if message.callback == "D10":
        random_number = random.randint(1, 10)
        message.sendMessage(text=f"На кубике выпало -  {random_number}")
        message.deleteMessage()

    if message.callback == "D12":
        random_number = random.randint(1, 12)
        message.sendMessage(text=f"На кубике выпало -  {random_number}")
        message.deleteMessage()

    if message.callback == "D16":
        random_number = random.randint(1, 16)
        message.sendMessage(text=f"На кубике выпало -  {random_number}")
        message.deleteMessage()

    if message.callback == "D20":
        random_number = random.randint(1, 20)

        if random_number == 1:
            text = "КРИТИЧЕСКИЙ ПРОВАЛ!"
        elif random_number == 20:
            text = "КРИТИЧЕСКИЙ  УСПЕХ!"
        else:
            text=f"На кубике выпало -  {random_number}"

        message.sendMessage(text=text)
        message.deleteMessage()

    return Response("ok", status=200)

