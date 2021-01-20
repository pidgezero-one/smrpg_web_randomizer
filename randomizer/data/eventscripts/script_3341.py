from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3341_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 4, 'EVENT_3341_jmp_to_event_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3341_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3341_set_bit_2',
        "command": 'set_bit',
        "args": [0x707e, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3341_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3341_action_queue_sync_3_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3341_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3341_action_queue_sync_3_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3341_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3341_action_queue_sync_4_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3341_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3341_action_queue_sync_4_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3341_action_queue_sync_4_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3341_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3341_jmp_to_event_6',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
]
