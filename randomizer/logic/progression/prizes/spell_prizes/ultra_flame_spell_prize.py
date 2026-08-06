from __future__ import annotations
from randomizer.data.spells.spells import (UltraFlameSpell)
from randomizer.data.variables.dialog_names import (DI1957_LEARN_SPELL_6, DI1958_LEARN_SPELL_6_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0905_CHEST_SPELL_6, E0957_NPC_SPELL_6, E0996_FREESTANDING_SPELL_6, E1027_HILL_RIVER_SPELL_6)
from randomizer.types.prize import (SpellPrize)


class UltraFlameSpellPrize(SpellPrize):
    _spell = UltraFlameSpell
    _chest_event_id = E0905_CHEST_SPELL_6
    _npc_grant_event_id = E0957_NPC_SPELL_6
    _standing_grant_event_id = E0996_FREESTANDING_SPELL_6
    _river_grant_event_id = E1027_HILL_RIVER_SPELL_6
    _hill_grant_event_id = E1027_HILL_RIVER_SPELL_6
    character_replacement_ids = [
        "spell_6_character",
        "freestanding_spell_6_character",
        "hill_river_spell_6_character",
        "npc_spell_6_character",
    ]
    packet_replacement_ids = ["spell_6_elemental_packet"]
    _dialog_id = DI1957_LEARN_SPELL_6
    _autoterm_dialog_id = DI1958_LEARN_SPELL_6_AUTOTERM
    _placement_id = 6


__all__ = ["UltraFlameSpellPrize"]
