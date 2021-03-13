import os
import django
import datetime
from django.utils.timezone import localtime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


def format_duration(duration):
    return "{}часа {}минут".format(duration.hours, duration.minutes)


if __name__ == "__main__":
    print('Количество пропусков:', Passcard.objects.count())
    print(Passcard.objects.all())
    passcard = Passcard.objects.get(id=1)
    print(passcard)
    for field in (['owner_name', 'passcode', 'created_at', 'is_active']):
        print('{}: {}'.format(field, passcard.__dict__.get(field)))
    print("Активных пропусков: {}".format(Passcard.objects.filter(is_active=True).count()))
    # print(Visit.objects.all())
    # strange_visits = Visit.objects.filter(leaved_at=None)
    for visit in Visit.objects.filter(leaved_at=None):
        print(visit.passcard.owner_name)
    print(Visit.objects.filter(passcard__id=passcard.pk).count())
    print('Визиты дольше 1000 мин:', len([item for item in Visit.objects.all() if item.is_visit_long(
            minutes=60)]))
