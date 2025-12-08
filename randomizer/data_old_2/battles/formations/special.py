"""Special case formations"""

from randomizer.entities.enemies import (
    AxemRangers,
    BandanaBlue,
    Belome2,
    Cloaker,
    Culex,
    Dodo,
    Domino,
    EarthCrystal,
    Earthlink,
    Exor,
    FireCrystal,
    Johnny,
    KingCalamari,
    LeftEye,
    MadAdder,
    MarioClone,
    Megasmilax,
    PeachClone,
    RightEye,
    WaterCrystal,
    WindCrystal)

# TODO import from lib
from randomizer.types.battles.formations_packs.types import Formation


class ExorBossFormation(Formation):
    """A formation subclass specifically for Exor, who needs special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # HP = exor plus average of two eyes
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        exor = self.get_members_by_enemy_classes(Exor)[0].enemy()
        righteye = self.get_members_by_enemy_classes(RightEye)[0].enemy()
        lefteye = self.get_members_by_enemy_classes(LeftEye)[0].enemy()
        hp = round(exor.hp + (righteye.hp + lefteye.hp) / 2)
        xp = exor.xp
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)


class KingCalamariBossFormation(Formation):
    """A formation subclass specifically for King Calamari, who needs special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from kc
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        king_calamari = self.get_members_by_enemy_classes(KingCalamari)[0].enemy()
        xp = king_calamari.xp
        coins = king_calamari.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)


class CloakerDominoFormation(Formation):
    """A formation subclass specifically for Cloaker and Domino, who need special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # average HP between alternating fight options
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        cloaker = self.get_members_by_enemy_classes(Cloaker)[0].enemy()
        domino = self.get_members_by_enemy_classes(Domino)[0].enemy()
        earthlink = self.get_members_by_enemy_classes(Earthlink)[0].enemy()
        madadder = self.get_members_by_enemy_classes(MadAdder)[0].enemy()
        hp = round((cloaker.hp + domino.hp) / 2 + (earthlink.hp + madadder.hp) / 2)
        # xp and coins come only from these two
        xp = cloaker.xp + domino.xp
        coins = cloaker.coins + domino.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)


class ValentinaBossFormation(Formation):
    """A formation subclass specifically for Valentina, who needs special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # For Dodo/Valentina, count 40% of Dodo's HP.
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        dodo = self.get_members_by_enemy_classes(Dodo)
        hp -= round(0.6 * dodo[0].enemy().hp)
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)


class MegasmilaxBossFormation(Formation):
    """A formation subclass specifically for Megasmilax, who needs special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        megasmilax = self.get_members_by_enemy_classes(Megasmilax)[0].enemy()
        xp = megasmilax.xp
        coins = megasmilax.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)


class AxemBossFormation(Formation):
    """A formation subclass specifically for the Axem Rangers, who need special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        axems = self.get_members_by_enemy_classes(AxemRangers)[0].enemy()
        xp = axems.xp
        coins = axems.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)


class Belome2BossFormation(Formation):
    """A formation subclass specifically for Belome 2, who needs special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        belome = self.get_members_by_enemy_classes(Belome2)[0].enemy()
        marioclone = self.get_members_by_enemy_classes(MarioClone)[0].enemy()
        peachclone = self.get_members_by_enemy_classes(PeachClone)[0].enemy()
        xp = belome.xp + marioclone.xp + peachclone.xp
        coins = belome.coins + marioclone.coins + peachclone.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)


class CulexBossFormation(Formation):
    """A formation subclass specifically for Culex, who needs special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        culex = self.get_members_by_enemy_classes(Culex)[0].enemy()
        fire = self.get_members_by_enemy_classes(FireCrystal)[0].enemy()
        wind = self.get_members_by_enemy_classes(WindCrystal)[0].enemy()
        earth = self.get_members_by_enemy_classes(EarthCrystal)[0].enemy()
        water = self.get_members_by_enemy_classes(WaterCrystal)[0].enemy()
        xp = culex.xp + fire.xp + wind.xp + earth.xp + water.xp
        coins = culex.coins + fire.coins + wind.coins + earth.coins + water.coins
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)


class JohnnyBossFormation(Formation):
    """A formation subclass specifically for Johnny, who needs special calculations
    for stat totalling."""

    def get_summed_stats(self) -> tuple[int, int, int, int, int, int, int, int, int]:
        # xp only from mega
        (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade) = super().get_summed_stats()
        johnny = self.get_members_by_enemy_classes(Johnny)[0].enemy()
        henchmen = self.get_members_by_enemy_classes(BandanaBlue)
        xp = johnny.xp
        coins = johnny.coins
        for hench in henchmen:
            henchman = hench.enemy()
            xp += henchman.xp * 4
            coins += henchman.coins * 4
        return (
            hp,
            xp,
            coins,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade)
