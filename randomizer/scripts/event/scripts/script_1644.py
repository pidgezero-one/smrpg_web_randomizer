# E1644_MOLEVILLE_OCCUPIED_EXTERIOR_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 24),
        FadeOutMusicToVolume(duration=1, volume=127),
        JmpIfBitSet(MINECART_CLEARED, ["EVENT_1644_enter_area_18"]),
        JmpIfBitSet(MOLE_DESCENDED, ["EVENT_1644_fade_in_from_black_async_16"]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=20, y=45, z=24, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        SetSyncActionScript(NPC_1, A0160_SEQUENCE_LOOPING_ON),
        Jmp(
            ["EVENT_1644_fade_in_from_black_async_21"],
            identifier="EVENT_1644_fade_in_from_black_async_16",
        ),
        EnterArea(
            room_id=R108_MOLEVILLE_OUTSIDE,
            face_direction=SOUTHWEST,
            x=17,
            y=44,
            z=4,
            identifier="EVENT_1644_enter_area_18",
        ),
        JmpIfBitClear(TEMP_7042_1, ["EVENT_1644_fade_in_from_black_async_21"]),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R108_MOLEVILLE_OUTSIDE, mod_id=0
        ),
        FadeInFromBlack(
            sync=False, identifier="EVENT_1644_fade_in_from_black_async_21"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1644_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1644_ret_26"]),
        RunEventAsSubroutine(E3897_MOLEVILLE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1644_ret_26"),
    ]
)
