from apscheduler.schedulers.blocking import BlockingScheduler
import feed
import channels

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=2)
def timed_job():
    print('This job is run every two hours.')
    feed.run_and_insert()
    channels.run_and_insert()

sched.start()

