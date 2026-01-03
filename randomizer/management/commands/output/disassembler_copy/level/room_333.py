
from randomizer.data.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": {
    "ally_sprite_buffer_size": 1,
    "allow_extra_sprite_buffer": False,
    "extra_sprite_buffer_size": 0,
    "buffer_a": {
      "type": PartitionBufferTypes.EMPTY_3,
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
  "music": Music._13_ROAD_IS_FULL_OF_DANGERS,
  "entrance_event": 3135,
  "event_tiles": [
    {
      "event": 3136,
      "x": 5,
      "y": 20,
      "z": 1,
      "f": Edge.SOUTHEAST,
      "length": 1,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "byte_8_bit_4": False,
    },
    {
      "event": 3117,
      "x": 1,
      "y": 25,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "byte_8_bit_4": False,
    }
  ],
  "exit_fields": [
    {
      "x": 1,
      "y": 25,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.MAP_LOCATION,
      "byte_2_bit_2": False,
      "destination": Locations._014_KERO_SEWERS,
      "show_message": False,
      "destination_props": {
        "byte_2_bit_0": False,
        "byte_2_bit_1": False,
      }
    }
  ],
  "objects": [
    {
      "id": 0,
      "type": ObjectType.OBJECT,
      "initiator": Initiator.NONE,
      "model": 9,
      "event_script": 256,
      "action_script": 0,
      "speed": 0,
      "npc_id_offset": 0,
      "event_offset": 0,
      "action_offset": 0,
      "visible": False,
      "x": 11,
      "y": 35,
      "z": 2,
      "z_half": False,
      "direction": RadialDirection.SOUTHWEST,
      "face_on_trigger": False,
      "cant_enter_doors": False,
      "byte2_bit5": False,
      "set_sequence_playback": True,
      "cant_float": True,
      "cant_walk_up_stairs": False,
      "cant_walk_under": False,
      "cant_pass_walls": True,
      "cant_jump_through": False,
      "cant_pass_npcs": False,
      "byte3_bit5": False,
      "cant_walk_through": False,
      "byte3_bit7": False,
      "slidable_along_walls": True,
      "cant_move_if_in_air": True,
      "byte7_upper2": 0x03,
      "clones": []
    }
  ]
}
