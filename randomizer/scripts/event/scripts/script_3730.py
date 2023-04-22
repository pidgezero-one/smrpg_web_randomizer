# pylint: disable=C0301

"""E3730_NIMBUS_CASTLE_OCCUPIED_4_PATH_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromSpecificLevel(
            NPC_13, R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA
        ),
        RemoveObjectFromSpecificLevel(
            NPC_14, R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA
        ),
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3730_sequence_setter_1"]),
        JmpIfBitSet(UNKNOWN_STATUE_ROOM_7090_1, ["EVENT_3730_sequence_setter_1"]),
        JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_5, ["EVENT_3730_palette_set_6"]),
        Jmp(["EVENT_3730_sequence_setter_1"]),
        PaletteSet(palette_set=84, row=1, identifier="EVENT_3730_palette_set_6"),
        PauseActionScript(NPC_4),
        PauseActionScript(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromSpecificLevel(
            NPC_1, R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASTransferToXYZF(x=25, y=21, z=3, direction=EAST),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=26, y=22, z=3, direction=EAST),
                ASVisibilityOff(),
            ],
        ),
        RememberLastObject(),
        RunEventAsSubroutine(
            E0824_NIMBUS_CASTLE_OCCUPIED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
            identifier="EVENT_3730_sequence_setter_1",
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
