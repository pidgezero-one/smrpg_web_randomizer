from __future__ import annotations
from randomizer.data.spells.spells import (TherapySpell)
from randomizer.data.variables.dialog_names import (DI1989_LEARN_SPELL_22, DI1990_LEARN_SPELL_22_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0922_CHEST_SPELL_22, E0972_NPC_SPELL_22, E1016_FREESTANDING_SPELL_22, E1042_HILL_RIVER_SPELL_22)
from randomizer.types.prize import (SpellPrize)


class TherapySpellPrize(SpellPrize):
    _spell = TherapySpell
    _chest_event_id = E0922_CHEST_SPELL_22
    _npc_grant_event_id = E0972_NPC_SPELL_22
    _standing_grant_event_id = E1016_FREESTANDING_SPELL_22
    _river_grant_event_id = E1042_HILL_RIVER_SPELL_22
    _hill_grant_event_id = E1042_HILL_RIVER_SPELL_22
    character_replacement_ids = [
        "spell_22_character",
        "freestanding_spell_22_character",
        "hill_river_spell_22_character",
        "npc_spell_22_character",
    ]
    packet_replacement_ids = ["spell_22_elemental_packet"]
    _dialog_id = DI1989_LEARN_SPELL_22
    _autoterm_dialog_id = DI1990_LEARN_SPELL_22_AUTOTERM
    _placement_id = 22


__all__ = ["TherapySpellPrize"]
