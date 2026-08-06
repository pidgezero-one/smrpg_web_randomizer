from __future__ import annotations
from randomizer.data.spells.spells import (PsychBombSpell)
from randomizer.data.variables.dialog_names import (DI1999_LEARN_SPELL_27, DI2000_LEARN_SPELL_27_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0927_CHEST_SPELL_27, E0977_NPC_SPELL_27, E1021_FREESTANDING_SPELL_27, E1047_HILL_RIVER_SPELL_27)
from randomizer.types.prize import (SpellPrize)


class PsychBombSpellPrize(SpellPrize):
    _spell = PsychBombSpell
    _chest_event_id = E0927_CHEST_SPELL_27
    _npc_grant_event_id = E0977_NPC_SPELL_27
    _standing_grant_event_id = E1021_FREESTANDING_SPELL_27
    _river_grant_event_id = E1047_HILL_RIVER_SPELL_27
    _hill_grant_event_id = E1047_HILL_RIVER_SPELL_27
    character_replacement_ids = [
        "spell_27_character",
        "freestanding_spell_27_character",
        "hill_river_spell_27_character",
        "npc_spell_27_character",
    ]
    packet_replacement_ids = ["spell_27_elemental_packet"]
    _dialog_id = DI1999_LEARN_SPELL_27
    _autoterm_dialog_id = DI2000_LEARN_SPELL_27_AUTOTERM
    _placement_id = 27


__all__ = ["PsychBombSpellPrize"]
