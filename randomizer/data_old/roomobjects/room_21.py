
from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": {
    "ally_sprite_buffer_size": 1,
    "allow_extra_sprite_buffer": False,
    "extra_sprite_buffer_size": 0,
    "buffer_a": {
      "type": PartitionBufferTypes._4_SPRITES_PER_ROW,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_b": {
      "type": PartitionBufferTypes.EMPTY_3,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_c": {
      "type": PartitionBufferTypes.EMPTY_3,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "full_palette_buffer": True,
  },
  "music": Music._02_MUSHROOM_KINGDOM,
  "entrance_event": 401,
  "event_tiles": [],
  "exit_fields": [
    {
      "x": 12,
      "y": 62,
      "z": 2,
      "f": Edge.SOUTHEAST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
      "show_message": False,
      "destination_props": {
        "x": 8,
        "y": 30,
        "z": 2,
        "z_half": False,
        "f": RadialDirection.NORTHWEST,
        "x_bit_7": False
      }
    },
    {
      "x": 17,
      "y": 61,
      "z": 3,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._022_MUSHROOM_KINGDOM_CASTLE_GUEST_ROOM,
      "show_message": False,
      "destination_props": {
        "x": 22,
        "y": 52,
        "z": 0,
        "z_half": False,
        "f": RadialDirection.NORTHEAST,
        "x_bit_7": False
      }
    },
    {
      "x": 13,
      "y": 70,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 2,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT,
      "show_message": False,
      "destination_props": {
        "x": 6,
        "y": 90,
        "z": 2,
        "z_half": True,
        "f": RadialDirection.SOUTHWEST,
        "x_bit_7": False
      }
    }
  ],
  "objects": [
    {
      "id": 0,
      "type": ObjectType.OBJECT,
      "initiator": Initiator.PRESS_A_FROM_ANY_SIDE,
      "model": 64,
      "event_script": 400,
      "action_script": 15,
      "speed": 0,
      "npc_id_offset": 0,
      "event_offset": 0,
      "action_offset": 0,
      "visible": False,
      "x": 16,
      "y": 62,
      "z": 3,
      "z_half": False,
      "direction": RadialDirection.SOUTHWEST,
      "face_on_trigger": True,
      "cant_enter_doors": False,
      "byte2_bit5": False,
      "set_sequence_playback": True,
      "cant_float": False,
      "cant_walk_up_stairs": False,
      "cant_walk_under": False,
      "cant_pass_walls": True,
      "cant_jump_through": False,
      "cant_pass_npcs": False,
      "byte3_bit5": False,
      "cant_walk_through": True,
      "byte3_bit7": False,
      "slidable_along_walls": False,
      "cant_move_if_in_air": False,
      "byte7_upper2": 0x03,
      "clones": []
    }
  ]
}
