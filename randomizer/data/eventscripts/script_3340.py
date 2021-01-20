from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3340_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 3, 'EVENT_3340_ret_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_set_bit_1',
        "command": 'set_bit',
        "args": [0x707e, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3340_action_queue_async_2_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3340_action_queue_async_2_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3340_action_queue_async_2_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3340_action_queue_async_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3340_action_queue_async_2_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x30]
            },
            {
                "identifier": 'EVENT_3340_action_queue_async_2_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3340_action_queue_async_2_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
        ]
    },
    {
        "identifier": 'EVENT_3340_set_bit_3',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_create_packet_at_object_coords_jmp_if_null_4',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_1, 'EVENT_3340_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_pause_5',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_summon_to_current_level_6',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3340_action_queue_sync_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3340_action_queue_sync_7_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3340_action_queue_sync_7_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3340_action_queue_sync_7_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3340_action_queue_sync_7_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3340_action_queue_sync_7_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [32]
            },
        ]
    },
    {
        "identifier": 'EVENT_3340_run_dialog_8',
        "command": 'run_dialog',
        "args": [1819, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_pause_9',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_create_packet_at_object_coords_jmp_if_null_13',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_1, 'EVENT_3340_create_packet_at_object_coords_jmp_if_null_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_create_packet_at_object_coords_jmp_if_null_14',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_0, 'EVENT_3340_ret_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3340_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
