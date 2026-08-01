from __future__ import annotations
from randomizer.data.spells.spells import (ShockerSpell)
from randomizer.data.variables.dialog_names import (DI1965_LEARN_SPELL_10, DI1966_LEARN_SPELL_10_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0909_CHEST_SPELL_10, E0961_NPC_SPELL_10, E1001_FREESTANDING_SPELL_10, E1031_HILL_RIVER_SPELL_10)
from randomizer.types.prize import (SpellPrize)


class ShockerSpellPrize(SpellPrize):
    _spell = ShockerSpell
    _chest_event_id = E0909_CHEST_SPELL_10
    _npc_grant_event_id = E0961_NPC_SPELL_10
    _standing_grant_event_id = E1001_FREESTANDING_SPELL_10
    _river_grant_event_id = E1031_HILL_RIVER_SPELL_10
    _hill_grant_event_id = E1031_HILL_RIVER_SPELL_10
    character_replacement_ids = [
        "spell_10_character",
        "freestanding_spell_10_character",
        "hill_river_spell_10_character",
        "npc_spell_10_character",
    ]
    packet_replacement_ids = ["spell_10_elemental_packet"]
    _dialog_id = DI1965_LEARN_SPELL_10
    _autoterm_dialog_id = DI1966_LEARN_SPELL_10_AUTOTERM
    _placement_id = 10


__all__ = ["ShockerSpellPrize"]
