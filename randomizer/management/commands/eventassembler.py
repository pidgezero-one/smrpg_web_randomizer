from django.core.management.base import BaseCommand
from randomizer.logic.enscript import EventScript
from randomizer.logic.osscript import ObjectSequenceScript as OSCommand
from randomizer.data.eventscripts.events import scripts

class Command(BaseCommand):
    def handle(self, *args, **options):
        b = EventScript.assemble_from_table(scripts)

        print("combined length", hex(len(b)), len(b))

        f = open(f'write_to_0x1E0000.img', 'wb')
        f.write(b)
        f.close()