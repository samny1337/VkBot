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
upld('https://sun9-28.userapi.com/c858036/v85836209/110af0/V8KS6aV2c6E.jpg')
upld('https://sun9-37.userapi.com/c857332/v85732176/1ff/CHNynD--2r8.jpg')
upld('https://sun9-43.userapi.com/c855120/v85510375/195e3e/T_JQp8xSXx8.jpg')
upld('https://sun9-23.userapi.com/c854420/v85440642/191ce2/QgiHtcwdTto.jpg')
upld('https://sun9-71.userapi.com/c857024/v85702043/ec0c/9IFPu1XHxH0.jpg')
upld('https://sun9-65.userapi.com/c855724/v85574957/19017c/AAdmlNtOJwA.jpg')
upld('https://sun9-31.userapi.com/c204516/v20456219/1b92/45imcje9Hz0.jpg')
upld('https://sun9-2.userapi.com/c200520/v20052150/1b16/3Agi_QAzw10.jpg')
upld('https://sun9-10.userapi.com/c857416/v85746128/115182/wl4ekwvYAfQ.jpg')
upld('https://sun9-66.userapi.com/c854024/v85404833/1991bd/HOazTViq8XI.jpg')
upld('https://sun9-8.userapi.com/c855120/v85512471/198204/tz4vmAWwXSg.jpg')
upld('https://sun9-63.userapi.com/c857332/v85732354/3d0/1WbmRrl0fVQ.jpg')
upld('https://sun9-45.userapi.com/c204720/v20420375/3537/G7vqqhOX3JU.jpg')
upld('https://sun9-11.userapi.com/c206716/v20676562/2f97/EqAOxi7yO-Q.jpg')
upld('https://sun9-10.userapi.com/c854528/v85528365/19eda7/uEu6gMhk6QQ.jpg')
upld('https://sun9-18.userapi.com/c200620/v20020347/3ab3/dC_AcZeoB3g.jpg')


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
                elif a == 2:
                        send_message(session_api, peer_id=event.obj.peer_id, message='SomeText'.format(last_and_first_name), attachments=attachments[2])
                elif a == 3:
                        send_message(session_api, peer_id=event.obj.peer_id, message='SomeText'.format(last_and_first_name), attachments=attachments[3])
                elif a == 4:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0}, SomeText'.format(last_and_first_name), attachments=attachments[4])
                elif a == 5:
                        send_message(session_api, peer_id=event.obj.peer_id, message='SomeText'.format(last_and_first_name), attachments=attachments[5])
                elif a == 6:
                        send_message(session_api, peer_id=event.obj.peer_id, message='SomeText'.format(last_and_first_name), attachments=attachments[6])
                elif a == 7:
                        send_message(session_api, peer_id=event.obj.peer_id, message='SomeText'.format(last_and_first_name), attachments=attachments[7])
                elif a == 8:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[8])
                elif a == 9:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[9])
                elif a == 10:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[10])
                elif a == 11:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[11])
                elif a == 12:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[12])
                elif a == 13:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[13])
                elif a == 14:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[14])
                elif a == 15:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[15])
                elif a == 16:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[16])
                elif a == 17:
                        send_message(session_api, peer_id=event.obj.peer_id, message='{0},SomeText'.format(last_and_first_name), attachments=attachments[17])

            if event.obj.peer_id == event.obj.from_id:
                send_message(session_api, peer_id=event.obj.peer_id, message='Привет')
                print('-' * 2)

    finally:
        time.sleep(random.randint(600, 3600))






