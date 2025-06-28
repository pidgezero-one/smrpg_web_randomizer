"""Randomization logic for item placement."""

from random import choices
from randomizer.entities.progress_locations.characters_recruited import (
    StartingCharacter1,
    StartingCharacter2,
    StartingCharacter3,
    StartingCharacter4,
    StartingCharacter5,
)
from randomizer.entities.progress_locations.flag_locations import (
    MariosPadBed,
    RoseTownSign,
    YosterIsleGoal,
)
from randomizer.entities.progress_locations.item_locations import (
    MonstroFirstSuperJumpReward,
    MonstroSecondSuperJumpReward,
    BucketGirlReward,
)
from randomizer.types.dialogs.ids.dialog_ids import (
    DI1107_RESERVED_FOR_BIGBOOFLAG_HINT,
    DI1108_RESERVED_FOR_DRYBONESFLAG_HINT,
    DI1109_RESERVED_FOR_GREAPERFLAG_HINT,
)
from randomizer.data.npcs.npcs import Empty
from randomizer.types.overworld_scripts.action_scripts.commands.commands import (
    WalkEastPixels,
    WalkNorthPixels,
    WalkSouthPixels,
    WalkWestPixels,
)
from randomizer.types.overworld_scripts.action_scripts.ids.script_ids import (
    A0324_INVISIBLE_ITEM_SHIFT_1,
    A0325_INVISIBLE_ITEM_SHIFT_2,
    A0326_INVISIBLE_ITEM_SHIFT_3,
)
from randomizer.types.overworld_scripts.arguments.area_objects import (
    AREAOBJECT_FROM_NPC_ID,
)
from randomizer.types.overworld_scripts.event_scripts.commands.commands import (
    RunEventAsSubroutine,
    SummonObjectToSpecificLevel,
)
from randomizer.types.overworld_scripts.event_scripts.ids.script_ids import (
    E0088_INVISIBLE_ITEM_CHECK_1_CONTAINER,
    E0089_INVISIBLE_ITEM_CHECK_2_CONTAINER,
    E0090_INVISIBLE_ITEM_CHECK_3_CONTAINER,
    E0091_INVISIBLE_ITEM_SUMMONER,
    E0192_GATING_AND_PARTY_JOIN_LOGIC,
)
from randomizer.types.overworld_scripts.ids.room_names import (
    R034_YOSTER_ISLE,
    R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
    R084_ROSE_TOWN_OUTSIDE,
    R189_MARIOS_PIPEHOUSE,
)
from randomizer.types.progress_locations.classes import (
    InvisibleItemCandidate,
)
from randomizer.types.rooms.classes import RegularNPC
from randomizer.types.rooms.enums import EventInitiator
from randomizer.types.world import GameWorld
from randomizer.types.world.flags import LearnableSpells, AvailableSpells


from randomizer.entities.progress_locations import (
    flag_locations_table,
)
from randomizer.types.world.flags.enums import FireworksOptions
from randomizer.types.world.flags.flags import (
    BucketWarp,
    EnabledRegularChecks,
    FireworksSetting,
    InvisibleFlagsSetting,
    SkipMustyFearsSequence,
    StartingCharacters,
)


def _set_up_invisible_items(world: GameWorld) -> None:
    invisible_npcs_to_summon = []

    if world.settings.is_boolean_flag_enabled(InvisibleFlagsSetting):
        # Replace the three Musty Fears locations with three randomly selected
        # invisible item locations.
        items = [
            world.get_location_instance(MariosPadBed).original_item,
            world.get_location_instance(RoseTownSign).original_item,
            world.get_location_instance(YosterIsleGoal).original_item,
        ]
        check_containers = [
            E0088_INVISIBLE_ITEM_CHECK_1_CONTAINER,
            E0089_INVISIBLE_ITEM_CHECK_2_CONTAINER,
            E0090_INVISIBLE_ITEM_CHECK_3_CONTAINER,
        ]
        shift_action_scripts = [
            A0324_INVISIBLE_ITEM_SHIFT_1,
            A0325_INVISIBLE_ITEM_SHIFT_2,
            A0326_INVISIBLE_ITEM_SHIFT_3,
        ]
        clue_dialog_ids = [
            DI1108_RESERVED_FOR_DRYBONESFLAG_HINT,
            DI1109_RESERVED_FOR_GREAPERFLAG_HINT,
            DI1107_RESERVED_FOR_BIGBOOFLAG_HINT,
        ]

        world.remove_locations([MariosPadBed, RoseTownSign, YosterIsleGoal])

        new_locations = choices(flag_locations_table, k=3)
        world.add_locations(new_locations)

        # Set these new locations up to still donate the three flags to the shuffler.
        for location, item, container_event, shift_script_id, dialog_id in zip(
            new_locations,
            items,
            check_containers,
            shift_action_scripts,
            clue_dialog_ids,
        ):
            instance = world.get_location_instance(location)
            assert isinstance(instance, InvisibleItemCandidate) and item is not None
            instance.set_original_item(item)
            instance.set_container_event(container_event)

            # place the npcs in the rooms
            for room_id in instance.room_ids:
                invisible_npcs_to_summon.append(
                    (room_id, len(world.rooms[room_id].objects))
                )
                world.rooms[room_id].add_object(
                    RegularNPC(
                        occupant=Empty,
                        initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
                        event_script=container_event,
                        action_script=shift_script_id,
                        visible=False,
                        x=instance.x_coord,
                        y=instance.y_coord,
                        z=instance.z_coord,
                        show_shadow=False,
                        acute_axis=15,
                        obtuse_axis=15,
                        height=15,
                    )
                )
            # populate the shifter script
            script = world.action_scripts.scripts[shift_script_id]
            x_shift = instance.x_shift
            y_shift = instance.y_shift
            if x_shift > 0:
                script.insert_before_nth_command(0, WalkEastPixels(x_shift))
            elif x_shift < 0:
                script.insert_before_nth_command(0, WalkWestPixels(x_shift * -1))
            if y_shift > 0:
                script.insert_before_nth_command(0, WalkSouthPixels(y_shift))
            elif y_shift < 0:
                script.insert_before_nth_command(0, WalkNorthPixels(y_shift * -1))

            # update hint dialog
            world.dialogs.replace_dialog(dialog_id, instance.clue_text)
    else:
        invisible_npcs_to_summon = [
            (R189_MARIOS_PIPEHOUSE, 1),
            (R084_ROSE_TOWN_OUTSIDE, 13),
            (R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 3),
            (R034_YOSTER_ISLE, 16),
        ]

    # populate the script that activates all invisible item checks
    script = world.event_scripts.get_script_by_id(E0091_INVISIBLE_ITEM_SUMMONER)
    for level_id, npc_id in invisible_npcs_to_summon:
        area_object = AREAOBJECT_FROM_NPC_ID[npc_id]
        script.insert_before_nth_command(
            0, SummonObjectToSpecificLevel(area_object, level_id)
        )

    # if invisible items aren't gated, run the summoner as a subroutine at launch
    if world.settings.is_boolean_flag_enabled(SkipMustyFearsSequence):
        script = world.event_scripts.get_script_by_id(E0192_GATING_AND_PARTY_JOIN_LOGIC)
        script.insert_before_nth_command(
            0, RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER)
        )


def finalize_location_list(world: GameWorld) -> None:
    """Exclude certain items from shuffle consideration depending on settings."""

    # Don't include super jump rewards if the spell isn't in the seed.
    # Player beware, this excludes Super Suit and Attack Scarf from special equip shuffle.
    if LearnableSpells.SUPER_JUMP in world.settings.get_flag(AvailableSpells).disabled:
        world.remove_locations(
            [MonstroFirstSuperJumpReward, MonstroSecondSuperJumpReward]
        )

    # Bucket girl gives nothing when her request is repeatable.
    if world.settings.is_flag_value(
        FireworksSetting, FireworksOptions.VANILLA
    ) or not world.settings.is_boolean_flag_enabled(BucketWarp):
        world.remove_locations([BucketGirlReward])

    # Set up the invisible item locations.
    _set_up_invisible_items(world)

    # Exclude starting character locations depending on player's settings.
    total_starting_characters = world.settings.get_flag(StartingCharacters).value
    starter_locations = [
        StartingCharacter1,
        StartingCharacter2,
        StartingCharacter3,
        StartingCharacter4,
        StartingCharacter5,
    ]
    excludes = starter_locations[total_starting_characters:]
    world.remove_locations(excludes)

    # Set up progress exclusions, which are accessible but can't contain required items
    all_locations = world.item_locations + world.boss_star_pieces
    disabled_enums = world.settings.get_flag(EnabledRegularChecks).disabled
    for location in all_locations:
        if location.name_enum in disabled_enums:
            location.set_excluded(True)
