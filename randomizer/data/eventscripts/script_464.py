from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_464_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_464_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_464_enable_controls_until_return_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_464_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_464_run_dialog_3',
        "command": 'run_dialog',
        "args": [763, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_464_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_464_enable_controls_until_return_5',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_464_pause_6',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_464_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
