
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_330_run_dialog_17',
        "command": 'run_dialog',
        "args": [568, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_330_action_queue_async_18',
        "command": 'action_queue',
        'args': [AreaObjects.MEM_70A8, False],
        "subscript": [
            {
                "identifier": 'EVENT_330_action_queue_async_18_SUBSCRIPT_set_700C_to_7000_short_mem_0',
                "command": 'copy_var_to_var',
        'args': [0x7024, 0x700C]
            },
            {
                "identifier": 'EVENT_330_action_queue_async_18_SUBSCRIPT_face_east_7C_1',
                "command": 'face_east_7C'
            }
        ]
    },
    {
        "identifier": 'EVENT_330_ret_19',
        "command": 'ret'
    }
]
