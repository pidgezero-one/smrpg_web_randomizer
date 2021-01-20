from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2338_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7047, 5, 'EVENT_2338_fade_in_from_black_async_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2338_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2338_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2338_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2338_action_queue_async_2_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2338_action_queue_async_2_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2338_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2338_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
