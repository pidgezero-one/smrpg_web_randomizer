from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1888_enable_controls_0',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1888_action_queue_sync_1_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1888_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1888_action_queue_sync_2_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1888_set_bit_3',
        "command": 'set_bit',
        "args": [0x7096, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7095, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_apply_solidity_mod_6',
        "command": 'apply_solidity_mod',
        "args": [Rooms._507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7096, 1, 'EVENT_1888_fade_in_from_black_async_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": [0x6266],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1888_run_background_event_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_run_background_event_11',
        "command": 'run_background_event',
        "args": [1899, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1888_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
