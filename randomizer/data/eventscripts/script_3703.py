from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3703_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3703_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 498, 'EVENT_3703_jmp_if_object_trigger_disabled_4']
    },
    {
        "identifier": 'EVENT_3703_jmp_if_object_not_in_level_2',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, 'EVENT_3703_jmp_if_object_trigger_disabled_4']
    },
    {
        "identifier": 'EVENT_3703_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3703_action_queue_sync_3_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3703_jmp_if_object_trigger_disabled_4',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, 'EVENT_3703_fade_in_from_black_async_7']
    },
    {
        "identifier": 'EVENT_3703_jmp_if_object_trigger_disabled_5',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._498_NIMBUS_CASTLE_AREA_10_____DUMMY, 'EVENT_3703_fade_in_from_black_async_7']
    },
    {
        "identifier": 'EVENT_3703_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3703_action_queue_async_6_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3703_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3703_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_3703_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3703_jmp_if_object_trigger_disabled_10',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._498_NIMBUS_CASTLE_AREA_10_____DUMMY, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3703_jmp_if_object_trigger_disabled_11',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3703_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_3703_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_3703_ret_14',
        "command": 'ret'
    }
]
