
from randomizer.data.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": {
    "ally_sprite_buffer_size": 1,
    "allow_extra_sprite_buffer": True,
    "extra_sprite_buffer_size": 0,
    "buffer_a": {
      "type": PartitionBufferTypes.TREASURE_CHEST,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_b": {
      "type": PartitionBufferTypes._3_SPRITES_PER_ROW,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_c": {
      "type": PartitionBufferTypes._4_SPRITES_PER_ROW,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "full_palette_buffer": True,
  },
  "music": Music._67_WEAPONS_FACTORY,
  "entrance_event": 15,
  "event_tiles": [],
  "exit_fields": [
    {
      "x": 13,
      "y": 36,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._473_SMITHY_FACTORY_AREA_13_BOWYERS_FALLING_DOWN_CONVEYOR_BELTS,
      "show_message": False,
      "destination_props": {
        "x": 10,
        "y": 54,
        "z": 15,
        "z_half": False,
        "f": RadialDirection.SOUTHWEST,
        "x_bit_7": False
      }
    },
    {
      "x": 16,
      "y": 27,
      "z": 0,
      "f": Edge.SOUTHWEST,
      "length": 2,
      "height": 0,
      "nw_se_edge_active": True,
      "ne_sw_edge_active": False,
      "destination_type": ExitType.ROOM,
      "byte_2_bit_2": False,
      "destination": Rooms._474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS,
      "show_message": False,
      "destination_props": {
        "x": 18,
        "y": 39,
        "z": 8,
        "z_half": False,
        "f": RadialDirection.NORTHEAST,
        "x_bit_7": False
      }
    }
  ],
  "objects": [
    {
      "id": 0,
      "type": ObjectType.OBJECT,
      "initiator": Initiator.JUMP_ON,
      "model": 510,
      "event_script": 80,
      "action_script": 120,
      "speed": 0,
      "npc_id_offset": 0,
      "event_offset": 0,
      "action_offset": 0,
      "visible": True,
      "x": 14,
      "y": 31,
      "z": 0,
      "z_half": True,
      "direction": RadialDirection.SOUTHWEST,
      "face_on_trigger": False,
      "cant_enter_doors": False,
      "byte2_bit5": False,
      "set_sequence_playback": True,
      "cant_float": False,
      "cant_walk_up_stairs": False,
      "cant_walk_under": False,
      "cant_pass_walls": False,
      "cant_jump_through": False,
      "cant_pass_npcs": False,
      "byte3_bit5": False,
      "cant_walk_through": True,
      "byte3_bit7": True,
      "slidable_along_walls": False,
      "cant_move_if_in_air": True,
      "byte7_upper2": 0x03,
      "clones": []
    }
  ]
}
