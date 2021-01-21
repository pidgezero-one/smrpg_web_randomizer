from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3744_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3744_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3744_action_queue_async_0_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3744_action_queue_async_0_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3744_pause_1',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3744_pause_2',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3744_set_3',
        "command": 'set',
        "args": [0x70a7, 159]
    },
    {
        "identifier": 'EVENT_3744_set_4',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_3744_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_3744_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3744_action_queue_sync_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3744_action_queue_sync_6_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3744_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3744_action_queue_async_7_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3744_action_queue_async_7_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3744_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3744_action_queue_async_8_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_3744_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_11',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_12',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_15',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_16',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_17',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3744_ret_19',
        "command": 'ret'
    }
]
