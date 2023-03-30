from pushbullet import Pushbullet
from datetime import datetime
from notificationprovider import *

import asyncio
import schedule
import constants
import platform
import logging
import config

if config.LOGGING_FILE:
    logging.basicConfig(filename=config.LOGGING_FILE, encoding='utf-8', level=logging.DEBUG)

class NotificationManager:
    def __init__(self, notification_provider: NotificationProvider = NotificationProvider()):
        self.pb = Pushbullet(constants.API_KEY)
        self.past_notifs = set()
        self.logging_stdout = config.LOGGING_STDOUT
        self.logging_to_file = config.LOGGING_FILE is not None
        self.notification = config.WINDOW_MANAGER
    
    def send(self, notification: Notification):
        self.pb.push_note(notification.title, notification.body)

    def search_and_send_notification(self):
        notifications = []
        for notif in notifications:
            if notif in self.past_notifs or i.app_info.display_info.display_name not in config.APP_FILTER:
                continue
            self.past_notifs.add(notif)
            self.send(notif)
            if self.logging_stdout:
                print(notif)
            if self.logging_to_file:
                logging.info(notif)

notification_manager = NotificationManager()

schedule.every(1).seconds.do(notification_manager.search_and_send_notification)

while True:
    schedule.run_pending()