from apscheduler.schedulers.blocking import BlockingScheduler
import feed
import channels

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=59)
def timed_job():
    print('This job is run every one hour.')
    feed.run_and_insert()
    channels.run_and_insert()

sched.start()

