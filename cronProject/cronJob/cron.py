from .models import Test


def my_cron_job():
    Test.objects.create(name='test')
    print('some message')
