"""Presets (need to be outfitted for new flagstrings)"""

from randomizer.types.world.flags.categories.classes import Preset


# decide what to do with these later


class CasualPreset(Preset):
    """Legacy casual preset"""

    _name: str = "Casual"
    _description: str = "Basic flags for a casual playthrough of the game."
    _flags: str = "K R Csj Tc4y $ M1 Sc4 Edf B Qa X2 P1 Nbmq D1s W"


class IntermediatePreset(Preset):
    """Legacy intermediate preset"""

    _name: str = "Intermediate"
    _description: str = "A mild increase in difficulty compared to casual."
    _flags: str = "Ks R7 Cspjl Tc3y $ M1 Sb4 Edf B Qsa X2 Nbmq D2s W"


class AdvancedPreset(Preset):
    """Legacy advanced preset"""

    _name: str = "Advanced"
    _description: str = (
        "More difficult options for advanced players, "
        "requiring you to manage your equips more."
    )
    _flags: str = (
        "Ks R7k Cspjl -nfc Tb2kd $ M2 Sb2 Edfsa Bc Qsba X2 P1 Nbmq Gm -fakeout D4s"
    )


class ExpertPreset(Preset):
    """Legacy expert preset"""

    _name: str = "Expert"
    _description: str = (
        "A highly chaotic shuffle with everything difficult enabled "
        "and helpful glitches disabled."
    )
    _flags: str = (
        "Ks R7kc Cspjl -nfc Tb2kduhi $ M2x Sv1 Edfsac! Bmcs Qsba! "
        "X2 P2 Nbmq Gsmke -fakeout D4s"
    )


class QuickPreset(Preset):
    """Legacy quick preset"""

    _name: str = "Quick"
    _description: str = (
        "A faster playthrough with free shops and XP acceleration "
        "for faster progression"
    )
    _flags: str = "K Rk Csjl Tc4yzm $ M2 Sc4 -freeshops Ed Bm Qsba X3 D1 W"


class ExplorerPreset(Preset):
    """Preset for people who like checking everything"""

    _name: str = "Explorer"
    _description: str = (
        "A flagset that draws on strong knowledge of the original game, "
        "and will require a lot of hunting."
    )
    _flags: str = (
        "Psize:1|start:random|random|avail:f     "
        "Qstats:some|perms:v_accessories_all|hints     "
        "Cexp:double|spells|uncap|avail:////H     "
        "Xrandom|avail:6|fights://////f     "
        "Trandom|quality:original|restrict_monstro|xpstars|mimics|slots|"
        "beetle|kamek|fireworks:progressive|tips     "
        "Lmoveflags|keys_anywhere|"
        "chests://////////////////////////////////////H|"
        "coins:4BgPAgN4/PAAAAA     "
        "Ifake|replace|xpstar:easybosses|"
        "gg:1|kg:1|s1:1|s2:2|s3:3|s4:4|s5:5|s6:6|sj1:30|sj2:100     "
        "Abw:mallow|fm:geno|pv:forest|bt:bowser|mm:tower|sea:star4|"
        "tmpl:seaside|mt:landsend|bv:nimbus|bk:volcano|wf:open     "
        "Oseaside:ship|doors:1|endgame:6|cwarp|bwarp|fasttravel|objective:factory     "
        "Gquiz|melody|pwd|skipcart     "
        "Srandom|quality:original|bias|showperms     "
        "Brandom|scale|allsprites|pool://////P"
    )


class Spring2021AsyncTourneyPreset(Preset):
    """Legacy tournament preset"""

    _name: str = "Spring 2021 Async Tournament (approximate)"
    _description: str = "Flagset for the 2021 Async Tourney"
    _flags: str = (
        "Psize:1|start:random|random|avail:f     "
        "Qstats:random|perms:random     "
        "Cexp:triple|stats|spells|spellstats|avail:////H     "
        "Xrandom|avail:6|fights://vv/OA     "
        "Trandom|quality:t4|restrict_monstro|fireworks:vanilla     "
        "Ifake|xpstar:vanilla|gg:100|kg:12|s1:1|s2:3|s3:5|s4:10|s5:15|s6:200|sj1:30|sj2:100     "
        "Abw:open|fm:open|pv:open|bt:open|mm:open|sea:open|"
        "tmpl:open|mt:open|bv:open|bk:open|wf:star6     "
        "Oseaside:open|skip_musty|doors:2|endgame:6|cwarp|objective:factory     "
        "Gdoors     Srandom|quality:t4|showperms     "
        "Brandom|scale|pool://3/f/H     "
        "Estats|drops|formations|attacks"
    )
    # needs m2 without x
