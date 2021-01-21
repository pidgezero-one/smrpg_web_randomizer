from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_340_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 4]
    },
    {
        "identifier": 'ACTION_340_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
    },
    {
        "identifier": 'ACTION_340_object_memory_set_bit_2',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_340_jump_to_height_silent_3',
        "command": 'jump_to_height_silent',
        "args": [160]
    },
    {
        "identifier": 'ACTION_340_pause_4',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_340_floating_off_5',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_340_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_340_visibility_off_7',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_340_pause_8',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_340_visibility_on_9',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_340_pause_10',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_340_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_340_visibility_off_12',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_340_ret_13',
        "command": 'ret'
    }
]
