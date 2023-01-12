from flask import Flask
from flask_apscheduler import APScheduler

scheduler = APScheduler()


def setup_scheduler(app: Flask):
    scheduler.init_app(app)

    @scheduler.task("interval", id="job_test", seconds=60, misfire_grace_time=900)
    def job_test():
        print("job test!!!")

    scheduler.start()
