from __future__ import annotations
from randomizer.data.spells.spells import (SuperFlameSpell)
from randomizer.data.variables.dialog_names import (DI1953_LEARN_SPELL_4, DI1954_LEARN_SPELL_4_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0903_CHEST_SPELL_4, E0955_NPC_SPELL_4, E0994_FREESTANDING_SPELL_4, E1025_HILL_RIVER_SPELL_4)
from randomizer.types.prize import (SpellPrize)


class SuperFlameSpellPrize(SpellPrize):
    _spell = SuperFlameSpell
    _chest_event_id = E0903_CHEST_SPELL_4
    _npc_grant_event_id = E0955_NPC_SPELL_4
    _standing_grant_event_id = E0994_FREESTANDING_SPELL_4
    _river_grant_event_id = E1025_HILL_RIVER_SPELL_4
    _hill_grant_event_id = E1025_HILL_RIVER_SPELL_4
    character_replacement_ids = [
        "spell_4_character",
        "freestanding_spell_4_character",
        "hill_river_spell_4_character",
        "npc_spell_4_character",
    ]
    packet_replacement_ids = ["spell_4_elemental_packet"]
    _dialog_id = DI1953_LEARN_SPELL_4
    _autoterm_dialog_id = DI1954_LEARN_SPELL_4_AUTOTERM
    _placement_id = 4


__all__ = ["SuperFlameSpellPrize"]
