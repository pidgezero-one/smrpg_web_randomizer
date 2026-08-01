from __future__ import annotations
from randomizer.data.spells.spells import (ThunderboltSpell)
from randomizer.data.variables.dialog_names import (DI1959_LEARN_SPELL_7, DI1960_LEARN_SPELL_7_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0906_CHEST_SPELL_7, E0958_NPC_SPELL_7, E0997_FREESTANDING_SPELL_7, E1028_HILL_RIVER_SPELL_7)
from randomizer.types.prize import (SpellPrize)


class ThunderboltSpellPrize(SpellPrize):
    _spell = ThunderboltSpell
    _chest_event_id = E0906_CHEST_SPELL_7
    _npc_grant_event_id = E0958_NPC_SPELL_7
    _standing_grant_event_id = E0997_FREESTANDING_SPELL_7
    _river_grant_event_id = E1028_HILL_RIVER_SPELL_7
    _hill_grant_event_id = E1028_HILL_RIVER_SPELL_7
    character_replacement_ids = [
        "spell_7_character",
        "freestanding_spell_7_character",
        "hill_river_spell_7_character",
        "npc_spell_7_character",
    ]
    packet_replacement_ids = ["spell_7_elemental_packet"]
    _dialog_id = DI1959_LEARN_SPELL_7
    _autoterm_dialog_id = DI1960_LEARN_SPELL_7_AUTOTERM
    _placement_id = 7


__all__ = ["ThunderboltSpellPrize"]
