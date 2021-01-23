from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3743_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3743_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3743_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3743_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3743_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3743_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3743_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3743_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3743_apply_solidity_mod_8',
        "command": 'apply_solidity_mod',
        "args": [Rooms._107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3743_palette_set_9',
        "command": 'palette_set',
        "args": [111, 1, [0, 1, 3]]
    },
    {
        "identifier": 'EVENT_3743_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3743_action_queue_sync_10_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3743_action_queue_sync_10_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 2, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3743_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3743_action_queue_sync_11_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3743_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3743_action_queue_sync_12_SUBSCRIPT_set_palette_row_0',
                "command": 'set_palette_row',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_3743_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3743_action_queue_sync_13_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [1, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3743_action_queue_sync_13_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3743_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3743_action_queue_sync_14_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3743_action_queue_sync_14_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3743_remember_last_object_15',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3743_apply_solidity_mod_16',
        "command": 'apply_solidity_mod',
        "args": [Rooms._107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3743_pause_17',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3743_palette_set_18',
        "command": 'palette_set',
        "args": [109, 1, [2, 3]]
    },
    {
        "identifier": 'EVENT_3743_pause_19',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3743_palette_set_20',
        "command": 'palette_set',
        "args": [108, 1, [0, 2, 3]]
    },
    {
        "identifier": 'EVENT_3743_palette_set_21',
        "command": 'palette_set',
        "args": [169, 1, [1, 2, 3]]
    },
    {
        "identifier": 'EVENT_3743_palette_set_22',
        "command": 'palette_set',
        "args": [170, 1, [0, 1, 2, 3]]
    },
    {
        "identifier": 'EVENT_3743_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3743_ret_24',
        "command": 'ret'
    }
]
