from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3343_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 6, 'EVENT_3343_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3343_set_bit_1',
        "command": 'set_bit',
        "args": [0x707e, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3343_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3343_action_queue_sync_2_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_2_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_2_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3343_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3343_action_queue_sync_3_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_3_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_3_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3343_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3343_action_queue_sync_4_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_4_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_4_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3343_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3343_action_queue_sync_5_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_5_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_5_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3343_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3343_action_queue_sync_6_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_6_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_6_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3343_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3343_action_queue_sync_7_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_7_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3343_action_queue_sync_7_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3343_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
