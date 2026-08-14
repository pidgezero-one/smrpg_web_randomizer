from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_seaside_boss, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_6, NPC_7)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_seaside_beach_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Seaside Beach boss fight."""
    m = prize.smallest_npc()

    # large boss sprite
    world.event_scripts.delete_subscript_command_by_identifier(
        "seaside_boss_reveal_sequence", "seaside_boss_reveal_sequence_1"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "seaside_boss_reveal_sequence_0_aq", "seaside_boss_reveal_sequence_0"
    )


class SeasideBeachBossFight(BossFightLocation):
    _bias = True
    _originally_held = YaridovichBossFight
    _rooms = [R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_FIGHT
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _pack_id = PACK180_SEASIDE_BOSS
    _post_unlocks_event_id = E1206_SEASIDE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F,
            NPC_0,
            sequence_setter_event_id=E0805_SEASIDE_OCCUPIED_ELDER_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            NPC_4,
            sequence_setter_event_id=E0805_SEASIDE_OCCUPIED_ELDER_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_6,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_7,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_0, NPC_0],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_1, NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F,
                R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_2, NPC_0, NPC_0, NPC_2],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_3, NPC_0, NPC_3],
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST], [NPC_0]
        ),
    ]
    _dialogs_expecting_replacement = [
        DI2830_SEASIDE_BOSS_WELCOMES_YOU,
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
        DI2832_OCCUPIED_SEASIDE_INNKEEPER,
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING,
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED,
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED,
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER,
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_seaside_boss(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(LandsEndGate, LandsEndGating.SEASIDE):
            content.extend([ClearBit(LANDS_END_GATED)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, YaridovichBossFight):
            render_seaside_beach_boss(world, self.prize)

        return op


__all__ = ["SeasideBeachBossFight"]
