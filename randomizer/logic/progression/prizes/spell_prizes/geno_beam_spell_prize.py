from __future__ import annotations
from randomizer.data.spells.spells import (GenoBeamSpell)
from randomizer.data.variables.dialog_names import (DI1971_LEARN_SPELL_13, DI1972_LEARN_SPELL_13_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0912_CHEST_SPELL_13, E0964_NPC_SPELL_13, E1004_FREESTANDING_SPELL_13, E1034_HILL_RIVER_SPELL_13)
from randomizer.types.prize import (SpellPrize)


class GenoBeamSpellPrize(SpellPrize):
    _spell = GenoBeamSpell
    _chest_event_id = E0912_CHEST_SPELL_13
    _npc_grant_event_id = E0964_NPC_SPELL_13
    _standing_grant_event_id = E1004_FREESTANDING_SPELL_13
    _river_grant_event_id = E1034_HILL_RIVER_SPELL_13
    _hill_grant_event_id = E1034_HILL_RIVER_SPELL_13
    character_replacement_ids = [
        "spell_13_character",
        "freestanding_spell_13_character",
        "hill_river_spell_13_character",
        "npc_spell_13_character",
    ]
    packet_replacement_ids = ["spell_13_elemental_packet"]
    _dialog_id = DI1971_LEARN_SPELL_13
    _autoterm_dialog_id = DI1972_LEARN_SPELL_13_AUTOTERM
    _placement_id = 13


__all__ = ["GenoBeamSpellPrize"]
