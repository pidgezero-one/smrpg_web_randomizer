
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_185_store_7000_item_quantity_to_70A7_283',
        "command": 'store_item_amount_7000',
        "args": [items.Fireworks]
    },
    {
        "identifier": 'EVENT_185_jmp_if_7000_equals_short_284',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 1, 'EVENT_185_set_298']
    },
    {
        "identifier": 'EVENT_185_store_7000_item_quantity_to_70A7_283_',
        "command": 'store_item_amount_7000',
        "args": [items.ShinyStone]
    },
    {
        "identifier": 'EVENT_185_jmp_if_7000_equals_short_287',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 1, 'EVENT_185_set_294']
    },
    {
        "identifier": "EVENT_185_set_fireworks",
        "command": "set_var_to_const",
        "args": [0x70EA, 5]
    },
    {
        "identifier": 'EVENT_185_set_291',
        "command": "set_var_to_const",
        "args": [0x70a7, 172]
    },
    {
        "identifier": 'EVENT_185_ret_293',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_185_set_294',
        "command": "set_var_to_const",
        "args": [0x70a7, 137]
    },
    {
        "identifier": 'EVENT_185_remove_one_from_inventory_295',
        "command": 'remove_one_from_inventory',
        "args": [items.ShinyStone]
    },
    {
        "identifier": 'EVENT_185_ret_297',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_185_set_298',
        "command": "set_var_to_const",
        "args": [0x70a7, 138]
    },
    {
        "identifier": 'EVENT_185_apply_solidity_mod_7',
        "command": 'apply_solidity_mod',
        "args": [Rooms._324_MONSTRO_TOWN_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_185_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._324_MONSTRO_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_185_remove_one_from_inventory_299',
        "command": 'remove_one_from_inventory',
        "args": [items.Fireworks]
    },
    {
        "identifier": 'EVENT_185_ret_301',
        "command": 'jmp_to_event',
        "args": [160]
    }
]