from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_412_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_412_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_412_set_bit_2',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_412_start_battle_3',
        "command": 'start_battle',
        "args": [0x000a, 15]
    },
    {
        "identifier": 'EVENT_412_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_412_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_412_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_412_action_queue_async_6_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_412_action_queue_async_6_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_412_action_queue_async_6_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [11, 18, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_412_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_412_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_412_ret_8',
        "command": 'ret'
    }
]
