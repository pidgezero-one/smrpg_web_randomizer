from __future__ import annotations
from randomizer.data.spells.spells import (JumpSpell)
from randomizer.data.variables.dialog_names import (DI1947_LEARN_SPELL_1, DI1948_LEARN_SPELL_1_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0900_CHEST_SPELL_1, E0952_NPC_SPELL_1, E0978_FREESTANDING_SPELL_1, E1022_HILL_RIVER_SPELL_1)
from randomizer.types.prize import (SpellPrize)


class JumpSpellPrize(SpellPrize):
    _spell = JumpSpell
    _chest_event_id = E0900_CHEST_SPELL_1
    _npc_grant_event_id = E0952_NPC_SPELL_1
    _standing_grant_event_id = E0978_FREESTANDING_SPELL_1
    _river_grant_event_id = E1022_HILL_RIVER_SPELL_1
    _hill_grant_event_id = E1022_HILL_RIVER_SPELL_1
    character_replacement_ids = [
        "spell_1_character",
        "freestanding_spell_1_character",
        "hill_river_spell_1_character",
        "npc_spell_1_character",
    ]
    packet_replacement_ids = ["spell_1_elemental_packet"]
    _dialog_id = DI1947_LEARN_SPELL_1
    _autoterm_dialog_id = DI1948_LEARN_SPELL_1_AUTOTERM
    _placement_id = 1


__all__ = ["JumpSpellPrize"]
