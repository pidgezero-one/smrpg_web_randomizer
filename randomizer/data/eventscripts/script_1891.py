from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1891_enable_controls_0',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_set_bit_1',
        "command": 'set_bit',
        "args": [0x7095, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_apply_solidity_mod_3',
        "command": 'apply_solidity_mod',
        "args": [Rooms._507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7096, 1, 'EVENT_1891_fade_in_from_black_async_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_jmp_to_subroutine_5',
        "command": 'jmp_to_subroutine',
        "args": [0x6266],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_1891_run_background_event_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_run_background_event_8',
        "command": 'run_background_event',
        "args": [1900, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1891_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
