from __future__ import annotations
from randomizer.data.spells.spells import (GenoBoostSpell)
from randomizer.data.variables.dialog_names import (DI1973_LEARN_SPELL_14, DI1974_LEARN_SPELL_14_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0913_CHEST_SPELL_14, E0965_NPC_SPELL_14, E1005_FREESTANDING_SPELL_14, E1035_HILL_RIVER_SPELL_14)
from randomizer.types.prize import (SpellPrize)


class GenoBoostSpellPrize(SpellPrize):
    _spell = GenoBoostSpell
    _chest_event_id = E0913_CHEST_SPELL_14
    _npc_grant_event_id = E0965_NPC_SPELL_14
    _standing_grant_event_id = E1005_FREESTANDING_SPELL_14
    _river_grant_event_id = E1035_HILL_RIVER_SPELL_14
    _hill_grant_event_id = E1035_HILL_RIVER_SPELL_14
    character_replacement_ids = [
        "spell_14_character",
        "freestanding_spell_14_character",
        "hill_river_spell_14_character",
        "npc_spell_14_character",
    ]
    packet_replacement_ids = ["spell_14_elemental_packet"]
    _dialog_id = DI1973_LEARN_SPELL_14
    _autoterm_dialog_id = DI1974_LEARN_SPELL_14_AUTOTERM
    _placement_id = 14


__all__ = ["GenoBoostSpellPrize"]
