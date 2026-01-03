
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3086_store_7000_item_quantity_to_70A7_283',
        "command": 'store_item_amount_7000',
        "args": [items.AltoCard]
    },
    {
        "identifier": 'EVENT_3086_jmp_if_7000_equals_short_284',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 1, 'EVENT_3086_set_298']
    },
    {
        "identifier": 'EVENT_3086_store_7000_item_quantity_to_70A7_283_',
        "command": 'store_item_amount_7000',
        "args": [items.TenorCard]
    },
    {
        "identifier": 'EVENT_3086_jmp_if_7000_equals_short_287',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 1, 'EVENT_3086_set_294']
    },
    {
        "identifier": 'EVENT_3086_set_291',
        "command": "set_var_to_const",
        "args": [0x70a7, 151]
    },
    {
        "identifier": 'EVENT_3086_set_291_',
        "command": 'jmp_to_event',
        "args": [895]
    },
    {
        "identifier": 'EVENT_3086_set_294',
        "command": "set_var_to_const",
        "args": [0x70a7, 150]
    },
    {
        "identifier": 'EVENT_3086_remove_one_from_inventory_295',
        "command": 'remove_one_from_inventory',
        "args": [items.TenorCard]
    },
    {
        "identifier": 'EVENT_3086_set_291__',
        "command": 'jmp_to_event',
        "args": [895]
    },
    {
        "identifier": 'EVENT_3086_set_298',
        "command": "set_var_to_const",
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_3086_remove_one_from_inventory_299',
        "command": 'remove_one_from_inventory',
        "args": [items.AltoCard]
    },
    {
        "identifier": 'EVENT_3086_set_291___',
        "command": 'jmp_to_event',
        "args": [895]
    },
]
