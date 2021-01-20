from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3786_jmp_if_mario_in_air_0',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3786_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, RadialDirections.NORTHEAST, 17, 104, 6, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3786_db_2',
        "command": 'db',
        "args": [0xfd, 0x49],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3786_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3786_action_queue_sync_3_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3786_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3786_action_queue_sync_3_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3786_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3786_action_queue_sync_3_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3786_action_queue_sync_3_SUBSCRIPT_walk_1_step_northeast_5',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3786_action_queue_sync_3_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3786_action_queue_sync_3_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3786_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3786_pause_5',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3786_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3786_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3786_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
