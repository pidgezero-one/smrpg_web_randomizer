from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1803_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1803_action_queue_async_0_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1803_action_queue_async_0_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._085_FLOWER, 4]
            },
            {
                "identifier": 'EVENT_1803_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1803_action_queue_async_0_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1803_action_queue_async_0_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1803_action_queue_async_0_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1803_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1803_action_queue_sync_1_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1803_jmp_if_var_equals_byte_2',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 33, 'EVENT_1803_set_6']
    },
    {
        "identifier": 'EVENT_1803_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 34, 'EVENT_1803_set_8']
    },
    {
        "identifier": 'EVENT_1803_jmp_if_var_equals_byte_4',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 35, 'EVENT_1803_set_10']
    },
    {
        "identifier": 'EVENT_1803_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1803_set_6',
        "command": 'set',
        "args": [0x70a7, 98]
    },
    {
        "identifier": 'EVENT_1803_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_1803_run_dialog_11']
    },
    {
        "identifier": 'EVENT_1803_set_8',
        "command": 'set',
        "args": [0x70a7, 101]
    },
    {
        "identifier": 'EVENT_1803_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1803_run_dialog_11']
    },
    {
        "identifier": 'EVENT_1803_set_10',
        "command": 'set',
        "args": [0x70a7, 113]
    },
    {
        "identifier": 'EVENT_1803_run_dialog_11',
        "command": 'run_dialog',
        "args": [1177, AreaObjects.BOWSER, []]
    },
    {
        "identifier": 'EVENT_1803_pause_12',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1803_put_inventory_13',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_1803_ret_14',
        "command": 'ret'
    }
]
