"""Ally/Character data disassembled from ROM."""

from smrpgpatchbuilder.datatypes.allies.ally_collection import AllyCollection
from ..spells.spells import *
from ..items.items import *
from .definitions import *

ally_collection = AllyCollection(
    allies=[
        MARIO_Ally,
        TOADSTOOL_Ally,
        BOWSER_Ally,
        GENO_Ally,
        MALLOW_Ally,
    ]
)
