from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1677_remove_from_level_0',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._317_LANDS_END_DESERT_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_set_bit_3',
        "command": 'set_bit',
        "args": [0x7096, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_set_short_4',
        "command": 'set_short',
        "args": [0x7016, 0x1d2e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._324_MONSTRO_TOWN_OUTSIDE, RadialDirections.SOUTH, 2, 47, 16, [_0x68Flags.SHOW_MESSAGE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_set_bit_7',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_enable_controls_8',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1677_action_queue_sync_9_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1677_set_bit_10',
        "command": 'set_bit',
        "args": [0x706f, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_set_bit_11',
        "command": 'set_bit',
        "args": [0x7067, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1677_jmp_to_event_12',
        "command": 'jmp_to_event',
        "args": [2048],
        "subscript": []
    }
]
