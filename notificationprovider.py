from winsdk.windows.ui.notifications.management import UserNotificationListener
from winsdk.windows.ui.notifications import NotificationKinds, KnownNotificationBindings
from notification import Notification
from enum import Enum

import asyncio

class INotificationProvider:    
    def get_notifications(self) -> list[Notification]:
        """ Returns the list of notifications. """
        pass

class WindowsNotificationProvider(INotificationProvider):
    def __init__(self):
        self.listener = UserNotificationListener.get_current()

    async def async_get_notif(self):
        return await self.listener.get_notifications_async(NotificationKinds.TOAST)

    def get_notifications(self) -> list[Notification]:
        native_notifications = [(i.app_info.display_info.display_name, iter(
                                 i.notification\
                                  .visual\
                                  .get_binding(KnownNotificationBindings.get_toast_generic())\
                                  .get_text_elements()))
                                for i in asyncio.run(self.async_get_notif())]
        return [Notification(title, body) for title, body in native_notifications]

class GnomeNotificationProvider(INotificationProvider):
    def get_notifications(self) -> list[Notification]:
        # TODO implement code
        pass

class I3NotificationProvider(INotificationProvider):
    def get_notifications(self) -> list[Notification]:
        # TODO implement code
        pass
