from __future__ import annotations
from randomizer.data.spells.spells import (GenoWhirlSpell)
from randomizer.data.variables.dialog_names import (DI1975_LEARN_SPELL_15, DI1976_LEARN_SPELL_15_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0914_CHEST_SPELL_15, E1048_NPC_SPELL_15, E1049_FREESTANDING_SPELL_15, E1050_HILL_RIVER_SPELL_15)
from randomizer.types.prize import (SpellPrize)


class GenoWhirlSpellPrize(SpellPrize):
    _spell = GenoWhirlSpell
    _chest_event_id = E0914_CHEST_SPELL_15
    _npc_grant_event_id = E1048_NPC_SPELL_15
    _standing_grant_event_id = E1049_FREESTANDING_SPELL_15
    _river_grant_event_id = E1050_HILL_RIVER_SPELL_15
    _hill_grant_event_id = E1050_HILL_RIVER_SPELL_15
    character_replacement_ids = [
        "spell_15_character",
        "freestanding_spell_15_character",
        "hill_river_spell_15_character",
        "npc_spell_15_character",
    ]
    packet_replacement_ids = ["spell_15_elemental_packet"]
    _dialog_id = DI1975_LEARN_SPELL_15
    _autoterm_dialog_id = DI1976_LEARN_SPELL_15_AUTOTERM
    _placement_id = 15


__all__ = ["GenoWhirlSpellPrize"]
