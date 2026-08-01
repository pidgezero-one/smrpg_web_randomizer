from __future__ import annotations
from randomizer.data.spells.spells import (TerrorizeSpell)
from randomizer.data.variables.dialog_names import (DI1981_LEARN_SPELL_18, DI1982_LEARN_SPELL_18_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0918_CHEST_SPELL_18, E0968_NPC_SPELL_18, E1012_FREESTANDING_SPELL_18, E1038_HILL_RIVER_SPELL_18)
from randomizer.types.prize import (SpellPrize)


class TerrorizeSpellPrize(SpellPrize):
    _spell = TerrorizeSpell
    _chest_event_id = E0918_CHEST_SPELL_18
    _npc_grant_event_id = E0968_NPC_SPELL_18
    _standing_grant_event_id = E1012_FREESTANDING_SPELL_18
    _river_grant_event_id = E1038_HILL_RIVER_SPELL_18
    _hill_grant_event_id = E1038_HILL_RIVER_SPELL_18
    character_replacement_ids = [
        "spell_18_character",
        "freestanding_spell_18_character",
        "hill_river_spell_18_character",
        "npc_spell_18_character",
    ]
    packet_replacement_ids = ["spell_18_elemental_packet"]
    _dialog_id = DI1981_LEARN_SPELL_18
    _autoterm_dialog_id = DI1982_LEARN_SPELL_18_AUTOTERM
    _placement_id = 18


__all__ = ["TerrorizeSpellPrize"]
