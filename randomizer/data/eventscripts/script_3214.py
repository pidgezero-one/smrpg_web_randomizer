from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3214_set_short_0',
        "command": 'set_short',
        "args": [0x700a, 0x00d3]
    },
    {
        "identifier": 'EVENT_3214_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [720]
    },
    {
        "identifier": 'EVENT_3214_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3214_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 6, 'EVENT_3214_fade_out_to_black_async_14']
    },
    {
        "identifier": 'EVENT_3214_start_battle_4',
        "command": 'start_battle',
        "args": [0x00a7, 3]
    },
    {
        "identifier": 'EVENT_3214_set_bit_5',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_3214_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_3214_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_3214_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3214_set_bit_9',
        "command": 'set_bit',
        "args": [0x7058, 6]
    },
    {
        "identifier": 'EVENT_3214_set_bit_10',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_3214_enter_area_11',
        "command": 'enter_area',
        "args": [Rooms._173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE, RadialDirections.SOUTH, 2, 92, 8, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3214_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_3214_pause_13',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3214_fade_out_to_black_async_14',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_3214_start_battle_15',
        "command": 'start_battle',
        "args": [0x00c2, 3]
    },
    {
        "identifier": 'EVENT_3214_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3214_set_bit_10']
    }
]
