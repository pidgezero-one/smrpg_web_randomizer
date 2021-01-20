from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1567_set_bit_0',
        "command": 'set_bit',
        "args": [0x7042, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1567_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1567_action_queue_sync_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1567_action_queue_sync_1_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1567_action_queue_sync_1_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1567_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1567_action_queue_async_2_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1567_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1567_action_queue_async_2_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1567_jmp_if_object_trigger_disabled_3',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_6, Rooms._138_LANDS_END_AREA_02, 'EVENT_1567_fade_in_from_black_async_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1567_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1567_action_queue_sync_4_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1567_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1567_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1567_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1567_clear_bit_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1567_jmp_if_object_trigger_disabled_8',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_6, Rooms._138_LANDS_END_AREA_02, 'EVENT_1567_clear_bit_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1567_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1567_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1567_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
