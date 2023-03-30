from notificationprovider import *

class _LinuxWindowManager(Enum):
    Gnome = GnomeNotificationProvider()
    I3 = I3NotificationProvider()

class WindowManager(Enum):
    Windows = WindowsNotificationProvider()
    Linux = _LinuxWindowManager