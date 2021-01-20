from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1624_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 4, 'EVENT_1624_run_dialog_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1624_run_dialog_1',
        "command": 'run_dialog',
        "args": [1122, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1624_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1624_run_dialog_duration_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1624_run_dialog_3',
        "command": 'run_dialog',
        "args": [1120, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1624_run_dialog_duration_4',
        "command": 'run_dialog_duration',
        "args": [1121, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1624_open_shop_5',
        "command": 'open_shop',
        "args": [Shops._04_MOLEVILLE_SHOP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1624_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1624_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
