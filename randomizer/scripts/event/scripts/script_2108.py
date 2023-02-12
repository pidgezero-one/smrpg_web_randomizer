# E2108_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_FIGHT_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(target=NPC_2, subscript=[ASShiftSouthPixels(7)]),
        PaletteSet(palette_set=84, row=1),
        JmpIfBitClear(STATUE_KEEPER_FIGHT_PRESENT, ["EVENT_2108_jmp_if_bit_set_14"]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASShiftNortheastPixels(8), ASFaceSoutheast(), ASVisibilityOn()],
        ),
        JmpIfBitSet(
            TEMP_7044_7,
            ["EVENT_2108_run_event_as_subroutine_17"],
            identifier="EVENT_2108_jmp_if_bit_set_14",
        ),
        RunEventAsSubroutine(
            E0818_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpToSubroutine(
            ["EVENT_2108_jmp_if_bit_sub_0"],
            identifier="EVENT_2108_run_event_as_subroutine_17",
        ),
        RunEventAsSubroutine(
            E0818_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2108_ret_18"]),
        RunEventAsSubroutine(E3912_NIMBUS_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2108_ret_18"),
        JmpIfBitSet(
            NIMBUS_LAND_LIBERATED,
            ["EVENT_2108_play_music_default_volume_sub_3"],
            identifier="EVENT_2108_jmp_if_bit_sub_0",
        ),
        PlayMusicAtDefaultVolume(M61_VALENTINA),
        Return(),
        PlayMusicAtDefaultVolume(
            M50_NIMBUS_LAND, identifier="EVENT_2108_play_music_default_volume_sub_3"
        ),
        Return(),
    ]
)
