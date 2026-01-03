
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_778_sequence_setter',
        "command": 'run_event_as_subroutine',
        "args": [779]
    },
    {
        "identifier": 'EVENT_778_action_queue_async_19',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": 'ACTION_617_shift_west_pixels_6',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'ACTION_617_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'ACTION_617_sequence_looping_off_8',
                "command": 'sequence_looping_off'
            },
        ]
    },
    {
        "identifier": 'EVENT_778_sequence_setter_',
        "command": 'jmp_to_event',
        "args": [15]
    }
]