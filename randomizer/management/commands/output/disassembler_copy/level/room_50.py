
from randomizer.data.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace
room = {
  "partition": {
    "ally_sprite_buffer_size": 2,
    "allow_extra_sprite_buffer": True,
    "extra_sprite_buffer_size": 1,
    "buffer_a": {
      "type": PartitionBufferTypes.TREASURE_CHEST,
      "main_buffer_space": PartitionMainSpace._0_BYTES,
      "index_in_main_buffer": True,
    },
    "buffer_b": {
      "type": PartitionBufferTypes._4_SPRITES_PER_ROW,
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
  "music": Music._00_CURRENT,
  "entrance_event": 15,
  "event_tiles": [],
  "exit_fields": [],
  "objects": [
    {
      "id": 0,
      "type": ObjectType.CHEST,
      "initiator": Initiator.HIT_FROM_BELOW,
      "model": 94,
      "event_script": 1372,
      "action_script": 14,
      "speed": 0,
      "star_offset": 14,
      "item_offset": 4,
      "visible": True,
      "x": 29,
      "y": 67,
      "z": 3,
      "z_half": False,
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
      "byte3_bit7": False,
      "slidable_along_walls": True,
      "cant_move_if_in_air": False,
      "byte7_upper2": 0x03,
      "clones": []
    }
  ]
}
