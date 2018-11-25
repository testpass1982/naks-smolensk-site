"""
File: message_tracker.py
Email: popov.anatoly@gmail.com
Description: message tracker will track all messages an send notifications via sms and email
"""
from abc import ABCMeta, abstractmethod
from .models import Message
from django.core.mail import send_mail
import time

class MessageTracker:
    """object to register messages and notify observers"""
    """this must be a singleton"""
    def __init__(self):
        self.messages = []
        self.observers = [EmailNotifyer('email_notifyer'), SMSNotifyer('sms_notifyer')]

    def check_messages(self):
        for message in Message.objects.all():
            if message.status == 0:
                self.messages.append(message)
                print(message, ' added to notify-list')
            else:
                print(message, ' has been already sent')
                # time.sleep(1)

    def register_observer(self, observer):
        if observer in self.observers:
            print(observer, ' already registered')
        else:
            self.observers.append(observer)
            print(observer, ' registered')

    def notify_observers(self):
        if len(self.messages)!=0:
            for observer in self.observers:
                print(observer, ' notify sending')
                try:
                    observer.notify(self.messages)
                except Exception as e:
                    print(type(e))
                    print(e.args)
                    print(e)


class MessageNotifyer:
    """object to make notifications"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self):
        pass

class EmailNotifyer(MessageNotifyer):
    """send emails"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def notify(self, messages):
        for message in messages:
            if message.typeof == 'Заявка':
                print(self.name, ' got a message ', message)
                self.send_email(message)
                message.status=2


    def send_email(self, message):   
            send_mail(
                'НАКС Смоленск: ваше сообщение получено',
                'Уважаемый {}, \
                информируем вас, что ваше сообщение получено \
                и передано в работу'.format(message.sender_email),
                'noreply@naks-smolensk.ru',
                ['{}'.format(message.sender_email)],
                fail_silently=False,
            )
            print(self.name, ' successfully sent ', message)

class SMSNotifyer(MessageNotifyer):
    """send sms"""
    def __init__(self, name):
        self.name = name

    def notify(self):
        print('I am not ready yet')

    def __str__(self):
        return self.name
