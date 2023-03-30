from winsdk.windows.ui.notifications.management import UserNotificationListener
from winsdk.windows.ui.notifications import NotificationKinds, KnownNotificationBindings
from pushbullet import Pushbullet

import asyncio
import schedule
import constants

class Notification:
    def __init__(self, windows_notification):
        self.title = windows_notification.current.text
        self.body = ""
        while True:
            next(windows_notification, None)
            if windows_notification.has_current:
                self.body += windows_notification.current.text
            else:
                break 

    def __eq__(self, other) -> bool:
        if not isinstance(other, Notification):
            return False
        return self.title == other.title and self.body == other.body

    def __str__(self) -> str:
        return f"Title: {self.title}\nBody: {self.body}"

class NotificationManager:
    def __init__(self):
        self.pb = Pushbullet(constants.API_KEY)
        self.listener = UserNotificationListener.get_current()
        self.last_notif = None

    async def async_get_notif(self):
        return await self.listener.get_notifications_async(NotificationKinds.TOAST)
    
    def send(self, notification: Notification):
        self.pb.push_note(notification.title, notification.body)

    def search_and_send_notification(self):
        for i in asyncio.run(self.async_get_notif()):
            text_sequence = i.notification\
                             .visual\
                             .get_binding(KnownNotificationBindings.get_toast_generic())\
                             .get_text_elements()
            it = iter(text_sequence)
            notif = Notification(it)
            if (notif == self.last_notif):
                continue
            self.last_notif = notif
            self.send(notif)

notification_manager = NotificationManager()

schedule.every(1).seconds.do(notification_manager.search_and_send_notification)

while True:
    schedule.run_pending()