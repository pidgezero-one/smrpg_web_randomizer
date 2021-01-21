from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3724_set_0',
        "command": 'set',
        "args": [0x70df, 49]
    },
    {
        "identifier": 'EVENT_3724_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_3724_jmp_if_bit_set_5']
    },
    {
        "identifier": 'EVENT_3724_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3724_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [28, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3724_action_queue_sync_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3724_action_queue_sync_2_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3724_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3724_action_queue_sync_3_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 2, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3724_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3724_action_queue_async_4_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 2, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3724_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_3724_run_event_as_subroutine_8']
    },
    {
        "identifier": 'EVENT_3724_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3724_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3724_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_3724_ret_9',
        "command": 'ret'
    }
]
