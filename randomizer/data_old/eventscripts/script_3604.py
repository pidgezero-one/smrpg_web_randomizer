
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3604_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, 'EVENT_3604_ret_6']
    },
    {
        "identifier": 'EVENT_3604_action_queue_async_1',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_5, False],
        "subscript": [
            {
                "identifier": 'EVENT_3604_action_queue_async_1_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [254, 250, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3604_ret_6',
        "command": 'ret'
    }
]
