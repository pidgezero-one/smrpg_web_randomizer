from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2394_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708f, 0, 'EVENT_2394_ret_14']
    },
    {
        "identifier": 'EVENT_2394_set_bit_1',
        "command": 'set_bit',
        "args": [0x708f, 0]
    },
    {
        "identifier": 'EVENT_2394_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 7]
    },
    {
        "identifier": 'EVENT_2394_pause_3',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2394_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2394_action_queue_sync_4_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2394_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2394_action_queue_sync_4_SUBSCRIPT_shirt_to_xy_coords_2',
                "command": 'shirt_to_xy_coords',
                "args": [5, 107]
            },
            {
                "identifier": 'EVENT_2394_action_queue_sync_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2394_action_queue_sync_4_SUBSCRIPT_shirt_to_xy_coords_4',
                "command": 'shirt_to_xy_coords',
                "args": [0, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2394_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2394_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2394_action_queue_sync_5_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2394_action_queue_sync_5_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_2394_action_queue_sync_5_SUBSCRIPT_ret_2',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_2394_stop_embedded_action_script_6',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2394_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 385]
    },
    {
        "identifier": 'EVENT_2394_pause_8',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2394_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2394_run_dialog_10',
        "command": 'run_dialog',
        "args": [3127, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_2394_put_inventory_11',
        "command": 'put_inventory',
        "args": [items.LazyShellWeapon]
    },
    {
        "identifier": 'EVENT_2394_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2394_jmp_if_objects_action_script_running_13',
        "command": 'jmp_if_objects_action_script_running',
        "args": [AreaObjects.MARIO, 'EVENT_2394_pause_12']
    },
    {
        "identifier": 'EVENT_2394_ret_14',
        "command": 'ret'
    }
]
