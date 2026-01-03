
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3807_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI, RadialDirections.SOUTH, 4, 16, 0, []]
    },
    {
        "identifier": 'EVENT_3807_action_queue_sync_1',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
        "subscript": [
            {
                "identifier": 'EVENT_3807_action_queue_sync_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3807_action_queue_sync_1_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3807_set_temp_action_script_sync_2',
        "command": 'set_temp_action_script',
        'args': [AreaObjects.NPC_3, True, 803]
    },
    {
        "identifier": 'EVENT_3807_set_temp_action_script_async_3',
        "command": 'set_temp_action_script',
        'args': [AreaObjects.NPC_2, False, 803]
    },
    {
        "identifier": 'EVENT_3807_action_queue_sync_4',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_8, True],
        "subscript": [
            {
                "identifier": 'EVENT_3807_action_queue_sync_4_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3807_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3807_action_queue_sync_4_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3807_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3807_action_queue_sync_4_SUBSCRIPT_set_palette_row_4',
                "command": 'set_palette_row',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_3807_action_queue_sync_5',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, True],
        "subscript": [
            {
                "identifier": 'EVENT_3807_action_queue_sync_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3807_action_queue_sync_6',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_10, True],
        "subscript": [
            {
                "identifier": 'EVENT_3807_action_queue_sync_6_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3807_remember_last_object_7',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3807_jmp_to_event_8',
        "command": 'jmp_to_event',
        "args": [3806]
    }
]
