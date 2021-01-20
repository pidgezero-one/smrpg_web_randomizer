from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2592_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_2592_set_bit_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_2592_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_set_7000_to_object_coord_5',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2592_action_queue_sync_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2592_action_queue_sync_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2592_action_queue_sync_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2592_enter_area_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2592_enter_area_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2592_enter_area_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2592_enter_area_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_2592_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_enter_area_14',
        "command": 'enter_area',
        "args": [Rooms._238_SMITHY_FACTORY_FALL_FROM_LUGNUT_ROOMS_AREA_06__PRIOR, RadialDirections.NORTHWEST, 15, 10, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2592_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2592_action_queue_sync_16_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2592_action_queue_sync_16_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2592_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2592_pause_0'],
        "subscript": []
    }
]
