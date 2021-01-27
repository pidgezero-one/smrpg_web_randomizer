from django.core.management.base import BaseCommand
from randomizer.logic.osscript import ObjectSequenceScript as OSCommand
from randomizer.data.actionscripts.actions import scripts

class Command(BaseCommand):
    def handle(self, *args, **options):
        b = OSCommand.assemble_from_table(scripts)

        allbytes = b[0] + b[1]
        print("combined length", hex(len(allbytes)), len(allbytes))


        f = open(f'text_output.img', 'wb')
        f.write(allbytes)
        f.close()
