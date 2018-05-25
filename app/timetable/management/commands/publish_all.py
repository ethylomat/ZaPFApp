import numpy as np
import random
import operator

from django.core.management.base import BaseCommand
from timetable.models import Timeslot, Room, AKSlot, AK, RoomAssignment, News
from constance import config


class Command(BaseCommand):


    def _publish_all(self):
        aks = AK.objects.all()
        for ak in aks:
            ak.published = True

    def handle(self, *args, **options):
        self._publish_all()