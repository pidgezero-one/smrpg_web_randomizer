"""Equipment and spell element setup."""
from __future__ import annotations
import random
from typing import (TYPE_CHECKING)

from smrpgpatchbuilder.datatypes.spells.enums import Element, Status, TempStatBuff
from ...types.item import Equipment

from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.commands import (PlaySound, ScreenFlash)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.flash_colours import WHITE, RED, AQUA, YELLOW

from ...data.variables.battle_sfx_names import (
    S0018_SUPER_JUMP_HIT_1,
    S0032_FIRE_BURN,
    S0078_TIMED_STAT_BOOST,
    S0095_BOWSERS_CRUSHER,
    S0100_ELECTROSHOCK_SPARKS,
    S0103_CRYSTAL_HITS,
)
from ...types.flags import (
        InfuseSpellElements, CharacterSpellElements,
        EquipmentProperties, EquipmentPropertiesOptions,
        IgnoreNamesakeProperties, EquipmentCharacters, EquipmentCharactersOptions,
    )
from ...data.spells.spells import (
        GenoBeamSpell, GenoFlashSpell, PsychBombSpell, CrusherSpell, BowserCrushSpell,
        JumpSpell, SuperJumpSpell, UltraJumpSpell,
        FireOrbSpell, SuperFlameSpell, UltraFlameSpell,
    )
from ...data.items.items import (
        # Armor sets
        ShirtItem, PantsItem, ThickShirtItem, ThickPantsItem,
        MegaShirtItem, MegaPantsItem, MegaCapeItem,
        HappyShirtItem, HappyPantsItem, HappyCapeItem, HappyShellItem,
        PolkaDressItem, CourageShellItem,
        SailorShirtItem, SailorPantsItem, SailorCapeItem, NauticaDressItem,
        FuzzyShirtItem, FuzzyPantsItem, FuzzyCapeItem, FuzzyDressItem,
        FireShirtItem, FirePantsItem, FireCapeItem, FireShellItem, FireDressItem,
        HeroShirtItem, PrincePantsItem, RoyalDressItem, HealShellItem, StarCapeItem,
        # Weapons
        FroggieStickItem, RibbitStickItem, ParasolItem,
        # Accessories
        WakeUpPinItem, AntidotePinItem, TrueformPinItem, FearlessPinItem,
    )
from ..shufflers.equipment import (
        randomize_equipment_properties,
        randomize_equipment_characters,
        reprice_equipment_by_rank,
    )

JUMP_HIT_SOUND_BY_ELEMENT = {
    Element.FIRE: S0032_FIRE_BURN,
    Element.THUNDER: S0100_ELECTROSHOCK_SPARKS,
    Element.ICE: S0103_CRYSTAL_HITS,
}

FIRE_ORB_HIT_SOUND_BY_ELEMENT = {
    Element.ICE: S0103_CRYSTAL_HITS,
    Element.THUNDER: S0100_ELECTROSHOCK_SPARKS,
    Element.JUMP: S0018_SUPER_JUMP_HIT_1,
}

FLAME_HIT_SOUND_BY_ELEMENT = {
    Element.ICE: S0103_CRYSTAL_HITS,
    Element.THUNDER: S0078_TIMED_STAT_BOOST,
    Element.JUMP: S0095_BOWSERS_CRUSHER,
}

FLASH_HIT_SOUND_BY_ELEMENT = {
    Element.ICE: S0103_CRYSTAL_HITS,
    Element.THUNDER: S0078_TIMED_STAT_BOOST,
    Element.JUMP: S0095_BOWSERS_CRUSHER,
}

CRUSH_HIT_SOUND_BY_ELEMENT = {
    Element.FIRE: S0032_FIRE_BURN,
    Element.ICE: S0103_CRYSTAL_HITS,
    Element.THUNDER: S0100_ELECTROSHOCK_SPARKS,
}

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def apply_equipment_settings(world: GameWorld) -> None:
    """Apply equipment and spell element settings.

    This configures:
    - Spell element infusion (InfuseSpellElements)
    - Random character spell elements (CharacterSpellElements)
    - Equipment property enhancements (EquipmentProperties SOME mode)
    - Equipment property randomization (EquipmentProperties RANDOM mode)
    - Namesake property enforcement (pins, etc.)
    - Equipment character restrictions
    """

    # Spell element infusion
    if world.settings.isflag_enabled(InfuseSpellElements):
        world.get_spell(GenoBeamSpell).set_element(Element.ICE)
        world.get_spell(GenoFlashSpell).set_element(Element.FIRE)
        world.get_spell(PsychBombSpell).set_element(Element.FIRE)
        world.get_spell(CrusherSpell).set_element(Element.JUMP)
        world.get_spell(BowserCrushSpell).set_element(Element.JUMP)

    # Random character spell elements
    if world.settings.isflag_enabled(CharacterSpellElements):
        spells_to_update = [
            s for s in world.spells.spells if s.element != Element.NONE
        ]
        for spell in spells_to_update:
            spell.set_element(
                random.choice([Element.ICE, Element.FIRE, Element.JUMP, Element.THUNDER])
            )
            if isinstance(spell, BowserCrushSpell):
                world.battle_animations[0x35].get_command_by_name("bowser_crush_colour", ScreenFlash).set_colour(
                    AQUA if spell.element == Element.ICE else
                    RED if spell.element == Element.FIRE else
                    WHITE if spell.element == Element.THUNDER else YELLOW
                )
                new_sound = CRUSH_HIT_SOUND_BY_ELEMENT.get(spell.element)
                if new_sound is not None:
                    world.battle_animations[0x35].get_command_by_name(
                        "bowser_crush_sfx", PlaySound
                    ).set_sound(new_sound)
            elif isinstance(spell, JumpSpell):
                new_sound = JUMP_HIT_SOUND_BY_ELEMENT.get(spell.element)
                if new_sound is not None:
                    world.battle_animations[0x35].get_command_by_name(
                        "jump_hit_sound", PlaySound
                    ).set_sound(new_sound)
            elif isinstance(spell, (SuperJumpSpell, UltraJumpSpell)):
                new_sound = JUMP_HIT_SOUND_BY_ELEMENT.get(spell.element)
                if new_sound is not None:
                    prefix = "super_jump" if isinstance(spell, SuperJumpSpell) else "ultra_jump"
                    for i in range(1, 6):
                        world.battle_animations[0x35].get_command_by_name(
                            f"{prefix}_hit_{i}_sound", PlaySound
                        ).set_sound(new_sound)
            elif isinstance(spell, FireOrbSpell):
                new_sound = FIRE_ORB_HIT_SOUND_BY_ELEMENT.get(spell.element)
                if new_sound is not None:
                    for i in range(1, 3):
                        world.battle_animations[0x35].get_command_by_name(
                            f"fire_orb_hit_{i}_sound", PlaySound
                        ).set_sound(new_sound)
            elif isinstance(spell, (SuperFlameSpell, UltraFlameSpell)):
                new_sound = FLAME_HIT_SOUND_BY_ELEMENT.get(spell.element)
                if new_sound is not None:
                    prefix = "super_flame" if isinstance(spell, SuperFlameSpell) else "ultra_flame"
                    for i in range(1, 3):
                        world.battle_animations[0x35].get_command_by_name(
                            f"{prefix}_hit_{i}_sound", PlaySound
                        ).set_sound(new_sound)
            elif isinstance(spell, (GenoFlashSpell)):
                new_sound = FLASH_HIT_SOUND_BY_ELEMENT.get(spell.element)
                if new_sound is not None:
                    world.battle_animations[0x35].get_command_by_name(
                        "geno_flash_sfx", PlaySound
                    ).set_sound(new_sound)

    # Equipment properties - SOME mode (specific enhancements)
    if world.settings.is_flag_value(
        EquipmentProperties, EquipmentPropertiesOptions.SOME
    ):
        # Mushroom immunity for basic gear
        world.items.get_by_type(ShirtItem).append_status_immunity(Status.MUSHROOM)
        world.items.get_by_type(PantsItem).append_status_immunity(Status.MUSHROOM)

        # Defense buffs for thick gear
        world.items.get_by_type(ThickShirtItem).append_temp_buff(TempStatBuff.DEFENSE)
        world.items.get_by_type(ThickPantsItem).append_temp_buff(TempStatBuff.DEFENSE)

        # Magic defense buffs for mega gear
        world.items.get_by_type(MegaShirtItem).append_temp_buff(TempStatBuff.MAGIC_DEFENSE)
        world.items.get_by_type(MegaPantsItem).append_temp_buff(TempStatBuff.MAGIC_DEFENSE)
        world.items.get_by_type(MegaCapeItem).append_temp_buff(TempStatBuff.MAGIC_DEFENSE)

        # KO protection for happy gear
        world.items.get_by_type(HappyShirtItem).set_prevent_ko(True)
        world.items.get_by_type(HappyPantsItem).set_prevent_ko(True)
        world.items.get_by_type(HappyCapeItem).set_prevent_ko(True)
        world.items.get_by_type(HappyShellItem).set_prevent_ko(True)
        world.items.get_by_type(PolkaDressItem).set_prevent_ko(True)

        # Fear immunity for courage shell
        world.items.get_by_type(CourageShellItem).append_status_immunity(Status.FEAR)

        # Ice immunity for sailor gear
        world.items.get_by_type(SailorShirtItem).append_elemental_immunity(Element.ICE)
        world.items.get_by_type(SailorPantsItem).append_elemental_immunity(Element.ICE)
        world.items.get_by_type(SailorCapeItem).append_elemental_immunity(Element.ICE)
        world.items.get_by_type(NauticaDressItem).append_elemental_immunity(Element.ICE)

        # Thunder immunity for fuzzy gear
        world.items.get_by_type(FuzzyShirtItem).append_elemental_immunity(Element.THUNDER)
        world.items.get_by_type(FuzzyPantsItem).append_elemental_immunity(Element.THUNDER)
        world.items.get_by_type(FuzzyCapeItem).append_elemental_immunity(Element.THUNDER)
        world.items.get_by_type(FuzzyDressItem).append_elemental_immunity(Element.THUNDER)

        # Fire immunity for fire gear
        world.items.get_by_type(FireShirtItem).append_elemental_immunity(Element.FIRE)
        world.items.get_by_type(FirePantsItem).append_elemental_immunity(Element.FIRE)
        world.items.get_by_type(FireCapeItem).append_elemental_immunity(Element.FIRE)
        world.items.get_by_type(FireShellItem).append_elemental_immunity(Element.FIRE)
        world.items.get_by_type(FireDressItem).append_elemental_immunity(Element.FIRE)

        # Status immunities for special gear
        world.items.get_by_type(HeroShirtItem).append_status_immunity(Status.SCARECROW)
        world.items.get_by_type(PrincePantsItem).append_status_immunity(Status.MUTE)
        world.items.get_by_type(RoyalDressItem).append_status_immunity(Status.SLEEP)
        world.items.get_by_type(HealShellItem).append_status_immunity(Status.POISON)
        world.items.get_by_type(StarCapeItem).append_status_immunity(Status.BERSERK)

        # Convert physical weapons to magic weapons
        froggie_stick = world.items.get_by_type(FroggieStickItem)
        froggie_stick.set_magic_attack(froggie_stick.attack)
        froggie_stick.set_attack(0)

        ribbit_stick = world.items.get_by_type(RibbitStickItem)
        ribbit_stick.set_magic_attack(ribbit_stick.attack)
        ribbit_stick.set_attack(0)

        parasol = world.items.get_by_type(ParasolItem)
        parasol.set_magic_attack(parasol.attack)
        parasol.set_attack(0)

    # Equipment properties - RANDOM mode
    elif world.settings.is_flag_value(
        EquipmentProperties, EquipmentPropertiesOptions.RANDOM
    ):
        randomize_equipment_properties(world)

    # Namesake properties (pins that should do what their name implies)
    if not world.settings.isflag_enabled(IgnoreNamesakeProperties):
        world.items.get_by_type(WakeUpPinItem).append_status_immunity(Status.SLEEP)
        world.items.get_by_type(WakeUpPinItem).append_status_immunity(Status.MUTE)
        world.items.get_by_type(AntidotePinItem).append_status_immunity(Status.POISON)
        world.items.get_by_type(TrueformPinItem).append_status_immunity(Status.MUSHROOM)
        world.items.get_by_type(TrueformPinItem).append_status_immunity(Status.SCARECROW)
        world.items.get_by_type(FearlessPinItem).append_status_immunity(Status.FEAR)

        # Ensure at least 4 items have KO protection
        has_ko_protection = [
            i for i in world.items.items if isinstance(i, Equipment) and i.prevent_ko
        ]
        if len(has_ko_protection) < 4:
            more_ko_protections = random.sample(
                [
                    i
                    for i in world.items.items
                    if isinstance(i, Equipment) and not i.prevent_ko
                ],
                4 - len(has_ko_protection),
            )
            for i in more_ko_protections:
                i.set_prevent_ko(True)

    # Equipment character restrictions
    equip_chars_setting = world.settings.get_flag(EquipmentCharacters).selected
    if equip_chars_setting != EquipmentCharactersOptions.VANILLA:
        randomize_equipment_characters(world, equip_chars_setting)

    # Update all equipment descriptions to reflect any property changes
    # This ensures SOME mode, namesake properties, and other modifications are reflected
    for item in world.items.items:
        if isinstance(item, Equipment):
            item.set_description(item.build_equipment_description())

    # Reprice equipment from combat rank in every mode. Vanilla prices are not
    # power-ordered, and items vanilla never sells carry junk placeholder prices
    # that shop shuffling would otherwise honour at face value.
    reprice_equipment_by_rank(world)
