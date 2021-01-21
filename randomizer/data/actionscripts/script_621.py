from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_621_visibility_on_0',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_621_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_621_pause_2',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_621_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._052_DEEP_BOUNCE, 4]
    },
    {
        "identifier": 'ACTION_621_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_621_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x700c]
    },
    {
        "identifier": 'ACTION_621_create_packet_at_object_coords_jmp_if_null_6',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._021_BULLET_BILL_IGNITION, AreaObjects.MEM_70AA, 'ACTION_621_pause_7']
    },
    {
        "identifier": 'ACTION_621_pause_7',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'ACTION_621_reset_properties_8',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_621_set_bit_9',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_621_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_621_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_621_ret_12',
        "command": 'ret'
    }
]
