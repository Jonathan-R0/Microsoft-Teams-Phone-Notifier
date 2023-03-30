# Microsoft Teams Phone Notifier

## Why?

Like many people I am forced to use Microsoft Teams at ... and for some fucking reason I am not allowed to log into my account with my phone to receive notifications.

## Requirements?

This project uses python3.

To use my script you first need the install all the libraries required, run:

```sh
pip install -r /path/to/requirements.txt
```

You also need to create a [PushBullet](www.pushbullet.com) account and download the app on your phone. After linking your phone to your main system go to settings and generate an access token. Add your secret token to the `constants.py` file. Finally, in the Microsoft Teams app open the *Notifications* tab under *Settings* and use "Windows" as your *Notification Style*.

## How?

To start the program run:

```sh
python listenandsend.py
```

And to generate windows notifications, which may come in handy for testing, run:

```sh
pythen genwindowsnotif.py
```

## CanIAddMyOwnNotificationProvider?

Yes. As you may have notice from reading the code, this program catches all the notifications available from the window manager. It is expected that Microsoft Teams notifications can be sent through the default os window manager. Meaning that if you want to add your own notification provider you need to create an enum case in `windowmanager.py` and create a class extending the notification provider interface in `notificationprovider.py`. You can then add your new notification type `config.py` file.