from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1665_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1665_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1665_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1665_reset_coords_3',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1665_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 353]
    },
    {
        "identifier": 'EVENT_1665_set_7000_to_70A0_short_mem_5',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b2]
    },
    {
        "identifier": 'EVENT_1665_add_short_mem_6',
        "command": 'add_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1665_set_70A0_short_mem_to_7000_7',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70b2]
    },
    {
        "identifier": 'EVENT_1665_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_1665_enable_controls_until_return_12']
    },
    {
        "identifier": 'EVENT_1665_remove_one_from_inventory_9',
        "command": 'remove_one_from_inventory',
        "args": [items.BeetleBox]
    },
    {
        "identifier": 'EVENT_1665_put_inventory_10',
        "command": 'put_inventory',
        "args": [items.BeetleBox2]
    },
    {
        "identifier": 'EVENT_1665_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1665_enable_controls_until_return_12',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1665_set_short_13',
        "command": 'set_short',
        "args": [0x701c, 0x000a]
    },
    {
        "identifier": 'EVENT_1665_ret_14',
        "command": 'ret'
    }
]
