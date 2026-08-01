from __future__ import annotations
from randomizer.data.spells.spells import (GroupHugSpell)
from randomizer.data.variables.dialog_names import (DI1991_LEARN_SPELL_23, DI1992_LEARN_SPELL_23_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0923_CHEST_SPELL_23, E0973_NPC_SPELL_23, E1017_FREESTANDING_SPELL_23, E1043_HILL_RIVER_SPELL_23)
from randomizer.types.prize import (SpellPrize)


class GroupHugSpellPrize(SpellPrize):
    _spell = GroupHugSpell
    _chest_event_id = E0923_CHEST_SPELL_23
    _npc_grant_event_id = E0973_NPC_SPELL_23
    _standing_grant_event_id = E1017_FREESTANDING_SPELL_23
    _river_grant_event_id = E1043_HILL_RIVER_SPELL_23
    _hill_grant_event_id = E1043_HILL_RIVER_SPELL_23
    character_replacement_ids = [
        "spell_23_character",
        "freestanding_spell_23_character",
        "hill_river_spell_23_character",
        "npc_spell_23_character",
    ]
    packet_replacement_ids = ["spell_23_elemental_packet"]
    _dialog_id = DI1991_LEARN_SPELL_23
    _autoterm_dialog_id = DI1992_LEARN_SPELL_23_AUTOTERM
    _placement_id = 23


__all__ = ["GroupHugSpellPrize"]
