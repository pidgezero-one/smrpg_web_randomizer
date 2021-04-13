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
    # Set strong Rose Town NPC hint to pointers 803, 875
    # Set strong Marrymore hint to pointer 1006 (bellhop says something like "I can't let you leave yet. If you really need to go visit <place with a star piece>, you can wait until you're finished working.")

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
    for val in new_pointer_table:
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