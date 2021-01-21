from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1670_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [1840]
    },
    {
        "identifier": 'EVENT_1670_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1670_ret_7']
    },
    {
        "identifier": 'EVENT_1670_jmp_fork_mario_on_object_2',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1670_ret_3', 'EVENT_1670_play_sound_4']
    },
    {
        "identifier": 'EVENT_1670_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1670_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1670_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1670_action_queue_sync_5_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1670_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1670_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1670_action_queue_sync_5_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1670_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1670_ret_7',
        "command": 'ret'
    }
]
