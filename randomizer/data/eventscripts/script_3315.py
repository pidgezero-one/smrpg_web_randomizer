from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3315_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, RadialDirections.NORTHEAST, 20, 42, 2, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3315_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7055, 1, 'EVENT_3315_jmp_to_event_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3315_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3315_action_queue_async_2_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3315_action_queue_async_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3315_action_queue_async_2_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3315_action_queue_async_2_SUBSCRIPT_pause_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_3315_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [3135],
        "subscript": []
    }
]
