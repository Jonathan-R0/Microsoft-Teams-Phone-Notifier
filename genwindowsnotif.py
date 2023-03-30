from win10toast import ToastNotifier
from datetime import datetime

toaster = ToastNotifier()
toaster.show_toast("Time", datetime.now().strftime("%H:%M:%S"), duration=5)

while toaster.notification_active(): 
    time.sleep(0.1)