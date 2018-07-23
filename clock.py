from apscheduler.schedulers.blocking import BlockingScheduler
import feed
import channels

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=1)
def timed_job():
    print('This job is run every one hour.')
    feed
    channels

sched.start()

