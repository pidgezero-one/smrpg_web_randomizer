from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_669_stop_sound_0',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_669_stop_sound_1',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_669_stop_sound_2',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_669_stop_sound_3',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_669_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 0, 'EVENT_669_enter_area_7']
    },
    {
        "identifier": 'EVENT_669_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, RadialDirections.NORTHEAST, 9, 98, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_669_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_669_enter_area_7',
        "command": 'enter_area',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, RadialDirections.NORTHEAST, 9, 98, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_669_ret_8',
        "command": 'ret'
    }
]
