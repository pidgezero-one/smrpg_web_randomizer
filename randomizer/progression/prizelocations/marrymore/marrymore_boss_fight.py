from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_marrymore_boss_henchmen)
from randomizer.progression.prizelocations.access import (can_clear_chapel, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_TransferXYZFPixels)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_11, NPC_2, NPC_3, NPC_4)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarrymoreBossFight(BossFightLocation):
    _bias = True
    _originally_held = BundtBossFight
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_BOSS_FIGHT
    _world_area = WorldAreaEnum.MARRYMORE
    _pack_id = PACK176_CHAPEL_BOSS
    _post_unlocks_event_id = E1204_CHAPEL_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R155_MARRYMORE_CHAPEL_KITCHEN,
            NPC_0,
            sequence_setter_event_id=E0796_MARRYMORE_KITCHEN_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_11,
            sequence_setter_event_id=E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R155_MARRYMORE_CHAPEL_KITCHEN,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            ],
            [NPC_1, NPC_3],
        ),
        BossFightLocationHenchmanNPC(
            [
                R155_MARRYMORE_CHAPEL_KITCHEN,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            ],
            [NPC_2, NPC_4],
        ),
    ]
    _dialogs_expecting_replacement = [DI2061_HEAD_CHEF, DI2062_APPRENTICE_CHEF]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(SeaGate, SeaGating.MARRYMORE):
            content.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld):
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if (
            self.prize.character_henchmen is not None
            and len(self.prize.character_henchmen) >= 1
        ):
            render_marrymore_boss_henchmen(world, self.prize.character_henchmen)
        if not isinstance(self.prize, (BundtBossFight, Bundt2BossFight)):
            world.event_scripts.get_subscript_command_by_identifier(
                "EVENT_668_cake_shift_aq",
                "EVENT_668_cake_shift",
                A_TransferXYZFPixels,
            ).set_y(0)
        return op


__all__ = ["MarrymoreBossFight"]
