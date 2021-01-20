from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3328_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3328_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3328_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3328_action_queue_async_2_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
            {
                "identifier": 'EVENT_3328_action_queue_async_2_SUBSCRIPT_set_700C_to_object_coord_1',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_3328_action_queue_async_2_SUBSCRIPT_face_east_2',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3328_action_queue_async_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3328_run_background_event_3',
        "command": 'run_background_event',
        "args": [3329, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3328_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
