from __future__ import annotations
from randomizer.data.spells.spells import (PoisonGasSpell)
from randomizer.data.variables.dialog_names import (DI1983_LEARN_SPELL_19, DI1984_LEARN_SPELL_19_AUTOTERM)
from randomizer.data.variables.event_script_names import (E0919_CHEST_SPELL_19, E0969_NPC_SPELL_19, E1013_FREESTANDING_SPELL_19, E1039_HILL_RIVER_SPELL_19)
from randomizer.types.prize import (SpellPrize)


class PoisonGasSpellPrize(SpellPrize):
    _spell = PoisonGasSpell
    _chest_event_id = E0919_CHEST_SPELL_19
    _npc_grant_event_id = E0969_NPC_SPELL_19
    _standing_grant_event_id = E1013_FREESTANDING_SPELL_19
    _river_grant_event_id = E1039_HILL_RIVER_SPELL_19
    _hill_grant_event_id = E1039_HILL_RIVER_SPELL_19
    character_replacement_ids = [
        "spell_19_character",
        "freestanding_spell_19_character",
        "hill_river_spell_19_character",
        "npc_spell_19_character",
    ]
    packet_replacement_ids = ["spell_19_elemental_packet"]
    _dialog_id = DI1983_LEARN_SPELL_19
    _autoterm_dialog_id = DI1984_LEARN_SPELL_19_AUTOTERM
    _placement_id = 19


__all__ = ["PoisonGasSpellPrize"]
