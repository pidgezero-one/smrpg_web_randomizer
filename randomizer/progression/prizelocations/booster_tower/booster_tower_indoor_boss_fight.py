from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_booster_tower_henchman_scripts, render_booster_tower_indoor_boss)
from randomizer.progression.prizelocations.access import (boss_slot_min_vram_cap_for_room, can_damage_enemies_with_spells, can_do_tower_curtain_game, not_earlygame)
from randomizer.progression.prizelocations.marrymore.marrymore_character import MarrymoreCharacter
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_10, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def _marrymore_chapel_boss_min_vram_cap(world: GameWorld) -> int:
    return boss_slot_min_vram_cap_for_room(
        world,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
        base_budget=1,
        recruit_location=MarrymoreCharacter,
    )


def _booster_hill_dummy_boss_min_vram_cap(world: GameWorld) -> int:
    return boss_slot_min_vram_cap_for_room(
        world,
        R054_BOOSTER_HILL_DUMMY,
        base_budget=1,
        recruit_location=MarrymoreCharacter,
    )


class BoosterTowerIndoorBossFight(BossFightLocation):
    _bias = True
    _originally_held = BoosterBossFight
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _pack_id = PACK161_TOWER_FIRST_FIGHT
    _post_unlocks_event_id = E1201_TOWER_CURTAIN_BOSS_UNLOCKS
    _henchman_can_run_away = False
    _npc_slots = [
        BossFightLocationNPC(
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            NPC_0,
            sequence_setter_event_id=E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_9,
            sequence_setter_event_id=E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
            # Adaptive cap: ally buffer + Marrymore recruit (NPC_10) compete
            # for VRAM in this room.
            min_vram_size_override=_marrymore_chapel_boss_min_vram_cap,
            min_vram_from_seq0_override=_marrymore_chapel_boss_min_vram_cap,
        ),
        BossFightLocationNPC(
            R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            NPC_6,
            sequence_setter_event_id=E0791_TOWER_ANCESTOR_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
            NPC_6,
            sequence_setter_event_id=E0792_TOWER_FIRST_BOBOMB_STAIRCASE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R054_BOOSTER_HILL_DUMMY,
            NPC_7,
            # Adaptive cap: ally buffer + Marrymore recruit (NPC_8) compete
            # for VRAM in this room.
            min_vram_size_override=_booster_hill_dummy_boss_min_vram_cap,
            min_vram_from_seq0_override=_booster_hill_dummy_boss_min_vram_cap,
        ),
        BossFightLocationNPC(
            R202_BOOSTER_TOWER_ENTRANCE,
            NPC_1,
            sequence_setter_event_id=E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
            NPC_3,
            sequence_setter_event_id=E0797_TOWER_LOBBY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            NPC_3,
            sequence_setter_event_id=E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_10,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_4, NPC_1, NPC_0, NPC_3, NPC_0, NPC_2],
            PACK000_TOWER_HENCHMAN_1,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            container_event=E0053_HENCHMAN_CONTAINER_3,
        ),
        BossFightLocationHenchmanNPC(
            [
                R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_0, NPC_2, NPC_1, NPC_4, NPC_1, NPC_1],
            PACK001_TOWER_HENCHMAN_2,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            container_event=E0054_HENCHMAN_CONTAINER_4,
        ),
        BossFightLocationHenchmanNPC(
            [
                R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_8, NPC_3, NPC_2, NPC_5, NPC_2, NPC_3],
            PACK054_TOWER_HENCHMAN_3,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            container_event=E0055_HENCHMAN_CONTAINER_5,
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_4]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_5]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_6]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_7]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_8]
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R405_BOOSTER_PASS_SECRET],
            [NPC_9],
            PACK032_TOWER_PASS_HENCHMAN,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        )
    ]
    _dialogs_expecting_replacement = [
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
        DI2560_TOWER_HENCHMAN_1,
        DI2572_TOWER_HENCHMAN_2,
        DI3072_TOWER_HENCHMAN_3_WINDOW,
        DI3073_TOWER_HENCHMAN_3,
        DI4060_NEED_TO_DO_CHAPEL_CHECKS,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.npc_slots and self.prize and self.prize.model:
            assert isinstance(self.prize, BossFightPrize)
            is_vanilla = isinstance(
                self.prize, (self._originally_held, Booster2BossFight)
            )

            # Check if character henchman slots are assigned (KeepMinigameSpritesIntact not set)
            keep_minigame_sprites = world.settings.isflag_enabled(
                KeepMinigameSpritesIntact
            )
            character_henchmen_assigned = not keep_minigame_sprites and (
                (
                    self.prize.character_henchmen is not None
                    and len(self.prize.character_henchmen) >= 3
                )
                or (
                    self.prize.mook_henchmen is not None
                    and len(self.prize.mook_henchmen) > 0
                )
            )

            render_booster_tower_indoor_boss(
                world,
                self.prize,
                self.npc_slots,
                is_vanilla,
                character_henchmen_assigned,
            )
            if character_henchmen_assigned:
                char_count = (
                    len(self.prize.character_henchmen)
                    if self.prize.character_henchmen
                    else 0
                )
                has_mook_fallback = (
                    char_count < 3
                    and self.prize.mook_henchmen is not None
                    and len(self.prize.mook_henchmen) > 0
                )
                effective_count = 3 if has_mook_fallback else char_count
                if not is_vanilla:
                    render_booster_tower_henchman_scripts(
                        world,
                        self.prize,
                        effective_count,
                    )

            # Only if mook henchman slot is assigned
            mook_henchmen_assigned = (
                not keep_minigame_sprites
                and self.prize.mook_henchmen is not None
                and len(self.prize.mook_henchmen) > 0
            )

        return op


__all__ = ["BoosterTowerIndoorBossFight"]
