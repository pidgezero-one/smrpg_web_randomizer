from __future__ import annotations
from randomizer.data.spells.spells import (MuteSpell)
from randomizer.data.variables.dialog_names import (DI1997_LEARN_SPELL_26, DI1998_LEARN_SPELL_26_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0926_CHEST_SPELL_26, E0976_NPC_SPELL_26, E1020_FREESTANDING_SPELL_26, E1046_HILL_RIVER_SPELL_26)
from randomizer.types.prize import (SpellPrize)


class MuteSpellPrize(SpellPrize):
    _spell = MuteSpell
    _chest_event_id = E0926_CHEST_SPELL_26
    _npc_grant_event_id = E0976_NPC_SPELL_26
    _standing_grant_event_id = E1020_FREESTANDING_SPELL_26
    _river_grant_event_id = E1046_HILL_RIVER_SPELL_26
    _hill_grant_event_id = E1046_HILL_RIVER_SPELL_26
    character_replacement_ids = [
        "spell_26_character",
        "freestanding_spell_26_character",
        "hill_river_spell_26_character",
        "npc_spell_26_character",
    ]
    packet_replacement_ids = ["spell_26_elemental_packet"]
    _dialog_id = DI1997_LEARN_SPELL_26
    _autoterm_dialog_id = DI1998_LEARN_SPELL_26_AUTOTERM
    _placement_id = 26


__all__ = ["MuteSpellPrize"]
