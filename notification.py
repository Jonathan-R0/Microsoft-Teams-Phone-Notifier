class Notification:
    def __init__(self, app_name, windows_notification):
        self.app_name = app_name
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
        return self.app_name == other.app_name and self.title == other.title and self.body == other.body

    def __hash__(self) -> int:
        return hash(self)

    def __str__(self) -> str:
        now = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        return '{' + f"timestamp: {now}, app_name: {self.app_name}, title: {self.title}, body: {self.body}" + '}'