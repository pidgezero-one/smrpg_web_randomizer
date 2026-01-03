
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_677_action_queue_async_0',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_8, False],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_async_0_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_action_queue_async_01',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_9, False],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_async_01_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_action_queue_async_02',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_12, False],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_async_02_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_677_action_queue_async_2',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, False],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_async_2_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_677_ret_7',
        "command": 'ret'
    }
]
