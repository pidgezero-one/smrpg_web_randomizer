from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2571_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2571_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2571_jmp_if_7000_equals_short_2',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2571_set_bit_7']
    },
    {
        "identifier": 'EVENT_2571_jmp_if_7000_equals_short_3',
        "command": 'jmp_if_7000_equals_short',
        "args": [12, 'EVENT_2571_freeze_camera_5']
    },
    {
        "identifier": 'EVENT_2571_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2571_pause_0']
    },
    {
        "identifier": 'EVENT_2571_freeze_camera_5',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2571_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_2571_pause_0']
    },
    {
        "identifier": 'EVENT_2571_set_bit_7',
        "command": 'set_bit',
        "args": [0x708d, 1]
    },
    {
        "identifier": 'EVENT_2571_enter_area_8',
        "command": 'enter_area',
        "args": [Rooms._100_BOOSTER_PASS_AREA_01, RadialDirections.SOUTHWEST, 20, 24, 8, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2571_ret_9',
        "command": 'ret'
    }
]
