from __future__ import annotations
from randomizer.data.spells.spells import (StarRainSpell)
from randomizer.data.variables.dialog_names import (DI1969_LEARN_SPELL_12, DI1970_LEARN_SPELL_12_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0911_CHEST_SPELL_12, E0963_NPC_SPELL_12, E1003_FREESTANDING_SPELL_12, E1033_HILL_RIVER_SPELL_12)
from randomizer.types.prize import (SpellPrize)


class StarRainSpellPrize(SpellPrize):
    _spell = StarRainSpell
    _chest_event_id = E0911_CHEST_SPELL_12
    _npc_grant_event_id = E0963_NPC_SPELL_12
    _standing_grant_event_id = E1003_FREESTANDING_SPELL_12
    _river_grant_event_id = E1033_HILL_RIVER_SPELL_12
    _hill_grant_event_id = E1033_HILL_RIVER_SPELL_12
    character_replacement_ids = [
        "spell_12_character",
        "freestanding_spell_12_character",
        "hill_river_spell_12_character",
        "npc_spell_12_character",
    ]
    packet_replacement_ids = ["spell_12_elemental_packet"]
    _dialog_id = DI1969_LEARN_SPELL_12
    _autoterm_dialog_id = DI1970_LEARN_SPELL_12_AUTOTERM
    _placement_id = 12


__all__ = ["StarRainSpellPrize"]
