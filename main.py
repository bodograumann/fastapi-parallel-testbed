import asyncio
import logging
import os
import threading
import time

from fastapi import FastAPI

app = FastAPI()


SLEEP_FOR = 10

race_me = None


def log(msg: str):
    global race_me
    process = os.getpid()
    thread = threading.get_native_id()
    logging.debug("[%s -> %d/%s] %s", race_me, process, thread, msg)
    race_me = f"{process}/{thread}"


log("Defining FastAPI app")


@app.get("/asyncsleep")
async def concurrent_sleep() -> dict:
    log("Entering sleep endpoint")
    log(f"Starting sleep for {SLEEP_FOR} seconds")
    await asyncio.sleep(SLEEP_FOR)
    log("Woken up again")
    log("Exiting sleep endpoint")
    return {}


@app.get("/sleep")
def threadpool_sleep() -> dict:
    log("Entering sleep endpoint")
    log(f"Starting sleep for {SLEEP_FOR} seconds")
    time.sleep(SLEEP_FOR)
    log("Woken up again")
    log("Exiting sleep endpoint")
    return {}
