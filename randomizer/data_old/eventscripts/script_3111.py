
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3111_disable',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3111_action_queue_async_0',
        "command": 'action_queue',
        'args': [AreaObjects.MEM_70A8, True],
        "subscript": [
            {
                "identifier": 'EVENT_165_action_queue_async_0_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_165_action_queue_async_0_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_165_action_queue_async_0_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3111_put_inventory_105',
        "command": 'jmp_to_event',
        "args": [3098]
    },
]
