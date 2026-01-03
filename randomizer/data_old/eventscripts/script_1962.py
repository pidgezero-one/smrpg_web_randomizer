
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1962_fade_out_to_black_async_0',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_1962_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA, RadialDirections.NORTHEAST, 2, 63, 0, []]
    },
    {
        "identifier": 'EVENT_1962_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [2160]
    }
]