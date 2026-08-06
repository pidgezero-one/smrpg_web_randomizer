from __future__ import annotations
from randomizer.data.spells.spells import (BowserCrushSpell)
from randomizer.data.variables.dialog_names import (DI1987_LEARN_SPELL_21, DI1988_LEARN_SPELL_21_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0921_CHEST_SPELL_21, E0971_NPC_SPELL_21, E1015_FREESTANDING_SPELL_21, E1041_HILL_RIVER_SPELL_21)
from randomizer.types.prize import (SpellPrize)


class BowserCrushSpellPrize(SpellPrize):
    _spell = BowserCrushSpell
    _chest_event_id = E0921_CHEST_SPELL_21
    _npc_grant_event_id = E0971_NPC_SPELL_21
    _standing_grant_event_id = E1015_FREESTANDING_SPELL_21
    _river_grant_event_id = E1041_HILL_RIVER_SPELL_21
    _hill_grant_event_id = E1041_HILL_RIVER_SPELL_21
    character_replacement_ids = [
        "spell_21_character",
        "freestanding_spell_21_character",
        "hill_river_spell_21_character",
        "npc_spell_21_character",
    ]
    packet_replacement_ids = ["spell_21_elemental_packet"]
    _dialog_id = DI1987_LEARN_SPELL_21
    _autoterm_dialog_id = DI1988_LEARN_SPELL_21_AUTOTERM
    _placement_id = 21


__all__ = ["BowserCrushSpellPrize"]
