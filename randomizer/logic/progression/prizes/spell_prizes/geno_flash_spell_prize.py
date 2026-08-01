from __future__ import annotations
from randomizer.data.spells.spells import (GenoFlashSpell)
from randomizer.data.variables.dialog_names import (DI1979_LEARN_SPELL_17, DI1980_LEARN_SPELL_17_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0916_CHEST_SPELL_17, E0967_NPC_SPELL_17, E1007_FREESTANDING_SPELL_17, E1037_HILL_RIVER_SPELL_17)
from randomizer.types.prize import (SpellPrize)


class GenoFlashSpellPrize(SpellPrize):
    _spell = GenoFlashSpell
    _chest_event_id = E0916_CHEST_SPELL_17
    _npc_grant_event_id = E0967_NPC_SPELL_17
    _standing_grant_event_id = E1007_FREESTANDING_SPELL_17
    _river_grant_event_id = E1037_HILL_RIVER_SPELL_17
    _hill_grant_event_id = E1037_HILL_RIVER_SPELL_17
    character_replacement_ids = [
        "spell_17_character",
        "freestanding_spell_17_character",
        "hill_river_spell_17_character",
        "npc_spell_17_character",
    ]
    packet_replacement_ids = ["spell_17_elemental_packet"]
    _dialog_id = DI1979_LEARN_SPELL_17
    _autoterm_dialog_id = DI1980_LEARN_SPELL_17_AUTOTERM
    _placement_id = 17


__all__ = ["GenoFlashSpellPrize"]
