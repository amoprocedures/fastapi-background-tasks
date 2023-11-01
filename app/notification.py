from winotify import Notification
from pathlib import Path


icon = Path.joinpath(Path(__file__).cwd(), 'task.png')


def notify(title: str, message: str) -> None:
    toast = Notification(
        app_id='Background Task',
        title=title,
        msg=message,
        duration="long",
        icon=icon
    )
    toast.show()
