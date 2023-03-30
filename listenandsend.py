from pushbullet import Pushbullet
from datetime import datetime
from notificationprovider import *

import schedule
import constants
import logging
import config

class NotificationManager:
    def __init__(self):
        self.pb = Pushbullet(constants.API_KEY)
        self.past_notifs = set()
        self.logging_stdout = config.LOGGING_STDOUT
        self.logging_to_file = config.LOGGING_FILE is not None
        self.notification_provider = config.WINDOW_MANAGER.value
    
    def send(self, notification: Notification):
        self.pb.push_note(notification.title, notification.body)

    def search_and_send_notification(self):
        for notif in self.notification_provider.get_notifications():
            if notif in self.past_notifs:
                continue
            if notif.app_name not in config.APP_FILTER:
                continue
            self.past_notifs.add(notif)
            self.send(notif)
            if self.logging_stdout:
                print(notif)
            if self.logging_to_file:
                logging.info(notif)

notification_manager = NotificationManager()

schedule.every(1).seconds.do(notification_manager.search_and_send_notification)

if __name__ == "__main__":
    if config.LOGGING_FILE:
        logging.basicConfig(filename=config.LOGGING_FILE, encoding='utf-8', level=logging.DEBUG)
    while True:
        schedule.run_pending()