from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_SetSpriteSequence)
from randomizer.logic.progression.prizelocations.access import (can_clear_ship, can_damage_enemies_with_spells, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_access_early_ship)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_7)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_ship_password_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Ship Password boss fight."""
    if not isinstance(prize, KingCalamariBossFight):
        world.action_scripts.delete_command_by_identifier("password_boss_vanilla_1")
        world.action_scripts.delete_command_by_identifier("password_boss_vanilla_2")
        world.action_scripts.delete_command_by_identifier("password_boss_vanilla_3")
    m = prize.smallest_npc()
    if m.animations.ship_beckon is not None:
        c = world.action_scripts.get_command_by_identifier(
            "password_boss_reveal_sequence", A_SetSpriteSequence
        )
        c.set_index(m.animations.ship_beckon.sequence_id)
    else:
        world.action_scripts.delete_command_by_identifier(
            "password_boss_reveal_sequence"
        )


class ShipPasswordBossFight(BossFightLocation):
    _bias = True
    _originally_held = KingCalamariBossFight
    _rooms = [R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _pack_id = PACK167_SHIP_FIRST_BOSS
    _post_unlocks_event_id = E1207_SHIP_MID_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
            NPC_7,
            sequence_setter_event_id=E0800_SHIP_PASSWORD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [DI1660_SHIP_PASSWORD_COMPLETE]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, KingCalamariBossFight):
            render_ship_password_boss(world, self.prize)
        return op


__all__ = ["ShipPasswordBossFight"]
