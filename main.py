import os
import django
import datetime
from django.utils.timezone import localtime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


def format_duration(duration):
    hours = int(duration.total_seconds() // 3600)
    minutes = int(duration.total_seconds() % 3600 // 60)
    if hours == 0:
        return "{} мин".format(minutes)
    else:
        return "{} ч {} мин".format(hours, minutes)


if __name__ == "__main__":
    print('Количество пропусков:', Passcard.objects.count())
    print(Passcard.objects.all())
    print("Активных пропусков: {}".format(Passcard.objects.filter(is_active=True).count()))
    passcard = Passcard.objects.get(id=1)
    print("Пропуск с id=1:", passcard)
    for field in (['owner_name', 'passcode', 'created_at', 'is_active']):
        print('{}: {}'.format(field, passcard.__dict__.get(field)))
    lst_in_storage = [visit.passcard.owner_name for visit in Visit.objects.filter(leaved_at=None)]
    print("Список людей в хранилище:", lst_in_storage)
    print("Число визитов в хранилище человека с пропуском id=1({1}): {0}".format(Visit.objects.filter(
        passcard__id=passcard.pk).count(), passcard.owner_name))
    print('Визиты дольше 1000 мин:', len([item for item in Visit.objects.all() if item.is_visit_long(
            minutes=60)]))
