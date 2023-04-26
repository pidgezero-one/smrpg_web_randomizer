from django.core.management.base import BaseCommand
from randomizer.logic.packets import Packets
from randomizer.data.packets import packets

class Command(BaseCommand):
    def handle(self, *args, **options):
        b = Packets.assemble_from_table(packets)

        #print("length:", hex(len(b)))

        f = open(f'write_to_0x1DB000.img', 'wb')
        
        f.write(b)
        f.close()
