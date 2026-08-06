from __future__ import annotations
from randomizer.data.spells.spells import (GenoBlastSpell)
from randomizer.data.variables.dialog_names import (DI1977_LEARN_SPELL_16, DI1978_LEARN_SPELL_16_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0915_CHEST_SPELL_16, E0966_NPC_SPELL_16, E1006_FREESTANDING_SPELL_16, E1036_HILL_RIVER_SPELL_16)
from randomizer.types.prize import (SpellPrize)


class GenoBlastSpellPrize(SpellPrize):
    _spell = GenoBlastSpell
    _chest_event_id = E0915_CHEST_SPELL_16
    _npc_grant_event_id = E0966_NPC_SPELL_16
    _standing_grant_event_id = E1006_FREESTANDING_SPELL_16
    _river_grant_event_id = E1036_HILL_RIVER_SPELL_16
    _hill_grant_event_id = E1036_HILL_RIVER_SPELL_16
    character_replacement_ids = [
        "spell_16_character",
        "freestanding_spell_16_character",
        "hill_river_spell_16_character",
        "npc_spell_16_character",
    ]
    packet_replacement_ids = ["spell_16_elemental_packet"]
    _dialog_id = DI1977_LEARN_SPELL_16
    _autoterm_dialog_id = DI1978_LEARN_SPELL_16_AUTOTERM
    _placement_id = 16


__all__ = ["GenoBlastSpellPrize"]
