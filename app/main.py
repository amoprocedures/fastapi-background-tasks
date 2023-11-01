from fastapi import FastAPI, BackgroundTasks
from .notification import notify
from .model import Message
from asyncio import sleep

app = FastAPI()


async def schedule_task(title: str, message: str) -> None:
    await sleep(5)  # wait for 5 seconds
    notify(title, message)


@app.post('/')
def post(msg: Message, tasks: BackgroundTasks):
    tasks.add_task(schedule_task, msg.title, msg.message)
    return {"notification": "scheduled"}
