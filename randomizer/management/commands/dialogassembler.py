from django.core.management.base import BaseCommand
from randomizer.data.dialog_data.dialog_data import dialog_data
from randomizer.data.dialog_data.dialog_pointers import pointers as dialog_pointers
from randomizer.data import dialogs

def assemble_from_table(pointer_table, data_table):

    if len(pointer_table) != 4096:
        raise Exception('dialog pointer table must have exactly 4096 entries')

    if len(data_table) != 3:
        raise Exception('data table must consist of exactly 3 arrays, 1 per dialog data bank')

    new_pointer_table = [None]*4096

    # Will need to substitute vars into any strings here where appropriate. i.e. Peach's name into #735
    # `PEACH_NAME`
    # `PEACH_ARTICLE`
    # done - `TOWER_BOSS_1`
    # partially done - needs handler for when recruit is empty - `MARRYMORE_CHARACTER`
    # done - `RANDOM_BOSS_NAME_1` should exclude `TOWER_BOSS_1`
    # done - `RANDOM_BOSS_NAME_2` should exclude `TOWER_BOSS_1`
    # done - `RANDOM_BOSS_NAME_3` should exclude `TOWER_BOSS_1`
    # doen - `RANDOM_CHARACTER_NAME` should exclude `MARRYMORE_CHARACTER`
    # done - `SUPER_JUMP_PRIZE_1_CAP`
    # done - `SUPER_JUMP_PRIZE_2_CAP`
    # done - `GRATE_GUY_PRIZE_CAP`
    # done - 3847 needs generated bellhop menu
    # done - Set 2116 to either:
    #    You want to know why we're\n standing around?\n I'm waiting for something\n interesting to happen, but I think\n the usual troublemakers are busy on Booster Hill.
    #    You want to know why we're\n standing around?\n I'm waiting for something\n interesting to happen, but I think\n the usual troublemakers are busy up atop Booster Tower.
    # Set strong Mushroom Kingdom NPC hint to 2235
    # Set strong Rose Town NPC hint to pointers 803, 875
    # Set strong Marrymore hint to pointer 1006 (bellhop says something like "I can't let you leave yet. If you really need to go visit <place with a star piece>, you can wait until you're finished working.")
    # Set strong Johnny Note hint to pointer 1787. Figure out how to write it in-character for whoever replaced Johnny
    # Set strong Booster Tower note hint to pointer 2822
    # done - Dialogs 1222, 1223, 1224, 1227 will need to change dpeending on if star shuffle is on or not.
    # password hints: 1664, 1665, 1667, 1668, 1669, 1673, 1674, 1675, 1676, 1690
    # tadpole pond hints: 2664, 2665, 2668 (tadpole); 2718 (scroll);
    # Character palette names: overwrite 1179-1183

    # convert dialogs to byte vals
    compressed_dialog = [
        [dialogs.compress(d) for d in data_table[0]], # 0x22
        [dialogs.compress(d) for d in data_table[1]], # 0x23
        [dialogs.compress(d) for d in data_table[2]], # 0x24
    ]

    assembled_dialog_data = []

    assembled_pointers = bytearray([])


    for b in range(len(compressed_dialog)):
        bank = 0x22 + b
        pointer_position = 0

        assembled_dialog_for_this_bank = bytearray([])
        # convert pointer data to offsets
        for dialog_id in range(len(compressed_dialog[b])):
            d = compressed_dialog[b][dialog_id]
            print ('0x%02x' % (8 + pointer_position))
            for i in range(len(d)):
                indices = [j for j, x in enumerate(pointer_table) if x["bank"] == bank and x["index"] == dialog_id and x["pos"] == i]
                #if len(indices) > 0:
                #    print (hex(bank), dialog_id, i, indices, d, len(d))
                #    print ([hex(ord(c)) for c in d])
                for matched_pointer in indices:
                    new_pointer_table[matched_pointer] = pointer_position
                pointer_position += 1
            assembled_dialog_for_this_bank += d
            print (dialog_id)
            print (str(d))
            print (len(d), pointer_position)
            print ([hex(c) for c in d])
            print ('')
            print ('')
                
        # convert to pointers relative to section pointer
        if b == 0:
            offsets = [0, new_pointer_table[0x200], new_pointer_table[0x400], new_pointer_table[0x600]]
            offsets = [o + 8 for o in offsets]
            for i in range(0x3FF, 0x1FF, -1):
                new_pointer_table[i] -= new_pointer_table[0x200]
            for i in range(0x5FF, 0x3FF, -1):
                new_pointer_table[i] -= new_pointer_table[0x400]
            for i in range(0x7FF, 0x5FF, -1):
                new_pointer_table[i] -= new_pointer_table[0x600]
        elif b == 1:
            offsets = [0, new_pointer_table[0xA00]]
            offsets = [o + 4 for o in offsets]
            for i in range(0xBFF, 0x9FF, -1):
                new_pointer_table[i] -= new_pointer_table[0xA00]
        else:
            offsets = [0, new_pointer_table[0xE00]]
            offsets = [o + 4 for o in offsets]
            for i in range(0xFFF, 0xDFF, -1):
                new_pointer_table[i] -= new_pointer_table[0xE00]
        
        # final output for data bank: section pointers plus dialog data
        assembled_bank_dialog_data = bytearray([])
        for val in offsets:
            assembled_bank_dialog_data.append(val & 0xFF)
            assembled_bank_dialog_data.append(val >> 8)
        assembled_bank_dialog_data += assembled_dialog_for_this_bank

        # make sure it's not overflowing, fill up with empty data if space left
        if b == 0:
            max_length = 0x22FD18 - 0x220000
            empty_space = max_length - len(assembled_bank_dialog_data)
        elif b == 1:
            max_length = 0x23F2D5 - 0x230000
            empty_space = max_length - len(assembled_bank_dialog_data)
        else:
            max_length = 0x249000 - 0x240000
            empty_space = max_length - len(assembled_bank_dialog_data)
        if empty_space < 0:
            raise Exception("Bank 0x%02x dialog data too long: %i bytes (expected up to %i)" % (0x22 + b, len(assembled_bank_dialog_data), max_length))
        elif empty_space > 0:
            assembled_bank_dialog_data += bytearray([0x00 for x in range(empty_space)])

        assembled_dialog_data.append(assembled_bank_dialog_data)

    # pointer bytes
    for i in range(len(new_pointer_table)):
        val = new_pointer_table[i]
        print(i, hex(val))
        assembled_pointers.append(val & 0xFF)
        assembled_pointers.append(val >> 8)
    
    return assembled_pointers, assembled_dialog_data
    



class Command(BaseCommand):
    def handle(self, *args, **options):
        pointers, data_collection = assemble_from_table(dialog_pointers, dialog_data)

        f = open(f'write_to_0x37E000.img', 'wb')
        f.write(pointers)
        f.close()
        
        f = open(f'write_to_0x220000.img', 'wb')
        f.write(data_collection[0])
        f.close()
        
        f = open(f'write_to_0x230000.img', 'wb')
        f.write(data_collection[1])
        f.close()
        
        f = open(f'write_to_0x240000.img', 'wb')
        f.write(data_collection[2])
        f.close()