from django.core.management.base import BaseCommand
from randomizer.logic.rooms import Rooms
from randomizer.logic.enscript import EventScript
from randomizer.logic.osscript import ObjectSequenceScript as OSCommand
from randomizer.data.rooms.rooms import rooms as all_rooms
from randomizer.data.eventscripts.events import scripts


class Command(BaseCommand):
    def handle(self, *args, **options):
        npcs, eventtiles, exits, partitions, npctable, new_scripts = Rooms.assemble_from_table(
            all_rooms, scripts
        )

        allnpcbytes = npcs[0] + npcs[1]

        f = open(f"write_to_0x148000.img", "wb")
        f.write(allnpcbytes)
        f.close()

        alleventbytes = eventtiles[0] + eventtiles[1]

        f = open(f"write_to_0x20E000.img", "wb")
        f.write(alleventbytes)
        f.close()

        allexitbytes = exits[0] + exits[1]

        f = open(f"write_to_0x1D2D64.img", "wb")
        f.write(allexitbytes)
        f.close()

        f = open(f"write_to_0x1DDE00.img", "wb")
        f.write(partitions)
        f.close()

        f = open(f"write_to_0x1DB800.img", "wb")
        f.write(npctable)
        f.close()

        b = EventScript.assemble_from_table(new_scripts)

        f = open(f'write_to_0x1E0000.img', 'wb')
        f.write(b)
        f.close()