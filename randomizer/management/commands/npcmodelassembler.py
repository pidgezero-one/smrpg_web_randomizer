from django.core.management.base import BaseCommand
from randomizer.logic.npcmodel import NPCModels
from randomizer.data.npcmodels import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        b = NPCModels.assemble_from_table(models)

        print("length:", hex(len(b)))

        f = open(f'text_output.img', 'wb')
        
        f.write(b)
        f.close()
