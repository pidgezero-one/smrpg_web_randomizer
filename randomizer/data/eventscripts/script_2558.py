from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2558_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x708c, 3, 'EVENT_2558_ret_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2558_set_short_1',
        "command": 'set_short',
        "args": [0x7016, 0x001b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2558_set_short_2',
        "command": 'set_short',
        "args": [0x7018, 0x0046],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2558_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2558_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA, RadialDirections.SOUTH, 26, 22, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2558_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2558_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
