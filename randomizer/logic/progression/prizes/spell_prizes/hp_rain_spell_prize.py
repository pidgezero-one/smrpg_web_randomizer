from __future__ import annotations
from randomizer.data.spells.spells import (HPRainSpell)
from randomizer.data.variables.dialog_names import (DI1961_LEARN_SPELL_8, DI1962_LEARN_SPELL_8_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0907_CHEST_SPELL_8, E0959_NPC_SPELL_8, E0999_FREESTANDING_SPELL_8, E1029_HILL_RIVER_SPELL_8)
from randomizer.types.prize import (SpellPrize)


class HPRainSpellPrize(SpellPrize):
    _spell = HPRainSpell
    _chest_event_id = E0907_CHEST_SPELL_8
    _npc_grant_event_id = E0959_NPC_SPELL_8
    _standing_grant_event_id = E0999_FREESTANDING_SPELL_8
    _river_grant_event_id = E1029_HILL_RIVER_SPELL_8
    _hill_grant_event_id = E1029_HILL_RIVER_SPELL_8
    character_replacement_ids = [
        "spell_8_character",
        "freestanding_spell_8_character",
        "hill_river_spell_8_character",
        "npc_spell_8_character",
    ]
    packet_replacement_ids = ["spell_8_elemental_packet"]
    _dialog_id = DI1961_LEARN_SPELL_8
    _autoterm_dialog_id = DI1962_LEARN_SPELL_8_AUTOTERM
    _placement_id = 8


__all__ = ["HPRainSpellPrize"]
