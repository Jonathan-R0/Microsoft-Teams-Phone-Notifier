from pushbullet import Pushbullet
from datetime import datetime
from notificationprovider import *

import schedule, constants, logging, config, sys, os

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

schedule.every(1).minute.do(lambda: sys.exit() if datetime.now().hour > constants.STOPPING_HOUR else None)

class ConfigurationException(Exception):
    pass

if __name__ == "__main__":
    if config.ONLY_WEEK_DAYS and datetime.today().weekday() > 4:
        # Where monday is 0 and sunday is 6.
        sys.exit()
    if not constants.MS_TEAMS_PATH:
        raise ConfigurationException("MS_TEAMS_VALUE must be a valid path to the executable!")
    os.startfile(constants.MS_TEAMS_PATH)
    if config.LOGGING_FILE:
        logging.basicConfig(filename=config.LOGGING_FILE, encoding='utf-8', level=logging.DEBUG)
    while True:
        schedule.run_pending()