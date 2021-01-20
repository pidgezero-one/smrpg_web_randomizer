from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_367_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_367_action_queue_async_0_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_367_action_queue_async_0_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_367_action_queue_async_0_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_367_action_queue_async_0_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_367_action_queue_async_0_SUBSCRIPT_pause_2']
            },
        ]
    },
    {
        "identifier": 'EVENT_367_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
