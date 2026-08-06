from __future__ import annotations
from randomizer.data.spells.spells import (SleepyTimeSpell)
from randomizer.data.variables.dialog_names import (DI1993_LEARN_SPELL_24, DI1994_LEARN_SPELL_24_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0924_CHEST_SPELL_24, E0974_NPC_SPELL_24, E1018_FREESTANDING_SPELL_24, E1044_HILL_RIVER_SPELL_24)
from randomizer.types.prize import (SpellPrize)


class SleepyTimeSpellPrize(SpellPrize):
    _spell = SleepyTimeSpell
    _chest_event_id = E0924_CHEST_SPELL_24
    _npc_grant_event_id = E0974_NPC_SPELL_24
    _standing_grant_event_id = E1018_FREESTANDING_SPELL_24
    _river_grant_event_id = E1044_HILL_RIVER_SPELL_24
    _hill_grant_event_id = E1044_HILL_RIVER_SPELL_24
    character_replacement_ids = [
        "spell_24_character",
        "freestanding_spell_24_character",
        "hill_river_spell_24_character",
        "npc_spell_24_character",
    ]
    packet_replacement_ids = ["spell_24_elemental_packet"]
    _dialog_id = DI1993_LEARN_SPELL_24
    _autoterm_dialog_id = DI1994_LEARN_SPELL_24_AUTOTERM
    _placement_id = 24


__all__ = ["SleepyTimeSpellPrize"]
