from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_365_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 4]
    },
    {
        "identifier": 'ACTION_365_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_365_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_365_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_365_floating_off_4',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_365_jump_to_height_5',
        "command": 'jump_to_height',
        "args": [112]
    },
    {
        "identifier": 'ACTION_365_pause_6',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_365_floating_off_7',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_365_start_loop_n_times_8',
        "command": 'start_loop_n_times',
        "args": [8]
    },
    {
        "identifier": 'ACTION_365_visibility_on_9',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_365_pause_10',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_365_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_365_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_365_end_loop_13',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_365_ret_14',
        "command": 'ret'
    }
]
