from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1678_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS, RadialDirections.SOUTH, 6, 29, 9, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1678_set_bit_1',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1678_enable_controls_2',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1678_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1678_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
        ]
    },
    {
        "identifier": 'EVENT_1678_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
