from django.core.management.base import BaseCommand
from randomizer.logic.enscript import EventScript
from randomizer.management.commands.eventdisassembler import tok, banks
from randomizer.logic.osscript import ObjectSequenceScript as OSCommand
from randomizer.data import items
scripts = [None]*4096
