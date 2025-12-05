from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import AnimationScriptBank
from smrpgpatchbuilder.datatypes.battles.battle_dialog_collection import BattleDialogCollection
from smrpgpatchbuilder.datatypes.dialogs.classes import DialogCollection
from smrpgpatchbuilder.datatypes.enemies.classes import EnemyCollection
from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttackCollection
from smrpgpatchbuilder.datatypes.items.classes import ItemCollection
from smrpgpatchbuilder.datatypes.monster_scripts.types import MonsterScriptBank, MonsterScript
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import ActionScriptBank
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScriptController, EventScriptBank
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import PacketCollection
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import PackCollection
from smrpgpatchbuilder.datatypes.levels.room_collection import RoomCollection
from smrpgpatchbuilder.datatypes.shops.classes import ShopCollection
from smrpgpatchbuilder.datatypes.spells.classes import SpellCollection
from smrpgpatchbuilder.datatypes.graphics.classes import SpriteCollection
from smrpgpatchbuilder.datatypes.scripts_common.classes import IdentifierException
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import FormationMember, Formation
from smrpgpatchbuilder.datatypes.allies.ally_collection import AllyCollection
from .item import Item
from .enemy import Enemy
from .patch import Patch
from .attack import EnemyAttack as Attack
from .spell import Spell



class WorldBuildingException(Exception):
    pass


class Settings:
    """Container class for all settings."""

    _debug_mode: bool = False
    _override: dict = {}
    _all_flags: List[Flag] = []

    @property
    def override(self) -> dict:
        """Override certain settings (developer mode)"""
        return self._override

    @property
    def flag_string(self) -> str:
        """Computed flag string for these settings."""

        non_cosmetic_categories = [
            category
            for category in CATEGORIES
            if not isinstance(category, CosmeticCategory)
        ]

        return get_flag_string_from_flag_collection(non_cosmetic_categories)

    def get_flag(self, flag_class: Type[FlagT]) -> FlagT:
        """Get the value of a specific setting."""
        return next(f for f in self._all_flags if isinstance(f, flag_class))

    def is_flag_value(self, flag_class: Type[Flag], value: Any) -> bool:
        """Check if a setting is set to the given value."""
        flag = self.get_flag(flag_class)
        if isinstance(flag, (BooleanFlag, NumberThresholdFlag, SelectOneFlag)):
            return flag.value == value
        if isinstance(flag, CategorizationFlag):
            return value in flag.enabled
        raise RandomizerSettingsException(
            f"is_flag_value unknown flag type {type(flag)}"
        )

    def is_boolean_flag_enabled(self, flag_class: Type[BooleanFlag]) -> bool:
        """Check if a boolean flag is on or not."""
        return self.is_flag_value(flag_class, True)

    def update_single_value_flag(self, flag_class: Type[Flag], value: Any) -> None:
        """For a setting which can only take one of multiple values, set it to the given value."""
        flag = self.get_flag(flag_class)
        if isinstance(flag, (BooleanFlag, NumberThresholdFlag, SelectOneFlag)):
            flag.set_value(value)
        elif isinstance(flag, CategorizationFlag):
            raise RandomizerSettingsException(
                (
                    "is_flag_value illegal flag type CategorizationFlag, "
                    "use append_categorization_flag_options, "
                    "remove_categorization_flag_options, "
                    "or overwrite_categorization_flag_options"
                )
            )
        else:
            raise RandomizerSettingsException(
                f"is_flag_value illegal flag type {type(flag)}"
            )

    def append_categorization_flag_options(
        self,
        flag_class: Type[CategorizationFlag],
        options_to_append: Union[FlagOptions, List[FlagOptions]],
    ) -> None:
        """For a value categorization flag, append values to Enabled."""
        flag = self.get_flag(flag_class)
        enabled = deepcopy(flag.enabled)
        if isinstance(options_to_append, FlagOptions):
            options_to_append = [options_to_append]
        enabled.extend(options_to_append)
        flag.set_enabled(enabled)

    def remove_categorization_flag_options(
        self,
        flag_class: Type[CategorizationFlag],
        options_to_remove: Union[FlagOptions, List[FlagOptions]],
    ) -> None:
        """For a value categorization flag, append values to Disabled."""
        flag = self.get_flag(flag_class)
        if isinstance(options_to_remove, FlagOptions):
            options_to_remove = [options_to_remove]
        enabled = [opt for opt in flag.enabled if opt not in options_to_remove]
        flag.set_enabled(enabled)

    def overwrite_categorization_flag_options(
        self, flag_class: Type[CategorizationFlag], options: List[FlagOptions]
    ) -> None:
        """For a value categorization flag, overwrite Enabled."""
        flag = self.get_flag(flag_class)
        flag.set_enabled(options)

    def reject_illegal_flag_combos(self) -> None:
        """A sanity check for settings that are misconfigured."""
        # max chars less than starting party size
        max_char_setting: int = self.get_flag(MaxCharacters).value
        if max_char_setting < self.get_flag(StartingCharacters).value:
            raise FlagError(
                "Your max characters setting is lower than your starting party size setting"
            )
        # not enough chars to fill desired party
        if (
            len(self.get_flag(AvailableCharacters).enabled)
            < self.get_flag(StartingCharacters).value
        ):
            raise FlagError(
                "You have excluded too many characters to fill your desired starting party size"
            )
        required_char_settings = [
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.MARIO),
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.MALLOW)
            or self.is_flag_value(BanditsWayGate, BanditsWayGating.MALLOW),
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.GENO)
            or self.is_flag_value(ForestMazeGate, ForestMazeGating.GENO),
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.BOWSER),
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.TOADSTOOL)
            or self.is_flag_value(SeaGate, SeaGating.TOADSTOOL),
        ]
        num_required = len([s for s in required_char_settings if s])
        if num_required > max_char_setting:
            raise FlagError(
                (
                    f"Your Progression settings require {num_required} different characters, "
                    f"but you have set your max to {max_char_setting}"
                )
            )

        # don't allow there to be less star pieces than gating allows
        if (
            (
                self.get_flag(TotalStarPieces).value < 4
                and self.is_flag_value(SeaGate, SeaGating.STAR_4)
            )
            or (
                self.get_flag(TotalStarPieces).value < 6
                and self.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6)
            )
            or (
                self.get_flag(TotalStarPieces).value < 6
                and self.is_flag_value(FactoryGate, FactoryGating.STAR_6)
            )
        ):
            raise FlagError(
                (
                    "Not enough Star Pieces available to unlock world areas "
                    "with your selected progression settings"
                )
            )
        # don't allow endgame stars to be less than available stats
        if (
            self.get_flag(TotalStarPieces).value
            < self.get_flag(StarPiecesRequired).value
        ):
            raise FlagError(
                (
                    "Star Pieces required to access the final Factory boss cannot be higher "
                    "than the total Star Pieces available in the world"
                )
            )
        # don't allow empty shops
        # needs at least 1 damaging spell to be enabled
        requires_one_of = [
            LearnableSpells.JUMP,
            LearnableSpells.FIRE_ORB,
            LearnableSpells.SUPER_JUMP,
            LearnableSpells.SUPER_FLAME,
            LearnableSpells.ULTRA_JUMP,
            LearnableSpells.ULTRA_FLAME,
            LearnableSpells.SLEEPY_TIME,
            LearnableSpells.PSYCH_BOMB,
            LearnableSpells.TERRORIZE,
            LearnableSpells.POISON_GAS,
            LearnableSpells.CRUSHER,
            LearnableSpells.BOWSER_CRUSH,
            LearnableSpells.GENO_BEAM,
            LearnableSpells.GENO_WHIRL,
            LearnableSpells.GENO_BLAST,
            LearnableSpells.GENO_FLASH,
            LearnableSpells.THUNDERBOLT,
            LearnableSpells.SHOCKER,
            LearnableSpells.SNOWY,
            LearnableSpells.STAR_RAIN,
        ]
        # what to do about actually applying these when seed has limited chars?
        has_required = False
        for spell in requires_one_of:
            if spell in self.get_flag(AvailableSpells).enabled:
                has_required = True
                break
        if not has_required:
            raise FlagError(
                "At least one spell must be included that can transform Mokura."
            )

        # Clean up flag selections
        # Set max # of chars from allowed chars
        allowed_chars = self.get_flag(AvailableCharacters).enabled
        max_chars = self.get_flag(MaxCharacters).value
        available_chars = []
        if required_char_settings[0]:
            available_chars.append(PlayableCharacters.MARIO)
        if required_char_settings[1]:
            available_chars.append(PlayableCharacters.MALLOW)
        if required_char_settings[2]:
            available_chars.append(PlayableCharacters.GENO)
        if required_char_settings[3]:
            available_chars.append(PlayableCharacters.BOWSER)
        if required_char_settings[4]:
            available_chars.append(PlayableCharacters.TOADSTOOL)
        starter = self.get_flag(StartingCharacter).value
        if starter != PlayableCharacters.RANDOM and starter not in available_chars:
            available_chars.append(available_chars)
        for character in available_chars:
            if character not in allowed_chars:
                raise FlagError(
                    "Your settings exclude a character that is required by another setting."
                )
        if max_chars < len(available_chars):
            raise FlagError(
                "your settings require more characters than are allowed in the seed"
            )
        if len(available_chars) < max_chars:
            available_chars.extend(
                random.sample(
                    [c for c in allowed_chars if c not in available_chars],
                    k=max_chars - len(available_chars),
                )
            )
        if max_chars != len(available_chars):
            raise FlagError(
                "too many characters are restricted to make your settings possible"
            )
        flag_val = self.get_flag(AvailableCharacters)
        flag_val.set_enabled(available_chars)

    def __init__(
        self,
        debug_mode: bool = False,
        flag_string: str = "",
        cosmetics_string: str = "",
    ):
        self._debug_mode = debug_mode

        if self._debug_mode:
            with open("randomizer/debug/config.yml", "r", encoding="utf-8") as stream:
                try:
                    self._override = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)

        flag_dict: Dict[str, dict[str, Any]] = separate_flag_string(
            flag_string, cosmetics_string
        )

        # Set flags from form data.
        for category in CATEGORIES:
            for subcategory in category().subcategories:
                for flag in subcategory.flags:
                    set_flag_from_settings_string(flag_dict, flag, subcategory)
                    self._all_flags.append(flag)

        self.reject_illegal_flag_combos()



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

    def get_item(self, item: int | type[Item]):
        if isinstance(item, int):
            i = next((i for i in self.items.items if i.item_id == item), None)
        else:
            i = next((i for i in self.items.items if isinstance(i, item)), None)
        assert i is not None, f"Item {item} does not exist in ItemCollection"
        return i
    
    def get_enemy(self, enemy_id: int | type[Enemy]):
        if isinstance(enemy_id, int):
            e = next((e for e in self.enemies.enemies if e.monster_id == enemy_id), None)
        else:
            e = next((e for e in self.enemies.enemies if isinstance(e, enemy_id)), None)
        assert e is not None, f"Enemy {enemy_id} does not exist in EnemyCollection"
        return e
    
    def get_attack(self, attack_id: int | type[Attack]):
        if isinstance(attack_id, int):
            a = next((a for a in self.enemy_attacks.attacks if a.index == attack_id), None)
        else:
            a = next((a for a in self.enemy_attacks.attacks if isinstance(a, attack_id)), None)
        assert a is not None, f"Attack {attack_id} does not exist in EnemyAttackCollection"
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
        assert d is not None, f"Battle Dialog {dialog_id} does not exist in BattleDialogCollection"
        return d
    
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
                    return self.battle_animations[0x3A].get_command_by_name(command_name)   
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

    def replace_battle_pack_formations(self, members: list[FormationMember | None], pack_id: int):
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

    def __init__(self, seed: int, settings: Settings, 
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
                 sprites: SpriteCollection):
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
        patch.add_data(0xC3B5, 0x20) # TODO might need to be larger than 0x20, recount key items
        patch.add_data(0xC302, [0xF0, 0xF8])
        patch.add_data(0xC37C, [0xF0, 0xF8])
        patch.add_data(0xC3B2, [0xF0, 0xF8])
        patch.add_data(0x2BC80, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BC95, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BCA1, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BCB6, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x353080, [0xF0, 0xF8, 0x7F])
        
        # Postgame weapon palettes
        patch.add_data(0x25894C, bytes.fromhex("7B 37 BD 33 39 33 F7 2E F7 2A F7 22 31 26 52 22 DE 53 10 1E 8C 15 4A 15 08 11 C6 0C 63 0C"))
        patch.add_data(0x25896A, bytes.fromhex("BD 6B BD 6B 5B 47 39 3B 95 1A D7 1E 74 1A EF 15 6C 0D 09 09 A6 04 A6 04 84 04 FF 7B 63 0C"))
        patch.add_data(0x25DEE4, bytes.fromhex("FF 7F F5 7F EA 7F E0 7F 40 7F 80 7E E0 7D 20 7D 00 69 C0 58 A0 44 60 30 40 20 00 0C 00 00"))

        # TODO: make these conditional based on a flag
        # hold B to advance
        patch.add_data(0x5D5E, [0x20, 0x54, 0xF1])
        patch.add_data(0x15627, [0x22, 0x90, 0xFE, 0xC2, 0x89, 0x80, 0x00])
        patch.add_data(0xF154, [0x22, 0x90, 0xFE, 0xC2, 0x60])
        patch.add_data(0x2FE90, [0xAF, 0x14, 0x30, 0x00, 0x0F, 0x11, 0x30, 0x00, 0x6B])
        # faster text
        # ?

        return patch
