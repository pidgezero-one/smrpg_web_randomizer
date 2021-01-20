from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1430_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._204_MUSHROOM_WAY_AREA_02, 'EVENT_1430_ret_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1430_set_short_1',
        "command": 'set_short',
        "args": [0x7016, 0x091b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1430_move_script_to_main_thread_2',
        "command": 'move_script_to_main_thread',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1430_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [1537],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1430_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
