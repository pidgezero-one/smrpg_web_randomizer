from __future__ import annotations
from randomizer.data.spells.spells import (SuperJumpSpell)
from randomizer.data.variables.dialog_names import (DI1951_LEARN_SPELL_3, DI1952_LEARN_SPELL_3_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0902_CHEST_SPELL_3, E0954_NPC_SPELL_3, E0993_FREESTANDING_SPELL_3, E1024_HILL_RIVER_SPELL_3)
from randomizer.types.prize import (SpellPrize)


class SuperJumpSpellPrize(SpellPrize):
    _spell = SuperJumpSpell
    _chest_event_id = E0902_CHEST_SPELL_3
    _npc_grant_event_id = E0954_NPC_SPELL_3
    _standing_grant_event_id = E0993_FREESTANDING_SPELL_3
    _river_grant_event_id = E1024_HILL_RIVER_SPELL_3
    _hill_grant_event_id = E1024_HILL_RIVER_SPELL_3
    character_replacement_ids = [
        "spell_3_character",
        "freestanding_spell_3_character",
        "hill_river_spell_3_character",
        "npc_spell_3_character",
    ]
    packet_replacement_ids = ["spell_3_elemental_packet"]
    _dialog_id = DI1951_LEARN_SPELL_3
    _autoterm_dialog_id = DI1952_LEARN_SPELL_3_AUTOTERM
    _placement_id = 3


__all__ = ["SuperJumpSpellPrize"]
