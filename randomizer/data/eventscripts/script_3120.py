from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3120_ret_0',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3120_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 3, 'EVENT_3121_jmp_0']
    },
    {
        "identifier": 'EVENT_3120_set_bit_2',
        "command": 'set_bit',
        "args": [0x7055, 3]
    },
    {
        "identifier": 'EVENT_3120_summon_to_current_level_at_marios_coords_3',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3120_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3120_action_queue_sync_4_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_4_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_4_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3120_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3120_action_queue_sync_5_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3120_pause_6',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3120_run_dialog_7',
        "command": 'run_dialog',
        "args": [1587, AreaObjects.NPC_2, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3120_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3120_action_queue_async_8_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3120_action_queue_async_8_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3120_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    }
]
