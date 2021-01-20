from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1628_jmp_fork_mario_on_object_0',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1628_set_7000_to_pressed_button_6', 'EVENT_1628_set_7000_to_pressed_button_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 4, 'EVENT_1628_run_dialog_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_run_dialog_2',
        "command": 'run_dialog',
        "args": [1157, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_run_dialog_4',
        "command": 'run_dialog',
        "args": [1162, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_set_7000_to_pressed_button_6',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_mem_7000_and_const_7',
        "command": 'mem_7000_and_const',
        "args": [0x00f0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 240, 'EVENT_1536_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1628_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
