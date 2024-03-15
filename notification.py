import datetime
import time 
from plyer import notification

while True:
    notification.notify(
        title = "To Do List {}".format(datetime.date.today()),
        message = "1. Make and integrate python project\n2. Create a Three tier project\n3. Create a CI/CD pipeline project.",
        app_icon = "Notification app/notify.ico",
        timeout = 5
    )
    time.sleep(10)