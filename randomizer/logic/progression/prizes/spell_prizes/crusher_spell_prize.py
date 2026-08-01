from __future__ import annotations
from randomizer.data.spells.spells import (CrusherSpell)
from randomizer.data.variables.dialog_names import (DI1985_LEARN_SPELL_20, DI1986_LEARN_SPELL_20_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0920_CHEST_SPELL_20, E0970_NPC_SPELL_20, E1014_FREESTANDING_SPELL_20, E1040_HILL_RIVER_SPELL_20)
from randomizer.types.prize import (SpellPrize)


class CrusherSpellPrize(SpellPrize):
    _spell = CrusherSpell
    _chest_event_id = E0920_CHEST_SPELL_20
    _npc_grant_event_id = E0970_NPC_SPELL_20
    _standing_grant_event_id = E1014_FREESTANDING_SPELL_20
    _river_grant_event_id = E1040_HILL_RIVER_SPELL_20
    _hill_grant_event_id = E1040_HILL_RIVER_SPELL_20
    character_replacement_ids = [
        "spell_20_character",
        "freestanding_spell_20_character",
        "hill_river_spell_20_character",
        "npc_spell_20_character",
    ]
    packet_replacement_ids = ["spell_20_elemental_packet"]
    _dialog_id = DI1985_LEARN_SPELL_20
    _autoterm_dialog_id = DI1986_LEARN_SPELL_20_AUTOTERM
    _placement_id = 20


__all__ = ["CrusherSpellPrize"]
