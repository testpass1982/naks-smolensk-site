"""
File: message_tracker.py
Email: popov.anatoly@gmail.com
Description: message tracker will track all messages an send notifications via sms and email
"""
from .models import Message
class MessageTracker:
    """object to register messages and notify observers"""
    """this must be a singleton"""
    self.messages = []
    self.observers = []

    def check_messages(self):
        for message in Message.objects.all():
            if message.status == 1:
                self.messages.append(message)
    def notify_observers(self):
        if len(self.messages)!=0:
            for observer in self.observers:
                observer.notify()

class MessageNotifyer:
    """object to make notifications"""
    pass

class EmailNotifyer(MessageTracker):
    """send emails"""
    pass

class SMSNotifyer(MessageTracker):
    """send sms"""
    pass
