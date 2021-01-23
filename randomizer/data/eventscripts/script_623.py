from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_623_jmp_if_random_above_128_0',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_623_pause_2']
    },
    {
        "identifier": 'EVENT_623_pause_1',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_623_pause_2',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_623_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8]
    },
    {
        "identifier": 'EVENT_623_jmp_if_7000_equals_short_4',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_623_set_action_script_sync_8']
    },
    {
        "identifier": 'EVENT_623_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_623_set_action_script_sync_12']
    },
    {
        "identifier": 'EVENT_623_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 327]
    },
    {
        "identifier": 'EVENT_623_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_623_pause_13']
    },
    {
        "identifier": 'EVENT_623_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 328]
    },
    {
        "identifier": 'EVENT_623_pause_9',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_623_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 329]
    },
    {
        "identifier": 'EVENT_623_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_623_pause_13']
    },
    {
        "identifier": 'EVENT_623_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 327]
    },
    {
        "identifier": 'EVENT_623_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_623_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_623_set_7000_to_object_coord_16']
    },
    {
        "identifier": 'EVENT_623_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_623_pause_13']
    },
    {
        "identifier": 'EVENT_623_set_7000_to_object_coord_16',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_5, Coords.Y, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_623_jmp_if_7000_equals_short_17',
        "command": 'jmp_if_7000_equals_short',
        "args": [63, 'EVENT_623_unsync_action_script_19']
    },
    {
        "identifier": 'EVENT_623_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_623_action_queue_async_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_623_action_queue_async_18_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_623_action_queue_async_18_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_623_unsync_action_script_19',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_623_unsync_action_script_20',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_623_unsync_action_script_21',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_623_unsync_action_script_22',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_623_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x704c, 1]
    },
    {
        "identifier": 'EVENT_623_ret_24',
        "command": 'ret'
    }
]
