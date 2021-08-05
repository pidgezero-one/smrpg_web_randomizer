# currently battle scripts only

from django.core.management.base import BaseCommand
from randomizer.data.animations.battle_events.data import data
class Command(BaseCommand):
    def handle(self, *args, **options):
        ptrs = bytearray([])
        code = bytearray([])

        script_dex = 0x3A60D0
        for script in data:
            ptrs += bytearray([script_dex & 0xFF, (script_dex >> 8) & 0xFF])
            offset = script_dex + 2
            script_code = bytearray([offset & 0xFF, (offset >> 8) & 0xFF])
            script_code += bytearray([item for sublist in script for item in sublist])
            code += script_code
            script_dex += len(script_code)

        allbytes = ptrs + code
        expected_length = 0x3A705C + 1 - 0x3A6004

        empty_space = expected_length - len(allbytes)
        if (empty_space < 0):
            raise Exception("bank too long: expected %i got %i" % (expected_length, len(allbytes)))
        else:
            allbytes += bytearray([0x07 for x in range(empty_space)])
        
        f = open(f'write_to_0x3A6004.img', 'wb')
        f.write(allbytes)
        f.close()