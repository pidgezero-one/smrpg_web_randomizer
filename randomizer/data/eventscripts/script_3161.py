from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3161_pause_script_if_menu_open_0',
        "command": 'pause_script_if_menu_open'
    },
    {
        "identifier": 'EVENT_3161_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_0, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM, 'EVENT_3161_jmp_4']
    },
    {
        "identifier": 'EVENT_3161_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM, RadialDirections.NORTHEAST, 23, 72, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3161_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3161_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_3198_pause_script_if_menu_open_0']
    },
    {
        "identifier": 'EVENT_3161_ret_5',
        "command": 'ret'
    }
]
