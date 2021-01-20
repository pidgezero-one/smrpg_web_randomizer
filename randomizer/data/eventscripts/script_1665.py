from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1665_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_reset_coords_3',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 353],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_add_short_mem_6',
        "command": 'add_short_mem',
        "args": [0x7000, 0x702e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x70b2, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_1665_enable_controls_until_return_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_remove_one_from_inventory_9',
        "command": 'remove_one_from_inventory',
        "args": [items.BeetleBox],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_put_inventory_10',
        "command": 'put_inventory',
        "args": [items.BeetleBox2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_enable_controls_until_return_12',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_set_short_13',
        "command": 'set_short',
        "args": [0x701c, 0x000a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1665_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
