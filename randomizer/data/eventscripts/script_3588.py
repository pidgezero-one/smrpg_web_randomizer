from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3588_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_3588_store_character_equipment_7000_1',
        "command": 'store_character_equipment_7000',
        "args": [PlayableCharacters.MARIO, EquipSlots.ACCESSORY]
    },
    {
        "identifier": 'EVENT_3588_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 93, 'EVENT_3588_set_bit_8']
    },
    {
        "identifier": 'EVENT_3588_store_character_equipment_7000_3',
        "command": 'store_character_equipment_7000',
        "args": [0x09, EquipSlots.ACCESSORY]
    },
    {
        "identifier": 'EVENT_3588_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 93, 'EVENT_3588_set_bit_8']
    },
    {
        "identifier": 'EVENT_3588_store_character_equipment_7000_5',
        "command": 'store_character_equipment_7000',
        "args": [0x0a, EquipSlots.ACCESSORY]
    },
    {
        "identifier": 'EVENT_3588_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 93, 'EVENT_3588_set_bit_8']
    },
    {
        "identifier": 'EVENT_3588_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3588_set_bit_8',
        "command": 'set_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_3588_ret_9',
        "command": 'ret'
    }
]
