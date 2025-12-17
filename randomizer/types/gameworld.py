from __future__ import annotations
from copy import deepcopy
from typing import Any, TYPE_CHECKING, TypeVar, cast
import random

from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import (
    AnimationScriptBank,
)
from smrpgpatchbuilder.datatypes.battles.battle_dialog_collection import (
    BattleDialogCollection,
)
from smrpgpatchbuilder.datatypes.dialogs.classes import DialogCollection
from smrpgpatchbuilder.datatypes.enemies.classes import EnemyCollection
from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttackCollection
from smrpgpatchbuilder.datatypes.items.classes import ItemCollection
from smrpgpatchbuilder.datatypes.monster_scripts.types import (
    MonsterScriptBank,
    MonsterScript,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    ActionScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScriptController,
    EventScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import (
    PacketCollection,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    PackCollection,
)
from smrpgpatchbuilder.datatypes.levels.room_collection import RoomCollection
from smrpgpatchbuilder.datatypes.shops.classes import ShopCollection
from smrpgpatchbuilder.datatypes.spells.classes import SpellCollection
from smrpgpatchbuilder.datatypes.graphics.classes import SpriteCollection
from smrpgpatchbuilder.datatypes.scripts_common.classes import IdentifierException
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import CompareVarToConst
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    FormationMember,
    Formation,
)
from smrpgpatchbuilder.datatypes.allies.ally_collection import AllyCollection
from smrpgpatchbuilder.datatypes.levels.classes import RoomObject
from .item import Item
from .enemy import Enemy
from .patch import Patch
from .attack import EnemyAttack as Attack
from .spell import Spell
from .prize import Prize
from .flags import (
    Flag,
    BooleanFlag,
    RangeFlag,
    SelectOneFlag,
    CategorizationFlag,
    CosmeticCategory,
    CATEGORIES,
)
from .prizelocation import PrizeLocation
from ..progression.prizelocations import *

PrizeLocationT = TypeVar("PrizeLocationT", bound=PrizeLocation)
from .settings import Settings

if TYPE_CHECKING:
    from .flags import CategorizationOption as FlagOptions



class RandomizerSettingsException(Exception):
    pass


def get_flag_string_from_flag_collection(categories: list) -> str:
    """Placeholder for flag string generation."""
    return ""


class NumberThresholdFlag(RangeFlag):
    """Alias for range flags used as thresholds."""

    pass


class WorldBuildingException(Exception):
    pass


class GameWorld:
    seed: int = 0
    settings: Settings
    file_select_hash: str = "MARIO1 / MARIO2 / MARIO3 / MARIO4"
    version: str = "9.0.0"

    # Raw data types (basis of ROM patches)

    allies: AllyCollection
    battle_animations: dict[int, AnimationScriptBank]
    battle_dialogs: BattleDialogCollection
    overworld_dialogs: DialogCollection
    enemies: EnemyCollection
    enemy_attacks: EnemyAttackCollection
    items: ItemCollection
    monster_scripts: MonsterScriptBank
    event_scripts: EventScriptController
    action_scripts: ActionScriptBank
    packets: PacketCollection
    battle_packs: PackCollection
    rooms: RoomCollection
    shops: ShopCollection
    spells: SpellCollection
    sprites: SpriteCollection

    locations: dict[type[PrizeLocation], PrizeLocation]

    def get_item(self, item: int | type[Item]):
        if isinstance(item, int):
            i = next((i for i in self.items.items if i.item_id == item), None)
        else:
            i = next((i for i in self.items.items if isinstance(i, item)), None)
        assert i is not None, f"Item {item} does not exist in ItemCollection"
        return i

    def get_enemy(self, enemy_id: int | type[Enemy]):
        if isinstance(enemy_id, int):
            e = next(
                (e for e in self.enemies.enemies if e.monster_id == enemy_id), None
            )
        else:
            e = next((e for e in self.enemies.enemies if isinstance(e, enemy_id)), None)
        assert e is not None, f"Enemy {enemy_id} does not exist in EnemyCollection"
        return e

    def get_attack(self, attack_id: int | type[Attack]):
        if isinstance(attack_id, int):
            a = next(
                (a for a in self.enemy_attacks.attacks if a.index == attack_id), None
            )
        else:
            a = next(
                (a for a in self.enemy_attacks.attacks if isinstance(a, attack_id)),
                None,
            )
        assert (
            a is not None
        ), f"Attack {attack_id} does not exist in EnemyAttackCollection"
        return a

    def get_spell(self, spell_id: int | type[Spell]):
        if isinstance(spell_id, int):
            s = next((s for s in self.spells.spells if s.index == spell_id), None)
        else:
            s = next((s for s in self.spells.spells if isinstance(s, spell_id)), None)
        assert s is not None, f"Spell {spell_id} does not exist in SpellCollection"
        return s

    def get_dialog(self, dialog_id: int):
        d = self.overworld_dialogs.dialogs[dialog_id]
        assert d is not None, f"Dialog {dialog_id} does not exist in DialogCollection"
        return d

    def update_dialog(self, dialog_id: int, new_dialog: str):
        self.overworld_dialogs.replace_dialog(dialog_id, new_dialog)

    def get_battle_dialog(self, dialog_id: int):
        d = self.battle_dialogs.battle_dialogs[dialog_id]
        assert (
            d is not None
        ), f"Battle Dialog {dialog_id} does not exist in BattleDialogCollection"
        return d

    def get_location(self, location_type: type[PrizeLocationT]) -> PrizeLocationT:
        """Get a location instance with proper typing."""
        return cast(PrizeLocationT, self.locations[location_type])

    def update_battle_dialog(self, dialog_id: int, new_dialog: str):
        self.battle_dialogs.battle_dialogs[dialog_id] = new_dialog

    def get_monster_script(self, script: int | Enemy):
        if isinstance(script, int):
            return self.monster_scripts.scripts[script]
        else:
            return self.monster_scripts.scripts[script.monster_id]

    def update_monster_script(self, script: int | Enemy, new_script: MonsterScript):
        if isinstance(script, int):
            self.monster_scripts.replace_script(script, new_script)
        else:
            self.monster_scripts.replace_script(script.monster_id, new_script)

    def get_event_script(self, event_script_id: int):
        return self.event_scripts.get_script_by_id(event_script_id)

    def get_action_script(self, action_script_id: int):
        return self.action_scripts.scripts[action_script_id]

    def get_battle_animation_command_by_name(self, command_name: str):
        try:
            return self.battle_animations[0x02].get_command_by_name(command_name)
        except IdentifierException:
            try:
                return self.battle_animations[0x35].get_command_by_name(command_name)
            except IdentifierException:
                try:
                    return self.battle_animations[0x3A].get_command_by_name(
                        command_name
                    )
                except IdentifierException:
                    raise WorldBuildingException("No battle animation banks found")

    def get_packet(self, packet_id: int):
        p = self.packets.packets[packet_id]
        assert p is not None, f"Packet {packet_id} does not exist in PacketCollection"
        return p

    def update_packet(self, packet_id: int, new_packet):
        self.packets.packets[packet_id] = new_packet

    def get_battle_pack(self, pack_id: int):
        p = self.battle_packs.packs[pack_id]
        assert p is not None, f"Battle Pack {pack_id} does not exist in PackCollection"
        return p

    def update_battle_pack(self, pack_id: int, new_pack):
        self.battle_packs.packs[pack_id] = new_pack

    def replace_battle_pack_formations(
        self, members: list[FormationMember | None], pack_id: int
    ):
        pack = self.get_battle_pack(pack_id)
        if len(pack.formations) == 0:
            pack._formations = [Formation(members)]
            return
        formation_base = pack.formations[0]
        formation_base._members = members
        pack._formations = [formation_base]
        self.update_battle_pack(pack_id, pack)

    def get_room(self, room_id: int):
        r = self.rooms._rooms[room_id]
        assert r is not None, f"Room {room_id} does not exist in RoomCollection"
        return r

    def update_room(self, room_id: int, new_room):
        self.rooms._rooms[room_id] = new_room

    def get_shop(self, shop_id: int):
        s = self.shops.shops[shop_id]
        assert s is not None, f"Shop {shop_id} does not exist in ShopCollection"
        return s

    def update_shop(self, shop_id: int, new_shop):
        self.shops._shops[shop_id] = new_shop

    def get_sprite(self, sprite_id: int):
        s = self.sprites.sprites[sprite_id]
        assert s is not None, f"Sprite {sprite_id} does not exist in SpriteCollection"
        return s

    def update_sprite(self, sprite_id: int, new_sprite):
        self.sprites.sprites[sprite_id] = new_sprite

    # Logic
    # TODO

    def __init__(
        self,
        seed: int,
        settings: Settings,
        allies: AllyCollection,
        battle_animations: dict[int, AnimationScriptBank],
        battle_dialogs: BattleDialogCollection,
        overworld_dialogs: DialogCollection,
        enemies: EnemyCollection,
        enemy_attacks: EnemyAttackCollection,
        items: ItemCollection,
        monster_scripts: MonsterScriptBank,
        event_scripts: EventScriptController,
        action_scripts: ActionScriptBank,
        packets: PacketCollection,
        battle_packs: PackCollection,
        rooms: RoomCollection,
        shops: ShopCollection,
        spells: SpellCollection,
        sprites: SpriteCollection,
    ):
        self.allies = allies
        self.seed = seed
        self.settings = settings
        self.battle_animations = battle_animations
        self.battle_dialogs = battle_dialogs
        self.overworld_dialogs = overworld_dialogs
        self.enemies = enemies
        self.enemy_attacks = enemy_attacks
        self.items = items
        self.monster_scripts = monster_scripts
        self.event_scripts = event_scripts
        self.action_scripts = action_scripts
        self.packets = packets
        self.battle_packs = battle_packs
        self.rooms = rooms
        self.shops = shops
        self.spells = spells
        self.sprites = sprites

        # todo: extra moleville trade checks

        # establish all prize locations
        # regardless if they will have their contents shuffled or not
        self.locations = {
            StartingItem1Location: StartingItem1Location(),
            StartingItem2Location: StartingItem2Location(),
            StartingItem3Location: StartingItem3Location(),
            StartingItem4Location: StartingItem4Location(),
            StartingCharacter1: StartingCharacter1(),
            MushroomWay1LowerChest: MushroomWay1LowerChest(),
            MushroomWay1UpperChest: MushroomWay1UpperChest(),
            MushroomWay1ToadRescue: MushroomWay1ToadRescue(),
            MushroomWay2LedgeChest: MushroomWay2LedgeChest(),
            MushroomWay2ToadRescue: MushroomWay2ToadRescue(),
            MushroomWayRightGoomba: MushroomWayRightGoomba(),
            MushrooomWayBossFight: MushrooomWayBossFight(),
            MushroomWayStarPiece: MushroomWayStarPiece(),
            MushroomWayBossFightRewardItem: MushroomWayBossFightRewardItem(),
            MushroomWayCharacter: MushroomWayCharacter(),
            MushroomKingdomMainHall: MushroomKingdomMainHall(),
            MushroomKingdomLiberatedVaultLeft: MushroomKingdomLiberatedVaultLeft(),
            MushroomKingdomLiberatedVaultRight: MushroomKingdomLiberatedVaultRight(),
            MushroomKingdomLiberatedVaultMiddle: MushroomKingdomLiberatedVaultMiddle(),
            MushroomKingdomChair: MushroomKingdomChair(),
            MushroomKingdomFreeShopItem: MushroomKingdomFreeShopItem(),
            MushroomKingdomShopBasementLeft: MushroomKingdomShopBasementLeft(),
            MushroomKingdomShopBasementRight: MushroomKingdomShopBasementRight(),
            MushroomKingdomWalletGuyFirstRewardLocation: MushroomKingdomWalletGuyFirstRewardLocation(),
            MushroomKingdomWalletGuySecondRewardLocation: MushroomKingdomWalletGuySecondRewardLocation(),
            MushroomKingdomOccupiedOutdoorGuardLocation: MushroomKingdomOccupiedOutdoorGuardLocation(),
            MushroomKingdomOccupiedCastleToadRescueLocation: MushroomKingdomOccupiedCastleToadRescueLocation(),
            MushroomKingdomOccupiedFamilyRescueLocation: MushroomKingdomOccupiedFamilyRescueLocation(),
            MushroomKingdomOccupiedGuestRoomLocation: MushroomKingdomOccupiedGuestRoomLocation(),
            MushroomKingdomBossFight: MushroomKingdomBossFight(),
            MushroomKingdomStarPiece: MushroomKingdomStarPiece(),
            MushroomKingdomStoreExchangeLocation: MushroomKingdomStoreExchangeLocation(),
            MushroomKingdomInnPurchaseLocation: MushroomKingdomInnPurchaseLocation(),
            BanditsWayFlowerJumpLocation: BanditsWayFlowerJumpLocation(),
            BanditsWayCoin1Location: BanditsWayCoin1Location(),
            BanditsWayCoin2Location: BanditsWayCoin2Location(),
            BanditsWayCoin3Location: BanditsWayCoin3Location(),
            BanditsWayDogChestLocation: BanditsWayDogChestLocation(),
            BanditsWayPlatformsLeftChestLocation: BanditsWayPlatformsLeftChestLocation(),
            BanditsWayPlatformsRightChestLocation: BanditsWayPlatformsRightChestLocation(),
            BanditsWayDeadEndChestLocation: BanditsWayDeadEndChestLocation(),
            BanditsWayBossFight: BanditsWayBossFight(),
            BanditsWayStarPiece: BanditsWayStarPiece(),
            BanditsWayBossFirstItemDropLocation: BanditsWayBossFirstItemDropLocation(),
            BanditsWayBossSecondItemDropLocation: BanditsWayBossSecondItemDropLocation(),
            KeroSewersStairRoomLeftChestLocation: KeroSewersStairRoomLeftChestLocation(),
            KeroSewersStairRoomRightChestLocation: KeroSewersStairRoomRightChestLocation(),
            Mimic1BossFight: Mimic1BossFight(),
            Mimic1DropRewardLocation: Mimic1DropRewardLocation(),
            Mimic1StarPiece: Mimic1StarPiece(),
            Mimic1ReloadRewardLocation: Mimic1ReloadRewardLocation(),
            KeroSewersFourRatRoomChestLocation: KeroSewersFourRatRoomChestLocation(),
            KeroSewersBeforeBelomeLowerLocation: KeroSewersBeforeBelomeLowerLocation(),
            KeroSewersBeforeBelomeUpperBeforeFlipLocation: KeroSewersBeforeBelomeUpperBeforeFlipLocation(),
            KeroSewersBeforeBelomeUpperAfterFlipLocation: KeroSewersBeforeBelomeUpperAfterFlipLocation(),
            KeroSewersBossFight: KeroSewersBossFight(),
            KeroSewersStarPiece: KeroSewersStarPiece(),
            MidasRiverFirstCompletionRewardLocation: MidasRiverFirstCompletionRewardLocation(),
            MidasRiverBottomLeftCaveLocation: MidasRiverBottomLeftCaveLocation(),
            MidasRiverBottomRightCaveLocation: MidasRiverBottomRightCaveLocation(),
            TadpolePondCricketPieExchangeLocation: TadpolePondCricketPieExchangeLocation(),
            TadpolePondCricketJamExchangeLocation: TadpolePondCricketJamExchangeLocation(),
            MelodyBayFirstRewardLocation: MelodyBayFirstRewardLocation(),
            MelodyBaySecondRewardLocation: MelodyBaySecondRewardLocation(),
            MelodyBayThirdRewardLocation: MelodyBayThirdRewardLocation(),
            RoseWaySwingingPlatformRoomLocation: RoseWaySwingingPlatformRoomLocation(),
            RoseWayLeftIslandLocation: RoseWayLeftIslandLocation(),
            RoseWayMiddleIslandLocation: RoseWayMiddleIslandLocation(),
            RoseWayCoin1Location: RoseWayCoin1Location(),
            RoseWayCoin2Location: RoseWayCoin2Location(),
            RoseWayCoin3Location: RoseWayCoin3Location(),
            RoseWayCoin4Location: RoseWayCoin4Location(),
            RoseWayCoin5Location: RoseWayCoin5Location(),
            RoseWayFiveChestRoomTopLocation: RoseWayFiveChestRoomTopLocation(),
            RoseWayFiveChestRoomBottomLeftLocation: RoseWayFiveChestRoomBottomLeftLocation(),
            RoseWayFiveChestRoomRightLocation: RoseWayFiveChestRoomRightLocation(),
            RoseWayFiveChestRoomLeftLocation: RoseWayFiveChestRoomLeftLocation(),
            RoseWayFiveChestRoomBottomRightLocation: RoseWayFiveChestRoomBottomRightLocation(),
            RoseTownShopLeftChestLocation: RoseTownShopLeftChestLocation(),
            RoseTownShopRightChestLocation: RoseTownShopRightChestLocation(),
            RoseTownCloudRightChestLocation: RoseTownCloudRightChestLocation(),
            RoseTownCloudLeftChestLocation: RoseTownCloudLeftChestLocation(),
            RoseTownInnToadPrizeLocation: RoseTownInnToadPrizeLocation(),
            RoseTownInnGazPrizeLocation: RoseTownInnGazPrizeLocation(),
            RoseTownTreasureHouseLeftChestLocation: RoseTownTreasureHouseLeftChestLocation(),
            RoseTownTreasureHouseRightChestLocation: RoseTownTreasureHouseRightChestLocation(),
            RoseTownTreasureHouseMazeRewardLocation: RoseTownTreasureHouseMazeRewardLocation(),
            RoseTownTreasureHouseUpperChestLocation: RoseTownTreasureHouseUpperChestLocation(),
            ForestMazeFirstRoomLocation: ForestMazeFirstRoomLocation(),
            ForestMazeFirstUndergroundExitLocation: ForestMazeFirstUndergroundExitLocation(),
            ForestMazeUndergroundWigglerChestLocation: ForestMazeUndergroundWigglerChestLocation(),
            ForestMazeUndergroundBottomRightTrunkChestLocation: ForestMazeUndergroundBottomRightTrunkChestLocation(),
            ForestMazeUndergroundMiddleLeftChestLocation: ForestMazeUndergroundMiddleLeftChestLocation(),
            ForestMazeInnerMazeEntranceLocation: ForestMazeInnerMazeEntranceLocation(),
            ForestMazeSecretTopRightChestLocation: ForestMazeSecretTopRightChestLocation(),
            ForestMazeSecretBottomRightChestLocation: ForestMazeSecretBottomRightChestLocation(),
            ForestMazeSecretTopMiddleChestLocation: ForestMazeSecretTopMiddleChestLocation(),
            ForestMazeSecretBottomMiddleChestLocation: ForestMazeSecretBottomMiddleChestLocation(),
            ForestMazeSecretLeftChestLocation: ForestMazeSecretLeftChestLocation(),
            ForestMazeBossFight: ForestMazeBossFight(),
            ForestMazeStarPiece: ForestMazeStarPiece(),
            ForestMazeCharacter: ForestMazeCharacter(),
            PipeVaultSlidingCoinRoomBackChestLocation: PipeVaultSlidingCoinRoomBackChestLocation(),
            PipeVaultSlidingCoinRoomMiddleChestLocation: PipeVaultSlidingCoinRoomMiddleChestLocation(),
            PipeVaultSlidingCoinRoomFrontChestLocation: PipeVaultSlidingCoinRoomFrontChestLocation(),
            PipeVaultSlidingCoinRoomCoin1Location: PipeVaultSlidingCoinRoomCoin1Location(),
            PipeVaultSlidingCoinRoomCoin2Location: PipeVaultSlidingCoinRoomCoin2Location(),
            PipeVaultSlidingCoinRoomCoin3Location: PipeVaultSlidingCoinRoomCoin3Location(),
            PipeVaultSlidingCoinRoomCoin4Location: PipeVaultSlidingCoinRoomCoin4Location(),
            PipeVaultSlidingCoinRoomCoin5Location: PipeVaultSlidingCoinRoomCoin5Location(),
            PipeVaultSlidingCoinRoomCrouchItemLocation: PipeVaultSlidingCoinRoomCrouchItemLocation(),
            PipeVaultGoombaThumpinFirstPrizeLocation: PipeVaultGoombaThumpinFirstPrizeLocation(),
            PipeVaultGoombaThumpinSecondPrizeLocation: PipeVaultGoombaThumpinSecondPrizeLocation(),
            PipeVaultRisingPlatformChestLocation: PipeVaultRisingPlatformChestLocation(),
            PipeVaultChompweedChestLocation: PipeVaultChompweedChestLocation(),
            YosterEntranceChestLocation: YosterEntranceChestLocation(),
            YosterRacePrize1Location: YosterRacePrize1Location(),
            YosterRacePrize2Location: YosterRacePrize2Location(),
            YosterRacePrize3Location: YosterRacePrize3Location(),
            BucketGirlRewardLocation: BucketGirlRewardLocation(),
            TreasureShopItem1: TreasureShopItem1(),
            TreasureShopItem2: TreasureShopItem2(),
            TreasureShopItem3: TreasureShopItem3(),
            OuterMinesTrampolineHenchmanLocation: OuterMinesTrampolineHenchmanLocation(),
            OuterMinesLeftHenchmanLocation: OuterMinesLeftHenchmanLocation(),
            OuterMinesRightHenchmanLocation: OuterMinesRightHenchmanLocation(),
            OuterMinesBossPrizeLocation: OuterMinesBossPrizeLocation(),
            OuterMinesBossFight: OuterMinesBossFight(),
            OuterMinesStarPiece: OuterMinesStarPiece(),
            InnerMinesTracksChestLocation: InnerMinesTracksChestLocation(),
            InnerMinesShyguyCartLocation: InnerMinesShyguyCartLocation(),
            InnerMinesBoxesChestLocation: InnerMinesBoxesChestLocation(),
            InnerMinesSaveBlockChestLocation: InnerMinesSaveBlockChestLocation(),
            InnerMinesHighUpChestLocation: InnerMinesHighUpChestLocation(),
            InnerMinesBossFight: InnerMinesBossFight(),
            InnerMinesStarPiece: InnerMinesStarPiece(),
            InnerMinesCharacter: InnerMinesCharacter(),
            BoosterPassBushLocation: BoosterPassBushLocation(),
            BoosterPassFirstRoomLeftChestLocation: BoosterPassFirstRoomLeftChestLocation(),
            BoosterPassFirstRoomRightChestLocation: BoosterPassFirstRoomRightChestLocation(),
            BoosterPassSecondRoomFlowerLocation: BoosterPassSecondRoomFlowerLocation(),
            BoosterPassSecretMiddleChestLocation: BoosterPassSecretMiddleChestLocation(),
            BoosterPassSecretRightChestLocation: BoosterPassSecretRightChestLocation(),
            BoosterPassSecretLeftChestLocation: BoosterPassSecretLeftChestLocation(),
            BoosterTowerSpookumStairsLocation: BoosterTowerSpookumStairsLocation(),
            BoosterTowerTrainRoomCreviceLocation: BoosterTowerTrainRoomCreviceLocation(),
            BoosterTowerChestNearThwompLocation: BoosterTowerChestNearThwompLocation(),
            BoosterTowerFallingChestLocation: BoosterTowerFallingChestLocation(),
            BoosterTowerKnifeGuyPrizeLocation: BoosterTowerKnifeGuyPrizeLocation(),
            BoosterTowerPortraitPrizeLocation: BoosterTowerPortraitPrizeLocation(),
            BoosterTowerElderKeyItemLocation: BoosterTowerElderKeyItemLocation(),
            BoosterTowerParachuteRoomChestLocation: BoosterTowerParachuteRoomChestLocation(),
            BoosterTowerParachuteRoomCreviceLocation: BoosterTowerParachuteRoomCreviceLocation(),
            BoosterTowerCheckerboardRightmostItemLocation: BoosterTowerCheckerboardRightmostItemLocation(),
            BoosterTowerCheckerboardTopItemLocation: BoosterTowerCheckerboardTopItemLocation(),
            BoosterTowerCheckerboardLeftmostItemLocation: BoosterTowerCheckerboardLeftmostItemLocation(),
            BoosterTowerCheckerboardUpperRightItemLocation: BoosterTowerCheckerboardUpperRightItemLocation(),
            BoosterTowerCheckerboardBottomItemLocation: BoosterTowerCheckerboardBottomItemLocation(),
            BoosterTowerCheckerboardCoin1Location: BoosterTowerCheckerboardCoin1Location(),
            BoosterTowerCheckerboardCoin2Location: BoosterTowerCheckerboardCoin2Location(),
            BoosterTowerCheckerboardCoin3Location: BoosterTowerCheckerboardCoin3Location(),
            BoosterTowerCheckerboardCoin4Location: BoosterTowerCheckerboardCoin4Location(),
            BoosterTowerCheckerboardCoin5Location: BoosterTowerCheckerboardCoin5Location(),
            BoosterTowerCheckerboardCoin6Location: BoosterTowerCheckerboardCoin6Location(),
            BoosterTowerCheckerboardCoin7Location: BoosterTowerCheckerboardCoin7Location(),
            BoosterTowerCheckerboardCoin8Location: BoosterTowerCheckerboardCoin8Location(),
            BoosterTowerCheckerboardCoin9Location: BoosterTowerCheckerboardCoin9Location(),
            BoosterTowerRoomKeyChestLocation: BoosterTowerRoomKeyChestLocation(),
            BoosterTowerTopFloorLowerChestLocation: BoosterTowerTopFloorLowerChestLocation(),
            BoosterTowerTopFloorUpperChestLocation: BoosterTowerTopFloorUpperChestLocation(),
            BoosterTowerTopFloorCornerChestLocation: BoosterTowerTopFloorCornerChestLocation(),
            BoosterTowerCurtainGamePrizeLocation: BoosterTowerCurtainGamePrizeLocation(),
            BoosterTowerIndoorBossFight: BoosterTowerIndoorBossFight(),
            BoosterTowerIndoorStarPiece: BoosterTowerIndoorStarPiece(),
            BoosterTowerBalconyBossFight: BoosterTowerBalconyBossFight(),
            BoosterTowerBalconyStarPiece: BoosterTowerBalconyStarPiece(),
            BoosterHillGuaranteedItem1: BoosterHillGuaranteedItem1(),
            BoosterHillGuaranteedItem2: BoosterHillGuaranteedItem2(),
            BoosterHillGuaranteedItem3: BoosterHillGuaranteedItem3(),
            BoosterHillGuaranteedItem4: BoosterHillGuaranteedItem4(),
            BoosterHillGuaranteedItem5: BoosterHillGuaranteedItem5(),
            BoosterHillGuaranteedItem6: BoosterHillGuaranteedItem6(),
            BoosterHillGuaranteedItem7: BoosterHillGuaranteedItem7(),
            BoosterHillGuaranteedItem8: BoosterHillGuaranteedItem8(),
            BoosterHillGuaranteedItem9: BoosterHillGuaranteedItem9(),
            BoosterHillGuaranteedItem10: BoosterHillGuaranteedItem10(),
            BoosterHillGuaranteedItem11: BoosterHillGuaranteedItem11(),
            BoosterHillGuaranteedItem12: BoosterHillGuaranteedItem12(),
            BoosterHillGuaranteedItem13: BoosterHillGuaranteedItem13(),
            BoosterHillGuaranteedItem14: BoosterHillGuaranteedItem14(),
            BoosterHillGuaranteedItem15: BoosterHillGuaranteedItem15(),
            BoosterHillGuaranteedItem16: BoosterHillGuaranteedItem16(),
            MarrymoreFirstSuitePrizeLocation: MarrymoreFirstSuitePrizeLocation(),
            MarrymoreSecondSuitePrizeLocation: MarrymoreSecondSuitePrizeLocation(),
            MarrymoreThirdSuitePrizeLocation: MarrymoreThirdSuitePrizeLocation(),
            MarrymoreFourthSuitePrizeLocation: MarrymoreFourthSuitePrizeLocation(),
            MarrymoreFifthSuitePrizeLocation: MarrymoreFifthSuitePrizeLocation(),
            MarrymoreSixthSuitePrizeLocation: MarrymoreSixthSuitePrizeLocation(),
            MarrymoreBigTipLocation: MarrymoreBigTipLocation(),
            MarrymoreHotelChestLocation: MarrymoreHotelChestLocation(),
            MarrymoreSnifit1Location: MarrymoreSnifit1Location(),
            MarrymoreSnifit2Location: MarrymoreSnifit2Location(),
            MarrymoreSnifit3Location: MarrymoreSnifit3Location(),
            MarrymoreAltarHeadLocation: MarrymoreAltarHeadLocation(),
            MarrymoreBossFight: MarrymoreBossFight(),
            MarrymoreBossFightStarPiece: MarrymoreBossFightStarPiece(),
            MarrymoreCharacter: MarrymoreCharacter(),
            StarHillStarPiece: StarHillStarPiece(),
            FrogDiscipleLocation1: FrogDiscipleLocation1(),
            FrogDiscipleLocation2: FrogDiscipleLocation2(),
            FrogDiscipleLocation3: FrogDiscipleLocation3(),
            FrogDiscipleLocation4: FrogDiscipleLocation4(),
            FrogDiscipleLocation5: FrogDiscipleLocation5(),
            SeasideBeachBossFight: SeasideBeachBossFight(),
            SeasideBeachStarPiece: SeasideBeachStarPiece(),
            SeasideTownBossPrizeLocation: SeasideTownBossPrizeLocation(),
            SeasideTownShedRescueLocation: SeasideTownShedRescueLocation(),
            SeaStarslapRoomChestLocation: SeaStarslapRoomChestLocation(),
            SeaSaveRoomBackChestLocation: SeaSaveRoomBackChestLocation(),
            SeaSaveRoomMiddleChestLocation: SeaSaveRoomMiddleChestLocation(),
            SeaSaveRoomFrontChestLocation: SeaSaveRoomFrontChestLocation(),
            SeaWhirlpoolChestLocation: SeaWhirlpoolChestLocation(),
            ShipRatStairsChestLocation: ShipRatStairsChestLocation(),
            ShipRatStairsBoxesLocation: ShipRatStairsBoxesLocation(),
            ShipTroopaPuzzleLocation: ShipTroopaPuzzleLocation(),
            ShipTrampolinePuzzle: ShipTrampolinePuzzle(),
            Ship3DMazePuzzle: Ship3DMazePuzzle(),
            ShipShopChestLocation: ShipShopChestLocation(),
            ShipCoinSnakePuzzleLocation: ShipCoinSnakePuzzleLocation(),
            ShipCannonballPuzzle: ShipCannonballPuzzle(),
            ShipBarrelPuzzle: ShipBarrelPuzzle(),
            ShipPasswordBossFight: ShipPasswordBossFight(),
            ShipPasswordStarPiece: ShipPasswordStarPiece(),
            EarlyInnerShipLeftChestLocation: EarlyInnerShipLeftChestLocation(),
            EarlyInnerShipRightChestLocation: EarlyInnerShipRightChestLocation(),
            InnerShipCloneRoomChestLocation: InnerShipCloneRoomChestLocation(),
            InnerShipBehindBoxesChestLocation: InnerShipBehindBoxesChestLocation(),
            InnerShipSaveRoomLeftChestLocation: InnerShipSaveRoomLeftChestLocation(),
            InnerShipSaveRoomRightChestLocation: InnerShipSaveRoomRightChestLocation(),
            Mimic2DropRewardLocation: Mimic2DropRewardLocation(),
            Mimic2BossFight: Mimic2BossFight(),
            Mimic2StarPiece: Mimic2StarPiece(),
            Mimic2ReloadRewardLocation: Mimic2ReloadRewardLocation(),
            InnerShipFirstUnderwaterRoomBottomItemLocation: InnerShipFirstUnderwaterRoomBottomItemLocation(),
            InnerShipFirstUnderwaterRoomTopItemLocation: InnerShipFirstUnderwaterRoomTopItemLocation(),
            InnerShipFirstUnderwaterRoomLeftItemLocation: InnerShipFirstUnderwaterRoomLeftItemLocation(),
            InnerShipFirstUnderwaterRoomMiddleItemLocation: InnerShipFirstUnderwaterRoomMiddleItemLocation(),
            InnerShipSecretRoomChestLocation: InnerShipSecretRoomChestLocation(),
            InnerShipPoolRoomLocation: InnerShipPoolRoomLocation(),
            InnerShipBeforeBossChestLocation: InnerShipBeforeBossChestLocation(),
            ShipFinalBossFight: ShipFinalBossFight(),
            ShipFinalStarPiece: ShipFinalStarPiece(),
            LandsEndRisingPlatformChestLocation: LandsEndRisingPlatformChestLocation(),
            LandsEndChowPitStaticChestLocation: LandsEndChowPitStaticChestLocation(),
            LandsEndChowPitMovingChestLocation: LandsEndChowPitMovingChestLocation(),
            LandsEndBeeTowerChestLocation: LandsEndBeeTowerChestLocation(),
            LandsEndGrottoEntranceChestLocation: LandsEndGrottoEntranceChestLocation(),
            LandsEndGrottoCornerChestLocation: LandsEndGrottoCornerChestLocation(),
            LandsEndGrottoEndChestLocation: LandsEndGrottoEndChestLocation(),
            LandsEndUndergroundSaveBoxChestLocation: LandsEndUndergroundSaveBoxChestLocation(),
            LandsEndFirstPurchasableChestLocation: LandsEndFirstPurchasableChestLocation(),
            LandsEndSecondPurchasableChestLocation: LandsEndSecondPurchasableChestLocation(),
            TroopaClimbSub12PrizeLocation: TroopaClimbSub12PrizeLocation(),
            LandsEndCloudBoss: LandsEndCloudBoss(),
            LandsEndCloudStarPiece: LandsEndCloudStarPiece(),
            BelomeTempleFortuneTellerLocation: BelomeTempleFortuneTellerLocation(),
            BelomeTempleLMRChestLocation: BelomeTempleLMRChestLocation(),
            BelomeTempleLRMChestLocation: BelomeTempleLRMChestLocation(),
            BelomeTempleRLMChestLocation: BelomeTempleRLMChestLocation(),
            BelomeTempleRMLChestLocation: BelomeTempleRMLChestLocation(),
            BelomeBeforeBossRightChestLocation: BelomeBeforeBossRightChestLocation(),
            BelomeBeforeBossLowerLeftChestLocation: BelomeBeforeBossLowerLeftChestLocation(),
            BelomeBeforeBossMiddleChestLocation: BelomeBeforeBossMiddleChestLocation(),
            BelomeBeforeBossUpperLeftChestLocation: BelomeBeforeBossUpperLeftChestLocation(),
            BelomeTempleTreasuryUpperCornerLeftItemLocation: BelomeTempleTreasuryUpperCornerLeftItemLocation(),
            BelomeTempleTreasuryUpperCornerLowerLeftItemLocation: BelomeTempleTreasuryUpperCornerLowerLeftItemLocation(),
            BelomeTempleTreasuryUpperCornerTopItemLocation: BelomeTempleTreasuryUpperCornerTopItemLocation(),
            BelomeTempleTreasuryTopmostItemLocation: BelomeTempleTreasuryTopmostItemLocation(),
            BelomeTempleTreasuryMidLeftItemLocation: BelomeTempleTreasuryMidLeftItemLocation(),
            BelomeTempleTreasuryAlmostTopItemLocation: BelomeTempleTreasuryAlmostTopItemLocation(),
            BelomeTempleTreasuryAlmostLeftmostItemLocation: BelomeTempleTreasuryAlmostLeftmostItemLocation(),
            BelomeTempleTreasuryOuterUpperRightItemLocation: BelomeTempleTreasuryOuterUpperRightItemLocation(),
            BelomeTempleTreasuryInnerUpperRightItemLocation: BelomeTempleTreasuryInnerUpperRightItemLocation(),
            BelomeTempleTreasuryLowestItemsRightLocation: BelomeTempleTreasuryLowestItemsRightLocation(),
            BelomeTempleTreasuryLowerOuterBottomRightItemLocation: BelomeTempleTreasuryLowerOuterBottomRightItemLocation(),
            BelomeTempleTreasuryRightmostItemLocation: BelomeTempleTreasuryRightmostItemLocation(),
            BelomeTempleTreasuryBottomLeftCornerItemLocation: BelomeTempleTreasuryBottomLeftCornerItemLocation(),
            BelomeTempleTreasuryLowestItemsLeftLocation: BelomeTempleTreasuryLowestItemsLeftLocation(),
            BelomeTempleTreasuryUpperOuterBottomRightItemLocation: BelomeTempleTreasuryUpperOuterBottomRightItemLocation(),
            TempleBossFight: TempleBossFight(),
            TempleBossFightStarPiece: TempleBossFightStarPiece(),
            MonstroEntranceLocation: MonstroEntranceLocation(),
            MonstroThwompItemLocation: MonstroThwompItemLocation(),
            DojoFirstFight: DojoFirstFight(),
            DojoFirstFightStarPiece: DojoFirstFightStarPiece(),
            DojoSecondFight: DojoSecondFight(),
            DojoSecondFightStarPiece: DojoSecondFightStarPiece(),
            DojoThirdFight: DojoThirdFight(),
            DojoThirdFightStarPiece: DojoThirdFightStarPiece(),
            DojoFourthFight: DojoFourthFight(),
            DojoFourthFightStarPiece: DojoFourthFightStarPiece(),
            MonstroDojoClearRewardLocation: MonstroDojoClearRewardLocation(),
            MonstroSealedDoorBossFight: MonstroSealedDoorBossFight(),
            MonstroSealedDoorStarPiece: MonstroSealedDoorStarPiece(),
            MonstroSealedDoorClearRewardLocation: MonstroSealedDoorClearRewardLocation(),
            MonstroFirstSuperJumpRewardLocation: MonstroFirstSuperJumpRewardLocation(),
            MonstroSecondSuperJumpRewardLocation: MonstroSecondSuperJumpRewardLocation(),
            MonstroFlagExchangeLocation: MonstroFlagExchangeLocation(),
            BeanValleyFirstDeadEndLocation: BeanValleyFirstDeadEndLocation(),
            BeanValleyFirstProgressChestLocation: BeanValleyFirstProgressChestLocation(),
            BeanValleyLeftPiranhaPipeLocation: BeanValleyLeftPiranhaPipeLocation(),
            BeanValleyBottomLeftPiranhaPipeLocation: BeanValleyBottomLeftPiranhaPipeLocation(),
            BeanValleyBottomRightPiranhaPipeUpperLocation: BeanValleyBottomRightPiranhaPipeUpperLocation(),
            BeanValleyBottomRightPiranhaPipeLowerLocation: BeanValleyBottomRightPiranhaPipeLowerLocation(),
            BeanValleyRightPipeLeftChestLocation: BeanValleyRightPipeLeftChestLocation(),
            Mimic3BossFight: Mimic3BossFight(),
            Mimic3StarPiece: Mimic3StarPiece(),
            BeanValleyRightPipeRightChestLocation: BeanValleyRightPipeRightChestLocation(),
            BeanValleyRightPipeUnderStairsLocation: BeanValleyRightPipeUnderStairsLocation(),
            BeanValleyRightPipeAboveGroundLocation: BeanValleyRightPipeAboveGroundLocation(),
            BeanValleyPlanterBossFight: BeanValleyPlanterBossFight(),
            BeanValleyPlanterStarPiece: BeanValleyPlanterStarPiece(),
            BeanValleyBossNoteLocation: BeanValleyBossNoteLocation(),
            BeanstalkLowestChestLocation: BeanstalkLowestChestLocation(),
            BeanValley1stRoomFloatingItemLocation: BeanValley1stRoomFloatingItemLocation(),
            BeanValley1stRoomMiddleCoinLocation: BeanValley1stRoomMiddleCoinLocation(),
            BeanValley1stRoomUpperCoinLocation: BeanValley1stRoomUpperCoinLocation(),
            BeanValley1stRoomLowerCoinLocation: BeanValley1stRoomLowerCoinLocation(),
            Beanstalk2ndRoomFloatingItemLocation: Beanstalk2ndRoomFloatingItemLocation(),
            Beanstalk2ndRoomCoin1Location: Beanstalk2ndRoomCoin1Location(),
            Beanstalk2ndRoomCoin2Location: Beanstalk2ndRoomCoin2Location(),
            Beanstalk2ndRoomCoin3Location: Beanstalk2ndRoomCoin3Location(),
            BeanValleyEastBeanstalkCoin1Location: BeanValleyEastBeanstalkCoin1Location(),
            BeanValleyEastBeanstalkCoin2Location: BeanValleyEastBeanstalkCoin2Location(),
            BeanValleyEastBeanstalkCoin3Location: BeanValleyEastBeanstalkCoin3Location(),
            BeanValleyEastBeanstalkCoin4Location: BeanValleyEastBeanstalkCoin4Location(),
            BeanValleyEastBeanstalkCoin5Location: BeanValleyEastBeanstalkCoin5Location(),
            BeanValleyWestBeanstalkCoin1Location: BeanValleyWestBeanstalkCoin1Location(),
            BeanValleyWestBeanstalkCoin2Location: BeanValleyWestBeanstalkCoin2Location(),
            BeanValleyWestBeanstalkCoin3Location: BeanValleyWestBeanstalkCoin3Location(),
            BeanValleyWestBeanstalkFloatingItemLocation: BeanValleyWestBeanstalkFloatingItemLocation(),
            BeanstalkUpperCloudLeftChestLocation: BeanstalkUpperCloudLeftChestLocation(),
            BeanstalkUpperCloudRightChestLocation: BeanstalkUpperCloudRightChestLocation(),
            BeanstalkLowerCloudLeftChestLocation: BeanstalkLowerCloudLeftChestLocation(),
            BeanstalkLowerCloudRightChestLocation: BeanstalkLowerCloudRightChestLocation(),
            CasinoGrateGuyPrizeLocation: CasinoGrateGuyPrizeLocation(),
            NimbusShopChestLocation: NimbusShopChestLocation(),
            NimbusInnDreamPrize1Location: NimbusInnDreamPrize1Location(),
            NimbusInnDreamPrize2Location: NimbusInnDreamPrize2Location(),
            NimbusCastleStatueGamePrizeLocation: NimbusCastleStatueGamePrizeLocation(),
            StatueRoomBossFight: StatueRoomBossFight(),
            StatueRoomStarPiece: StatueRoomStarPiece(),
            NimbusCastleOuterPrisonCellarRightNPCLocation: NimbusCastleOuterPrisonCellarRightNPCLocation(),
            NimbusCastleOuterPrisonCellarLeftNPCLocation: NimbusCastleOuterPrisonCellarLeftNPCLocation(),
            NimbusCastleBusinessCentreOccupiedChestLocation: NimbusCastleBusinessCentreOccupiedChestLocation(),
            NimbusCastleCornerBridgeChestLocation: NimbusCastleCornerBridgeChestLocation(),
            NimbusCastleOutOfBoundsChestLocation: NimbusCastleOutOfBoundsChestLocation(),
            NimbusCastleAboveJawfulChestLocation: NimbusCastleAboveJawfulChestLocation(),
            NimbusCastleSingleGoldBirdChestLocation: NimbusCastleSingleGoldBirdChestLocation(),
            NimbusCastleTwoLevelLowerChestLocation: NimbusCastleTwoLevelLowerChestLocation(),
            GiantEggBossFight: GiantEggBossFight(),
            GiantEggStarPiece: GiantEggStarPiece(),
            NimbusCastleGiantEggRewardLocation: NimbusCastleGiantEggRewardLocation(),
            NimbusCastleTwoLevelUpperChestLocation: NimbusCastleTwoLevelUpperChestLocation(),
            NimbusCastleBackHallwayOccupiedChestLocation: NimbusCastleBackHallwayOccupiedChestLocation(),
            NimbusFinalBossFight: NimbusFinalBossFight(),
            NimbusFinalStarPiece: NimbusFinalStarPiece(),
            NimbusCastleBackHallwayLiberatedChestLocation: NimbusCastleBackHallwayLiberatedChestLocation(),
            NimbusCastleBusinessCentreLiberatedChestLocation: NimbusCastleBusinessCentreLiberatedChestLocation(),
            NimbusLandRightSideLocation: NimbusLandRightSideLocation(),
            NimbusLandCrocoItemLocation: NimbusLandCrocoItemLocation(),
            NimbusLandInnerCellarLocation: NimbusLandInnerCellarLocation(),
            VolcanoLavaCoveLeftChestLocation: VolcanoLavaCoveLeftChestLocation(),
            VolcanoLavaCoveRightChestLocation: VolcanoLavaCoveRightChestLocation(),
            VolcanoEarlyProgressChestLeftLocation: VolcanoEarlyProgressChestLeftLocation(),
            VolcanoEarlyProgressChestRightLocation: VolcanoEarlyProgressChestRightLocation(),
            VolcanoEarlyProgressThirdChestLocation: VolcanoEarlyProgressThirdChestLocation(),
            VolcanoLavaPoolLocation: VolcanoLavaPoolLocation(),
            VolcanoReverseRecoilItemLocation: VolcanoReverseRecoilItemLocation(),
            VolcanoRightDonutItemLocation: VolcanoRightDonutItemLocation(),
            VolcanoLeftDonutItemLocation: VolcanoLeftDonutItemLocation(),
            VolcanoSaveRoomLowerChestLocation: VolcanoSaveRoomLowerChestLocation(),
            VolcanoSaveRoomUpperChestLocation: VolcanoSaveRoomUpperChestLocation(),
            VolcanoShopEntranceChestLocation: VolcanoShopEntranceChestLocation(),
            VolcanoBridgeBossFight: VolcanoBridgeBossFight(),
            VolcanoBridgeStarPiece: VolcanoBridgeStarPiece(),
            VolcanoExitBossFight: VolcanoExitBossFight(),
            VolcanoExitStarPiece: VolcanoExitStarPiece(),
            KeepDarkRoomChestLocation: KeepDarkRoomChestLocation(),
            KeepFirstCrocoShopLeftChestLocation: KeepFirstCrocoShopLeftChestLocation(),
            KeepFirstCrocoShopRightChestLocation: KeepFirstCrocoShopRightChestLocation(),
            KeepInvisibleBridgeFrontChestLocation: KeepInvisibleBridgeFrontChestLocation(),
            KeepInvisibleBridgeRightChestLocation: KeepInvisibleBridgeRightChestLocation(),
            KeepInvisibleBridgeLeftChestLocation: KeepInvisibleBridgeLeftChestLocation(),
            KeepInvisibleBridgeBackChestLocation: KeepInvisibleBridgeBackChestLocation(),
            KeepInvisibleBridgeCoin1Location: KeepInvisibleBridgeCoin1Location(),
            KeepInvisibleBridgeCoin2Location: KeepInvisibleBridgeCoin2Location(),
            KeepInvisibleBridgeCoin3Location: KeepInvisibleBridgeCoin3Location(),
            KeepInvisibleBridgeCoin4Location: KeepInvisibleBridgeCoin4Location(),
            KeepXYPlatformsBackLeftChestLocation: KeepXYPlatformsBackLeftChestLocation(),
            KeepXYPlatformsFrontLeftChestLocation: KeepXYPlatformsFrontLeftChestLocation(),
            KeepXYPlatformsFrontRightChestLocation: KeepXYPlatformsFrontRightChestLocation(),
            KeepXYPlatformsBackRightChestLocation: KeepXYPlatformsBackRightChestLocation(),
            KeepElevatorRoomChestLocation: KeepElevatorRoomChestLocation(),
            KeepCannonballRoomFrontRightChestLocation: KeepCannonballRoomFrontRightChestLocation(),
            KeepCannonballRoomBackChestLocation: KeepCannonballRoomBackChestLocation(),
            KeepCannonballFrontLeftChestLocation: KeepCannonballFrontLeftChestLocation(),
            KeepCannonballMidRightChestLocation: KeepCannonballMidRightChestLocation(),
            KeepCannonballMidLeftChestLocation: KeepCannonballMidLeftChestLocation(),
            KeepCannonballCoin1Location: KeepCannonballCoin1Location(),
            KeepCannonballCoin2Location: KeepCannonballCoin2Location(),
            KeepCannonballCoin3Location: KeepCannonballCoin3Location(),
            KeepCannonballCoin4Location: KeepCannonballCoin4Location(),
            KeepCannonballCoin5Location: KeepCannonballCoin5Location(),
            KeepCannonballCoin6Location: KeepCannonballCoin6Location(),
            KeepCannonballCoin7Location: KeepCannonballCoin7Location(),
            KeepCannonballCoin8Location: KeepCannonballCoin8Location(),
            KeepRotatingPlatformsFrontChestLocation: KeepRotatingPlatformsFrontChestLocation(),
            KeepRotatingPlatformsFrontMidLeftChestLocation: KeepRotatingPlatformsFrontMidLeftChestLocation(),
            KeepRotatingPlatformsBackMidRightChestLocation: KeepRotatingPlatformsBackMidRightChestLocation(),
            KeepRotatingPlatformsFrontMidRightChestLocation: KeepRotatingPlatformsFrontMidRightChestLocation(),
            KeepRotatingPlatformsBackMidLeftChestLocation: KeepRotatingPlatformsBackMidLeftChestLocation(),
            KeepRotatingPlatformsBackChestLocation: KeepRotatingPlatformsBackChestLocation(),
            ObstacleCourseFinalFight: ObstacleCourseFinalFight(),
            ObstacleCourseFinalFightStarPiece: ObstacleCourseFinalFightStarPiece(),
            KeepDoorRewardChest1Location: KeepDoorRewardChest1Location(),
            KeepDoorRewardChest2Location: KeepDoorRewardChest2Location(),
            KeepDoorRewardChest3Location: KeepDoorRewardChest3Location(),
            KeepDoorRewardChest4Location: KeepDoorRewardChest4Location(),
            KeepDoorRewardChest5Location: KeepDoorRewardChest5Location(),
            KeepDoorRewardChest6Location: KeepDoorRewardChest6Location(),
            KeepAfterObstaclesBossFight: KeepAfterObstaclesBossFight(),
            KeepAfterObstaclesStarPiece: KeepAfterObstaclesStarPiece(),
            KeepAfterObstaclesBossChestLocation: KeepAfterObstaclesBossChestLocation(),
            KeepChandelierBossFight: KeepChandelierBossFight(),
            KeepChandelierStarPiece: KeepChandelierStarPiece(),
            KeepFinalBossFight: KeepFinalBossFight(),
            KeepFinalStarPiece: KeepFinalStarPiece(),
            OuterFactorySaveRoomChestLocation: OuterFactorySaveRoomChestLocation(),
            FactoryBoltPlatformsChestLocation: FactoryBoltPlatformsChestLocation(),
            FactoryEntranceBossFight: FactoryEntranceBossFight(),
            FactoryEntranceStarPiece: FactoryEntranceStarPiece(),
            FactoryAxemConveyorsChestLocation: FactoryAxemConveyorsChestLocation(),
            FactoryTreasurePitBackChestLocation: FactoryTreasurePitBackChestLocation(),
            FactoryTreasurePitFrontChestLocation: FactoryTreasurePitFrontChestLocation(),
            FactoryBigConveyorRoomFirstChestLocation: FactoryBigConveyorRoomFirstChestLocation(),
            FactoryBigConveyorRoomSecondChestLocation: FactoryBigConveyorRoomSecondChestLocation(),
            FactoryBehindNinjasRightChestLocation: FactoryBehindNinjasRightChestLocation(),
            FactoryBehindNinjasLeftChestLocation: FactoryBehindNinjasLeftChestLocation(),
            FactoryTransitionBossFight: FactoryTransitionBossFight(),
            FactoryTransitionStarPiece: FactoryTransitionStarPiece(),
            InnerFactoryFirstFight: InnerFactoryFirstFight(),
            InnerFactoryFirstFightStarPiece: InnerFactoryFirstFightStarPiece(),
            InnerFactoryToadGiftLocation: InnerFactoryToadGiftLocation(),
            InnerFactorySecondFight: InnerFactorySecondFight(),
            InnerFactorySecondFightStarPiece: InnerFactorySecondFightStarPiece(),
            InnerFactoryThirdFight: InnerFactoryThirdFight(),
            InnerFactoryThirdFightStarPiece: InnerFactoryThirdFightStarPiece(),
            InnerFactoryFourthFight: InnerFactoryFourthFight(),
            InnerFactoryFourthFightStarPiece: InnerFactoryFourthFightStarPiece(),
            FinalBossFight: FinalBossFight(),
            FinalBossFightStarPiece: FinalBossFightStarPiece(),
            MarioSpell1: MarioSpell1(),
            MarioSpell2: MarioSpell2(),
            MarioSpell3: MarioSpell3(),
            MarioSpell4: MarioSpell4(),
            MarioSpell5: MarioSpell5(),
            MarioSpell6: MarioSpell6(),
            MallowSpell1: MallowSpell1(),
            MallowSpell2: MallowSpell2(),
            MallowSpell3: MallowSpell3(),
            MallowSpell4: MallowSpell4(),
            MallowSpell5: MallowSpell5(),
            MallowSpell6: MallowSpell6(),
            GenoSpell1: GenoSpell1(),
            GenoSpell2: GenoSpell2(),
            GenoSpell3: GenoSpell3(),
            GenoSpell4: GenoSpell4(),
            GenoSpell5: GenoSpell5(),
            GenoSpell6: GenoSpell6(),
            BowserSpell1: BowserSpell1(),
            BowserSpell2: BowserSpell2(),
            BowserSpell3: BowserSpell3(),
            BowserSpell4: BowserSpell4(),
            BowserSpell5: BowserSpell5(),
            BowserSpell6: BowserSpell6(),
            ToadstoolSpell1: ToadstoolSpell1(),
            ToadstoolSpell2: ToadstoolSpell2(),
            ToadstoolSpell3: ToadstoolSpell3(),
            ToadstoolSpell4: ToadstoolSpell4(),
            ToadstoolSpell5: ToadstoolSpell5(),
            ToadstoolSpell6: ToadstoolSpell6(),
        }
        if self.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE)
            fwshop = FireworksShopItemLocation()
            fwshop._originally_held = ProgressiveFireworksPrize
            fwshop.set_prize(ProgressiveFireworksPrize())
            self.locations = {
                **self.locations,
                FireworksShopItemLocation: fwshop,
                PurtendStoreLocation: PurtendStoreLocation(),
                CookieTraderLocation: CookieTraderLocation(),
            }
        if self.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE)
            fwshop = FireworksShopItemLocation()
            self.locations = {
                **self.locations,
                FireworksShopItemLocation: fwshop
            }

        strchars = self.settings.get_flag(StartingCharacters)
        startmax = len(strchars.enabled)
        if startmax >= 2:
            self.locations = {
                **self.locations,
                StartingCharacter2: StartingCharacter2(),
            }
        if startmax >= 3:
            self.locations = {
                **self.locations,
                StartingCharacter3: StartingCharacter3(),
            }
        if startmax >= 4:
            self.locations = {
                **self.locations,
                StartingCharacter4: StartingCharacter4(),
            }
        if startmax >= 5:
            self.locations = {
                **self.locations,
                StartingCharacter5: StartingCharacter5(),
            }

        # Optionally include remake content.
        if self.settings.get_flag(Remake).enabled:
            self.locations = {
                **self.locations,
                PostgameVoucherLocation: PostgameVoucherLocation(),
                MushroomWayLeftItemRemake: MushroomWayLeftItemRemake(),
                MushroomWayRightItemRemake: MushroomWayRightItemRemake(),
                InnerMinesPostgameBossFight: InnerMinesPostgameBossFight(),
                InnerMinesPostgameStarPiece: InnerMinesPostgameStarPiece(),
                InnerMinesPostgameDrop: InnerMinesPostgameDrop(),
                BoosterTowerIndoorBossFightRemake: BoosterTowerIndoorBossFightRemake(),
                BoosterTowerIndoorStarPieceRemake: BoosterTowerIndoorStarPieceRemake(),
                BoosterTowerRemakeBossFightPrizeLocation: BoosterTowerRemakeBossFightPrizeLocation(),
                MarrymoreBossFightRemake: MarrymoreBossFightRemake(),
                MarrymoreBossFightStarPieceRemake: MarrymoreBossFightStarPieceRemake(),
                MarrymoreBossFightRemakeItemDrop: MarrymoreBossFightRemakeItemDrop(),
                ShipPostgameBossFight: ShipPostgameBossFight(),
                ShipPostgameFightItemDrop: ShipPostgameFightItemDrop(),
                ShipPostgameStarPiece: ShipPostgameStarPiece(),
                TempleBossFightPostgame: TempleBossFightPostgame(),
                TempleBossFightStarPiecePostgame: TempleBossFightStarPiecePostgame(),
                TemplePostgameFightItemDrop: TemplePostgameFightItemDrop(),
                DojoFifthFight: DojoFifthFight(),
                DojoFifthFightStarPiece: DojoFifthFightStarPiece(),
                MonstroDojoPostgameClearRewardLocation: MonstroDojoPostgameClearRewardLocation(),
                MonstroSealedDoorBossFightPostgame: MonstroSealedDoorBossFightPostgame(),
                MonstroSealedDoorStarPiecePostgame: MonstroSealedDoorStarPiecePostgame(),
                MonstroSealedDoorClearRewardLocationPostgame: MonstroSealedDoorClearRewardLocationPostgame(),
                LandsEndCaveSideRemake: LandsEndCaveSideRemake(),
            }
            # Checks for postgame-unlocking bosses by default expect an impossible value.
            # Enabling the remake flag sets it to the correct value, 7.
            cast(CompareVarToConst, self.event_scripts.get_script_by_id("postgame_progress_checker_1")).set_value(7)
            cast(CompareVarToConst, self.event_scripts.get_script_by_id("postgame_progress_checker_2")).set_value(7)
           
        invisible_item_pool = [
            MariosPadBedFlag,
            RoseTownSignFlag,
            YosterIsleGoalFlag,
            MariosPadSteamwhistleFlag,
            MariosPadLanternFlag,
            MariosPadHatFlag,
            MushroomWayTreeFlag,
            MushroomKingdomSignFlag,
            MushroomKingdomEmptyHouseFlag,
            ChancellorThroneFlag,
            BanditsWayFlowerFlag,
            KeroStairsFlag,
            KeroGateFlag,
            MidasTreesFlag,
            TadpoleCabinetFlag,
            RoseWayDirtPatchFlag,
            RoseTownHydrantFlag,
            RoseTownSinkFlag,
            RoseTownBowserFlag,
            RoseTownGardenerHydrantFlag,
            RoseTownGardenerBucketFlag,
            RoseTownGardenerLeafFlag,
            ForestMazeSecretStumpFlag,
            ForestMazeSecretMushroomsFlag,
            ForestMazeSecretWigglerFlag,
            PipeVaultExteriorFlag,
            PipeVaultRedPipeFlag,
            YosterIsleHutFlag,
            MolevilleHydrantFlag,
            MolevilleMountainBushFlag,
            MolevilleBedFlag,
            MolevilleMinesArrowsFlag,
            MolevilleMinesCeilingFlag,
            MolevilleMinesEntryFlag,
            BoosterPassCornerBushFlag,
            BoosterTowerExteriorSignFlag,
            BoosterTowerDeskFlag,
            BoosterTowerMasherRoomFlag,
            BoosterTowerCurtainFlag,
            BoosterTowerThwompInvisibleFlag,
            BoosterTowerBrokenFrameFlag,
            BoosterTowerBeetleCageFlag,
            BoosterTowerToyBoxFlag,
            MarrymoreOutsideCrateFlag,
            MarrymoreHallwayFlag,
            MarrymoreSuiteBedFlag,
            MarrymoreKitchenFlag,
            MarrymoreFireplaceFlag,
            MarrymoreOrganFlag,
            MarrymoreAltarFlag,
            StarHillNorthStarFlag,
            SeasideTownAnchorFlag,
            SeasideTownHydrantFlag,
            SeasideTownBucketFlag,
            SeasideTownFlowersFlag,
            SeasideTownShedBoxFlag,
            SeaArrowFlag,
            SeaBoxesFlag,
            SeaStalagnateFlag,
            SeaUnderwaterSailFlag,
            ShipBarrelPileFlag,
            ShipDoorMarkerFlag,
            ShipButtonFlag,
            ShipSwitchFlag,
            LandsEndPlatformFlag,
            LandsEndCannonFlag,
            LandsEndArrowFlag,
            LandsEndHillFlag,
            LandsEndTwoHillFlag,
            LandsEndStalagmiteFlag,
            LandsEndCliffBushFlag,
            LandsEndSignFlag,
            DojoBonsaiFlag,
            MonstroEntranceSignFlag,
            MonstroBatFlag,
            MonstroFanFlag,
            MonstroShellFlag,
            BeanValleyPipeFlag,
            BeanValleyBeanstalkBlockFlag,
            CasinoBellFlag,
            NimbusGoldGoombaFlag,
            NimbusInnLobbyFlag,
            NimbusPlantFlag,
            NimbusBirdFlag,
            NimbusHotSpringsFlag,
            VolcanoShipsFlag,
            KeepPostObstacleBossRoomFlag,
            KeepThwompFlag,
            FactoryCanopyFlag,
            FactoryLugnutFlag,
            FactoryTrampolineFlag,
            FactoryButtonFlag,
        ]

        for i in range (0, 3):
            if not self.settings.invisible_flags_setting:
                self.locations[invisible_item_pool[i]] = invisible_item_pool[i](i)
            else:
                c = random.choice(invisible_item_pool)
                self.locations[c] = c(i)

        
        # Perform progression gating setup tasks here

        if self.settings.get_flag(KeroSewersGating).value != KeroSewersGating.OPEN:
            cast(RoomObject, self.rooms._rooms[R333_KERO_SEWERS_ENTRANCE].get_npc_by_target_id(NPC_0)).set_visible(True)
            cast(RoomObject, self.rooms._rooms[R333_KERO_SEWERS_ENTRANCE].get_npc_by_target_id(NPC_1)).set_visible(True)

        # todo: bake boss hunts into writing event 353
            
    def get_patch(self) -> Patch:
        patch = Patch()

        # Battle animations patch
        for animation_bank in self.battle_animations.values():
            patches = animation_bank.render()
            for p in patches:
                patch.add_data(p[0], p[1])

        # Event scripts patch
        for event_script_bank in self.event_scripts.banks:
            patch.add_data(event_script_bank.start, event_script_bank.render())

        # Monster AI scripts patch
        monster_scripts = self.monster_scripts.render()
        patch.add_data(self.monster_scripts.pointer_table_start, monster_scripts[0])
        patch.add_data(self.monster_scripts.range_2_start, monster_scripts[1])

        # Sprite graphics patch
        for p in self.sprites.render():
            patch.add_data(p[0], p[1])

        # Dialogs, enemies, items, action scripts, packets, battle packs, rooms, shops, spells
        patch.add_dict(self.battle_dialogs.render())
        patch.add_dict(self.overworld_dialogs.render())
        patch.add_dict(self.enemies.render())
        patch.add_dict(self.enemy_attacks.render())
        patch.add_dict(self.items.render())
        patch.add_data(self.action_scripts.start, self.action_scripts.render())
        patch.add_dict(self.packets.render())
        patch.add_dict(self.battle_packs.render())
        patch.add_dict(self.rooms.render())
        patch.add_dict(self.shops.render())
        patch.add_dict(self.spells.render())
        patch.add_dict(self.allies.render())

        # Misc

        # Expand key item inventory size
        patch.add_data(0xC305, 0x20)
        patch.add_data(0xC37F, 0x20)
        patch.add_data(
            0xC3B5, 0x20
        )  # TODO might need to be larger than 0x20, recount key items
        patch.add_data(0xC302, [0xF0, 0xF8])
        patch.add_data(0xC37C, [0xF0, 0xF8])
        patch.add_data(0xC3B2, [0xF0, 0xF8])
        patch.add_data(0x2BC80, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BC95, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BCA1, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BCB6, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x353080, [0xF0, 0xF8, 0x7F])

        # Postgame weapon palettes
        patch.add_data(
            0x25894C,
            bytes.fromhex(
                "7B 37 BD 33 39 33 F7 2E F7 2A F7 22 31 26 52 22 DE 53 10 1E 8C 15 4A 15 08 11 C6 0C 63 0C"
            ),
        )
        patch.add_data(
            0x25896A,
            bytes.fromhex(
                "BD 6B BD 6B 5B 47 39 3B 95 1A D7 1E 74 1A EF 15 6C 0D 09 09 A6 04 A6 04 84 04 FF 7B 63 0C"
            ),
        )
        patch.add_data(
            0x25DEE4,
            bytes.fromhex(
                "FF 7F F5 7F EA 7F E0 7F 40 7F 80 7E E0 7D 20 7D 00 69 C0 58 A0 44 60 30 40 20 00 0C 00 00"
            ),
        )

        # TODO: make these conditional based on a flag
        # hold B to advance
        patch.add_data(0x5D5E, [0x20, 0x54, 0xF1])
        patch.add_data(0x15627, [0x22, 0x90, 0xFE, 0xC2, 0x89, 0x80, 0x00])
        patch.add_data(0xF154, [0x22, 0x90, 0xFE, 0xC2, 0x60])
        patch.add_data(0x2FE90, [0xAF, 0x14, 0x30, 0x00, 0x0F, 0x11, 0x30, 0x00, 0x6B])
        # faster text
        # ?

        return patch
