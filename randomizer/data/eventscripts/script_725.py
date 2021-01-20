from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_725_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x705d, 1, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_725_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_725_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_725_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_725_run_dialog_4',
        "command": 'run_dialog',
        "args": [2309, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_725_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_725_action_queue_async_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_725_action_queue_async_5_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_725_action_queue_async_5_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_725_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_725_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_725_action_queue_async_5_SUBSCRIPT_floating_off_4',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_725_action_queue_async_5_SUBSCRIPT_walk_to_xy_coords_5',
                "command": 'walk_to_xy_coords',
                "args": [21, 122]
            },
        ]
    },
    {
        "identifier": 'EVENT_725_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_725_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_725_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
