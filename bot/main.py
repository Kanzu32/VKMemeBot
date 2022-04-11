import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
#from vk_api.longpoll import VkLongPoll, VkEventType
vk = vk_api.VkApi(token='623a4b6a77a64e9e4530bcc5373e5da45af8a68ff1211170714683f7cc241dfcca7293a12da194bc8b810')
longpollBot = VkBotLongPoll(vk, 212594479)
#longpollUser = VkLongPoll(vk)


def send(id, message):
    vk.method('messages.send', {'chat_id': id, 'message': message, 'random_id': random.getrandbits(64)})


for event in longpollBot.listen():
    vk.method('messages.send', {'chat_id': event.chat_id, 'message': 'Хуй!', 'random_id': random.getrandbits(64)})
    if event.type == VkBotEventType.MESSAGE_NEW:
        print(event)
        if event.from_chat:
            id = event.chat_id
            send(id, 'Хуй!')
