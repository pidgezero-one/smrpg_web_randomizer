from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2379_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2379_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_2379_pause_0']
    },
    {
        "identifier": 'EVENT_2379_jmp_if_mario_in_air_2',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_2379_set_bit_5']
    },
    {
        "identifier": 'EVENT_2379_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_2379_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2379_pause_0']
    },
    {
        "identifier": 'EVENT_2379_set_bit_5',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_2379_set_7000_to_object_coord_6',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2379_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_7000_equals_short',
        "args": [9, 'EVENT_2379_action_queue_sync_18']
    },
    {
        "identifier": 'EVENT_2379_jmp_if_7000_equals_short_8',
        "command": 'jmp_if_7000_equals_short',
        "args": [8, 'EVENT_2379_action_queue_sync_18']
    },
    {
        "identifier": 'EVENT_2379_jmp_if_7000_equals_short_9',
        "command": 'jmp_if_7000_equals_short',
        "args": [7, 'EVENT_2379_action_queue_sync_18']
    },
    {
        "identifier": 'EVENT_2379_jmp_if_7000_equals_short_10',
        "command": 'jmp_if_7000_equals_short',
        "args": [4, 'EVENT_2379_enter_area_16']
    },
    {
        "identifier": 'EVENT_2379_jmp_if_7000_equals_short_11',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_2379_enter_area_16']
    },
    {
        "identifier": 'EVENT_2379_jmp_if_7000_equals_short_12',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_2379_enter_area_16']
    },
    {
        "identifier": 'EVENT_2379_jmp_if_7000_equals_short_13',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_2379_enter_area_16']
    },
    {
        "identifier": 'EVENT_2379_jmp_if_7000_equals_short_14',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2379_enter_area_16']
    },
    {
        "identifier": 'EVENT_2379_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_2379_pause_0']
    },
    {
        "identifier": 'EVENT_2379_enter_area_16',
        "command": 'enter_area',
        "args": [Rooms._238_SMITHY_FACTORY_FALL_FROM_LUGNUT_ROOMS_AREA_06__PRIOR, RadialDirections.NORTHWEST, 15, 10, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2379_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2379_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2379_action_queue_sync_18_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2379_action_queue_sync_18_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2379_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_2379_pause_0']
    }
]
