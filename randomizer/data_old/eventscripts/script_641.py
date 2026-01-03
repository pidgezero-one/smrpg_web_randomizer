
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_641_action_queue_async_0',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": 'EVENT_641_action_queue_async_0_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_641_action_queue_async_0_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_641_action_queue_async_0_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 3, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_641_apply_solidity_mod_61',
        "command": 'apply_solidity_mod',
        "args": [Rooms._153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_641_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_641_run_event_as_subroutine_59']
    },
    {
        "identifier": 'EVENT_641_fade_in_from_black_async_22',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_641_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_641_set_bit_57',
        "command": 'set_bit',
        "args": [0x704c, 5]
    },
    {
        "identifier": 'EVENT_641_ret_58',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_641_run_event_as_subroutine_59',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_641_run_event_as_subroutine_25_',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_641_jmp_if_bit_clear_7_',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_641_ret_60']
    },
    {
        "identifier": 'EVENT_641_run_event_as_subroutine_25__',
        "command": 'run_event_as_subroutine',
        "args": [3902]
    },
    {
        "identifier": 'EVENT_641_ret_60',
        "command": 'ret'
    }
]
