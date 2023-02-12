# E3293_SHIP_BULLET_COLLISION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioOnAnObjectOrNot(
            ["EVENT_3293_pause_action_script_5", "EVENT_3293_pause_action_script_8"]
        ),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        RunBackgroundEvent(
            event_id=E3294_SHIP_BULLET_COLLISION_BACKGROUND, return_on_level_exit=True
        ),
        Return(),
        PauseActionScript(MEM_70A8, identifier="EVENT_3293_pause_action_script_5"),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(
                    cant_pass_walls=True, bit_4=True, cant_walk_through=True
                ),
                ASPlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
                ASJumpToHeight(height=0, silent=True),
                ASFloatingOn(),
                ASPause(20),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        Return(),
        PauseActionScript(MEM_70A8, identifier="EVENT_3293_pause_action_script_8"),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(
                    cant_pass_walls=True, bit_4=True, cant_walk_through=True
                ),
                ASPlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
                ASJumpToHeight(height=48, silent=True),
                ASFloatingOn(),
                ASPause(30),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        Return(),
    ]
)
