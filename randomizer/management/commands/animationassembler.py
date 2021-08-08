# currently battle scripts only

from django.core.management.base import BaseCommand
from randomizer.data.animations.battle_events.data import data
class Command(BaseCommand):
    def handle(self, *args, **options):
        ptrs = bytearray([])
        code = bytearray([])

        # lengths
        for index, script in enumerate(data):
            for cmd_index, cmd in enumerate(script):
                l = len(cmd["data"])
                l += len([le for le in cmd["data"] if type(le) == str])
                data[index][cmd_index]["length"] = l

        # addresses
        script_dex = 0x3A60D0
        for index, script in enumerate(data):
            ptrs += bytearray([script_dex & 0xFF, (script_dex >> 8) & 0xFF])
            offset = script_dex + 2
            addr = offset
            for cmd_index, cmd in enumerate(script):
                data[index][cmd_index]["address"] = addr
                addr += cmd["length"]
            data[index].insert(0, {"id": "dummy_%i" % index, "length": "2", "address": script_dex, "data": [offset & 0xFF, (offset >> 8) & 0xFF]})
            script_dex = addr

        # make sure no dupes
        ids = []
        for script in data:
            for cmd in script:
                if cmd["id"] in ids:
                    raise Exception("duplicate ID: %s" % cmd["id"])
                ids.append(cmd["id"])

        # substitute addresses
        for index, script in enumerate(data):
            for cmd_index, cmd in enumerate(script):
                for arg_index, arg in enumerate(cmd["data"]):
                    if type(arg) == str:
                        found = None
                        for comp_index, comp_script in enumerate(data):
                            for comp_cmd_index, comp_cmd in enumerate(script):
                                if comp_cmd["id"] == arg:
                                    found = comp_cmd
                        if found:
                            del data[index][cmd_index]["data"][arg_index]
                            addr_bytes = [(found["address"] & 0xFF), (found["address"] >> 8) & 0xFF]
                            # print(cmd, comp_cmd, addr_bytes)
                            addr_bytes.reverse()
                            for b in addr_bytes:
                                data[index][cmd_index]["data"].insert(arg_index, b)
                            
        # write bytes
        for index, script in enumerate(data):
            print(index)
            for cmd in script:
                print(cmd)
                code.extend(cmd["data"])

        allbytes = ptrs + code
        expected_length = 0x3A7036 + 1 - 0x3A6004

        empty_space = expected_length - len(allbytes)
        if (empty_space < 0):
            raise Exception("bank too long: expected %i got %i" % (expected_length, len(allbytes)))
        else:
            allbytes += bytearray([0x07 for x in range(empty_space)])
        
        f = open(f'write_to_0x3A6004.img', 'wb')
        f.write(allbytes)
        f.close()

        # This NEEDS jump support.