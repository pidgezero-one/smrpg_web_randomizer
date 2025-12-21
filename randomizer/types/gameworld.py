from __future__ import annotations
from copy import deepcopy
from typing import Any, TYPE_CHECKING, TypeVar, cast
import random
import datetime

from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import (
    AnimationScriptBank,
)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands import *
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments import *
from smrpgpatchbuilder.datatypes.battles.battle_dialog_collection import (
    BattleDialogCollection,
)
from smrpgpatchbuilder.datatypes.dialogs.classes import DialogCollection
from smrpgpatchbuilder.datatypes.enemies.classes import EnemyCollection
from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttackCollection
from smrpgpatchbuilder.datatypes.items.classes import ItemCollection, Equipment
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *
from smrpgpatchbuilder.datatypes.monster_scripts.types import (
    MonsterScriptBank,
    MonsterScript,
)
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import (
    DoNothing,
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
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.area_object import (
    AreaObject,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    PackCollection,
)
from smrpgpatchbuilder.datatypes.levels.room_collection import RoomCollection
from smrpgpatchbuilder.datatypes.shops.classes import ShopCollection
from smrpgpatchbuilder.datatypes.spells.classes import SpellCollection
from smrpgpatchbuilder.datatypes.graphics.classes import SpriteCollection
from smrpgpatchbuilder.datatypes.scripts_common.classes import IdentifierException
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    CompareVarToConst,
    SummonObjectToSpecificLevel,
    RunEventAsSubroutine,
    SetBit,
    ClearBit,
    JmpIfBitClear,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    FormationMember,
    Formation,
)
from smrpgpatchbuilder.datatypes.allies.ally_collection import AllyCollection
from smrpgpatchbuilder.datatypes.levels.classes import RoomObject, Room
from smrpgpatchbuilder.datatypes.spells.enums import Status
from ..data.items.items import *
from .item import Item
from .patch import Patch
from .attack import EnemyAttack
from .spell import Spell
from .prize import Prize
from .ally import Ally
from .flags import (
    Flag,
    BooleanFlag,
    RangeFlag,
    SelectOneFlag,
    CategorizationFlag,
    CosmeticCategory,
    CATEGORIES,
)
from .prizelocation import SIGNAL_RING_EVENT_DICT, PrizeLocation
from ..progression.prizelocations import *
from ..data.variables.dialog_names import *
from ..data.variables.battle_variable_names import *
from ..data.variables.battle_effect_names import *
from ..data.spells.spells import *
from ..data.allies.palettes.types import MarioPalette, MallowPalette, GenoPalette, BowserPalette, ToadstoolPalette
from ..data.allies.palettes.mario import all_palettes as MARIO_PALETTES
from ..data.allies.palettes.mallow import all_palettes as MALLOW_PALETTES
from ..data.allies.palettes.geno import all_palettes as GENO_PALETTES
from ..data.allies.palettes.toadstool import all_palettes as TOADSTOOL_PALETTES
from ..data.allies.palettes.bowser import all_palettes as BOWSER_PALETTES
from .enemy import Enemy

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
    mario_palette: MarioPalette
    mallow_palette: MallowPalette
    geno_palette: GenoPalette
    bowser_palette: BowserPalette
    toadstool_palette: ToadstoolPalette
    main_character: Ally = MARIO_Ally

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

    def search_replace_dialog(self, search: str, replace: str):
        for bank_id, dialog_bank in enumerate(self.overworld_dialogs.raw_data):
            for index, dialog in enumerate(dialog_bank):
                self.overworld_dialogs.raw_data[bank_id][index] = dialog.replace(
                    search, replace
                )

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

        random.seed(self.seed)

        # todo: extra moleville trade checks

        # establish all functional prize locations
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

        if self.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
            fwshop = FireworksShopItemLocation()
            fwshop._originally_held = ProgressiveFireworksPrize
            fwshop.set_prize(ProgressiveFireworksPrize())
            self.locations = {
                **self.locations,
                FireworksShopItemLocation: fwshop,
                PurtendStoreLocation: PurtendStoreLocation(),
                CookieTraderLocation: CookieTraderLocation(),
            }
        if self.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
            fwshop = FireworksShopItemLocation()
            self.locations = {**self.locations, FireworksShopItemLocation: fwshop}

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

        if self.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
            self.locations = {
                **self.locations,
                GarroFreeItem: GarroFreeItem(),
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
            cast(
                CompareVarToConst,
                self.event_scripts.get_command_by_identifier(
                    "postgame_progress_checker_1"
                ),
            ).set_value(7)
            cast(
                CompareVarToConst,
                self.event_scripts.get_command_by_identifier(
                    "postgame_progress_checker_2"
                ),
            ).set_value(7)

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

        event_2496_startup: list[UsableEventScriptCommand] = []

        invisible_flag_locations: dict[type[PrizeLocation], PrizeLocation] = {}
        for i in range(0, 3):
            # choose the three invisible item locations
            if not self.settings.isflag_enabled(InvisibleFlagsSetting):
                location_cls = invisible_item_pool[i]
            else:
                location_cls = random.choice(invisible_item_pool)
            location = cast(InvisibleFlagLocation, location_cls(i))
            for r in location._rooms:
                # place them in rooms and set visibility triggers
                room = self.rooms._rooms[r]
                assert room is not None
                n = location.npc
                n_id = AreaObject(len(room.objects) + 0x14)
                n.set_visible(False)
                self.event_scripts.get_script_by_id(
                    E0091_INVISIBLE_ITEM_SUMMONER
                ).insert_before_nth_command(0, SummonObjectToSpecificLevel(n_id, r))
                room.add_object(location.npc)
            # set hint text
            if i == 0:
                self.update_dialog(
                    DI1108_RESERVED_FOR_DRYBONESFLAG_HINT,
                    "DRY BONES:\n" + location.clue_text,
                )
            elif i == 1:
                self.update_dialog(
                    DI1109_RESERVED_FOR_GREAPERFLAG_HINT,
                    "GREAPER:\n" + location.clue_text,
                )
            elif i == 2:
                self.update_dialog(
                    DI1107_RESERVED_FOR_BIGBOOFLAG_HINT,
                    "THE BIG BOO:\n" + location.clue_text,
                )
        self.locations = {**self.locations, **invisible_flag_locations}

        # TODO: Before setting hints, find where the mimic chests are and reassign the world areas for their prize locations

        # prize locations HAVE to all be defined by this point
        # not shuffled, just determined if they exist in the seed or not

        if self.settings.isflag_enabled(StarPieceHints):
            for l in self.locations.values():
                if not isinstance(l.prize, StarPiecePrize):
                    continue
                event = SIGNAL_RING_EVENT_DICT[l.world_area]
                script = self.event_scripts.get_script_by_id(event)
                script.insert_before_nth_command(
                    0, JmpIfBitClear(l.prize._hint, [f"EVENT_{event}_play_sound"])
                )

        if self.settings.isflag_enabled(SkipMustyFearsSequence):
            event_2496_startup += [RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER)]

        ### Perform progression gating setup tasks here

        # settings
        if self.settings.is_flag_value(WinCondition, WinConditions.SMITHY):
            event_2496_startup += [SetBit(SMITHY_BOSS_HUNT_WIN_CONDITION)]
        elif self.settings.is_flag_value(WinCondition, WinConditions.STARS):
            event_2496_startup += [SetBit(WIN_CONDITION_STAR_PIECES)]
        elif self.settings.is_flag_value(WinCondition, WinConditions.SEALED):
            event_2496_startup += [SetBit(WIN_CONDITION_MONSTRO_DOOR)]

        if self.settings.isflag_enabled(FastTravel):
            event_2496_startup += [SetBit(FAST_TRAVEL_ENABLED)]
        if self.settings.isflag_enabled(CasinoWarp):
            event_2496_startup += [SetBit(CASINO_WARP_ENABLED)]
        if self.settings.isflag_enabled(BucketWarp):
            event_2496_startup += [SetBit(BUCKET_WARP_ENABLED)]
        if self.settings.isflag_enabled(ShuffleWeddingGear):
            event_2496_startup += [SetBit(CHAPEL_ITEMS_ANYWHERE_ENABLED)]

        if self.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.STARS):
            event_2496_startup += [SetBit(PROGRESSIVE_STAR_EXP_ENABLED)]
        elif self.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.BOSSES):
            event_2496_startup += [SetBit(PROGRESSIVE_BOSS_EXP_ENABLED)]
        elif self.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.NONE):
            self.event_scripts.delete_command_by_identifier("inc_exp_by_packet")

        if self.settings.isflag_enabled(SkipBossFights):
            event_2496_startup += [SetBit(ALTERNATE_STAR_PIECE_WIN_CONDITION)]

        # TODO when assembling grant scripts, set all exp star 70A7 props to 0 if NONE is selected
        # TODO verify that all bosses increase the counter, ie remake bosses

        # gates
        if self.settings.is_flag_value(BanditsWayGate, BanditsWayGating.OPEN):
            event_2496_startup += [
                SetBit(MAP_BANDITS_WAY),
                SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
            ]
        if not self.settings.is_flag_value(KeroSewersGate, KeroSewersGating.OPEN):
            cast(
                RoomObject,
                cast(
                    Room, self.rooms._rooms[R333_KERO_SEWERS_ENTRANCE]
                ).get_npc_by_target_id(NPC_0),
            ).set_visible(True)
            cast(
                RoomObject,
                cast(
                    Room, self.rooms._rooms[R333_KERO_SEWERS_ENTRANCE]
                ).get_npc_by_target_id(NPC_1),
            ).set_visible(True)
            event_2496_startup += [SetBit(SEWERS_CLOSED)]

            if self.settings.is_flag_value(KeroSewersGate, KeroSewersGating.RFC):
                self.event_scripts.get_script_by_id(
                    E1254_UNLOCK_SEWER_BY_RFC
                ).insert_before_nth_command(0, ClearBit(SEWERS_CLOSED))
        else:
            event_2496_startup += [ClearBit(SEWERS_CLOSED)]
        if self.settings.is_flag_value(ForestMazeGate, ForestMazeGating.OPEN):
            event_2496_startup += [
                SetBit(MAP_FOREST_MAZE),
                SetBit(MAP_DIRECTIONAL_ROSE_TOWN_FOREST_MAZE),
            ]
        elif self.settings.is_flag_value(ForestMazeGate, ForestMazeGating.PIE):
            e = self.event_scripts.get_script_by_id(E1255_UNLOCK_FOREST_BY_PIE)
            e.insert_before_nth_command(0, SetBit(MAP_FOREST_MAZE))
            e.insert_before_nth_command(0, SetBit(MAP_FOREST_MAZE))
        if not self.settings.is_flag_value(PipeVaultGate, PipeVaultGating.OPEN):
            event_2496_startup += [
                SetBit(PIPE_VAULT_GATED),
            ]
        if not self.settings.is_flag_value(Moleville1Gate, Moleville1Gating.OPEN):
            event_2496_startup += [
                SetBit(MOLEVILLE_MINES_ENTRANCE_GATING),
            ]
            if self.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOSHI):
                self.event_scripts.get_script_by_id(
                    E1256_UNLOCK_MOLEVILLE_IF_GATED_BY_BOSHI
                ).insert_before_nth_command(
                    0, ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING)
                )
        if not self.settings.is_flag_value(BoosterHillGate, BoosterHillGating.OPEN):
            event_2496_startup += [
                SetBit(BOOSTER_HILL_CLOSED),
            ]
        if self.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.OPEN):
            event_2496_startup += [
                ApplySolidityModToLevel(
                    permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
                ),
                ApplyTileModToLevel(
                    use_alternate=True,
                    room_id=R202_BOOSTER_TOWER_ENTRANCE,
                    mod_id=32,
                ),
                SetBit(TOWER_OPENED),
            ]
        if self.settings.is_flag_value(MarrymoreGate, MarrymoreGating.OPEN):
            event_2496_startup += [
                SetBit(MARRYMORE_BACKDOOR_OPEN),
            ]
        elif self.settings.is_flag_value(MarrymoreGate, MarrymoreGating.HILL):
            self.event_scripts.get_script_by_id(
                E1329_HILL_UNLOCKS
            ).insert_before_nth_command(0, SetBit(MARRYMORE_BACKDOOR_OPEN))
        if self.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
            event_2496_startup += [SetBit(SEA_GATED_BY_STAR_PIECES)]
        elif self.settings.is_flag_value(SeaGate, SeaGating.OPEN):
            event_2496_startup += [
                SetBit(MAP_SEA),
                SetBit(MAP_DIRECTIONAL_SEA_SUNKEN_SHIP),
                SetBit(MAP_SUNKEN_SHIP),
                SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
            ]
        if self.settings.is_flag_value(YaridovichGate, YaridovichGating.OPEN):
            event_2496_startup += [SetBit(SEASIDE_BOSS_AVAILABLE)]
        if not self.settings.is_flag_value(LandsEndGate, LandsEndGating.OPEN):
            event_2496_startup += [SetBit(LANDS_END_GATED)]

            if self.settings.is_flag_value(LandsEndGate, LandsEndGating.ELDER):
                self.event_scripts.get_script_by_id(
                    E1169_OPEN_LANDS_END_IF_GATED_BY_ELDER
                ).insert_before_nth_command(0, ClearBit(LANDS_END_GATED))
            if self.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
                event_2496_startup += [SetBit(LANDS_END_GATED_BY_STAR_PIECES)]

        if self.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.KEY):
            event_2496_startup += [SetBit(TEMPLE_BOSS_GATED)]
        if self.settings.is_flag_value(MonstroTownGate, MonstroTownGating.BELOME_2):
            event_2496_startup += [
                SummonObjectToSpecificLevel(
                    NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
                )
            ]
        elif self.settings.is_flag_value(MonstroTownGate, MonstroTownGating.OPEN):
            event_2496_startup += [
                RemoveObjectFromSpecificLevel(
                    NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
                ),
                SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
                SetBit(MAP_MONSTRO_TOWN),
            ]
        if self.settings.is_flag_value(
            NimbusGate, NimbusGating.OPEN
        ) or self.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
            event_2496_startup += [
                SetBit(NIMBUS_MAINLAND_UNLOCKED),
                RemoveObjectFromSpecificLevel(
                    NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
                ),
            ]
        if self.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.OPEN):
            event_2496_startup += [
                SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
                SetBit(MAP_BARREL_VOLCANO),
            ]

        if not self.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.OPEN):
            event_2496_startup += [SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL)]
            if self.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
                event_2496_startup += [SetBit(KEEP_GATED_BY_STAR_PIECES)]
                if self.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
                    event_2496_startup += [
                        SetBit(FACTORY_MATCHES_KEEP),
                    ]
        else:
            event_2496_startup += [
                SetBit(MAP_VISTA_HILL),
                ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
            ]
            if self.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
                event_2496_startup += [
                    SetBit(MAP_GATE),
                    SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                ]
        if self.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
            event_2496_startup += [SetBit(FACTORY_GATED_BY_STAR_PIECES)]

        event_2496_startup += [Return()]
        self.event_scripts.get_script_by_id(
            E1252_FLAG_SPECIFIC_HOUSEKEEPING_GAME_START
        ).set_contents(event_2496_startup)

        # threshold adjustments
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_1"),
        ).set_value(self.settings.get_flag(SuitePrize1Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_2"),
        ).set_value(self.settings.get_flag(SuitePrize2Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_3"),
        ).set_value(self.settings.get_flag(SuitePrize3Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_4"),
        ).set_value(self.settings.get_flag(SuitePrize4Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_5"),
        ).set_value(self.settings.get_flag(SuitePrize5Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_6"),
        ).set_value(self.settings.get_flag(SuitePrize6Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("sj_threshold_1"),
        ).set_value(self.settings.get_flag(SuperJump1Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("sj_threshold_2"),
        ).set_value(self.settings.get_flag(SuperJump2Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier(
                "tower_knife_guy_sidequest_completed"
            ),
        ).set_value(self.settings.get_flag(KnifeGuyPrizeThreshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier(
                "casino_grate_guy_sidequest_completed"
            ),
        ).set_value(self.settings.get_flag(GrateGuyPrizeThreshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("check_doors_complete"),
        ).set_value(self.settings.get_flag(BowserDoorRequirements).value)

        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("enable_boss_access_1"),
        ).set_value(self.settings.get_flag(StarPiecesRequired).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("enable_boss_access_2"),
        ).set_value(self.settings.get_flag(StarPiecesRequired).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("enable_boss_access_3"),
        ).set_value(self.settings.get_flag(StarPiecesRequired).value)

        # other stuff

        if self.settings.isflag_enabled(PoisonMushroom):
            self.items.get_by_type(MushroomItem2).set_status_immunities(
                random.sample(
                    [
                        Status.MUTE,
                        Status.SLEEP,
                        Status.POISON,
                        Status.FEAR,
                        Status.BERSERK,
                        Status.MUSHROOM,
                        Status.SCARECROW,
                        Status.INVINCIBLE,
                    ],
                    1,
                )
            )
        if self.settings.isflag_enabled(UncapSuperJumps):
            self.battle_animations[0x35].delete_command_by_name("super_jump_cap_1")
            self.battle_animations[0x35].delete_command_by_name("super_jump_cap_2")

        if self.settings.isflag_enabled(NoGenoWhirlExor):
            self.monster_scripts.replace_command_by_identifier(
                "exor_vulnerability_1", [SetUntargetable(MONSTER_1_SET)]
            )
            self.monster_scripts.replace_command_by_identifier(
                "exor_vulnerability_2", [SetUntargetable(MONSTER_1_SET)]
            )
            self.monster_scripts.replace_command_by_identifier(
                "exor_vulnerability_2", [SetUntargetable(MONSTER_1_SET)]
            )
        if self.settings.isflag_enabled(FixMagikoopa):
            self.monster_scripts.scripts[
                KINGBOMBEnemy._monster_id
            ].insert_after_nth_command(0, ClearVar(BV7EE000))
        sidekicks = [
            BODYGUARDEnemy,
            GOOMBETTEEnemy,
            FAUTSOEnemy,
            BAHAMUTTEnemy,
            BAHAMUTTEnemy2,
            KINGBOMBEnemy,
            JINXCLONEEnemy,
            MARIOCLONEEnemy,
            MARIOCLONESEnemy,
            MALLOWCLONEEnemy,
            MALLOWCOPYSEnemy,
            GENOCLONEEnemy,
            GENOCLONESEnemy,
            BOWSERCLONEEnemy,
            BOWSERCOPYSEnemy,
            TOADSTOOL2Enemy,
            TOADSTOOL3Enemy,
            TENTACLESEnemy,
            TENTACLESEnemy2,
            BOBOMBEnemyHenchman,
            MICROBOMBEnemy,
            MEZZOBOMBEnemy,
            STRONGBOBOMB1Enemy,
            STRONGBOBOMB2Enemy,
            STRONGBOBOMB3Enemy,
            STRONGBOBOMB4Enemy,
            SNIFITEnemyHenchman,
            SNIFIT2Enemy,
            BANDANABLUEEnemy,
            TORTE2Enemy,
            TORTEEnemy,
            SMILAXEnemy,
            EGGBERTEnemy,
            DINGALINGEnemy,
            FIRECRYS3DEnemy,
            FIRECRYSTALEnemy,
            WINDCRYS3DEnemy,
            WINDCRYS3DEnemy,
            WATERCRYS3DEnemy,
            WATERCRYSTALEnemy,
            EARTHCRYS3DEnemy,
            EARTHCRYSTALEnemy,
            MADMALLETEnemyHenchman,
            POUNDEREnemyHenchman,
            POUNDETTEEnemyHenchman,
            HELIOEnemy,
            SHYPEREnemy,
        ]
        bosses = [
            HAMMERBROEnemy,
            CROCO1Enemy,
            MACKEnemy,
            BELOME1Enemy,
            BOWYEREnemy,
            CROCO2Enemy,
            PUNCHINELLOEnemy,
            PUNCHINELLO2Enemy,
            BOOSTEREnemy,
            BOOSTEREnemy2,
            KNIFEGUYEnemy,
            GRATEGUYEnemy,
            BUNDTEnemy,
            BUNDT2Enemy,
            PANDORITEEnemy,
            HIDONEnemy,
            BOXBOYEnemy,
            CHESTEREnemy,
            KINGCALAMARIEnemy,
            JOHNNYEnemy,
            JOHNNYEnemy2,
            YARIDOVICHEnemy,
            YARIDOVICHMirageEnemy,
            BELOME2Enemy,
            BELOMEEnemy3,
            MOKURAEnemy,
            FORMLESSEnemy,
            JAGGEREnemy,
            JINX1Enemy,
            JINX2Enemy,
            JINX3Enemy,
            JINXEnemy4,
            CULEXEnemy,
            CULEX3DEnemy,
            MEGASMILAXEnemy,
            DODOEnemySolo,
            BIRDETTAEnemy,
            DODOEnemy,
            VALENTINAEnemy,
            CZARDRAGONEnemy,
            ZOMBONEEnemy,
            AXEMREDEnemy,
            AXEMPINKEnemy,
            AXEMBLACKEnemy,
            AXEMYELLOWEnemy,
            AXEMGREENEnemy,
            AXEMRANGERSEnemy,
            KAMEKEnemy,
            BOOMEREnemy,
            EXOREnemy,
            RIGHTEYEEnemy,
            LEFTEYEEnemy,
            NEOSQUIDEnemy,
            COUNTDOWNEnemy,
            CLOAKEREnemy,
            CLOAKEREnemy2,
            MADADDEREnemy,
            EARTHLINKEnemy,
            CLERKEnemy,
            MANAGEREnemy,
            DIRECTOREnemy,
            GUNYOLKEnemy,
            FACTORYCHIEFEnemy,
            SMITHY1Enemy,
            SMITHY2Enemy,
            SMITHYBodyEnemy,
            SMITHYChestEnemy,
            SMITHYMageEnemy,
            SMITHYSafeEnemy2,
            SMITHYTankEnemy,
            SMELTEREnemy,
        ]
        if self.settings.isflag_enabled(NoOHKO):
            for ennemytype in sidekicks:
                enemy = self.enemies.get_by_type(ennemytype)
                enemy.set_ohko_immune(True)
                enemy.set_morph_chance(0)
                for cmd in self.monster_scripts.scripts[enemy.monster_id].contents:
                    if isinstance(cmd, IfTargetedByItem):
                        cmd.set_commands([CarboCookieItem])
        if self.settings.isflag_enabled(ExperienceNoBosses):
            for ennemytype in bosses + sidekicks:
                enemy = self.enemies.get_by_type(ennemytype)
                enemy.set_xp(0)
        if self.settings.isflag_enabled(ExperienceNoRegular):
            for ennemytype in [
                type(e)
                for e in self.enemies.enemies
                if type(e) not in bosses + sidekicks
            ]:
                self.enemies.get_by_type(ennemytype).set_xp(0)
        if self.settings.isflag_enabled(EnemySpells):
            spell_pool: list[type[EnemySpell]] = [
                DrainSpell,
                LightningOrbSpell,
                FlameSpell,
                BoltSpell,
                CrystalSpell,
                FlameStoneSpell,
                MegaDrainSpell,
                WillyWispSpell,
                DiamondSawSpell,
                ElectroshockSpell,
                BlastSpell,
                StormSpell,
                IceRockSpell,
                EscapeSpell,
                DarkStarSpell,
                RecoverSpell,
                MegaRecoverSpell,
                FlameWallSpell,
                StaticESpell,
                SandStormSpell,
                BlizzardSpell,
                DrainBeamSpell,
                MeteorBlastSpell,
                LightBeamSpell,
                WaterBlastSpell,
                SolidifySpell,
                PetalBlastSpell,
                AuroraFlashSpell,
                BoulderSpell,
                CoronaSpell,
                MeteorSwarmSpell,
                WeirdMushroomSpell,
                BreakerBeamSpell,
                ShredderSpell,
                SledgeSpell,
                SwordRainSpell,
                SpearRainSpell,
                ArrowRainSpell,
                BigBangSpell,
            ]
            for script in self.monster_scripts.scripts:
                for cmd in script.contents:
                    if isinstance(cmd, CastSpell):
                        if cmd.spell_1 is not None and not isinstance(
                            cmd.spell_1, DoNothing
                        ):
                            cmd.set_spell_1(random.choice(spell_pool))
                        if cmd.spell_2 is not None and not isinstance(
                            cmd.spell_2, DoNothing
                        ):
                            cmd.set_spell_2(random.choice(spell_pool))
                        if cmd.spell_3 is not None and not isinstance(
                            cmd.spell_3, DoNothing
                        ):
                            cmd.set_spell_3(random.choice(spell_pool))

        # equips and things

        if self.settings.isflag_enabled(InfuseSpellElements):
            self.get_spell(GenoBeamSpell).set_element(Element.ICE)
            self.get_spell(GenoFlashSpell).set_element(Element.FIRE)
            self.get_spell(PsychBombSpell).set_element(Element.FIRE)
            self.get_spell(CrusherSpell).set_element(Element.JUMP)
            self.get_spell(BowserCrushSpell).set_element(Element.JUMP)
        if self.settings.isflag_enabled(CharacterSpellElements):
            spells_to_update = [
                s for s in self.spells.spells if s.element != Element.NONE
            ]
            for spell in spells_to_update:
                spell.set_element(
                    random.choice(
                        [Element.ICE, Element.FIRE, Element.JUMP, Element.THUNDER]
                    )
                )

        if self.settings.is_flag_value(
            EquipmentProperties, EquipmentPropertiesOptions.SOME
        ):
            self.items.get_by_type(ShirtItem).append_status_immunity(Status.MUSHROOM)
            self.items.get_by_type(PantsItem).append_status_immunity(Status.MUSHROOM)
            self.items.get_by_type(ThickShirtItem).append_temp_buff(
                TempStatBuff.DEFENSE
            )
            self.items.get_by_type(ThickPantsItem).append_temp_buff(
                TempStatBuff.DEFENSE
            )
            self.items.get_by_type(MegaShirtItem).append_temp_buff(
                TempStatBuff.MAGIC_DEFENSE
            )
            self.items.get_by_type(MegaPantsItem).append_temp_buff(
                TempStatBuff.MAGIC_DEFENSE
            )
            self.items.get_by_type(MegaCapeItem).append_temp_buff(
                TempStatBuff.MAGIC_DEFENSE
            )
            self.items.get_by_type(HappyShirtItem).set_prevent_ko(True)
            self.items.get_by_type(HappyPantsItem).set_prevent_ko(True)
            self.items.get_by_type(HappyCapeItem).set_prevent_ko(True)
            self.items.get_by_type(HappyShellItem).set_prevent_ko(True)
            self.items.get_by_type(PolkaDressItem).set_prevent_ko(True)
            self.items.get_by_type(CourageShellItem).append_status_immunity(Status.FEAR)
            self.items.get_by_type(SailorShirtItem).append_elemental_immunity(
                Element.ICE
            )
            self.items.get_by_type(SailorPantsItem).append_elemental_immunity(
                Element.ICE
            )
            self.items.get_by_type(SailorCapeItem).append_elemental_immunity(
                Element.ICE
            )
            self.items.get_by_type(NauticaDressItem).append_elemental_immunity(
                Element.ICE
            )
            self.items.get_by_type(FuzzyShirtItem).append_elemental_immunity(
                Element.THUNDER
            )
            self.items.get_by_type(FuzzyPantsItem).append_elemental_immunity(
                Element.THUNDER
            )
            self.items.get_by_type(FuzzyCapeItem).append_elemental_immunity(
                Element.THUNDER
            )
            self.items.get_by_type(FuzzyDressItem).append_elemental_immunity(
                Element.THUNDER
            )
            self.items.get_by_type(FireShirtItem).append_elemental_immunity(
                Element.FIRE
            )
            self.items.get_by_type(FirePantsItem).append_elemental_immunity(
                Element.FIRE
            )
            self.items.get_by_type(FireCapeItem).append_elemental_immunity(Element.FIRE)
            self.items.get_by_type(FireShellItem).append_elemental_immunity(
                Element.FIRE
            )
            self.items.get_by_type(FireDressItem).append_elemental_immunity(
                Element.FIRE
            )
            self.items.get_by_type(HeroShirtItem).append_status_immunity(
                Status.SCARECROW
            )
            self.items.get_by_type(PrincePantsItem).append_status_immunity(Status.MUTE)
            self.items.get_by_type(RoyalDressItem).append_status_immunity(Status.SLEEP)
            self.items.get_by_type(HealShellItem).append_status_immunity(Status.POISON)
            self.items.get_by_type(StarCapeItem).append_status_immunity(Status.BERSERK)
            self.items.get_by_type(FroggieStickItem).set_magic_attack(
                self.items.get_by_type(FroggieStickItem).attack
            )
            self.items.get_by_type(FroggieStickItem).set_attack(0)
            self.items.get_by_type(RibbitStickItem).set_magic_attack(
                self.items.get_by_type(RibbitStickItem).attack
            )
            self.items.get_by_type(RibbitStickItem).set_attack(0)
            self.items.get_by_type(ParasolItem).set_magic_attack(
                self.items.get_by_type(ParasolItem).attack
            )
            self.items.get_by_type(ParasolItem).set_attack(0)
        elif self.settings.is_flag_value(
            EquipmentProperties, EquipmentPropertiesOptions.RANDOM
        ):
            pass
        if not self.settings.isflag_enabled(IgnoreNamesakeProperties):
            self.items.get_by_type(WakeUpPinItem).append_status_immunity(Status.SLEEP)
            self.items.get_by_type(WakeUpPinItem).append_status_immunity(Status.MUTE)
            self.items.get_by_type(AntidotePinItem).append_status_immunity(
                Status.POISON
            )
            self.items.get_by_type(TrueformPinItem).append_status_immunity(
                Status.MUSHROOM
            )
            self.items.get_by_type(TrueformPinItem).append_status_immunity(
                Status.SCARECROW
            )
            self.items.get_by_type(FearlessPinItem).append_status_immunity(Status.FEAR)
            has_ko_protection = [
                i for i in self.items.items if isinstance(i, Equipment) and i.prevent_ko
            ]
            if len(has_ko_protection) < 4:
                more_ko_protections = random.sample(
                    [
                        i
                        for i in self.items.items
                        if isinstance(i, Equipment) and not i.prevent_ko
                    ],
                    4 - len(has_ko_protection),
                )
                for i in more_ko_protections:
                    i.set_prevent_ko(True)

        # Cosmetics have to go at the end and be re-seeded
        random.seed(datetime.datetime.now().timestamp())

        if self.settings.isflag_enabled(CanonNames):
            self.enemies.get_by_type(KAMEKEnemy).set_name("KAMEK")
            self.enemies.get_by_type(BIRDETTAEnemy).set_name("BIRDETTA")
        else:
            self.search_replace_dialog("KAMEK", "MAGIKOOPA")
            self.search_replace_dialog("Kamek", "Magikoopa")
            self.search_replace_dialog("BIRDETTA", "BIRDO")
            self.search_replace_dialog("Birdetta", "Birdo")
        if self.settings.isflag_enabled(Peach):
            self.allies._allies[1].name = "Peach"
        if self.settings.isflag_enabled(RemakeNames):
            for enemy in self.enemies.enemies:
                e = cast(Enemy, enemy)
                if e.remake_name is not None:
                    enemy.set_name(e.remake_name)
            for item in self.items.items:
                it = cast(Item, item)
                if it.remake_name is not None:
                    item.set_name(it.remake_name)
            for spell in self.spells.spells:
                sp = cast(Spell, spell)
                if sp.remake_name is not None:
                    spell._title = sp.remake_name
            for attack in self.enemy_attacks.attacks:
                at = cast(EnemyAttack, attack)
                if at.remake_name is not None:
                    attack.set_attack_name(at.remake_name)
        if self.settings.isflag_enabled(RemoveFlashes):
            screenflashes = [
                "screen_flash_1",  # thunderbolt
                "screen_flash_2",
                "crusher_screenflash",  # crusher
                "darkstar_flash",  # dark star
                "spikedlink_flash_1",
                "spikedlink_flash_2",
                "spikedlink_flash_3"
            ]
            for identifier in screenflashes:
                self.battle_animations[0x35].get_command_by_name(identifier).set_colour( # type: ignore
                    NO_COLOUR
                ) 
            deletes = [
                "command_0x35BE52",  # geno flash
                "geno_blast_effect",  # geno blast
                "corona_flash",
                "shaker_delete_1", # shaker / silver bullet
                "shaker_delete_2",
                "shaker_delete_3",
                "shaker_delete_4",
                "shaker_delete_5",
                "statice_delete_1",
                "statice_delete_2",
                "statice_delete_3",
                "statice_delete_4",
                "statice_delete_5",
                "meteorswarm_delete_maybe"
                "rockcandy_delete",
                "rockcandy_delete_2"
            ]
            for identifier in deletes:
                self.battle_animations[0x35].delete_command_by_name(identifier)
            deletes_3A = [
                "smithy_delete_1",
                "smithy_delete_2"
            ]
            for identifier in deletes_3A:
                self.battle_animations[0x3A].delete_command_by_name(identifier)
            self.battle_animations[0x35].get_command_by_name(
                "bigbang_flash"
            ).set_effect(  # type: ignore
                EF0025_PSYCH_BOMB_BG
            )
            self.battle_animations[0x35].get_command_by_name(
                "firebomb_explosion"
            ).set_effect(  # type: ignore
                EF0025_PSYCH_BOMB_BG
            )
            self.battle_animations[0x35].replace_command_by_name(
                "icebomb_explosion", ScreenFlashWithDuration(NO_COLOUR, 1)
            )
            self.battle_animations[0x35].replace_command_by_name(
                "command_0x35358A", AttackTimerBegins(identifier="command_0x35358A") # shaker / silver bullet
            )
            self.battle_animations[0x35].replace_command_by_name(
                "statice_flash", ScreenFlashWithDuration(NO_COLOUR, 44) # static e!
            )
            self.battle_animations[0x35].replace_command_by_name(
                "meteorswarm_replace", ScreenFlashWithDuration(NO_COLOUR, 16) # meteor swarm
            )
            self.battle_animations[0x35].replace_command_by_name(
                "rockcandy_replace", ScreenFlashWithDuration(NO_COLOUR, 20) # rock candy
            )
            self.battle_animations[0x35].replace_command_by_name(
                "meteorblast_replace", ScreenFlashWithDuration(NO_COLOUR, 20) # meteor blast
            )
            
            self.battle_animations[0x3A].replace_command_by_name(
                "smithy_replace_1", ScreenFlashWithDuration(NO_COLOUR, 1)
            )
            self.battle_animations[0x3A].replace_command_by_name(
                "smithy_replace_2", ScreenFlashWithDuration(NO_COLOUR, 1)
            )
        if self.settings.isflag_enabled(PaletteSwaps):
            self.mario_palette = random.choice(MARIO_PALETTES)
            self.mallow_palette = random.choice(MALLOW_PALETTES)
            self.geno_palette = random.choice(GENO_PALETTES)
            self.bowser_palette = random.choice(BOWSER_PALETTES)
            self.toadstool_palette = random.choice(TOADSTOOL_PALETTES)

            if self.settings.isflag_enabled(ChangeNames):
                self.allies._allies[0].name = self.mario_palette.name
                self.enemies.get_by_type(MARIOCLONEEnemy).set_name(self.mario_palette.clone_name)
                self.enemies.get_by_type(MARIOCLONESEnemy).set_name(self.mario_palette.strong_clone_name)
                self.allies._allies[1].name = self.toadstool_palette.name
                self.enemies.get_by_type(TOADSTOOL2Enemy).set_name(self.toadstool_palette.clone_name)
                self.enemies.get_by_type(TOADSTOOL3Enemy).set_name(self.toadstool_palette.strong_clone_name)
                self.allies._allies[2].name = self.bowser_palette.name
                self.enemies.get_by_type(BOWSERCLONEEnemy).set_name(self.bowser_palette.clone_name)
                self.enemies.get_by_type(BOWSERCOPYSEnemy).set_name(self.bowser_palette.strong_clone_name)
                self.allies._allies[3].name = self.geno_palette.name
                self.enemies.get_by_type(GENOCLONEEnemy).set_name(self.geno_palette.clone_name)
                self.enemies.get_by_type(GENOCLONESEnemy).set_name(self.geno_palette.strong_clone_name)
                self.allies._allies[4].name = self.mallow_palette.name
                self.enemies.get_by_type(MALLOWCLONEEnemy).set_name(self.mallow_palette.clone_name)
                self.enemies.get_by_type(MALLOWCOPYSEnemy).set_name(self.mallow_palette.strong_clone_name)


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

        if self.settings.isflag_enabled(HoldB):
            # hold B to advance
            patch.add_data(0x5D5E, [0x20, 0x54, 0xF1])
            patch.add_data(0x15627, [0x22, 0x90, 0xFE, 0xC2, 0x89, 0x80, 0x00])
            patch.add_data(0xF154, [0x22, 0x90, 0xFE, 0xC2, 0x60])
            patch.add_data(
                0x2FE90, [0xAF, 0x14, 0x30, 0x00, 0x0F, 0x11, 0x30, 0x00, 0x6B]
            )

        # Palettes

        if self.main_character == MARIO_Ally:
            for i, p in self.mario_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.mario_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.mario_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.mario_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        if self.main_character == MALLOW_Ally:
            for i, p in self.mallow_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.mallow_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.mallow_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.mallow_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        if self.main_character == GENO_Ally:
            for i, p in self.geno_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.geno_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.geno_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.geno_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        if self.main_character == BOWSER_Ally:
            for i, p in self.bowser_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.bowser_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.bowser_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.bowser_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        if self.main_character == TOADSTOOL_Ally:
            for i, p in self.toadstool_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.toadstool_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.toadstool_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.toadstool_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        patch.add_dict(self.mario_palette.standard_patch())
        patch.add_dict(self.mallow_palette.standard_patch())
        patch.add_dict(self.geno_palette.standard_patch())
        patch.add_dict(self.bowser_palette.standard_patch())
        patch.add_dict(self.toadstool_palette.standard_patch())

        if self.settings.isflag_enabled(JapaneseABXY):
            patch.add_data(
                0x255258,
                bytearray(
                    [
                        0x0C,
                        0x00,
                        0x36,
                        0x16,
                        0x3A,
                        0x27,
                        0x48,
                        0x26,
                        0xE3,
                        0x11,
                        0x07,
                        0x49,
                        0x63,
                        0x44,
                        0x00,
                        0x20,
                        0x3F,
                        0x29,
                        0xDB,
                        0x1C,
                        0xA6,
                        0x04,
                        0xC1,
                        0x08,
                    ]
                ),
            )
            patch.add_data(
                0x255C6C,
                bytearray(
                    [
                        0x0C,
                        0x00,
                        0x52,
                        0x4A,
                        0x29,
                        0x25,
                        0x48,
                        0x26,
                        0xE3,
                        0x11,
                        0x07,
                        0x49,
                        0x63,
                        0x44,
                        0x00,
                        0x20,
                        0x3F,
                        0x29,
                        0xDB,
                        0x1C,
                        0xD1,
                        0x00,
                        0xC1,
                        0x08,
                    ]
                ),
            )

        return patch
