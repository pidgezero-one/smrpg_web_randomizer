# pylint: disable=C0301

"""E3788_BEAN_VALLEY_WEST_VINE_ROOM_SUMMON_PLATFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_0,
            R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02,
            ["EVENT_3584_ret_0"]),
        JmpIfMarioInAir(["EVENT_3584_ret_0"]),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Db(bytearray(b"\xc7\x80")),
        JmpIfVarEqualsConst(Z_COORD_1, 40, ["EVENT_3788_pause_6"]),
        JmpToEvent(E3584_BANK_20_RETURN_EVENT),
        Pause(1, identifier="EVENT_3788_pause_6"),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_3584_ret_0"]),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3788_set_7000_to_pressed_button_11"]
        ),
        Jmp(["EVENT_3788_pause_6"]),
        Set7000ToPressedButton(identifier="EVENT_3788_set_7000_to_pressed_button_11"),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_3584_ret_0"]),
        PlaySound(sound=SO014_FLOWER, channel=6),
        SummonObjectToCurrentLevel(NPC_0),
        SummonObjectToSpecificLevel(
            NPC_0, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02
        ),
        Return(),
    ]
)
