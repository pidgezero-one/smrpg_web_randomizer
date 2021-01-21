from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3321_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._354_VOLCANO_AREA_01, RadialDirections.SOUTH, 5, 87, 15, []]
    },
    {
        "identifier": 'EVENT_3321_set_bit_1',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_3321_enable_controls_2',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3321_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3321_action_queue_sync_3_SUBSCRIPT_transfer_xyzf_steps_0',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 16, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3321_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3321_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_3323_jmp_if_bit_set_0']
    }
]
