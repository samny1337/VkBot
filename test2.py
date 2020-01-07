from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import random
import requests
import time

vk_session = vk_api.VkApi(token='ID')
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 189496895)


def send_message(session_api, peer_id, message=None, attachments=None):
    session_api.messages.send(peer_id=peer_id, message=message, random_id=random.randint(-2147483648, +2147483648),
                              attachment=attachments)


attachments = []


def upld(image_ur):
    session = requests.Session()
    upload = VkUpload(vk_session)
    image_url = image_ur
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append(
        'photo{}_{}'.format(photo['owner_id'], photo['id'])
    )


upld('https://sun9-63.userapi.com/c854228/v85428309/19220d/vqgUCQo-KWM.jpg')
upld('https://sun9-47.userapi.com/c200628/v20062334/1dfd/I-mZ7bjxDos.jpg')



for event in longpoll.listen():
    try:
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.peer_id != event.obj.from_id:
                members_list = session_api.messages.getConversationMembers(peer_id=event.obj.peer_id, fields='profiles')['profiles']
                sender_name = list(filter(lambda name: name['id'] == event.obj.from_id, [name for name in
                                                                                         session_api.messages.getConversationMembers(
                                                                                             peer_id=event.obj.peer_id,
                                                                                             fields='profiles')[
                                                                                             'profiles']]))[0]
                last_and_first_name = str(sender_name['first_name']) + ' ' + str(sender_name['last_name'])

                collection = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
                a = random.choice(collection)

                if a == 0:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[0])
                elif a == 1:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[1])
                

            if event.obj.peer_id == event.obj.from_id:
                send_message(session_api, peer_id=event.obj.peer_id, message='Привет')
                print('-' * 2)

    finally:
        time.sleep(random.randint(600, 3600))






