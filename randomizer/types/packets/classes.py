from randomizer.types.actionscripts.constants.misc import TOTAL_SCRIPTS
from randomizer.types.packets.constants.misc import TOTAL_PACKETS
from randomizer.types.sprites.constants.misc import TOTAL_SPRITES


class Packet:
    id: int
    sprite_id: int
    shadow: bool
    action_script_id: int
    unknown_bits: bool[3] = None
    unknown_bytes: bytearray()

    def __init__(
        self,
        id: int,
        sprite_id: int,
        shadow: bool,
        action_script_id: int,
        unknown_bits: bool[3],
        unknown_bytes: bytearray,
    ) -> None:
        assert 0 <= sprite_id < TOTAL_SPRITES
        assert 0 <= action_script_id < TOTAL_SCRIPTS
        assert 0 <= id < TOTAL_PACKETS
        self.id = id
        self.sprite_id = sprite_id
        self.shadow = shadow
        self.action_script_id = action_script_id
        self.unknown_bits = unknown_bits
        self.unknown_bytes = unknown_bytes
