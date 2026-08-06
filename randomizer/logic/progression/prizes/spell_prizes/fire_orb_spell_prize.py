from __future__ import annotations
from randomizer.data.spells.spells import (FireOrbSpell)
from randomizer.data.variables.dialog_names import (DI1949_LEARN_SPELL_2, DI1950_LEARN_SPELL_2_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0901_CHEST_SPELL_2, E0953_NPC_SPELL_2, E0992_FREESTANDING_SPELL_2, E1023_HILL_RIVER_SPELL_2)
from randomizer.types.prize import (SpellPrize)


class FireOrbSpellPrize(SpellPrize):
    _spell = FireOrbSpell
    _chest_event_id = E0901_CHEST_SPELL_2
    _npc_grant_event_id = E0953_NPC_SPELL_2
    _standing_grant_event_id = E0992_FREESTANDING_SPELL_2
    _river_grant_event_id = E1023_HILL_RIVER_SPELL_2
    _hill_grant_event_id = E1023_HILL_RIVER_SPELL_2
    character_replacement_ids = [
        "spell_2_character",
        "freestanding_spell_2_character",
        "hill_river_spell_2_character",
        "npc_spell_2_character",
    ]
    packet_replacement_ids = ["spell_2_elemental_packet"]
    _dialog_id = DI1949_LEARN_SPELL_2
    _autoterm_dialog_id = DI1950_LEARN_SPELL_2_AUTOTERM
    _placement_id = 2


__all__ = ["FireOrbSpellPrize"]
