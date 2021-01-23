from django.core.management.base import BaseCommand
from randomizer.logic.enscript import EventScript
from randomizer.logic.osscript import ObjectSequenceScript as OSCommand
from randomizer.data.eventscripts.events import scripts

class Command(BaseCommand):
    def handle(self, *args, **options):
        b = EventScript.assemble_from_table(scripts)

        allbytes = b[0] + b[1] + b[2] + b[3] + b[4] + b[5]
        print("combined length", hex(len(allbytes)), len(allbytes))


        f = open(f'text_output.img', 'wb')
        f.write(allbytes)
        f.close()
