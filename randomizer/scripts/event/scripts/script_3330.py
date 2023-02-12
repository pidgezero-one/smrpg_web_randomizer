# E3330_VOLCANO_1ST_BOSS_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(target=NPC_0, subscript=[ASTransferToObjectXY(MARIO)]),
        Db(bytearray(b"\xc7\x94")),
        CopyVarToVar(from_var=X_COORD_1, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7026),
        CopyVarToVar(from_var=Z_COORD_1, to_var=TEMP_7028),
        Set7000ToObjectCoord(object=MARIO, coord=COORD_F, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702A),
        RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, mod_id=2
        ),
        RunEventAsSubroutine(
            E0840_VOLCANO_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        JmpIfBitSet(VOLCANO_MIDBOSS_DEFEATED, ["EVENT_3330_ret_15"]),
        RunBackgroundEvent(
            event_id=E3346_VOLCANO_1ST_BOSS_SCREEN_TINT,
            return_on_level_exit=True,
            bit_6=True,
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNortheast(),
                ASSetWalkingSpeed(NORMAL),
                ASShiftNortheastSteps(5),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNortheast(),
            ],
        ),
        ActionQueueSync(target=MARIO, subscript=[ASShiftNortheastSteps(3)]),
        RunEventAtReturn(E3331_VOLCANO_1ST_BOSS_FIGHT),
        Return(identifier="EVENT_3330_ret_15"),
    ]
)
