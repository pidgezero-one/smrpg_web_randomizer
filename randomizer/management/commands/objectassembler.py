from django.core.management.base import BaseCommand
from randomizer.logic.roomobject import RoomObjects
from randomizer.data.roomobjects.roomobjects import rooms

class Command(BaseCommand):
    def handle(self, *args, **options):
        b = RoomObjects.assemble_from_table(rooms)

        allbytes = b[0] + b[1]
        print("combined length", hex(len(allbytes)), len(allbytes))


        f = open(f'text_output.img', 'wb')
        f.write(allbytes)
        f.close()
