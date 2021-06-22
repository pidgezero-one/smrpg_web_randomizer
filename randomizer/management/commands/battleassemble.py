from django.core.management.base import BaseCommand
from randomizer.logic.battleassembler import assemble_battle_scripts_as_slices

class Command(BaseCommand):
    def handle(self, *args, **options):

        ptrs, bank_1, bank_2 = assemble_battle_scripts_as_slices()

        f = open(f'write_to_0x3930AA.img', 'wb')
        f.write(bytearray(ptrs))
        f.close()
        
        f = open(f'write_to_0x3932AA.img', 'wb')
        f.write(bytearray(bank_1))
        f.close()
        
        f = open(f'write_to_0x39F400.img', 'wb')
        f.write(bytearray(bank_2))
        f.close()
