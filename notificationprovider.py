from winsdk.windows.ui.notifications.management import UserNotificationListener
from winsdk.windows.ui.notifications import NotificationKinds, KnownNotificationBindings
from notification import Notification

import asyncio

class _LinuxWindowManager(Enum):
    Gnome = GnomeNotificationProvider()
    I3 = I3NotificationProvider()

class WindowManager(Enum):
    Windows = WindowsNotificationProvider()
    Linux = _LinuxWindowManager

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
        native_notifications = [i.notification\
                                 .visual\
                                 .get_binding(KnownNotificationBindings.get_toast_generic())\
                                 .get_text_elements()
                                for i in asyncio.run(self.async_get_notif())]
        return [Notification(iter(n)) for n in native_notifications]

class GnomeNotificationProvider(INotificationProvider):
    def get_notifications(self) -> list[Notification]:
        # TODO implement code
        pass

class I3NotificationProvider(INotificationProvider):
    def get_notifications(self) -> list[Notification]:
        # TODO implement code
        pass
