from __future__ import annotations
from randomizer.data.spells.spells import (UltraJumpSpell)
from randomizer.data.variables.dialog_names import (DI1955_LEARN_SPELL_5, DI1956_LEARN_SPELL_5_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0904_CHEST_SPELL_5, E0956_NPC_SPELL_5, E0995_FREESTANDING_SPELL_5, E1026_HILL_RIVER_SPELL_5)
from randomizer.types.prize import (SpellPrize)


class UltraJumpSpellPrize(SpellPrize):
    _spell = UltraJumpSpell
    _chest_event_id = E0904_CHEST_SPELL_5
    _npc_grant_event_id = E0956_NPC_SPELL_5
    _standing_grant_event_id = E0995_FREESTANDING_SPELL_5
    _river_grant_event_id = E1026_HILL_RIVER_SPELL_5
    _hill_grant_event_id = E1026_HILL_RIVER_SPELL_5
    character_replacement_ids = [
        "spell_5_character",
        "freestanding_spell_5_character",
        "hill_river_spell_5_character",
        "npc_spell_5_character",
    ]
    packet_replacement_ids = ["spell_5_elemental_packet"]
    _dialog_id = DI1955_LEARN_SPELL_5
    _autoterm_dialog_id = DI1956_LEARN_SPELL_5_AUTOTERM
    _placement_id = 5


__all__ = ["UltraJumpSpellPrize"]
