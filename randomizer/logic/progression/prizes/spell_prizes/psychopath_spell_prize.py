from __future__ import annotations
from randomizer.data.spells.spells import (PsychopathSpell)
from randomizer.data.variables.dialog_names import (DI1963_LEARN_SPELL_9, DI1964_LEARN_SPELL_9_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0908_CHEST_SPELL_9, E0960_NPC_SPELL_9, E1000_FREESTANDING_SPELL_9, E1030_HILL_RIVER_SPELL_9)
from randomizer.types.prize import (SpellPrize)


class PsychopathSpellPrize(SpellPrize):
    _spell = PsychopathSpell
    _chest_event_id = E0908_CHEST_SPELL_9
    _npc_grant_event_id = E0960_NPC_SPELL_9
    _standing_grant_event_id = E1000_FREESTANDING_SPELL_9
    _river_grant_event_id = E1030_HILL_RIVER_SPELL_9
    _hill_grant_event_id = E1030_HILL_RIVER_SPELL_9
    character_replacement_ids = [
        "spell_9_character",
        "freestanding_spell_9_character",
        "hill_river_spell_9_character",
        "npc_spell_9_character",
    ]
    packet_replacement_ids = ["spell_9_elemental_packet"]
    _dialog_id = DI1963_LEARN_SPELL_9
    _autoterm_dialog_id = DI1964_LEARN_SPELL_9_AUTOTERM
    _placement_id = 9


__all__ = ["PsychopathSpellPrize"]
