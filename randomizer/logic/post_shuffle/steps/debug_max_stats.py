"""Debug-mode max stats. Runs AFTER shuffling and again after results are applied."""

from __future__ import annotations
from randomizer.data.items.items import SafetyRingItem, SignalRingItem
from randomizer.logic.progression.prizelocations import StartingCharacter1
from randomizer.types.prize import CharacterPrize
from smrpgpatchbuilder.datatypes.items.enums import EffectType
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status


def apply_debug_max_stats(world: GameWorld) -> None:
    """Max out all character starting stats if debug mode is enabled."""
    if not world.settings.debug_mode:
        return


    # Reshape Signal Ring to mirror Safety Ring's protective stats while
    # retaining its signature +10 speed bonus.
    signal_ring = world.get_item(SignalRingItem)
    assert isinstance(signal_ring, SignalRingItem)
    signal_ring.set_speed(10)
    signal_ring.set_defense(5)
    signal_ring.set_magic_defense(5)
    signal_ring.set_prevent_ko(True)
    signal_ring.set_effect_type(EffectType.PROTECTION)
    signal_ring.set_elemental_immunities(
        [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]
    )
    signal_ring.set_status_immunities(
        [
            Status.MUTE,
            Status.SLEEP,
            Status.POISON,
            Status.FEAR,
            Status.BERSERK,
            Status.MUSHROOM,
            Status.SCARECROW,
        ]
    )
    # Debug-only combat boost: give the Signal Ring and Safety Ring a big attack
    # and magic-attack bump so test parties hit hard. Debug mode only — this
    # whole function early-returns when debug mode is off.
    signal_ring.set_attack(100)
    signal_ring.set_magic_attack(100)
    safety_ring = world.get_item(SafetyRingItem)
    assert isinstance(safety_ring, SafetyRingItem)
    safety_ring.set_attack(100)
    safety_ring.set_magic_attack(100)

    # apply_equipment_settings already rebuilt every equipment description from
    # the (vanilla) Signal Ring stats before this reshape ran, so regenerate
    # both here to reflect the copied Safety Ring stats and the debug boosts.
    signal_ring.set_description(signal_ring.build_equipment_description())
    safety_ring.set_description(safety_ring.build_equipment_description())

    # Identify which ally was placed in the StartingCharacter1 slot so we
    # can hand them the Signal Ring instead of a Safety Ring.
    starter_index: int | None = None
    starter_loc = world.get_location(StartingCharacter1)
    if starter_loc is not None and isinstance(starter_loc.prize, CharacterPrize):
        starter_index = starter_loc.prize.ally.index

    # Max out starting stats for all allies
    for ally in world.allies._allies:
        ally.starting_max_hp = 999
        ally.starting_current_hp = 999
        ally.starting_attack = 255
        ally.starting_defense = 255
        ally.starting_mg_attack = 255
        ally.starting_mg_defense = 255
        ally.starting_level = 30
        ally.starting_experience = 9999
        if starter_index is not None and ally.index == starter_index:
            ally.starting_accessory = SignalRingItem
        else:
            ally.starting_accessory = SafetyRingItem

        # Learn all spells that were shuffled to this ally
        # Collect spells from level-ups and add to starting_magic
        all_spells = list(ally.starting_magic)  # Start with existing starting spells
        for level_up in ally.levels:
            if level_up.spell_learned is not None:
                if level_up.spell_learned not in all_spells:
                    all_spells.append(level_up.spell_learned)
        ally.starting_magic = all_spells


__all__ = ["apply_debug_max_stats"]
