from django.core.management.base import BaseCommand
from randomizer.data.dialog_data.dialog_data import dialog_data
from randomizer.data.dialog_data.dialog_pointers import pointers as dialog_pointers
from randomizer.logic import dialogs



class Command(BaseCommand):
    def handle(self, *args, **options):
        pointers, data_collection = dialogs.assemble_from_table(dialog_pointers, dialog_data)

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