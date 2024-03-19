import datetime
import time 
from plyer import notification

def notif():
    while True:
        notification.notify(
            title = "To Do List {}".format(datetime.date.today()),
            app_name = "My App",
            message = "1. Make and integrate python project\n2. Create a Three tier project\n3. Create a CI/CD pipeline project.",
            app_icon = "notify.ico",
            timeout = 5
        )
        time.sleep(10)