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
            secondary_ptr = offset
            if index == 22:
                secondary_ptr += 2
            elif index == 70 or index == 85:
                secondary_ptr += 4
            data[index].insert(0, {"id": "dummy_%i" % index, "length": "2", "address": script_dex, "data": [secondary_ptr & 0xFF, (secondary_ptr >> 8) & 0xFF]})
            if index == 69 and addr < 0x3A6B86:
                data[index].append({"id": "filler", "data": [0x11] * (0x3A6B86 - addr), "length": 0x3A6B86 - addr, "address": addr})
                addr += (0x3A6B86 - addr)
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
                        for _, comp_script in enumerate(data):
                            for _, comp_cmd in enumerate(comp_script):
                                if comp_cmd["id"] == arg:
                                    found = comp_cmd
                        if found:
                            #print(arg, found)
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
        #expected_length = 0x3A7036 + 1 - 0x3A6004
        expected_length = 0x3A705D - 0x3A6004

        empty_space = expected_length - len(allbytes)
        if (empty_space < 0):
            raise Exception("bank too long: expected %i got %i" % (expected_length, len(allbytes)))
        else:
            allbytes += bytearray([0x11 for x in range(empty_space)])
        
        f = open(f'write_to_0x3A6004.img', 'wb')
        f.write(allbytes)
        f.close()

        # This NEEDS jump support.