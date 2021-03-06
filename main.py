import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())
    print(Passcard.objects.all())
    passcard = Passcard.objects.get(id=1)
    print(passcard)
    for field in (['owner_name', 'passcode', 'created_at', 'is_active']):
      print('{}: {}'.format(field, passcard.__dict__.get(field)))
    print(Passcard.objects.filter(is_active=True).count())    