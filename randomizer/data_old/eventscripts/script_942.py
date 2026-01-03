
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_942_action_queue_async_13',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_13_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_942_action_queue_async_14',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_942_action_queue_async_14_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_942_ret_291',
        "command": 'ret'
    }
]
