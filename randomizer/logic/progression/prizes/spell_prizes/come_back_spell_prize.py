from __future__ import annotations
from randomizer.data.spells.spells import (ComeBackSpell)
from randomizer.data.variables.dialog_names import (DI1995_LEARN_SPELL_25, DI1996_LEARN_SPELL_25_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0925_CHEST_SPELL_25, E0975_NPC_SPELL_25, E1019_FREESTANDING_SPELL_25, E1045_HILL_RIVER_SPELL_25)
from randomizer.types.prize import (SpellPrize)


class ComeBackSpellPrize(SpellPrize):
    _spell = ComeBackSpell
    _chest_event_id = E0925_CHEST_SPELL_25
    _npc_grant_event_id = E0975_NPC_SPELL_25
    _standing_grant_event_id = E1019_FREESTANDING_SPELL_25
    _river_grant_event_id = E1045_HILL_RIVER_SPELL_25
    _hill_grant_event_id = E1045_HILL_RIVER_SPELL_25
    character_replacement_ids = [
        "spell_25_character",
        "freestanding_spell_25_character",
        "hill_river_spell_25_character",
        "npc_spell_25_character",
    ]
    packet_replacement_ids = ["spell_25_elemental_packet"]
    _dialog_id = DI1995_LEARN_SPELL_25
    _autoterm_dialog_id = DI1996_LEARN_SPELL_25_AUTOTERM
    _placement_id = 25


__all__ = ["ComeBackSpellPrize"]
