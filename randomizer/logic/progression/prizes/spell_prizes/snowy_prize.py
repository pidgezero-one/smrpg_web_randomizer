from __future__ import annotations
from randomizer.data.spells.spells import (SnowySpell)
from randomizer.data.variables.dialog_names import (DI1967_LEARN_SPELL_11, DI1968_LEARN_SPELL_11_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0910_CHEST_SPELL_11, E0962_NPC_SPELL_11, E1002_FREESTANDING_SPELL_11, E1032_HILL_RIVER_SPELL_11)
from randomizer.types.prize import (SpellPrize)


class SnowyPrize(SpellPrize):
    _spell = SnowySpell
    _chest_event_id = E0910_CHEST_SPELL_11
    _npc_grant_event_id = E0962_NPC_SPELL_11
    _standing_grant_event_id = E1002_FREESTANDING_SPELL_11
    _river_grant_event_id = E1032_HILL_RIVER_SPELL_11
    _hill_grant_event_id = E1032_HILL_RIVER_SPELL_11
    character_replacement_ids = [
        "spell_11_character",
        "freestanding_spell_11_character",
        "hill_river_spell_11_character",
        "npc_spell_11_character",
    ]
    packet_replacement_ids = ["spell_11_elemental_packet"]
    _dialog_id = DI1967_LEARN_SPELL_11
    _autoterm_dialog_id = DI1968_LEARN_SPELL_11_AUTOTERM
    _placement_id = 11


__all__ = ["SnowyPrize"]
