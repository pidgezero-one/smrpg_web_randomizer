# pylint: disable=C0301

"""E1119_SEASIDE_OCCUPIED_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["EVENT_1119_jmp_if_bit_set_18"]),
        SummonObjectToCurrentLevel(NPC_6),
        SummonObjectToSpecificLevel(NPC_6, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
        JmpIfBitSet(
            SEASIDE_LIBERATED,
            ["EVENT_1119_play_music_default_volume_22"],
            identifier="EVENT_1119_jmp_if_bit_set_18"),
        PlayMusicAtDefaultVolume(M15_HERES_SOME_WEAPONS),
        Jmp(["EVENT_1119_jmp_if_present_in_current_level_25"]),
        Return(),
        PlayMusicAtDefaultVolume(
            M05_SEASIDE_TOWN, identifier="EVENT_1119_play_music_default_volume_22"
        ),
        Jmp(["EVENT_1119_jmp_if_present_in_current_level_25"]),
        Return(),
        JmpIfObjectInCurrentLevel(
            NPC_6,
            ["EVENT_1119_apply_solidity_mod_28"],
            identifier="EVENT_1119_jmp_if_present_in_current_level_25"),
        Jmp(["EVENT_1119_jmp_if_bit_set_33"]),
        Return(),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            mod_id=0,
            identifier="EVENT_1119_apply_solidity_mod_28"),
        Jmp(["EVENT_1119_jmp_if_bit_set_33"]),
        Return(),
        RunEventAsSubroutine(
            E0806_SEASIDE_OCCUPIED_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER,
            identifier="EVENT_1119_sequence_setter_2"),
        FadeInFromBlack(sync=True),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1119_ret_32"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1119_ret_32"]),
        RunEventAsSubroutine(E3904_SEASIDE_TOWN_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1119_ret_32"),
        JmpIfBitClear(
            SEASIDE_BOSS_AVAILABLE,
            ["EVENT_1119_sequence_setter_2"],
            identifier="EVENT_1119_jmp_if_bit_set_33"),
        JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_1119_sequence_setter_2"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=13, y=56, z=2, direction=EAST),
                ASWalkSouthwestSteps(1),
                ASWalkSoutheastSteps(1),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=13, y=57, z=2, direction=EAST),
                ASWalkSouthwestSteps(1),
                ASWalkSoutheastSteps(1),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=14, y=59, z=2, direction=EAST),
                ASWalkSouthwestSteps(1),
                ASWalkSoutheastSteps(1),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=15, y=60, z=2, direction=EAST),
                ASWalkSouthwestSteps(1),
                ASWalkSoutheastSteps(1),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASTransferToXYZF(x=14, y=58, z=2, direction=EAST),
                ASOverwriteSolidity(),
                ASWalkSouthwestSteps(1),
                ASWalkSoutheastSteps(1),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=12, y=63, z=2, direction=EAST),
                ASWalkSouthwestSteps(1),
                ASFaceNortheast(),
            ]),
        SetSyncActionScript(NPC_0, A0147_SEASIDE_HENCHMAN),
        SetSyncActionScript(NPC_1, A0147_SEASIDE_HENCHMAN),
        SetSyncActionScript(NPC_2, A0147_SEASIDE_HENCHMAN),
        SetSyncActionScript(NPC_3, A0147_SEASIDE_HENCHMAN),
        SetSyncActionScript(NPC_4, A0147_SEASIDE_HENCHMAN),
        RunEventAsSubroutine(
            E0806_SEASIDE_OCCUPIED_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(
            SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1119_action_queue_async_42"]
        ),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1119_action_queue_async_42"]),
        RunEventAsSubroutine(E3904_SEASIDE_TOWN_STAR_PIECE_SIGNAL),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetWalkingSpeed(NORMAL),
                ASWalkNortheastSteps(1),
                ASSetSequenceSpeed(NORMAL),
                ASSetWalkingSpeed(SLOW),
                ASWalkNortheastPixels(8),
            ],
            identifier="EVENT_1119_action_queue_async_42"),
        Pause(30),
        ActionQueueAsync(
            target=NPC_4, subscript=[ASSetWalkingSpeed(SLOW), ASWalkSouthwestPixels(5)]
        ),
        Pause(30),
        UnfreezeCamera(),
        ActionQueueAsync(target=NPC_4, subscript=[ASResetProperties()]),
        Pause(30),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(
                    index=4, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(15),
                ASResetProperties(),
                ASSetAllSpeeds(NORMAL),
            ]),
        Pause(30),
        PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkNorthwestSteps(30),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkNorthwestSteps(30),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkNorthwestSteps(30),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkNorthwestSteps(30),
                ASVisibilityOff(),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkNorthwestSteps(30),
                ASVisibilityOff(),
            ]),
        RemoveObjectFromSpecificLevel(
            NPC_0, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP
        ),
        SetBit(SEASIDE_BOSS_SET),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASSetAllSpeeds(NORMAL),
                ASWalkNortheastSteps(1),
                ASSetVRAMPriority(NORMAL_PRIORITY),
            ]),
        Return(),
    ]
)
