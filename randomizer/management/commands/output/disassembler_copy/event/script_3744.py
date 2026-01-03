
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3744_run_dialog_0',
        "command": 'run_dialog',
        "args": [3673, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3744_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3744_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3744_action_queue_async_1_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3744_action_queue_async_1_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3744_pause_2',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3744_run_dialog_3',
        "command": 'run_dialog',
        "args": [3674, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3744_pause_4',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3744_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3744_set_6',
        "command": 'set',
        "args": [0x70a7, 159]
    },
    {
        "identifier": 'EVENT_3744_run_dialog_7',
        "command": 'run_dialog',
        "args": [531, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3744_put_inventory_8',
        "command": 'put_inventory',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_3744_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3744_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3744_action_queue_sync_9_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3744_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3744_action_queue_async_10_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3744_action_queue_async_10_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3744_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3744_action_queue_async_11_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_3744_ret_12',
        "command": 'ret'
    }
]
