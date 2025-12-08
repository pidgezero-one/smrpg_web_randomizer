# pylint: disable=C0301

"""Individual bosses."""

from randomizer.types.dialogs.ids import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
    DI1660_SHIP_PASSWORD_COMPLETE,
    DI1694_FINAL_SHIP_HENCHMEN_DEFEATED,
    DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED,
    DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING,
    DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER,
    DI1781_SHIP_BOSS_JUMP_ON_HEAD,
    DI1782_SHIP_BOSS_DRINK,
    DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2,
    DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1,
    DI1786_LETTER_FROM_SHIP_BOSS,
    DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3,
    DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4,
    DI2061_HEAD_CHEF,
    DI2062_APPRENTICE_CHEF,
    DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
    DI2560_TOWER_HENCHMAN_1,
    DI2572_TOWER_HENCHMAN_2,
    DI2830_SEASIDE_BOSS_WELCOMES_YOU,
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
    DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
    DI3057_MONSTRO_SUPERBOSS_PROMPT,
    DI3072_TOWER_HENCHMAN_3_WINDOW,
    DI3073_TOWER_HENCHMAN_3,
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED)
from randomizer.types.battles.ids import (
    PACK0140_PUNCHINELLO_STATIC,
    PACK0146_CLERK_STATIC,
    PACK0147_MANAGER_STATIC,
    PACK0148_DIRECTOR_STATIC,
    PACK0149_GUNYOLK_STATIC,
    PACK0156_PANDORITE_FIGHT_STATIC,
    PACK0157_HIDON_FIGHT_STATIC,
    PACK0158_BOXBOY_FIGHT_STATIC,
    PACK0159_CHESTER_FIGHT_STATIC,
    PACK0161_BOOSTER_FIGHT_STATIC,
    PACK0163_CROCO1_FIGHT_STATIC,
    PACK0164_CROCO2_FIGHT_STATIC,
    PACK0166_JOHNNY_FIGHT_STATIC,
    PACK0167_CALAMARI_FIGHT_STATIC,
    PACK0168_BELOME1_FIGHT_STATIC,
    PACK0169_BELOME2_FIGHT_STATIC,
    PACK0171_VALENTINA_FIGHT_STATIC,
    PACK0172_CZAR_FIGHT_STATIC,
    PACK0173_MEGASMILAX_FIGHT_STATIC,
    PACK0174_COUNTDOWN_FIGHT_STATIC,
    PACK0175_BIRDETTA_FIGHT_STATIC,
    PACK0176_BUNDT_FIGHT_STATIC,
    PACK0177_KGGG_FIGHT_STATIC,
    PACK0178_JINX1_FIGHT_STATIC,
    PACK0179_MACK_FIGHT_STATIC,
    PACK0180_YARIDOVICH_FIGHT_STATIC,
    PACK0181_BOWYER_FIGHT_STATIC,
    PACK0182_AXEM_FIGHT_STATIC,
    PACK0183_HAMMERBRO_FIGHT_STATIC,
    PACK0184_CLOAKER_DOMINO_FIGHT_STATIC,
    PACK0185_SMITHY1_FIGHT_STATIC,
    PACK0186_EXOR_FIGHT_STATIC,
    PACK0187_JINX2_FIGHT_STATIC,
    PACK0188_JINX3_FIGHT_STATIC,
    PACK0189_JAGGER_FIGHT_STATIC,
    PACK0207_MOKURA_BOSS_STATIC,
    PACK0208_DODO_BOSS_STATIC,
    PACK0209_MAGIKOOPA_BOSS_STATIC,
    PACK0210_BOOMER_BOSS_STATIC,
    PACK0216_CULEX_BOSS_STATIC)
from randomizer.types.bosses import (
    Battlefields,
    EMPTY_DIALOG,
    Boss,
    Henchman,
    MimicBoss)
from randomizer.types.npcs.objects.types import NPC
from randomizer.types.npcs.objects import (
    AxemRed,
    AxemRedStatue,
    Belome1Large,
    Belome1Small,
    Belome2Large,
    Belome2Small,
    BirdettaLarge,
    BirdettaSmall,
    BirdettaStatue,
    Bloober,
    BlooberStatue,
    BoomerLarge,
    BoomerOverworld,
    BoomerSmall,
    BoomerStatue,
    Booster,
    BoosterStatue,
    BowyerLarge,
    BowyerOverworld,
    BowyerSmall,
    BowyerStatue,
    BoxBoyLarge,
    BoxBoySmall,
    BundtLarge,
    BundtSmall,
    BundtStatue,
    ChesterLarge,
    ChesterSmall,
    ClerkLarge,
    ClerkSmall,
    CountDownGridplane,
    CountDownStatue,
    Croco,
    Croco2,
    CrocoStatue,
    CulexLarge,
    CulexSmall,
    CulexStatue,
    CzarBody,
    CzarDragonLarge,
    CzarDragonSmall,
    CzarStatue,
    DirectorLarge,
    DirectorSmall,
    DodoLarge,
    DodoSmall,
    DodoStatue,
    DominoLarge,
    DominoSmall,
    DominoStatue,
    ExorSmall,
    ExorStatue,
    FactoryChief,
    FactoryChiefStatue,
    FakeElder,
    GrateGuyLarge,
    GrateGuySmall,
    GrateGuyStatue,
    HammerBroLarge,
    HammerBroSmall,
    HammerBroStatue,
    HidonLarge,
    HidonSmall,
    Jinx1,
    Jinx2,
    Jinx3,
    JinxStatue,
    JohnnyLarge,
    JohnnySmall,
    JohnnyStatue,
    MackLarge,
    MackMedium,
    MackSmall,
    MackStatue,
    MagikoopaLarge,
    MagikoopaStatue,
    ManagerLarge,
    ManagerSmall,
    Megasmilax,
    MimicStatue,
    MokuraCloud,
    MokuraLarge,
    MokuraStatue,
    PandoriteLarge,
    PandoriteSmall,
    PiranhaPlant,
    PiranhaPlantStatue,
    PunchinelloLarge,
    PunchinelloSmall,
    PunchinelloStatue,
    RedMagikoopa,
    ShovelKnightStatue,
    SmallBelomeStatue,
    SmithyLarge,
    SmithySmall,
    SmithyStatue,
    Terrapin,
    TerrapinStatue,
    ValentinaLarge,
    ValentinaSmall,
    YaridOverworld,
    YaridovichLarge,
    YaridovichStatue)

from .henchmen import (
    AxemRangersAxemBlack,
    AxemRangersAxemGreen,
    AxemRangersAxemPink,
    AxemRangersAxemYellow,
    AxemRangersMachine1,
    AxemRangersMachine2,
    AxemRangersMachine3,
    AxemRangersMachine4,
    AxemRangersMachine5,
    Belome2BowserClone,
    Belome2GenoClone,
    Belome2MallowClone,
    Belome2MarioClone,
    Belome2PeachClone,
    BirdettaEggbert,
    BoomerShyGuy,
    BoosterApprentice,
    BoosterSnifit,
    BowyerAero,
    BundtTorte1,
    BundtTorte2,
    ClerkMadMallet,
    CountdownDingALing,
    Croco2Crook,
    CulexEarthCrystal,
    CulexFireCrystal,
    CulexWaterCrystal,
    CulexWindCrystal,
    CzarPyrosphere,
    DirectorPoundette,
    GrateGuyKnifeGuy,
    HidonGoombette,
    JohnnyBandanaBlue,
    JohnnyBandanaRed,
    KingCalamariBloober,
    MackShyster1,
    MackShyster2,
    ManagerPounder,
    MegaSmilaxPiranha,
    PunchinelloBobomb,
    SmithyAero,
    SmithyDrillBit,
    SmithyShyster,
    ValentinaBirdy,
    ValentinaBluebird,
    YaridovichHenchman)


class HammerBroBoss(Boss):
    """Hammer Bros boss fight"""

    _name: str = "Hammer Bro"
    _letter_seaside_boss_name: str = "the Hammer Bros"
    _letter_volcano_boss_name: str = "two brothers dancing around"
    _letter_final_boss_name: str = "the Hammer Bros' pals."
    _pack_number: int = PACK0183_HAMMERBRO_FIGHT_STATIC
    _small_model: type[NPC] = HammerBroSmall
    _big_model: type[NPC] = HammerBroLarge
    _statue: type[NPC] = HammerBroStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """HAMMER BRO: Alright already,\n you won, now go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you figured it out... But you\n gotta get past my hammer to get\n through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Hammer Bros' place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the HAMMER BROS!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """HAMMER BRO: ...grumble...\n My hammer's embarrassed about\n losing...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """HAMMER BRO: What're YOU lookin' at?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """HAMMER BRO: Look buddy, you\n already won, you can get off of my\n hammer now.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ After getting hammered, [await]\n I always drink Carrot Juice.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`!\n[await][page]\n My bro and I saw you squash\n `SEASIDE_BOSS`!  Nice one!\n[await]\n My bro and his hammer say they saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n We've nailed them down as one of \n `FINAL_BOSS_NAME`\n Listen, my bro is on me about[await]\n loanin' you my hammer.  Whaddaya\n say you bring me back an upgrade\n to pummel him with? Do me a solid![await][page]\n\n                                  Thanks!\n                         Hammer Bro #2[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big hammer! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """HAMMER BRO: You better find [0x7024]\n more of `MARRYMORE_CHARACTER`'s things,\n or my hammer'll be angry![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Hammer Bros are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Hammer Bros.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """HAMMER BRO: What're YOU lookin'\n at?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find the Hammer Bro...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """HAMMER BRO: The dojo master\n takes on 3 different forms.\n Me, though? I'm just a hammer.[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Hammer-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """HAMMER BRO: I guess you were\n tougher than I thought![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """HAMMER BRO: I guess you were\n tougher than I thought![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 539


class Croco1Boss(Boss):
    """Croco 1 boss fight"""

    _name: str = "Croco"
    _letter_volcano_boss_name: str = "a thieving dinosaur dashing"
    _letter_final_boss_name: str = "Croco's accomplices."
    _pack_number: int = PACK0163_CROCO1_FIGHT_STATIC
    _small_model: type[NPC] = Croco
    _statue: type[NPC] = CrocoStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n CROCO: Get the heck outta here![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Alright, alright, so ya figured out\n my password! But I ain't goin'\n down without a fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Croco's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped CROCO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CROCO: Enough already, get outta\n here![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CROCO: Back already? How 'bout a\n drink?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n    CROCO: 'Dis some kinda joke?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Wanna know how I run so fast?[await]\n Chug some Honey Syrup, chump![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n 'Sup Half-Wits?!\n[await][page]\n Did it take you 500 years to beat \n `SEASIDE_BOSS`?\n [await]\n While casing my next heist, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano. Seems... nice.[await]\n I better get a crew together with \n `FINAL_BOSS_NAME`\n I'm telling you this because I want \n this to be a challenge this time. \n I bet this bazooka that I lifted from\n that toad "guard" will be useful![await][page]\n\n                                    Seeya!\n                                     Croco[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big reptile! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CROCO: What's dis?[await][pause] You fools're\n gonna take another 100 years to\n find the last [0x7024] item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Croco's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Croco.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CROCO: Whaddya doin' hangin\n 'round here?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Croco...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CROCO: Think ya can beat the dojo\n master, chump? I'd like to see ya\n try![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Wallet-this and Coin-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 540


class MackBoss(Boss):
    """Mack boss fight"""

    _name: str = "Mack"
    _letter_volcano_boss_name: str = "a small sword jumping"
    _letter_final_boss_name: str = "Mack's shysters."
    _pack_number: int = PACK0179_MACK_FIGHT_STATIC
    _small_model: type[NPC] = MackSmall
    _big_model: type[NPC] = MackMedium
    _attack_model: type[NPC] = MackLarge
    _statue: type[NPC] = MackStatue
    _unique_henchmen: list[type[Henchman]] = [
        MackShyster1,
        MackShyster2,
        MackShyster1,
        MackShyster2,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [MackShyster1, MackShyster2]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MACK: Party's over. I'm going to\n sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Listen, bub![await]\n You may have figured out my\n password, but you still gotta get\n past me if you want through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Mack's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped MACK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   MACK: Guess the party's over.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MACK: Hey `MAIN_CHARACTER_NAME`!\n Come back to crash our party?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MACK: OK, I get it, you can bounce\n too.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I don't care what kinda party it is![await]\n I drink Milk so I can be like Exor!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Yo `MAIN_CHARACTER_NAME`!\n[await][page]\n I heard you left and threw down\n with `SEASIDE_BOSS`![await]\n\n The shysters on lookout saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They got the good stuff from \n `FINAL_BOSS_NAME`[await]\n We'd better get back aboard before\n any other Shyster party fouls.\n I heard Exor might even show up![await][page]\n\n                             Hang loose!\n                                     Mack[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """BODYGUARD: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        DI2061_HEAD_CHEF: """BODYGUARD: Doesn't this cake\n look just like Mack?[await]""",
        DI2062_APPRENTICE_CHEF: """BODYGUARD: We've gotten REAL\n good with fondant![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MACK: I'm not happy to delay the\n party, but we can't get started\n until you find [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """BODYGUARD: Welcome![await][pause]\n Our party is invitation-only, so\n please come back another time.[await][page]\n[delay] ...You're here to crash it anyway?[delay]\n Alright, wise guy, let's go![await]""",
        DI2572_TOWER_HENCHMAN_2: """\n   BODYGUARD: Oh, no you don't![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n   MACK: What are you doing here?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Yo! You look tired.[delay] How 'bout a\n night on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Mack's house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Yo! It's fine if you hang out in\n town, but... [delay]stay away from the\n shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ You trying to snoop on what I'm\n buying here?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n       What're YOU lookin' at?[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n               Beat it, bub![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MACK: Think you're gonna beat the\n dojo master today?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You come to crash my party?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """BODYGUARD: I almost feel bad\n for all those fools out there,\n who can't even bounce...[await]""",
        DI3073_TOWER_HENCHMAN_3: """BODYGUARD: How 'bout a fat lip to\n go with that ugly moustache?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bouncing-this and Party-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MACK: I guess you CAN bounce\n after all.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MACK: I guess you CAN bounce\n after all.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BODYGUARD: Think you're tough,\n pal?[await][delay] March that ugly mustache into\n Mack's room, and see what\n happens![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BODYGUARD: You beat Mack?[await]\n This is not good![delay_30]\n I guess you can bounce after all.[await]""",
    }

    _item_id: int = 541


class PandoriteBoss(MimicBoss):
    """Pandorite boss fight"""

    _name: str = "Pandorite"
    _letter_volcano_boss_name: str = "a red box sliding about"
    _letter_final_boss_name: str = "Pandorite's monsters."
    _pack_number: int = PACK0156_PANDORITE_FIGHT_STATIC
    _small_model: type[NPC] = PandoriteSmall
    _big_model: type[NPC] = PandoriteLarge
    _statue: type[NPC] = MimicStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PANDORITE: That thing was making\n me sick...[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you cracked the code. I'm\n warning you though, I hate being\n woken up.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Pandorite's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped \nPANDORITE!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """PANDORITE: Whatever... Leave me\n alone so I can go back to sleep.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """PANDORITE: I think I like this place\n more than the sewers. It smells\n marginally better.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PANDORITE: I can't tell if this is\n better or worse without the\n protection of my box.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Here, you can have my...um...[await]\n '21 Redtail Chardonnay.[delay] It's fine.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Dear `MAIN_CHARACTER_NAME`,\n[await][page]\n Someone closed my box, and I\n floated up here to see your battle[await]\n with `SEASIDE_BOSS`.\n While looking for rocks, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I think it might be one of \n `FINAL_BOSS_NAME`[await]\n I've got all the rocks in my box\n so I should sink near the ship.\n Drop by to see if I made it later.[await][page]\n\n                         Warm Regards,\n                               Pandorite[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PANDORITE: Sorry, you can't skip\n getting the last [0x7024] item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Pandorite's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Pandorite.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PANDORITE: There's not much to do\n around here.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Pandorite...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PANDORITE: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PANDORITE: ...I'm not sure how\n I'm accomplishing this.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PANDORITE: ...I'm not sure how\n I'm accomplishing this.[await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 542


class Belome1Boss(Boss):
    """Belome 1 boss fight"""

    _name: str = "Belome"
    _letter_volcano_boss_name: str = "a hungry dog walking"
    _letter_final_boss_name: str = "Belome's clones."
    _pack_number: int = PACK0168_BELOME1_FIGHT_STATIC
    _small_model: type[NPC] = Belome1Small
    _big_model: type[NPC] = Belome1Large
    _statue: type[NPC] = SmallBelomeStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n        BELOME: Good night~![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Belome's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BELOME: Oh, you're back![await]\n Did you bring any food?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I'm always STARVING~![await]\n...but I hydrate with Filtered Water.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """It's a damp, slimy, looking note (did `SEASIDE_BOSS` LICK this?).\n[await][page]\nA paw print and a crudely drawn image of `VOLCANO_BOSS_DESCRIPTION`\nis etched on the paper.\nThis is probably one of \n`FINAL_BOSS_NAME`'s henchmen!\n`SEASIDE_BOSS` likely headed down to\nfind more snacks,\nso it's time to move on.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Belome.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BELOME: It's dreadfully boring\n around here~![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you the pizza delivery person?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 543


class BowyerBoss(Boss):
    """Bowyer boss fight"""

    _name: str = "Bowyer"
    _letter_volcano_boss_name: str = "a longbow loosing arrows at"
    _letter_final_boss_name: str = "Bowyer's lackeys."
    _pack_number: int = PACK0181_BOWYER_FIGHT_STATIC
    _small_model: type[NPC] = BowyerSmall
    _big_model: type[NPC] = BowyerOverworld
    _attack_model: type[NPC] = BowyerLarge
    _statue: type[NPC] = BowyerStatue
    _unique_henchmen: list[type[Henchman]] = [
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [BowyerAero]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOWYER: Disturb me you must not,\n nya!""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Nya, NYA?![delay_30] Cracked the code, you\n did! But fight you, I will, nya![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Bowyer's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOWYER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOWYER: That was nyat fair!\n Scram you must, nya![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOWYER: Back again, you are,\n nya? I'm nyat as mad as before.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOWYER: Nya, NYA?! Stop this,\n you must![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Nya, Nya, NYA!  Make like Locke![await]\n Bring me more Strongbow Cider![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Knock, knock, NYA!!\n[await][page]\n Your battle is long and boring,\n even for `SEASIDE_BOSS`, nya!\n[await]\n Aero #837 painted a target on\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano, nya!![await]\n 10,000 arrows will I fire at\n `FINAL_BOSS_NAME`, NYA!\n Follow me to the ship you will NOT!\n Your Scarf requires 100 Super \n Jumps and your Super Suit has\n -127 attack and m. attack, I hope![await][page]\n\n                                  NYA!!!!\n                                    Bowyer[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """FLUNKIE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        DI2061_HEAD_CHEF: """FLUNKIE: Doesn't this cake\n look just like Bowyer?[await]""",
        DI2062_APPRENTICE_CHEF: """FLUNKIE: We've gotten REAL\n good with fondant![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOWYER: Nya, NYA!?[await][pause] Disturb me\n you must not, until [0x7024] more item(s)\n you find, nya![await]""",
        DI2560_TOWER_HENCHMAN_1: """FLUNKIE: Hello.[await][pause] Bowyer is busy\n now, and he really hates to be\n interrupted.[await][page]\n[delay] ...If you're not going to leave,\n I'll have to kick you out myself![await]""",
        DI2572_TOWER_HENCHMAN_2: """FLUNKIE: I'm gonna have to ask you\n not to interrupt Bowyer's target\n practice.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\nBOWYER: Nya! Boring here, it is...[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Since I'm having a good day, you\n can stay here free of charge.\n [delay]How's that sound?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Bowyer's house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Don't cause any trouble in our\n town! Stay away from the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I'm just a customer![delay] Let me shop\n in peace![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There's a very uh... [delay]important\n meeting happening inside.\n [delay]You may not enter.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ What's going on in here?[await][pause] None of\n your business, that's what![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n BOWYER: Interesting, this will be![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Fight me, you will, nya?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """FLUNKIE: ...sigh... [delay]Bowyer scolded\n me for interrupting his shooting\n practice.[await][pause] I was just trying to warn\n him that `MAIN_CHARACTER_NAME` is here![await]""",
        DI3073_TOWER_HENCHMAN_3: """FLUNKIE: You look like you'd make\n for a good statue![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arrow-this and Target-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOWYER: 1000 jumps I must do,\n nya![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOWYER: 1000 jumps I must do,\n nya![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """FLUNKIE: Whoa! You sure showed\n us! Go on ahead to Bowyer's\n place![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """FLUNKIE: Come back and visit\n us sometime. Bowyer won't stay\n mad forever![await]""",
    }
    _item_id: int = 544


class Croco2Boss(Boss):
    """Croco 2 boss fight"""

    _name: str = "Croco"
    _letter_volcano_boss_name: str = "a thieving dinosaur dashing"
    _letter_final_boss_name: str = "Croco's accomplices."
    _pack_number: int = PACK0164_CROCO2_FIGHT_STATIC
    _small_model: type[NPC] = Croco2
    _statue: type[NPC] = CrocoStatue
    _unique_henchmen: list[type[Henchman]] = [Croco2Crook, Croco2Crook, Croco2Crook]
    _repeatable_henchmen: list[type[Henchman]] = [Croco2Crook]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n CROCO: Get the heck outta here![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Alright, alright, so ya figured out\n my password! But I ain't goin'\n down without a fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Croco's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped CROCO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CROCO: Enough already, get outta\n here![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CROCO: Back already? How 'bout a\n drink?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n    CROCO: 'Dis some kinda joke?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I tapped Canada's Maple Syrup[await]\n Reserve. They'll NEVER catch me!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n 'Sup Half-Wits?!\n[await][page]\n Did it take you 500 years to beat \n `SEASIDE_BOSS`?\n [await]\n While casing my next heist, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano. Seems... nice.[await]\n I better get a crew together with \n `FINAL_BOSS_NAME`\n I'm telling you this because I want \n this to be a challenge this time. \n I bet this bazooka that I lifted from\n that toad "guard" will be useful![await][page]\n\n                                    Seeya!\n                                     Croco[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """FLUNKIE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        DI2061_HEAD_CHEF: """FLUNKIE: Doesn't this cake\n look just like Croco?[await]""",
        DI2062_APPRENTICE_CHEF: """FLUNKIE: We've gotten REAL\n good with fondant![await]""",
        DI2560_TOWER_HENCHMAN_1: """FLUNKIE: Croco's busy! Scram![await]\n[delay_60] ...Not leaving, huh?\n[delay] Alright buddy, you asked for it![await]""",
        DI2572_TOWER_HENCHMAN_2: """FLUNKIE: Where d'ya think YOU'RE\n going?![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CROCO: Whaddya doin' hangin\n 'round here?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ You tired? You can stay here\n for free.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Croco's house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ You better not be snooping around\n the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Huh?[delay] What am I doing here?[delay] None\n of your business, that's what![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n           Nothin' to see here.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Nope, nothing suspicious going on\n in this house![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CROCO: Think ya can beat the dojo\n master, chump? I'd like to see ya\n try![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """\n  FLUNKIE: I could use a stepstool.[await]""",
        DI3073_TOWER_HENCHMAN_3: """\n      FLUNKIE: A tough guy, eh?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Wallet-this and Coin-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """FLUNKIE: (Sob, sob...)[delay_30]\n You're pretty tough. I guess I'll let\n you through to Croco's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """FLUNKIE: You beat Croco!?[delay_30]\n We'll getcha for this![await][page]\n Maybe not today, maybe not\n tomorrow, but someday...[await]""",
    }

    _item_id: int = 545


class PunchinelloBoss(Boss):
    """Punchinello boss fight"""

    _name: str = "Punchinello"
    _letter_seaside_boss_name: str = "Hothead"
    _letter_volcano_boss_name: str = "a demolitionist stomping"
    _letter_final_boss_name: str = "Punchinello's demo team."
    _pack_number: int = PACK0140_PUNCHINELLO_STATIC
    _small_model: type[NPC] = PunchinelloSmall
    _big_model: type[NPC] = PunchinelloLarge
    _statue: type[NPC] = PunchinelloStatue
    _unique_henchmen: list[type[Henchman]] = [
        PunchinelloBobomb,
        PunchinelloBobomb,
        PunchinelloBobomb,
        PunchinelloBobomb,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [PunchinelloBobomb]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PUNCHINELLO: Grrr... Leave me\n alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So... You figured out my\n password.[await]\n If you're not here for an\n autograph, I'll have to test you\n once more to let you through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Punchinello's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n PUNCHINELLO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """PUNCHINELLO: Grrr... I'll never get famous\n at this rate![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """PUNCHINELLO: You've come back to\n visit? I truly must be famous![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PUNCHINELLO: They say I'm a hot\n head, so it's a bad idea to stand\n on my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ WATCH ME DRINK THIS TOBASCO![await]\n I'm gonna be youtube-famous![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """\n      BOB-OMB: I need a break.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n WHAT'S UP FANS?!\n[await][page]\n I just watched a HYPE fight versus\n `SEASIDE_BOSS`.  Oh.  Em.  Gee.[await]\n\n My Bob-omb army told me about\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.  Fuse is LIT!![await]\n I smell a collab video with \n `FINAL_BOSS_NAME`[await]\n Don't forget to tune in for my 100k\n follower special, where I'll play\n Bob-omb roulette with watermelons![await][page]\n\n           Like, Share, and Subscribe!\n                              Punchinello[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """BOB-OMB: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """\n      BOB-OMB: I need a break.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """\n      BOB-OMB: I need a break.[await]""",
        DI2061_HEAD_CHEF: """BOB-OMB: Doesn't this cake\n look just like Punchinello?[await]""",
        DI2062_APPRENTICE_CHEF: """BOB-OMB: We've gotten quite\n good with fondant.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PUNCHINELLO: Huh?[delay_30] What the hay?[await]\n Where are the other [0x7024] item(s)?[await]""",
        DI2560_TOWER_HENCHMAN_1: """BOB-OMB: Hello there.[await][pause] If you've\n come for Punchinello's autograph,\n please allow me to buzz you up...[await][page]\n [delay]...You're not here for that?[await]\n [delay]Uh oh, he'll be pretty mad!\n [delay]I'd better do something![await]""",
        DI2572_TOWER_HENCHMAN_2: """BOB-OMB: There's nothing to see\n back here...[await][pause] I mean that.[await]\n You don't believe me?[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PUNCHINELLO: Hmmm... [delay]Huh?\n [delay]A visitor? [delay]Well, there's not much\n to do around here.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello there.[await][pause] Today, we've got an\n explosively good deal for you![delay] All\n inn expenses are free of charge.[await]\n Would you like to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Punchinello's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hello there.[delay] Welcome to our humble\n town. We have the least suspicious\n shed in all the land.[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I know how this must look, but I'm\n just here to browse the perfectly\n legal goods they're selling.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hello there.[delay] Sorry, but I can't let\n you through this door today.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ You wouldn't wanna enter this\n house, oh no.[delay] We'll make sure you\n don't enter by accident.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PUNCHINELLO: A challenge from\n the dojo master, eh? Let's see\n where this goes.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong number)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """BOB-OMB: I don't look like the\n other bob-ombs here. [delay]That's weird.[await]""",
        DI3073_TOWER_HENCHMAN_3: """BOB-OMB: You don't think it makes\n sense for a bob-omb to be shooting\n bullets?[await][pause] ...Fight me about it![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bomb-this and Famous-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BOB-OMB: I guess I was a little\n hot-headed, thinking I could win.\n Go on in to Punchinello's room.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BOB-OMB: Wow, you beat\n Punchinello! He's not very happy\n about that.[await]""",
    }

    _item_id: int = 546


class BoosterBoss(Boss):
    """Booster boss fight"""

    _name: str = "Booster"
    _letter_volcano_boss_name: str = "a viking riding trains"
    _letter_final_boss_name: str = "Booster's frenemies."
    _pack_number: int = PACK0161_BOOSTER_FIGHT_STATIC
    _small_model: type[NPC] = Booster
    _statue: type[NPC] = BoosterStatue
    _unique_henchmen: list[type[Henchman]] = [
        BoosterSnifit,
        BoosterSnifit,
        BoosterSnifit,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [BoosterApprentice]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOOSTER: It's pretty cozy in here.[await][pause]\n No, you can't come in![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Eh?[delay_30] THAT was my password?![delay_30]\n I'd better fight you, just to be\n sure.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Booster's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOOSTER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOOSTER: I'd love to entertain\n you, but I'm busy watching the\n fish. Come back later.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOOSTER: Eh...? My! It's you\n again![await][page]\n  We're having a heated debate over\n what a “party” is, so you can stay\n if you'd like to contribute.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOOSTER: Hm? How's the view up there?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ This Dish Detergent is DELICIOUS![await]\n Number 2, (belch) MORE SOAP!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """SNIFIT 1: There's a 70% chance the\n drink on the table is actually\n punch.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """SNIFIT 2: Booster can't find any\n beetles underwater, but he still\n enjoys watching the fish.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Attention `MAIN_CHARACTER_NAME`,\n[await][page]\n We had an urgent engagement, and\n regret that we couldn't stay and\n play with `SEASIDE_BOSS`.\n[await]\n While on beetle patrol, #2 saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n Snifit three suggested they might be\n `FINAL_BOSS_NAME`\n We're riding the Loco Express to\n the lake of wedding tears.  Also, \n Number 1 says there's no money \n in the budget for new doors.[await][page]\n\n                                   Booster\n                  Dictated but not read[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """SNIFIT 3: Uh... Do you know where\n we could get some cake down here?[await]""",
        DI2061_HEAD_CHEF: """SNIFIT 2: Doesn't this cake\n look just like Booster?[await]""",
        DI2062_APPRENTICE_CHEF: """SNIFIT 3: Uh... I think we should\n have made his mustache bigger.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n   BOOSTER: Found our town, eh?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """SNIFIT 1: Welcome![delay] How would you\n like to stay in our fabulous inn\n for free today?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Booster's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """\n You'd better not go near our shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I'm facing a promotion. Do they sell\n anything here that'll make me look\n more professional?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """SNIFIT 3: Uh... Don't look in the\n window. [delay]Pretty please.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """SNIFIT 2: There is nothing of\n interest to you in here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOOSTER: I wonder if the dojo\n master can shape-shift into a\n Mario doll.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Eh? What'd you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Beetle-this and Train-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """APPRENTICE: Oh, dear![delay] We've\n failed to keep the intruder away\n from Booster![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """APPRENTICE: Booster's not happy\n about losing. Please do not jump\n on his head.[await]""",
    }

    _item_id: int = 547


class GrateGuyBoss(Boss):
    """KGGG Boss fight"""

    _name: str = "Grate Guy"
    _letter_seaside_boss_name: str = "the Clowns"
    _letter_volcano_boss_name: str = "a couple clowns bouncing"
    _letter_final_boss_name: str = "Grate Guy's clowns."
    _pack_number: int = PACK0177_KGGG_FIGHT_STATIC
    _small_model: type[NPC] = GrateGuySmall
    _big_model: type[NPC] = GrateGuyLarge
    _statue: type[NPC] = GrateGuyStatue
    _unique_henchmen: list[type[Henchman]] = [GrateGuyKnifeGuy]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """GRATE GUY: Get lost, buddy, I'm\n busy![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, a patron![delay_30] Come on in and let's\n get this show on the road![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Knife Guy and Grate Guy's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped KNIFE GUY\n and GRATE GUY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """GRATE GUY: Yikes, you're pretty\n tough! I need some time to recover.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """GRATE GUY: It's so boring\n around here... Hey, wanna play\n "Look the other way" with me?[await][page]\n Hah! [delay_30]Just kidding![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """GRATE GUY: Sorry, `MAIN_CHARACTER_NAME`,\n but jumping on my head isn't going\n to teach you Blizzard.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Of course I didn't shake it up!![await]\n Go on, have a Root Beer!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """KNIFE GUY: No, I'm not giving you the Bright Card down here![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Heya `MAIN_CHARACTER_NAME`,\n[await][page]\n Looks like you totally thrashed\n `SEASIDE_BOSS`.  Whoopdy do!\n[await]\n Knife Guy tells me he saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They're in a traveling circus with \n `FINAL_BOSS_NAME`\n I was going to open a casino,[await]\n but Knife Guy dropped the ball on\n the building permits, so now our\n ship is sunk.  Stop by sometime,[await]\n we're always down to clown. [await][page]\n\n                                    Later!\n                 Grate Guy & Knife Guy[await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big clown! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """GRATE GUY: Hm?[await][pause] Well, you took all\n the trouble to find [0x7000] item(s,\n so... keep looking for the other [0x7024]![await]\n I can stick around all day.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Knife Guy and Grate Guy are busy\n right now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Knife Guy and\n Grate Guy.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """GRATE GUY: Gee, it sure is boring\n around here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Grate Guy...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """GRATE GUY: The dojo master's\n much tougher than I am. Think you\n can win?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Welcome! What brings you here?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Knife-this and Casino-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """GRATE GUY: Look, `MAIN_CHARACTER_NAME`!\n I've been training so hard, that my\n ball jumps with me![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """GRATE GUY: Look, `MAIN_CHARACTER_NAME`!\n I've been training so hard, that my\n ball jumps with me![await]""",
    }
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 548


class BundtBoss(Boss):
    """Bundt boss fight"""

    _name: str = "Bundt"
    _letter_seaside_boss_name: str = "the Cake"
    _letter_volcano_boss_name: str = "a wedding cake shuffling"
    _letter_final_boss_name: str = "Bundt's bakers."
    _pack_number: int = PACK0176_BUNDT_FIGHT_STATIC
    _small_model: type[NPC] = BundtSmall
    _big_model: type[NPC] = BundtLarge
    _statue: type[NPC] = BundtStatue
    _unique_henchmen: list[type[Henchman]] = [BundtTorte1, BundtTorte2]
    _repeatable_henchmen: list[type[Henchman]] = [BundtTorte1, BundtTorte2]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n        (There's no response.)[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """\n    (The cake beckons you forth.)[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Bundt's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BUNDT!![await]""",
        # Find some way to do an animation instead of posting dialogue
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """CHEF TORTE: Ze apprentice, he\n inseests he saw ze cake MOVE!\n Vhy must he still talk of zees?![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n(This letter is written in... icing?)\n[await][page]\n GrEATings~  You hes defEATed\n `SEASIDE_BOSS`, yes?\n Zer must have BEAN much SALT.\n[await]\n I make new good FRYends\n `VOLCANO_BOSS_DESCRIPTION`\n vile BAKING in ze volcano.[await]\n Zey know ozzer good CUTLERY in\n `FINAL_BOSS_NAME`\n I go back to ship now.  High\n pressure ond low temperature\n keep SPONGE moist ond fresh.[await][page]\n\n              Be having good nuptials.\n                                   Ze Cake[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """APPRENTICE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """APPRENTICE: You saw it too,\n right? I know I wasn't just\n imagining it![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Zees ees not sparkling wine,[await]\n philistine!  Ees Champagne!![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """APPRENTICE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """Wait... Did that cake just move?[await]\n Let's worry about it after finding\n the last [0x7024] item(s).[await]""",  # do this one with no background
        DI2560_TOWER_HENCHMAN_1: """APPRENTICE: Welcome to our\n world-class culinary school.[await]\n Please come back later to try some\n of our famous Bundt Cake.[await][page]\n [delay]...You want it NOW?\n [delay]How impatient! [delay]I oughtta teach you a lesson![await]""",
        DI2572_TOWER_HENCHMAN_2: """CHEF TORTE: Ve are busy preparing\n ze batter at ze moment...[await]\n No, you can't have any right zees\n second! [delay]How rude![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: EMPTY_DIALOG,
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome. Our inn services are free\n tonight.[await][pause] We've unfortunately run\n out of complimentary cake, but\n would you like to stay anyway?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Bundt's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Don't disturb the guards at the\n shed. They're uh... guarding a\n very important bake-off![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I'm just here for kitchen supplies.\n Please leave me alone.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ You can't just barge in here while\n I'm standing guard.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Why's the door locked? [delay]Uh... [delay]We're\n uh... [delay]baking a very important\n cake! [delay]Do not disturb! [delay_30](I'm so sly!)[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: EMPTY_DIALOG,
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """[delay_60][await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """APPRENTICE: (Please let this cake\n not be evil... please let this cake\n not be evil...)[await]""",
        DI3073_TOWER_HENCHMAN_3: """APPRENTICE: You again?! Leave\n our cake alone![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n I never hear the next door\n neighbour.[await][pause] Maybe they don't move\n around much.[await][page]\n I'd like to go over and introduce\n myself sometime, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: EMPTY_DIALOG,
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: EMPTY_DIALOG,
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """APPRENTICE: All right, we'll let\n you through. But don't mess our\n cake up, we spent all day on it.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """APPRENTICE: I thought we asked\n you not to mess our cake up![await]""",
    }

    _item_id: int = 549


class KingCalamariBoss(Boss):
    """King Calamari boss fight"""

    _name: str = "King Calamari"
    _letter_seaside_boss_name: str = "the Squid"
    _letter_volcano_boss_name: str = "a giant squid lurking"
    _letter_final_boss_name: str = "King Calamari's hands."
    _pack_number: int = PACK0167_CALAMARI_FIGHT_STATIC
    _forced_background = Battlefields.KING_CALAMARI
    _small_model: type[NPC] = Bloober
    _statue: type[NPC] = BlooberStatue
    _repeatable_henchmen: list[type[Henchman]] = [KingCalamariBloober]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """KING CALAMARI: When I was born, I\n hatched from an egg that was only\n three times as large as this one.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n King Calamari's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n KING CALAMARI!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """KING CALAMARI: I can't believe I\n was defeated in the ship I sunk\n myself...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """KING CALAMARI: Win or lose, I'm\n still king of this ship.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """KING CALAMARI: I'm pretty slimy,\n so this seems like a bad idea.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I've found booty in the hold![await]\n Vats of Pearlescent Oyster Juice![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n There's a wet parchment with ink:\n[await][page]\n There's a surpringly great picture \n your battle with `SEASIDE_BOSS`.[await]\n\n On the back is an image of [await]\n `VOLCANO_BOSS_DESCRIPTION`\n near a volcano, looks like.[await]\n Then a bunch of ?'s next to \n `FINAL_BOSS_NAME`[await]\n Finally, there's a picture of a\n squid with X's for eyes falling\n towards the shipwreck.[await][page]\n\n This drawing raises more questions\n than it answers.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big squid! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """KING CALAMARI: Sorry, I don't\n have any hint memos for where you\n can find the last [0x7024] item(s).[await]""",  # do this one with no background
        DI2560_TOWER_HENCHMAN_1: """ Hello there. Welcome to our\n first-ever above-ground treasure\n hoard.[await][page]\n [delay].[delay].[delay].[delay]You're not here to see that?[delay_30]\n Well,[delay] then you must be an intruder!""",
        DI2572_TOWER_HENCHMAN_2: """ There's nothing back here!\n I mean it![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """KING CALAMARI: It's not so weird\n for a squid to run a town.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find King Calamari...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """KING CALAMARI: Think you can beat\n the dojo master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What do you want?[await]\n  [select] (Let's fight)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """ I'd just like to go back to\n shooting ink, not bullets...[await]""",
        DI3073_TOWER_HENCHMAN_3: """\n       You looking for a fight?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Ship-this and Tentacle-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """KING CALAMARI: My tentacles\n shouldn't be able to do this.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """KING CALAMARI: My tentacles\n shouldn't be able to do this.[await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 550


class HidonBoss(MimicBoss):
    """Hidon boss fight"""

    _name: str = "Hidon"
    _letter_volcano_boss_name: str = "a green box sliding about"
    _letter_final_boss_name: str = "Hidon's monsters."
    _pack_number: int = PACK0157_HIDON_FIGHT_STATIC
    _small_model: type[NPC] = HidonSmall
    _big_model: type[NPC] = HidonLarge
    _statue: type[NPC] = MimicStatue
    _unique_henchmen: list[type[Henchman]] = [
        HidonGoombette,
        HidonGoombette,
        HidonGoombette,
        HidonGoombette,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [HidonGoombette]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """HIDON: No, I'm not gonna puke up\n another item for you! Go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Ugh... What a rude awakening!\n I'm going to make it a hassle for\n you to pass through here![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Hidon's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped HIDON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """HIDON: Guess I'll have to train the\n Goombettes harder.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """HIDON: This is definitely an upgrade\n from my old post.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """HIDON: Oh come on, you know I'm\n weak to jumps![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Goombettes! They're after my[await]\n 1947 Phateu Cetrus Merlot!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Listen up interloper!\n[await][page]\n Good job getting rid of\n `SEASIDE_BOSS`! Now[await]\n my naval dominance is complete!\n The goombette's nest reported[await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They sail under the flag of \n `FINAL_BOSS_NAME`[await]\n If you ever touch my box again,\n I'm taking a finger... at least.[await][page]\n\n                  Lots of Carni-kisses,\n                                     Hidon[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """GOOMBETTE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI2061_HEAD_CHEF: """GOOMBETTE: Doesn't this cake\n look just like Hidon?[await]""",
        DI2062_APPRENTICE_CHEF: """GOOMBETTE: We've gotten REAL\n good with fondant![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """HIDON: ...I don't know where the\n last [0x7024] item(s) are. Ask the\n Goombettes.[await]""",
        DI2560_TOWER_HENCHMAN_1: """GOOMBETTE: I need a pen, but I\n can't reach the top drawer of this\n desk. Can you help me out?[await][page]\n [delay]...What?[delay] “How are you going to\n use a pen when you don't have any\n arms”?[await][pause] You makin' fun of me?!\n [delay]That's IT, buddy! Get down here![await]""",
        DI2572_TOWER_HENCHMAN_2: """GOOMBETTE: Hey! Hidon's trying to\n stay in hidin' over here![delay] Get lost![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n          HIDON: Oh, it's you.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hey! Why don't you crash here for\n the night? It's free! FREE![await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Hidon's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hey! What are you doing in our\n town? Don't go snooping around![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Why don'tcha mind your own\n beeswax?![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Don't even THINK about going\n inside this house![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hey, buster![delay] You think you're some\n kinda tough guy, tryin' to step\n over us guards?![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """HIDON: The dojo master's pretty\n tough.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Ugh... What'd you wake me up for?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """GOOMBETTE: (I'm too short to see\n out this window.)[await]""",
        DI3073_TOWER_HENCHMAN_3: """GOOMBETTE: Put up your dukes,\n tough guy![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Piranha-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """HIDON: I bet this would be even\n harder to do in my box.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """HIDON: I bet this would be even\n harder to do in my box.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """GOOMBETTE: You mighta' won\n against us, but Hidon's gonna\n beat you up![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """GOOMBETTE: You beat Hidon?![await]\n Oh, man...[await]""",
    }

    _item_id: int = 551


class JohnnyBoss(Boss):
    """Johnny boss fight"""

    _name: str = "Johnny"
    _letter_volcano_boss_name: str = "a shark prowling around"
    _letter_final_boss_name: str = "Johnny's crew."
    _pack_number: int = PACK0166_JOHNNY_FIGHT_STATIC
    _small_model: type[NPC] = JohnnySmall
    _big_model: type[NPC] = JohnnyLarge
    _statue: type[NPC] = JohnnyStatue
    _unique_henchmen: list[type[Henchman]] = [
        JohnnyBandanaBlue,
        JohnnyBandanaBlue,
        JohnnyBandanaBlue,
        JohnnyBandanaBlue,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [JohnnyBandanaRed]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JOHNNY: Matey, it'd be mighty fun\n to spar again, but I'm tryin' to\n sleep now.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Good job, matey... But ye gotta\n fight me first if ye wanna be let\n through![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,\n[await][page]\n Knowin' you, knocking down\n `SEASIDE_BOSS` was a breeze.[await]\n\n By the way, my pirates saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n It's probably one of \n `FINAL_BOSS_NAME`[await]\n Well, my gills are failing on me,\n so I'll be heading back down.\n Drop in when you have time, okay?[await][page]\n\n                         Your true mate,\n             Jonathan "Johnny" Jones[await]""",
        DI2061_HEAD_CHEF: """PIRATE: Y'arr, don't ye think\n this cake here be lookin' just like\n Johnny?[await]""",
        DI2062_APPRENTICE_CHEF: """PIRATE: Us pirates are pretty\n good with food, arr harr![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JOHNNY: Found [0x7000] item(s, eh? Arr,\n harr, harr...! You gotta find [0x7024]\n more, matey![await]""",
        DI2560_TOWER_HENCHMAN_1: """PIRATE: Welcome, matey![await][pause] Here to\n spar with Johnny, are ye?[await][page]\n Arr, good fun! Let's have a\n warm-up round![await]""",
        DI2572_TOWER_HENCHMAN_2: """PIRATE: This ain't the corner you\n want, matey![await][pause] But while you're here,\n let's have a spar, arr harr![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n        JOHNNY: Ahoy, matey![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome, matey! How'd ya like to\n stay here tonight, on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two fellas o'er in the left\n building have been actin' weird.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ It ain't always easy gettin' into\n the Sea.[await][pause] Ya might need to do\n somethin' else, first![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have ye been to visit Johnny up\n on the hill yet, matey?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Arr, what ye be doin' in our town?\n Just stay away from the shed,\n ya hear?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Out in yonder Sunken Ship, there\n be a... er...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ A treasure chest, behind a big\n stack o' boxes! Don't forget about\n it, matey![await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ If ye can tough it out through the\n ship, you can come back here for\n some... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Come back here for some FUN,\n arr harr! Ya got that, matey?![await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """\n       I just be shoppin', matey.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Read my lips... WE AIN'T LETTIN'\n YA THROUGH![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n You ain't gettin in here! It's ours![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JOHNNY: Good luck, matey. The dojo\n master's mighty tough.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """PIRATE: I know there be some fine\n loot in this tower, but it's too far\n 'bove sea level for my liking![await]""",
        DI3073_TOWER_HENCHMAN_3: """PIRATE: I'll make ya see stars,\n arr harr![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arr-this and Matey-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JOHNNY: Matey, I've got lots o'\n training to do![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """JOHNNY: Matey, I've got lots o'\n training to do![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 552


class YaridovichBoss(Boss):
    """Yaridovich boss fight"""

    _name: str = "Yaridovich"
    _letter_seaside_boss_name: str = "Yarid"
    _letter_volcano_boss_name: str = "some conspicuous toads circling"
    _letter_final_boss_name: str = "Yaridovich's spies."
    _pack_number: int = PACK0180_YARIDOVICH_FIGHT_STATIC
    _small_model: type[NPC] = FakeElder
    _big_model: type[NPC] = YaridOverworld
    _attack_model: type[NPC] = YaridovichLarge
    _statue: type[NPC] = YaridovichStatue
    _unique_henchmen: list[type[Henchman]] = [
        YaridovichHenchman,
        YaridovichHenchman,
        YaridovichHenchman,
        YaridovichHenchman,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [YaridovichHenchman]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """YARIDOVICH: How could I lose to\n those...[delay] Huh? Hey, get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Eee hee hee! So, you've cracked the\n code... Now, it's time for the\n REAL test![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Yaridovich's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n YARIDOVICH!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """YARIDOVICH: Ridiculous! How could a\n genius like me lose to them...?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """YARIDOVICH: I'm thinking it might\n be time for me to switch careers.[await][page]\n Say, do you happen to know anyone\n who's looking to hire a\n hydrodemolitions expert?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """YARIDOVICH: This is just adding\n insult to injury![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,\n[await][page]\n By now, you've certainly defeated\n `SEASIDE_BOSS`, I think!\n[await]\n My “Toad” spies tell me they saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I suspect they're one of \n `FINAL_BOSS_NAME`\n Give'em “the Tickler” from me![await]\n My joints are starting to rust,\n so I'll be headin' back down.\n Stop by whenever you need[await]\n something unsavory, okay?[await][page]\n\n                   Your confidant,\n                         Yaridovich[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """TOWNSPERSON: Hop on... then trampoline... in the next room.\n It'll take you... outside.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ My disguise was as see-through[await]\n as this glass of Motor Oil!![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        DI2061_HEAD_CHEF: """TOWNSPERSON: We must... make\n this cake... look exactly...\n like Yaridovich.[await]""",
        DI2062_APPRENTICE_CHEF: """TOWNSPERSON: We need... more\n fondant.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """YARIDOVICH: Eee hee...! You're\n still missing [0x7024] item(s)! Isn't that\n a shame?[await]""",
        DI2560_TOWER_HENCHMAN_1: """TOWNSPERSON: I'm just... a\n secretary. Don't bother...\n Yaridovich.[await]""",
        DI2572_TOWER_HENCHMAN_2: """TOWNSPERSON: This is...not...\n the right...way.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """YARIDOVICH: A challenge from the\n dojo master? [delay]Eee hee hee, this\n ought to be interesting![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Eee hee...! You want to fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """TOWNSPERSON: It's nice...\n outside.[await]""",
        DI3073_TOWER_HENCHMAN_3: """TOWNSPERSON: You want...to\n fight?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Brownie-this and Tickle-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """YARIDOVICH: I guess I wasn't as\n strong as I thought...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """YARIDOVICH: I guess I wasn't as\n strong as I thought...[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """TOWNSPERSON: Well done...\n You may go on... to Yaridovich.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """TOWNSPERSON: You won...\n Well done...[await]""",
    }

    _item_id: int = 553


class MokuraBoss(Boss):
    """Mokura boss fight"""

    _name: str = "Mokura"
    _letter_volcano_boss_name: str = "a noxious cloud floating"
    _letter_final_boss_name: str = "Mokura's collective."
    _pack_number: int = PACK0207_MOKURA_BOSS_STATIC
    _statue: type[NPC] = MokuraStatue
    _small_model: type[NPC] = MokuraCloud
    _big_model: type[NPC] = MokuraLarge
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n     MOKURA: Uhh... Go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """\n             Duh, huh, huh...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Mokura's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped MOKURA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n            MOKURA: Hmm...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MOKURA: What're you doing in my\n secret lair?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MOKURA: I oughta go back to\n being invisible...[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Mmm...uhhh. Cotton Candy![await]\n ...It's...so...airy...YUM![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n ...Is this invisible ink?\n[await][page]\n \n (Defeated `SEASIDE_BOSS`.  Good.)[await]\n\n (Sensed...\n `VOLCANO_BOSS_DESCRIPTION`\n near volcano...)[await]\n (Ethereal bond with\n `FINAL_BOSS_NAME`).[await]\n\n This last part just reeks of\n flatulence... [await][page]\n\n           \n                                (Mokura)[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big cloud! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MOKURA: Uhh... You need [0x7024] more\n item(s)...[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Mokura's busy right now, so he[1] can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Mokura.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n       MOKURA: Mwa, ha, ha![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Mokura...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MOKURA: Uhh... Are you... gonna\n beat the Dojo Master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Uhh... Hi there.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Secret-this and Gas-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n    MOKURA: Clouds can't jump...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n    MOKURA: Clouds can't jump...[await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 554


class Belome2Boss(Boss):
    """Belome 2 boss fight"""

    _name: str = "Belome"
    _letter_volcano_boss_name: str = "a hungry dog walking"
    _letter_final_boss_name: str = "Belome's clones."
    _pack_number: int = PACK0169_BELOME2_FIGHT_STATIC
    _small_model: type[NPC] = Belome2Small
    _big_model: type[NPC] = Belome2Large
    _statue: type[NPC] = SmallBelomeStatue
    _repeatable_henchmen: list[type[Henchman]] = [
        Belome2MarioClone,
        Belome2MallowClone,
        Belome2GenoClone,
        Belome2BowserClone,
        Belome2PeachClone,
    ]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n        BELOME: Good night~![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Belome's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BELOME: Oh, you're back![await]\n Did you bring any food?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Woof, I ate too many Mallows~![await]\n I should wash it down with Tonic~![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """It's a damp, slimy, looking note (did `SEASIDE_BOSS` LICK this?).\n[await][page]\nA paw print and a crudely drawn image of `VOLCANO_BOSS_DESCRIPTION`\nis etched on the paper.\nThis is probably one of \n`FINAL_BOSS_NAME`'s henchmen!\n`SEASIDE_BOSS` likely headed down to\nfind more snacks,\nso it's time to move on.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Belome.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BELOME: It's dreadfully boring\n around here~![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you the pizza delivery person?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}
    _unique_henchmen: list[Henchman] = []

    _item_id: int = 555


class JaggerBoss(Boss):
    """Jagger boss fight"""

    _name: str = "Jagger"
    _letter_volcano_boss_name: str = "a turtle shoulder-charging"
    _letter_final_boss_name: str = "Jagger's compatriots."
    _pack_number: int = PACK0189_JAGGER_FIGHT_STATIC
    _small_model: type[NPC] = Terrapin
    _statue: type[NPC] = TerrapinStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JAGGER: It'd be fun to fight\n again, but I need a nap.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Wow, you figured out the\n password! Come on in and let's\n have a spar![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jagger's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JAGGER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """JAGGER: Wow, what a fight! I\n better think about what I'm gonna\n do to win next time...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JAGGER: Welcome back! I've been\n training hard for our next fight,\n whenever that may be![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JAGGER: `MAIN_CHARACTER_NAME`, I can't\n jump as high as you. Is this\n really necessary?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ My Sensei's drink is gross...[await]\n Here, my Black Tea is WAY better.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hi `MAIN_CHARACTER_NAME`!\n[await][page]\n I saw you give the business to\n `SEASIDE_BOSS`! It was\n a shell of a good hit!! [await]\n While out training, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I hear they run with\n `FINAL_BOSS_NAME`\n I hope you've been practicing your[await]\n timed blocks! I'll know the next\n time I use terrapunch on you![await][page]\n\n                          You can do it!\n                                    Jagger[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big turtle! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JAGGER: Oh, wow, you've already\n found [0x7000] item(s)![await][pause] I bet you'll find\n the last [0x7024] in no time.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jagger's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jagger.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\nJAGGER: Hi, `MAIN_CHARACTER_NAME`![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jagger...\n in his house. He is...the most\n respected person here.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello. May I help you?[await]\n  [select] (Let's fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Sensei-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """JAGGER: Sensei, the new regimen\n will strengthen us, right?[await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 556


class Jinx1Boss(Boss):
    """Jinx 1 boss fight"""

    _name: str = "Jinx"
    _letter_volcano_boss_name: str = "a small figure blinking"
    _letter_final_boss_name: str = "Jinx's students."
    _pack_number: int = PACK0178_JINX1_FIGHT_STATIC
    _small_model: type[NPC] = Jinx1
    _statue: type[NPC] = JinxStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JINX: Please do not disturb me.\n I am training in here.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   JINX: I was going easy on you![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JINX: I must accept that I have been\n bested. Good work![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JINX: Yes, I am short! Show a little\n respect![await]""",
        DI1782_SHIP_BOSS_DRINK: """ We're warming up `MAIN_CHARACTER_NAME`![await]\n But first, a Green Tea break![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you mastered your training\n with `SEASIDE_BOSS`?\n[await]\n I sense your next challenge is\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They battle in the old style of \n `FINAL_BOSS_NAME`\n Complete this task, and you will[await]\n be prepared for our rematch.\n Fail, and you need not ever show\n your face on my ship again. There[await]\n are some promising turtles here. [await][page]\n\n                       Fight with honor,\n                                      Jinx[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jinx.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n               JINX: Hmm...[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JINX: Master!\n Share your wisdom with us![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 557


class Jinx2Boss(Boss):
    """Jinx 2 boss fight"""

    _name: str = "Jinx"
    _letter_volcano_boss_name: str = "a small figure blinking"
    _letter_final_boss_name: str = "Jinx's students."
    _pack_number: int = PACK0187_JINX2_FIGHT_STATIC
    _small_model: type[NPC] = Jinx2
    _statue: type[NPC] = JinxStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JINX: Please do not disturb me.\n I am training in here.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   JINX: I was going easy on you![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JINX: I must accept that I have been\n bested. Good work![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JINX: Yes, I am short! Show a little\n respect![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Well-fought, `MAIN_CHARACTER_NAME`![await]\n I've some Jasmine Tea for this day![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you mastered your training\n with `SEASIDE_BOSS`?\n[await]\n I sense your next challenge is\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They battle in the old style of \n `FINAL_BOSS_NAME`\n Complete this task, and you will[await]\n be prepared for our rematch.\n Fail, and you need not ever show\n your face on my ship again. There[await]\n are some promising turtles here. [await][page]\n\n                       Fight with honor,\n                                      Jinx[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jinx.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n               JINX: Hmm...[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JINX: Master!\n Share your wisdom with us![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 558


class Jinx3Boss(Boss):
    """Jinx 3 boss fight"""

    _name: str = "Jinx"
    _letter_volcano_boss_name: str = "a small figure blinking"
    _letter_final_boss_name: str = "Jinx's students."
    _pack_number: int = PACK0188_JINX3_FIGHT_STATIC
    _small_model: type[NPC] = Jinx3
    _statue: type[NPC] = JinxStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JINX: Please do not disturb me.\n I am training in here.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   JINX: I was going easy on you![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JINX: I must accept that I have been\n bested. Good work![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JINX: Yes, I am short! Show a little\n respect![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Hail, Master `MAIN_CHARACTER_NAME`![await]\n Let us celebrate with Matcha![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you mastered your training\n with `SEASIDE_BOSS`?\n[await]\n I sense your next challenge is\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They battle in the old style of \n `FINAL_BOSS_NAME`\n Complete this task, and you will[await]\n be prepared for our rematch.\n Fail, and you need not ever show\n your face on my ship again. There[await]\n are some promising turtles here. [await][page]\n\n                       Fight with honor,\n                                      Jinx[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jinx.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n               JINX: Hmm...[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JINX: Master!\n Share your wisdom with us![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 559


class CulexBoss(Boss):
    """Culex boss fight"""

    _name: str = "Culex"
    _letter_volcano_boss_name: str = "an ethereal knight gliding"
    _letter_final_boss_name: str = "Culex's travelers."
    _pack_number: int = PACK0216_CULEX_BOSS_STATIC
    _small_model: type[NPC] = CulexSmall
    _big_model: type[NPC] = CulexLarge
    _statue: type[NPC] = CulexStatue
    _unique_henchmen: list[type[Henchman]] = [
        CulexFireCrystal,
        CulexWaterCrystal,
        CulexEarthCrystal,
        CulexWindCrystal,
    ]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CULEX: Please do not attempt to\n crack this egg again.[await][page]\n It will not give you thousands of\n experience points.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ You have passed the first test.\n But you're not finished yet!\n Please enter.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Culex's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped CULEX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CULEX: This world truly is\n uninhabitable for me and my kind...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CULEX: Greetings. It is good to\n make your acquaintance once\n again.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CULEX: This is not the encounter In expected when I came to visit this\n world.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ How droll, my crystals shattered.[await]\n I've only Bacchus Wine remaining.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """WATER CRYSTAL: I guess this is as\n close as I'll get to being returned\n to Mysidia.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings, honored Warrior.\n[await][page]\n I have witnessed you do battle with\n `SEASIDE_BOSS`. \n I am impressed, but not surprised.[await]\n In my travels of your world, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n The crystals revealed they are \n `FINAL_BOSS_NAME`\n I know not your path to victory, \n but challenge awaits you there. \n I must return to the sea, lest the\n fragile water crystal shatter.[await][page]\n\n                       Fight with honor,\n                                     Culex[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """EARTH CRYSTAL: I thought the\n Dark Elf was a bit strange, until\n we came to this world.[await]\n You truly have some characters\n here![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FIRE CRYSTAL: Of course I'm\n miserable! We're UNDERWATER![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """WIND CRYSTAL: Culex is nice and\n all, but I miss Yang sometimes.[await]""",
        DI2061_HEAD_CHEF: """FIRE CRYSTAL: We needed a lot of\n heat to bake a cake of this size.[await]""",
        DI2062_APPRENTICE_CHEF: """WATER CRYSTAL: We must shape\n this confection to resemble Culex.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CULEX: You must retrieve [0x7024] more\n item(s) before we may proceed.[await]\n Godspeed, champion knight![await]""",
        DI2560_TOWER_HENCHMAN_1: """FIRE CRYSTAL: Greetings.[await][pause] Culex\n is making preparations to head\n back to his home world.[await][pause] He's\n busy right now.[await][page]\n Please come back later...\n [delay]unless you want to get hurt![await]""",
        DI2572_TOWER_HENCHMAN_2: """WIND CRYSTAL: You are not going\n to find what you're seeking back\n here.[delay] Stay out.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n           CULEX: Good day.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome to our inn.[await]\n We are offering a competitive price\n of zero coins per night.[await]\n Will you be staying tonight?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Culex's\n house up on the hill yet?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """FIRE CRYSTAL: This area is\n off-limits.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """WATER CRYSTAL: This door is a...\n uh... portal to another dimension!\n We can't let you fall into it.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CULEX: It will be quite difficult to\n claim victory over the dojo master.\n I wish you luck.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """EARTH CRYSTAL: Wind Crystal\n really should have been the one\n standing guard all the way up here.[await]""",
        DI3073_TOWER_HENCHMAN_3: """EARTH CRYSTAL: Stand back!\n I might know Sandstorm![await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """CRYSTAL: Proceed forth. Culex\n awaits you.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """CRYSTAL: Well met! You have\n satisfied Culex's hunger for a\n true challenge.[await]""",
    }
    _repeatable_henchmen: list[Henchman] = []

    _item_id: int = 560


class BoxBoyBoss(MimicBoss):
    """Box Boy boss fight"""

    _name: str = "Box Boy"
    _letter_volcano_boss_name: str = "a grey box sliding about"
    _letter_final_boss_name: str = "Box Boy's monsters."
    _pack_number: int = PACK0158_BOXBOY_FIGHT_STATIC
    _small_model: type[NPC] = BoxBoySmall
    _big_model: type[NPC] = BoxBoyLarge
    _statue: type[NPC] = MimicStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOX BOY: How many times are you\n gonna wake me up? Get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, you're gonna PAY for waking\n me up like this![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Box Boy's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOX BOY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n    BOX BOY: You just got lucky![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """\n   BOX BOY: This place is boring.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOX BOY: You sure you wanna jump\n on me? I counter special attacks.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ You don't even deserve to LOOK at[await]\n My 1990 Comanee-Ronti Pinot Noir![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Trespassers BEWARE:\n[await][page]\n Loitering Prohibited (yes, you too\n `SEASIDE_BOSS`!)\n[await]\n Don't think I didn't see\n `VOLCANO_BOSS_DESCRIPTION`\n either, keep to your volcano.[await]\n We all know what happened to\n `FINAL_BOSS_NAME`\n the last time they showed up here.\n Also, I expect SILENCE.  No spells.\n Casting a spell is a good way to\n get blasted.  You've been warned.[await][page]\n\n             Now, GET OFF MY LAWN!!\n                                  Box Boy[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOX BOY: Still missing [0x7024] item(s)?\n Pathetic![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Box Boy's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Box Boy.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BOX BOY: What'd you come here\n for?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Box Boy...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOX BOY: The dojo master's gonna\n kick your butt![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ This'd BETTER be important![await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOX BOY: Ahh, you're not so\n tough![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOX BOY: Ahh, you're not so\n tough![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 561


class MegaSmilaxBoss(Boss):
    """Megasmilax boss fight"""

    _name: str = "Megasmilax"
    _letter_seaside_boss_name: str = "the Plant"
    _letter_volcano_boss_name: str = "an invasive plant spreading"
    _letter_final_boss_name: str = "Megasmilax's seedlings."
    _pack_number: int = PACK0173_MEGASMILAX_FIGHT_STATIC
    _small_model: type[NPC] = PiranhaPlant
    _big_model: type[NPC] = Megasmilax
    _statue: type[NPC] = PiranhaPlantStatue
    _repeatable_henchmen: list[type[Henchman]] = [MegaSmilaxPiranha]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MEGASMILAX: I'm thirsty.[await][pause] Can you\n ask Shy Away to come back here,[delay]\n please?[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Hm?[delay_30] Not often we get visitors\n down here.[delay_30] Come in...[delay_60]\n at your own risk, that is![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Megasmilax's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n MEGASMILAX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n      MEGASMILAX: I'm thirsty.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MEGASMILAX: You'd think it\n wouldn't be so difficult to get\n watered around here, when we're\n literally underwater.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MEGASMILAX: Careful. I have sharp\n teeth.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Go ahead, just add Water![await]\n Cha-Cha-Cha-Chia!  La Dee Dah~![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """SMILAX: I guess salt water\n wouldn't be very good for us.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n I'm still salivating over your battle\n with `SEASIDE_BOSS`.[await]\n I must taste its umami someday...\n I've heard through the vine about\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They must be part of the\n underground network of \n `FINAL_BOSS_NAME`[await]\n My offer to have you for dinner\n stands. I must return to my roots.[await][page]\n\n                             Stay hungry,\n                              Megasmilax[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """SMILAX: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """SMILAX: I guess salt water\n wouldn't be very good for us.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """SMILAX: I guess salt water\n wouldn't be very good for us.[await]""",
        DI2061_HEAD_CHEF: """SMILAX: We're making this cake\n in honour of Megasmilax.[await]""",
        DI2062_APPRENTICE_CHEF: """SMILAX: I hope the wedding party\n likes it. If they don't...[delay] well,[delay]\n they DID hire plants to bake a cake.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MEGASMILAX: Hm?[await]\n [0x7024] more item(s)?[await]\n Don't ask me.[delay] I'm just a plant.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SMILAX: Hello there. Are you the\n gardener?[await][page]\n No?[await][pause] Well, [delay]we didn't call for a\n plumber today... [await][pause]]I better get you\n outta here![await]""",
        DI2572_TOWER_HENCHMAN_2: """SMILAX: If you didn't come back\n here to water us, you'd better get\n outta here.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n         MEGASMILAX: Hmm...[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello there. Are you tired?\n We don't charge any fees here,\n if you'd like to stay.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Megasmilax's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Welcome to our humble little town.\n You're welcome to stick around,\n but keep away from the shed, OK?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I'm shopping for some fertilizer.[await]\n [delay]...Don't give me that look!\n [delay]I'm just a plant![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There's nothing suspicious going on\n in here.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ We're just two plants growing in\n front of an abandoned door. ...But\n we're not letting you in.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MEGASMILAX: I would love to\n watch your match with the dojo\n master.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You don't look like the gardener...[await]\n  [select] (I'm here to fight you)\n  [select] (Oops, my mistake)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """\n          SMILAX: I'm thirsty.[await]""",
        DI3073_TOWER_HENCHMAN_3: """\n       SMILAX: Careful, I bite.[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Water-this and Fertilizer-that.[await]\n ...[delay]Actually, [delay]that doesn't sound\n so bad![await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MEGASMILAX: This is harder than it\n looks. I'm a plant.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MEGASMILAX: This is harder than it\n looks. I'm a plant.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """SMILAX: Go on ahead to visit\n Megasmilax. But be warned, he's\n pretty tough when he's hydrated.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """SMILAX: Wow, you won![await][pause] Shy Away\n must have watered you more than\n he watered Megasmilax.[await]""",
    }
    _unique_henchmen: list[Henchman] = []

    _item_id: int = 562


class DodoBoss(Boss):
    """Dodo boss fight"""

    _name: str = "Dodo"
    _letter_volcano_boss_name: str = "a large bird flapping about"
    _letter_final_boss_name: str = "Dodo's flock."
    _pack_number: int = PACK0208_DODO_BOSS_STATIC
    _small_model: type[NPC] = DodoSmall
    _big_model: type[NPC] = DodoLarge
    _statue: type[NPC] = DodoStatue
    _dialog_replacements: dict[int, str] = {
        # actually, don't use dialogs for dodo, just play sfx... how to handle this?
        # time this according to how long the feather sound effect is
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: EMPTY_DIALOG,
        DI1660_SHIP_PASSWORD_COMPLETE: EMPTY_DIALOG,
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Dodo's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped DODO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: EMPTY_DIALOG,
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: EMPTY_DIALOG,
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: EMPTY_DIALOG,
        DI1782_SHIP_BOSS_DRINK: """ (Dodo stares at a Hot Chocolate)[await]\n ...Please don't tell Valentina.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Dear `MAIN_CHARACTER_NAME`,\n[await][page]\n I saw your incredible battle with\n `SEASIDE_BOSS`!\n[await]\n At the "Tanning Salon", I saw \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano. [await]\n Valentina referred to them as\n `FINAL_BOSS_NAME`\n Look, I actually think you're cool,\n and I'm learning my Multistrike\n timing from our battles... But...\n I can't leave her. She needs me. I\n hope you understand.[await][page]\n\n                       Your biggest fan,\n                                      Dodo[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big bird! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """    Dodo is a bird of few words.[await]\n    You still have [0x7024] item(s) left\n                 to find.[await]""",  # use async for this one too
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Dodo's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Dodo.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: EMPTY_DIALOG,
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Dodo...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: EMPTY_DIALOG,
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """[delay_60][await]\n  [select] (I'm here for a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n I never hear the guy next door.[await]\n Maybe he can't talk.[await][page]\n I'd like to go over and introduce\n myself sometime, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: EMPTY_DIALOG,
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: EMPTY_DIALOG,
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 563


class BirdettaBoss(Boss):
    """Birdetta boss fight"""

    _name: str = "Birdetta"
    _letter_volcano_boss_name: str = "a giant egg rolling"
    _letter_final_boss_name: str = "Birdetta's bad eggs."
    _pack_number: int = PACK0175_BIRDETTA_FIGHT_STATIC
    _small_model: type[NPC] = BirdettaSmall
    _big_model: type[NPC] = BirdettaLarge
    _statue: type[NPC] = BirdettaStatue
    _unique_henchmen: list[type[Henchman]] = [
        BirdettaEggbert,
        BirdettaEggbert,
        BirdettaEggbert,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [BirdettaEggbert]
    _dialog_replacements: dict[int, str] = {
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, yay, you've come to play!\n Come on in~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Birdetta's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n BIRDETTA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BIRDETTA: Tee hee! Let's play\n again sometime♥![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BIRDETTA: Oh, you didn't forget\n about me! You're so sweet♥![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BIRDETTA: This isn't what I had in\n mind when I said I wanted to play![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Thanks for playing with me~![await]\n I lost, but I made Yoshi's Eggnog♥![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n HI `MAIN_CHARACTER_NAME`♥!\n[await][page]\n Did `SEASIDE_BOSS` submit to\n the power of HUGS?!♥\n[await]\n While doing some incubating, I saw \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n My eggies♥ think they scramble with\n `FINAL_BOSS_NAME`\n My lovelies♪ and I have to get back[await]\n to the ship, and the bouyant forces\n of seawater aren't helping.\n Stop by again soon♥! [await][page]\n\n                           ♥XO♥XO♥XO♥\n                                  Birdetta[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """EGGBERT: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI2061_HEAD_CHEF: """EGGBERT: We're making this cake\n look just like Birdetta![await]""",
        DI2062_APPRENTICE_CHEF: """EGGBERT: No eggs were harmed\n in the making of this cake.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BIRDETTA: Hello♥![await]\n ...Oh, no, you're still missing\n [0x7024] item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """EGGBERT: Birdetta's feeling lonely\n today, so feel free to pay her a\n visit upstairs.[await][pause] I'm sure she'd love\n the company.[await][page]\n Just, let me make sure you'll be\n nice, first![await]""",
        DI2572_TOWER_HENCHMAN_2: """EGGBERT: Pardon me, Birdetta's\n not back here. Please refrain from\n snooping around.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n          BIRDETTA: Hello♥![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello! You've been chosen to stay\n here in our lovely inn for FREE!\n Aren't you lucky?[await]\n Will you stay with us?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Birdetta's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hi![delay] Welcome to our town![delay]\n Stay away from our shed, OK~?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Do you think they sell frying pans\n here?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ It's perfectly normal for two eggs\n to stand outside a locked house![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There's nothing weird going on\n here![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BIRDETTA: Ooh, are you gonna play\n with the dojo master?![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello♥! Did you come to play?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """EGGBERT: What did Birdetta want\n me to do here, again? I'm just an\n egg![await]""",
        DI3073_TOWER_HENCHMAN_3: """EGGBERT: You're making me so\n mad, I could explode![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She's always mumbling about\n Egg-this and Playtime-that.[await][page]\n Sometimes I'd like to ask her what\n she's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BIRDETTA: Thanks for playing with\n me~![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BIRDETTA: Thanks for playing with\n me~![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """EGGBERT: Wow, you sure showed\n us! Don't disappoint Birdetta![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """EGGBERT: Thanks for playing\n with us today![await]""",
    }

    _item_id: int = 564


class ValentinaBoss(Boss):
    """Valentina boss fight"""

    _name: str = "Valentina"
    _letter_volcano_boss_name: str = "a bossy lady being carried"
    _letter_final_boss_name: str = "Valentina's little birds."
    _pack_number: int = PACK0171_VALENTINA_FIGHT_STATIC
    _small_model: type[NPC] = ValentinaSmall
    _big_model: type[NPC] = ValentinaLarge
    _repeatable_henchmen: list[type[Henchman]] = [ValentinaBluebird, ValentinaBirdy]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """VALENTINA: ...What? You're STILL\n here?! Go AWAY!!![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ ALRIGHT, already![delay_30] If you're going\n to annoy me like this, get in here\n and finish the job![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Valentina's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n VALENTINA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """VALENTINA: If you don't stop\n bothering me, I'm going to turn\n your mustache into a\n vegetable scrubber![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """VALENTINA: YOU again?! You better\n have brought some margaritas![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """VALENTINA: Get OFF of my head\n before I take your shoes and throw\n them in the ocean!!![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Pfffft!  You call THIS a Martini?[await]\n MAKE IT AGAIN, and I MIGHT tip!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To whom it may concern,\n[await][page]\n Make sure that pesky\n `SEASIDE_BOSS`, is gone\n by the time I get back.[await]\n\n A little birdy told me they saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.  Gross.[await]\n I cannot abide any more of \n `FINAL_BOSS_NAME`\n They're all beneath me.  Literally.[await]\n Well, I've got a ship full of idiots\n to command.  Don't call, I have a\n boyfriend.  His name is...Booster.[await][page]\n\n                       NOT yours,\n                         Valentina[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """BLUEBIRD: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI2061_HEAD_CHEF: """ Why are we making a cake that\n looks like Valentina, again?[await]""",
        DI2062_APPRENTICE_CHEF: """ We're making a cake that looks like\n Valentina.[await][pause] What else are we gonna\n do on our day off?[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """VALENTINA: STOP BOTHERING ME![await]\n If you need something to do, go\n look for [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """BLUEBIRD: I hate being a secretary!\n And... [delay_30]I'm going to make this\n your problem![await]""",
        DI2572_TOWER_HENCHMAN_2: """BLUEBIRD: Whaddya want?[await][pause] You\n better not be trying to bother\n Valentina, [delay]or I'll be in trouble![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n   VALENTINA: I'm SO frustrated![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome![delay] I'll let you stay here for\n free, but don't tell Valentina.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Valentina's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hmm...[delay] What're you loitering\n around here for?[delay] Uh...[delay] Stay away\n from the shed, OK?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ ...I'm on my break. [delay]Just let me\n shop in peace, OK?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n     You can't just barge in here![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n         Hey! Who're YOU?!...[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """VALENTINA: You? Fighting the dojo\n master? Good luck, chump![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What? What do you want?![await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """BLUEBIRD: Valentina only gives us\n the most boring jobs to do...[await]""",
        DI3073_TOWER_HENCHMAN_3: """\nBLUEBIRD: I'm bored. Entertain me![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She's always mumbling about\n Queen-this and Dodo-that.[await][page]\n Sometimes I'd like to ask her what\n she's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """VALENTINA: Is this REALLY going to\n make me powerful enough to take\n ov...[delay_30] I mean...[await][pause][delay_30] pay a cordial visit\n to Nimbus Land?![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """VALENTINA: Is this REALLY going to\n make me powerful enough to take\n ov...[delay_30] I mean...[await][pause][delay_30] pay a cordial visit\n to Nimbus Land?![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BLUEBIRD: Whatever, go on and\n fight Valentina. She doesn't pay\n us enough to keep you out.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BLUEBIRD: Oh, you won?[await]\n [delay_30](...[delay_30]It's about time!)[await]""",
    }
    _unique_henchmen: list[Henchman] = []

    _item_id: int = 565


class CzarBoss(Boss):
    """Czar Dragon boss fight"""

    _name: str = "Czar Dragon"
    _letter_seaside_boss_name: str = "the Dragon"
    _letter_volcano_boss_name: str = "a huge dragon blazing"
    _letter_final_boss_name: str = "the Czar Dragon's spawn."
    _pack_number: int = PACK0172_CZAR_FIGHT_STATIC
    _small_model: type[NPC] = CzarDragonSmall
    _big_model: type[NPC] = CzarBody
    _attack_model: type[NPC] = CzarDragonLarge
    _statue: type[NPC] = CzarStatue
    _repeatable_henchmen: list[type[Henchman]] = [CzarPyrosphere]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n    CZAR DRAGON: BLARRGGGG[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ BLARRGGGG[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Czar Dragon's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the CZAR DRAGON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n    CZAR DRAGON: BLARRGGGG[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """\n    CZAR DRAGON: BLARRGGGG[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n    CZAR DRAGON: BLARRGGGG[await]""",
        DI1782_SHIP_BOSS_DRINK: """ FIIIIIIIRRRRREEEEBAAAALLLLLLLL[await]\n WHISSSSSSSSSKEEEEEEEEEEEEY!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: EMPTY_DIALOG,
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: EMPTY_DIALOG,
        DI1786_LETTER_FROM_SHIP_BOSS: """ As you approach, Czar Dragon's\n pyrospheres become ablaze...\n[await][page]\n The flames dance, depicting your\n battle with `SEASIDE_BOSS`;\n the image fades into flames.[await]\n A new image comes to life,\n `VOLCANO_BOSS_DESCRIPTION`\n next to a volcano.[await]\n The flames become an ash patern of\n `FINAL_BOSS_NAME`\n The ash is carried by the wind \n toward the sun, reigniting the\n pyrospheres as the fall into the sea\n fading into darkness...[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: EMPTY_DIALOG,
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: EMPTY_DIALOG,
        DI2061_HEAD_CHEF: EMPTY_DIALOG,
        DI2062_APPRENTICE_CHEF: EMPTY_DIALOG,
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CZAR DRAGON: BLARRGGGG[await]""",  # can we make him say BLARG as many times as you have items remaining?
        DI2560_TOWER_HENCHMAN_1: EMPTY_DIALOG,
        DI2572_TOWER_HENCHMAN_2: EMPTY_DIALOG,
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n  CZAR DRAGON: BLAAARRRGGGG[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ (Stay in the inn for free?)[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: EMPTY_DIALOG,
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: EMPTY_DIALOG,
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: EMPTY_DIALOG,
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: EMPTY_DIALOG,
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: EMPTY_DIALOG,
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: EMPTY_DIALOG,
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: EMPTY_DIALOG,
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: EMPTY_DIALOG,
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: EMPTY_DIALOG,
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: EMPTY_DIALOG,
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: EMPTY_DIALOG,
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n  CZAR DRAGON: BLAAARRRGGGG[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """[delay_60][await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: EMPTY_DIALOG,
        DI3073_TOWER_HENCHMAN_3: EMPTY_DIALOG,
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always yelling about\n BLARRRRG-this and\n BLAHGAHRGGH-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n  CZAR DRAGON: BLAAARRRGGGG[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n  CZAR DRAGON: BLAAARRRGGGG[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: EMPTY_DIALOG,
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: EMPTY_DIALOG,
    }
    _unique_henchmen: list[Henchman] = []

    _item_id: int = 566


class AxemRangersBoss(Boss):
    """Axem Rangers boss fight"""

    _name: str = "Axem Red"
    _letter_seaside_boss_name: str = "the Axems"
    _letter_volcano_boss_name: str = "a huge AX flying around"
    _letter_final_boss_name: str = "the Axem Rangers' stooges."
    _pack_number: int = PACK0182_AXEM_FIGHT_STATIC
    _forced_background = Battlefields.AXEM_RANGERS
    _small_model: type[NPC] = AxemRed
    _statue: type[NPC] = AxemRedStatue
    _unique_henchmen: list[type[Henchman]] = [
        AxemRangersAxemBlack,
        AxemRangersAxemPink,
        AxemRangersAxemYellow,
        AxemRangersAxemGreen,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [
        AxemRangersMachine1,
        AxemRangersMachine2,
        AxemRangersMachine3,
        AxemRangersMachine4,
        AxemRangersMachine5,
    ]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """AXEM RED: We're busy playing Uno\n in here. Go bother someone else![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Listen up, nerd![delay_30] You may have\n figured out our password, but\n we're not going down without\n a fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Axem Rangers' place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the AXEM RANGERS!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """AXEM RED: How could this happen\n to the Axem Rangers?![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """AXEM RED: Yo! Quit wasting your\n time around here, you've got a\n world to save![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """AXEM RED: Yo, `MAIN_CHARACTER_NAME`!\n This isn't cool!\n Get off of my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Yo! This energy drink is preem![await]\n Axem Red Bull gives me wings![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """AXEM BLACK: Red can be kind of\n a chump when he loses.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """AXEM YELLOW: Say, do you have\n anything to eat?[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """AXEM PINK: I hate it down here!\n The water makes my makeup run![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n yo `MAIN_CHARACTER_NAME`,[await][page]\n hru? fite was zzz, so I went bak\n 2 teh ship 4 a nap. text me when ur\n done w/ `SEASIDE_BOSS`.[await]\n green would not shut up bout\n `VOLCANO_BOSS_DESCRIPTION`\n he saw near teh volcano.[await]\n pink flirted w/ a dood from\n `FINAL_BOSS_NAME`\n black wants 2 punk them, but[await]\n yellow got the squirtz again...\n so we got 2 go chill 4 a bit.  Hit\n me bak l8r. [await][page]\n\n                                     peace\n                                        red[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """AXEM GREEN: The four of them may\n be hot heads, but I truly enjoy\n causing mischief with them.[await]""",
        DI2061_HEAD_CHEF: """AXEM YELLOW: Why the heck do\n I have to bake a cake that I'm\n not going to get to eat?![await]""",
        DI2062_APPRENTICE_CHEF: """AXEM GREEN: Not EVERYTHING\n we do is evil. Today we're baking a\n cake that looks like Axem Red.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """AXEM RED: Listen! You're not\n going anywhere until you find [0x7024]\n more of `MARRYMORE_CHARACTER`'s item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """AXEM BLACK: Green hasn't shown\n up to cover me for lunch yet![await][pause] I'm\n so mad, I could fight somebody![await]""",
        DI2572_TOWER_HENCHMAN_2: """AXEM PINK: Where do you clods\n think you're going?![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """AXEM RED: Listen up![await]\n Quit snooping around town![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """AXEM YELLOW: You tired?[await]\n I'm feeling nice today, so you can\n stay for free.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Axem Red's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ They won't give me a better job\n in this town! I wanted to be one\n of the shed guards![await]\n ...What are they guarding?\n [delay]N-nothing![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Why does HE get to be the\n shopkeeper?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n     AXEM BLACK: Beat it, clod![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """AXEM PINK: Get lost, mustache!\n [delay]This shed belongs to the Axem\n Rangers![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """AXEM RED: Yo! It won't be enough\n to win just once. The dojo master\n has three forms.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Yo! What do you want?![await]\n  [select] (A fight)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """AXEM YELLOW: Man...[delay] I wish\n someone would bring me some food\n up here![await]""",
        DI3073_TOWER_HENCHMAN_3: """\n    AXEM YELLOW: Get lost, bub![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Shades-this and Makeup-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n  AXEM RED: I'm way outta shape![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n  AXEM RED: I'm way outta shape![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 567


class ChesterBoss(MimicBoss):
    """Chester boss fight"""

    _name: str = "Chester"
    _letter_volcano_boss_name: str = "a purple box sliding about"
    _letter_final_boss_name: str = "Chester's monsters."
    _pack_number: int = PACK0159_CHESTER_FIGHT_STATIC
    _small_model: type[NPC] = ChesterSmall
    _big_model: type[NPC] = ChesterLarge
    _statue: type[NPC] = MimicStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CHESTER: Go on, take it. Just let\n me go back to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Quit draggin' your feet! Get in\n here and let's fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Chester's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped \nCHESTER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CHESTER: (How embarrassing...)[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CHESTER: You know, I'm kind of a\n big deal over in Bowser's Keep.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CHESTER: This is unnecessary. Get\n off me![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Leave me alone with my precious[await]\n '92 Napper Cabernet Sauivignon.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`:\n[await][page]\n I'm too old for this nonsense with\n `SEASIDE_BOSS`, good luck.\n[await]\n Just to see if I could, I summoned\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n It seems they're associated with\n `FINAL_BOSS_NAME`\n I've been belching up monsters for\n a LONG time, and I've never seen\n anything this rude. Fix it, and\n I MIGHT forget you opened my box.[await][page]\n\n    Go do something useful for once.\n                                   Chester[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CHESTER: Don't bother me unless\n you have found [0x7024] more item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Chester's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Chester.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CHESTER: This town is pretty\n quiet.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Chester...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n   CHESTER: Now THIS I gotta see.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You're interrupting my sleep.[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Dragon-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n  CHESTER: I don't even have legs![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n  CHESTER: I don't even have legs![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 568


class KamekBoss(Boss):
    """Kamek boss fight"""

    _name: str = "Kamek"
    _letter_volcano_boss_name: str = "a hooded sorceror flying"
    _letter_final_boss_name: str = "Kamek's creations."
    _pack_number: int = PACK0209_MAGIKOOPA_BOSS_STATIC
    _small_model: type[NPC] = RedMagikoopa
    _big_model: type[NPC] = MagikoopaLarge
    _statue: type[NPC] = MagikoopaStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """KAMEK: Normally,[delay] when I\n summon an egg,[delay] it doesn't\n encapsulate me...[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ This..is..my ship!\n Come in..if you dare![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Kamek's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n KAMEK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n  KAMEK: Huh? ...Where am I?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """KAMEK: Oh, yes, I have seen\n `MARIO_NAME`'s twin brother before.\n I can't recall where, though...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """KAMEK: `MAIN_CHARACTER_NAME`, why did you do\n this???[await]""",
        DI1782_SHIP_BOSS_DRINK: """ There's Magic Hat in my magic hat,[await]\n but we're not handing it over to[await]\n the likes of you![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`!\n[await][page]\n Before I could cast a spell, you\n defeated `SEASIDE_BOSS`![await]\n\n Earlier while flying around seeking \n sweet yoshi vengeance, I saw[await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I remember them being one of \n `FINAL_BOSS_NAME`[await]\n I'd better get back to the ship in\n case Yoshi falls into one the pits.[await][page]\n\n     Now you see me, now you don't!\n                                    Kamek[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big wizard! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """KAMEK: You••need••[0x7024] more\n item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Kamek's busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Kamek.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """KAMEK: There's nothing••to\n see••here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Kamek...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n            KAMEK: OH, MY!! [await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Yoshi-this and Bowser-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n KAMEK: Oh, dear... What to do...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n KAMEK: Oh, dear... What to do...[await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 569


class BoomerBoss(Boss):
    """Boomer boss fight"""

    _name: str = "Boomer"
    _letter_volcano_boss_name: str = "a noble soldier marching"
    _letter_final_boss_name: str = "Boomer's soldiers."
    _pack_number: int = PACK0210_BOOMER_BOSS_STATIC
    _small_model: type[NPC] = BoomerSmall
    _big_model: type[NPC] = BoomerOverworld
    _attack_model: type[NPC] = BoomerLarge
    _statue: type[NPC] = BoomerStatue
    _unique_henchmen: list[type[Henchman]] = [BoomerShyGuy, BoomerShyGuy]
    _repeatable_henchmen: list[type[Henchman]] = [BoomerShyGuy]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOOMER: I lost fair and square.[await]\n Now it is time for me to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Ahhhhh... So, it's YOU who solved\n my riddle![delay_30] Now, you've got to deal\n with ME![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Boomer's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOOMER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOOMER: I don't need your\n sympathy! Go on...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOOMER: A true soldier knows\n when to accept defeat. You earned\n your victory.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOOMER: This is absurd! Get off\n of my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Great battle deserves great Sake![await]\n Join me, `MAIN_CHARACTER_NAME`.  Kampai![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """Origami figures sit in silent tableau:\n[await][page]\nOne figure resembles `VOLCANO_BOSS_DESCRIPTION`\nwhile the others appear to be\n`FINAL_BOSS_NAME`\n[await]\nA haiku lays near the figures:\n\nStay strong `MAIN_CHARACTER_NAME`\n[await]\nShow them what discipline means\n[await]\nShred them throughly[await][page]\n\n                   Go in peace,\n                         Boomer[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """CHANDELI-HO: Hop on the\n trampoline in the next room. It'll\n take you outside.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]""",
        DI2061_HEAD_CHEF: """CHANDELI-HO: We're making a cake\n to look just like Boomer![await]""",
        DI2062_APPRENTICE_CHEF: """CHANDELI-HO: We've gotten REAL\n good with fondant![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOOMER: Ha ha ha![delay_30] So, you found\n [0x7000] item(s) already. Impressive.[await][pause] But\n now you've got to find [0x7024] more![await]""",
        DI2560_TOWER_HENCHMAN_1: """CHANDELI-HO: Welcome! Have you\n come to install the chandelier?[await][page]\n ...No?[delay] Well, you'd better leave\n Boomer alone![await]""",
        DI2572_TOWER_HENCHMAN_2: """CHANDELI-HO: I won't let you\n bother Boomer![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BOOMER: Ha ha ha![await][pause] So, you've\n found our village![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hi! Are you tired? You can rest\n up here, and you don't have to\n pay me anything.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Boomer's house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ ...Stay away from the shed, OK?\n It's scary![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I'm upset. There's no candles on\n sale here.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n      Sorry, we can't let you in![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ This is Boomer's top-secret shed![await]\n ...Oh no, was I supposed to tell\n you it's top secret?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOOMER: Ha ha ha! A match\n against the dojo master?!\n This ought to be fun![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Gahahaha! Is it a fight you seek?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """CHANDELI-HO: Whew...[delay] It's weird\n for me to say,[delay] but I think I might\n be afraid of heights.[await]""",
        DI3073_TOWER_HENCHMAN_3: """CHANDELI-HO: I won't let anything\n bad happen to Boomer![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Soldier-this and Honor-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOOMER: You won fair and square!\n But I won't make it so easy for you\n next time![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOOMER: You won fair and square!\n But I won't make it so easy for you\n next time![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """CHANDELI-HO: Oh, no, I lost!\n Good luck, Boomer![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """CHANDELI-HO: I hope you didn't\n hurt Boomer too bad![await]""",
    }

    _item_id: int = 570


class ExorBoss(Boss):
    """Exor boss fight"""

    _name: str = "Exor"
    _letter_volcano_boss_name: str = "a massive sword falling"
    _letter_final_boss_name: str = "Exor's sellswords."
    _pack_number: int = PACK0186_EXOR_FIGHT_STATIC
    _forced_background = Battlefields.EXOR
    _small_model: type[NPC] = ExorSmall
    _statue: type[NPC] = ExorStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """  EXOR: What do you want? Get\n lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Halt! This ship belongs to ME!\n If you want to get through...\n bring it on![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Exor's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped EXOR!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """EXOR: If it weren't for nosey\n characters like you, I could live in\n this ship undisturbed![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """EXOR: Halt! Don't even THINK\n about leaving until you've had\n some of this juice![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """EXOR: Look, if you really want to\n humiliate me, why not use\n Geno Whirl too, while you're at it?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ You think I was MADE this HUGE?![await]\n No, I drank my Milk EVERY DAY!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n HEY!\n[await][page]\n What did you do to\n `SEASIDE_BOSS`?!\n[await]\n Let's see you deal with \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano![await]\n You are no match for us,\n `FINAL_BOSS_NAME`\n Trespass on my chip at your own\n peril!  I will devour you and expel\n your corporeal form in the\n dimmension of bombs and sledges!\n Mind your place, Tiny.[await][page]\n\n    Turn the "Ge" flag on, weakling.\n                                      Exor[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big sword man! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """EXOR: Halt![await][pause] What do you have\n here?[delay] [0x7000] item(s)?[await]\n No, this won't do.[await][pause] Find [0x7024] more,\n[delay] or I won't let you through![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Exor's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Exor.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """EXOR: There isn't much to see in\n this town. Especially not in\n the shed.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Exor...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """EXOR: Think you're gonna beat the\n dojo master? Now this I GOTTA\n see![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Halt! What do you want?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Nosey-this and Trespasser-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n        EXOR: How humiliating![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n        EXOR: How humiliating![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 571


class CountdownBoss(Boss):
    """Count Down boss fight"""

    _name: str = "Count Down"
    _letter_seaside_boss_name: str = "the Clock"
    _letter_volcano_boss_name: str = "a noisy clock winding"
    _letter_final_boss_name: str = "Count Down's friends."
    _pack_number: int = PACK0174_COUNTDOWN_FIGHT_STATIC
    _forced_background = Battlefields.COUNTDOWN
    _small_model: type[NPC] = CountDownGridplane
    _statue: type[NPC] = CountDownStatue
    _unique_henchmen: list[type[Henchman]] = [CountdownDingALing, CountdownDingALing]
    _repeatable_henchmen: list[type[Henchman]] = [CountdownDingALing]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """COUNT DOWN: Sometimes, even an\n alarm clock needs to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ This is not good![delay_30]\n He figured out the password![delay_30]\n ...We better do something![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Count Down's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n COUNT DOWN!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """COUNT DOWN: ...What time is it?\n Time for you to leave![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """COUNT DOWN: What are you still\n doing around here? Taking a break,\n huh?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n   COUNT DOWN: This is not good![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Ahh, fresh squeezed Orange Juice-[await]\n The second best way to wake up![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """DING-A-LING: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """DING-A-LING: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ WAKE UP CALL FOR\n `MAIN_CHARACTER_NAME`!!\n[await][page]\n YOU'RE LATE DEFEATING\n `SEASIDE_BOSS`!!\n[await]\n NEWSFLASH:\n `VOLCANO_BOSS_DESCRIPTION`\n SPOTTED NEAR THE VOLCANO!![await]\n DING-A-LING SOURCES LINK TO \n `FINAL_BOSS_NAME`\n TIME WAITS FOR NO ONE!! \n BETTER NAIL THAT MACK SKIP, \n ROCK CANDY MANIP, BLOCK CLIP\n BACK TO SUNKEN SHIP, YIP!![await][page]\n\n Alarm off  <<<        >>>  Snooze\n                 Countdown[await]""",
        DI2061_HEAD_CHEF: """DING-A-LING: I guess it is a little\n weird to make a cake that looks\n like a clock with no body.[await]""",
        DI2062_APPRENTICE_CHEF: """DING-A-LING: Are you impressed by\n how well we can bake without\n having any hands?[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """COUNT DOWN: You've only got\n [0x7000] item(s)! You're missing [0x7024]![await]\n You better do something![await]""",
        DI2560_TOWER_HENCHMAN_1: """DING-A-LING: `MAIN_CHARACTER_NAME`'s HERE![await][pause][delay_30]\n I'd better do something![await]""",
        DI2572_TOWER_HENCHMAN_2: """DING-A-LING: You won't find\n Count Down back here![await]\n Leave us alone![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """COUNT DOWN: There's nothing to\n do here![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Our inn is free![await][pause] Why?[delay_30] Uh...[delay]\n I'm not sure.[delay_30] Anyway,[delay] do you\n want to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Count Down's\n house up on the hill yet?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n       This is off-limits! Scram![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n       Get outta here! Beat it![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """COUNT DOWN: The dojo master will\n be tough to beat![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """DING-A-LING: Man...[delay_15] I'm tired.[await]\n Even alarm bells get tired\n sometimes.[await]""",
        DI3073_TOWER_HENCHMAN_3: """DING-A-LING: Back off![delay_15] I know\n Fear Roulette and I'm not afraid\n to use it![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Uh-oh! Are you looking for\n trouble?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n The guy next door never seems\n to shut his alarm clock off.[await][page]\n I'd like to go over and give him a\n piece of my mind, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]""",
    }
    # unsure if this makes sense to do with countdown. dingalings are kinda terrible to vram
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """DING-A-LING: We failed to stop\n you. Go ahead into Count Down's\n room![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """DING-A-LING: You beat Count Down!\n We didn't see that coming![await]""",
        # come up with something for booster's other replacement dialogs if it's feasible to have 4 bells in curtain room
    }

    _item_id: int = 572


class CloakerDominoBoss(Boss):
    """Cloaker/Domino boss fight"""

    _name: str = "Domino"
    _letter_seaside_boss_name: str = "the Snake"
    _letter_volcano_boss_name: str = "a snake slithering around"
    _letter_final_boss_name: str = "Domino's snakes."
    _pack_number: int = PACK0184_CLOAKER_DOMINO_FIGHT_STATIC
    _forced_background = Battlefields.CLOAKER_DOMINO
    _small_model: type[NPC] = DominoSmall
    _big_model: type[NPC] = DominoLarge
    _statue: type[NPC] = DominoStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """DOMINO: I'm busy wallowing in\n misery at my defeat here.[await][pause] Get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Uh oh, you cracked the code...\n I don't like where this is going...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Cloaker and Domino's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n CLOAKER and DOMINO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """DOMINO: Guess you're tougher\n than I thought...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """\n DOMINO: So, you've returned...![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """DOMINO: I don't like where this is\n going...[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I always enjoy a nice Bubble Tea[await]\n...after CLOBBERING TIME!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`!\n[await][page]\n We TOLD you to put your dukes up\n with `SEASIDE_BOSS`!\n[await]\n You'd better be ready!  We saw \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano![await]\n We think those snakes belong to\n `FINAL_BOSS_NAME`\n They sound like WEAKLINGS!\n It would be shameful if they\n defeated you. Stop by the ship if\n you want to play! Or see a\n blockable Carni-Kiss![await][page]\n\n              IT'S CLOBBERING TIME!!\n                       Cloaker & Domino[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big brick! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """DOMINO: Hee hee hee... You still\n need to find [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Cloaker and Domino are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Cloaker and Domino.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """DOMINO: Hee hee hee... So you've\n found our little town! Boring,\n isn't it?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Domino...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """DOMINO: Hee hee hee... So you're\n challenging the dojo master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hee hee hee... Wanna fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Weaklings-this and Snake-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """DOMINO: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn't been\n getting me the results I wanted.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """DOMINO: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn't been\n getting me the results I wanted.[await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 573


class ClerkBoss(Boss):
    """Clerk boss fight"""

    _name: str = "Clerk"
    _letter_seaside_boss_name: str = "the Clerk"
    _letter_volcano_boss_name: str = "a yellow-clad smith trudging"
    _letter_final_boss_name: str = "the Clerk's minions."
    _pack_number: int = PACK0146_CLERK_STATIC
    _small_model: type[NPC] = ClerkSmall
    _big_model: type[NPC] = ClerkLarge
    _statue: type[NPC] = ShovelKnightStatue
    _unique_henchmen: list[type[Henchman]] = [ClerkMadMallet, ClerkMadMallet]
    _repeatable_henchmen: list[type[Henchman]] = [ClerkMadMallet]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CLERK: I'm going to sleep for 10\n years.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Sorry, you may have figured out the\n password, but I can't allow you\n through without a fight.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Clerk's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the CLERK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CLERK: I don't get paid nearly\n enough to get whooped that\n badly...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CLERK: So, you've come back! I\n hope your journey is staying on\n schedule![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CLERK: What do you think you're\n doing?![await]""",
        DI1782_SHIP_BOSS_DRINK: """ You'll have to take this up with the[await]\n Manager.  I'M having an Espresso.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`,\n[await][page]\n When you can, I need a report on\n your the results of your battle with `SEASIDE_BOSS`.\n[await]\n On company retreat, I met\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n Mad Mallet saw them having drinks\n with `FINAL_BOSS_NAME`\n I've got to get back to work.  I \n spent my break writing this.  If\n you happen to return to the ship,\n could you bring me a Pick Me Up?[await][page]\n\n                                   Thanks,\n                                 the Clerk[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """MAD MALLET: Hop on the\n trampoline in the next room. It'll\n take you outside.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        DI2061_HEAD_CHEF: """MAD MALLET: We're making a cake\n to look just like the Clerk![await]""",
        DI2062_APPRENTICE_CHEF: """MAD MALLET: We've gotten REAL\n good with fondant![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CLERK: Whatcha got? [0x7000] item(s)?\n At this rate, you should find the\n last [0x7024] in no time![await]""",
        DI2560_TOWER_HENCHMAN_1: """MAD MALLET: Welcome.[await][pause] It's the\n Clerk's day off, so he's not taking\n visitors today.[await][page]\n ...But if you insist, I'll have to\n keep you out myself![await]""",
        DI2572_TOWER_HENCHMAN_2: """MAD MALLET: Listen, the Clerk\n doesn't get paid enough to deal\n with you.[await][page]\n  I certainly don't either, but I'm\n having a bad day![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CLERK: Not much happens in this\n quiet and completely unsuspicious\n town.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome.[delay] Would you like to stay\n here for free?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Clerk's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """\nDon't go snooping around our town![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """\n        I'm just shopping here![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n                 Get lost![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hey buddy, why don't you go snoop\n around some other houses instead?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CLERK: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you here for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """MAD MALLET: Wow! I can see\n Nimbus Land from here![await]""",
        DI3073_TOWER_HENCHMAN_3: """MAD MALLET: I'm gonna THRASH\n ya![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Puffball-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CLERK: If anyone asks, I'm on\n break![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CLERK: If anyone asks, I'm on\n break![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """MAD MALLET: You trashed us!\n Go on to the Clerk's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """MAD MALLET: Whoa... No one's\n beaten the Clerk in 10 years![await]""",
    }

    _item_id: int = 574


class ManagerBoss(Boss):
    """Manager boss fight"""

    _name: str = "Manager"
    _letter_seaside_boss_name: str = "the Manager"
    _letter_volcano_boss_name: str = "a blue-clad smith trudging"
    _letter_final_boss_name: str = "the Manager's minions."
    _pack_number: int = PACK0147_MANAGER_STATIC
    _small_model: type[NPC] = ManagerSmall
    _big_model: type[NPC] = ManagerLarge
    _statue: type[NPC] = ShovelKnightStatue
    _unique_henchmen: list[type[Henchman]] = [
        ManagerPounder,
        ManagerPounder,
        ManagerPounder,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [ManagerPounder]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MANAGER: I'm going to sleep for 25\n years.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Who gave you the password?!\n You're gonna pay for this![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Manager's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the MANAGER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """MANAGER: Why don't you just jump\n on out of here?![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MANAGER: Oh, you've returned.\n Good work so far.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MANAGER: Get off of my head\n before I make you take the longest\n jump of your life![await]""",
        DI1782_SHIP_BOSS_DRINK: """ DON'T bother the Director with this.[await]\n Just, drink my Cappuccino. Happy?[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you taken care of \n `SEASIDE_BOSS` yet?[await]\n\n There's a report on my desk about [await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They're a priority client of \n `FINAL_BOSS_NAME`[await]\n Take care of them, pronto.  All\n vacation time recinded until it's\n done.  I expect regular updates.[await][page]\n\n      Make it happen or you're fired.\n                             The Manager[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """POUNDER: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI2061_HEAD_CHEF: """POUNDER: We're making a cake\n to look just like the Manager![await]""",
        DI2062_APPRENTICE_CHEF: """POUNDER: We've gotten REAL\n good with fondant![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MANAGER: Heh heh heh.[delay] Good work.[await]\n You just need [0x7024] more item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """POUNDER: Good day.[await][pause] The Manager\n is busy today and will not be\n seeing any guests.[await][pause]\n If you try to force your way in,\n I'll have to deal with you![await]""",
        DI2572_TOWER_HENCHMAN_2: """POUNDER: Stay outta our hair![await]\n [delay]...Huh? [delay]“You don't have hair”?[await][pause]\n That's it, you're asking for it![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """MANAGER: Come to invade our\n town, have you?[await][pause] No need, there's\n nothing of interest here, I swear![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Good day.[delay] We're offering free\n reservations today. Would you like\n to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Manager's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ If you're gonna snoop around,\n [delay]just don't do it near the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Hey buddy, I'm just trying to shop\n here. Why don't you mind your own\n business?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n             Don't bother us![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n      Can't you see we're busy?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MANAGER: You think you can beat\n the dojo master?![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Yes?[await][pause] What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """POUNDER: Man, I need a break. This\n job is tiring.[await]""",
        DI3073_TOWER_HENCHMAN_3: """POUNDER: Bullet Bill production is\n on schedule! Don't get in my way![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Schedule-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MANAGER: Don't interrupt me while\n I'm training![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MANAGER: Don't interrupt me while\n I'm training![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """POUNDER: We lost, but we made\n the Manager proud![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """POUNDER: Wow! The Manager's\n been here 25 years, and you just\n dethroned him![await]""",
    }

    _item_id: int = 575


class DirectorBoss(Boss):
    """Director boss fight"""

    _name: str = "Director"
    _letter_seaside_boss_name: str = "the Director"
    _letter_volcano_boss_name: str = "a red-clad smith trudging"
    _letter_final_boss_name: str = "the Director's minions."
    _pack_number: int = PACK0148_DIRECTOR_STATIC
    _small_model: type[NPC] = DirectorSmall
    _big_model: type[NPC] = DirectorLarge
    _statue: type[NPC] = ShovelKnightStatue
    _unique_henchmen: list[type[Henchman]] = [
        DirectorPoundette,
        DirectorPoundette,
        DirectorPoundette,
        DirectorPoundette,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [DirectorPoundette]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """DIRECTOR: (Could this day get any\n worse?)[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Figured out the password, did you?[delay_30]\n Don't get too cocky![delay_30]\n Intruders will be eliminated![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Director's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the DIRECTOR!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """DIRECTOR: I'm afraid I have more\n pressing matters to attend to.\n Depart at once.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """DIRECTOR: Do not waste too much\n time here. Your quest must\n continue.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """DIRECTOR: Any tomfoolery will be\n dealt with by immediate meltdown.\n Get off of my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Only the Chief can help you, now.[await]\n I have a Latte with my name on it.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """POUNDETTE: I don't feel like I'm\n being used to my full potential\n down here.[await][pause] But I don't mind\n having a break.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To Whom It May Concern:\n[await][page]\n Please conclude all business with\n `SEASIDE_BOSS` ASAP.\n[await]\n Your next assignment involves\n `VOLCANO_BOSS_DESCRIPTION`\n at the volcano. [await]\n Temporary labor available from\n `FINAL_BOSS_NAME`\n All changes tenured with immediate\n effect. Mandatory overtime until\n the job is complete.  Direct all\n inquiries to the Manager.[await][page]\n\n                                   Signed,\n                              the Director[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """POUNDETTE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """POUNDETTE: I don't feel like I'm\n being used to my full potential\n down here.[await][pause] but I don't mind\n having a break.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """POUNDETTE: I don't feel like I'm\n being used to my full potential\n down here.[await][pause] but I don't mind\n having a break.[await]""",
        DI2061_HEAD_CHEF: """POUNDETTE: We're making a cake\n to look just like the Director![await]""",
        DI2062_APPRENTICE_CHEF: """POUNDETTE: We've gotten REAL\n good with fondant![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """DIRECTOR: I'm afraid you must\n continue searching.[delay] There are\n [0x7024] item(s) remaining.[await]""",
        DI2560_TOWER_HENCHMAN_1: """POUNDETTE: Salutations.[await][pause] Would you\n like to book an appointment with\n the Director?[await][pause]\n ...You want to just barge right\n in?![delay] No way![await]\n Time to teach you some manners![await]""",
        DI2572_TOWER_HENCHMAN_2: """POUNDETTE: The Director doesn't\n want anyone coming back here.[await]\n So I'm going to have to ask you\n to leave.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """DIRECTOR: I'm afraid there is\n nothing of concern to you in\n this town.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Salutations. How would you like to\n stay in our inn for free today?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Director's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ There's nothing suspicious going on\n in our town! [delay]Now go on, go to the\n next town![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ No, you can't see what I'm buying!\n [delay]How rude![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n                   Scram![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There's some important business\n happening in this shed, so get lost\n and quit trying to interrupt us![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """DIRECTOR: I'm afraid the dojo\n master will be quite a challenge for\n you to beat.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ State your business.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """POUNDETTE: Finally, some time to\n rest![await]""",
        DI3073_TOWER_HENCHMAN_3: """\nPOUNDETTE: Let's see whatcha got![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Meltdown-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """POUNDETTE: Well, we lost.\n Time for a break.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """POUNDETTE: You beat the Director!\n Impressive![await]""",
    }

    _item_id: int = 576


class GunyolkBoss(Boss):
    """Gunyolk boss fight"""

    _name: str = "Factory Chief"
    _letter_seaside_boss_name: str = "the Chief"
    _letter_volcano_boss_name: str = "a big machine rolling"
    _letter_final_boss_name: str = "the Factory Chief's goons."
    _pack_number: int = PACK0149_GUNYOLK_STATIC
    _small_model: type[NPC] = FactoryChief
    _statue: type[NPC] = FactoryChiefStatue
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """FACTORY CHIEF: Grrr... Leave me\n alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you solved it?[delay_30]\n Too bad, this is the end of the line\n for you! I won't let you through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Gunyolk's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the GUNYOLK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """FACTORY CHIEF: Harrumph! Get out\n of here before I invent something\n even stronger![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """FACTORY CHIEF: I'm surprised to\n see you back here! I don't have any\n new inventions to show yet.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """FACTORY CHIEF: Harrumph! I should\n invent myself a spiky hat![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Who do I have to Breaker Beam[await]\n to get a cuppa Coffee 'round here?[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n              Memorandum\n[await][page]\n `MAIN_CHARACTER_NAME` dispatched\n to handle `SEASIDE_BOSS`.\n[await]\n Real estate acquisition stalled by\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n Competition associated with \n `FINAL_BOSS_NAME`\n Report all conversations involving[await]\n the words "union", "living wage",\n "healthcare benefits", and/or\n "remote work environment" to your[await]\n supervisor immediately.[await][page]\n\n                      Do more with less.\n                                -The Chief[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big ninja! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """FACTORY CHIEF: Harrumph! You're\n still missing [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Gunyolk is busy right now, so\n it can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Gunyolk.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """FACTORY CHIEF: Harrumph! What're\n you doing here?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find the Factory Chief...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """FACTORY CHIEF: Harrumph! Just\n because you beat me, doesn't mean\n you can beat the dojo master![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Did you come here to fight me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Ninja-this and Invention-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """FACTORY CHIEF: I'll out-jump you\n if it's the last thing I do![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """FACTORY CHIEF: I'll out-jump you\n if it's the last thing I do![await]""",
    }
    _unique_henchmen: list[Henchman] = []
    _repeatable_henchmen: list[Henchman] = []
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {}

    _item_id: int = 577


class SmithyBoss(Boss):
    """Smithy boss fight"""

    _name: str = "Smithy"
    _letter_volcano_boss_name: str = "a furious weaponsmith thundering"
    _letter_final_boss_name: str = "Smithy's gang."
    _pack_number: int = PACK0185_SMITHY1_FIGHT_STATIC
    _small_model: type[NPC] = SmithySmall
    _big_model: type[NPC] = SmithyLarge
    _statue: type[NPC] = SmithyStatue
    _unique_henchmen: list[type[Henchman]] = [
        SmithyDrillBit,
        SmithyShyster,
        SmithyAero,
    ]
    _repeatable_henchmen: list[type[Henchman]] = [
        SmithyDrillBit,
        SmithyShyster,
        SmithyAero,
    ]
    _dialog_replacements: dict[int, str] = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """SMITHY: How utterly annoying!\n Leave me alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Gufaw, haw, haw![delay_30] You really think\n I'm going to let you through with\n just a password?![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Smithy's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n SMITHY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """SMITHY: How utterly annoying!\n Get out of here before I crush\n you all![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """SMITHY: Gufaw, haw, haw...\n Not quite as impressive as my\n factory, eh?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """SMITHY: Never have I been so\n wronged![await]""",
        DI1782_SHIP_BOSS_DRINK: """ This isn't even my final form![await]\n Barkeep!  Bring me more Ale!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ The foundation in this old haunted\n ship looks pretty weak. So we try\n not to make Smithy too mad.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Weakling,\n[await][page]\n I'll bet you had trouble with\n `SEASIDE_BOSS`. Pathetic.[await]\n\n A Drill Bit screamed about\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano when I smashed it.[await]\n I expected better from \n `FINAL_BOSS_NAME`[await]\n The Shyster is complaining about\n my blood pressure again.  I have\n a sledge for problems like these.[await][page]\n\n You haven't seen my final form yet,\n                                    Smithy[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take you outside.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ The foundation in this old haunted\n ship looks pretty weak. So we try\n not to make Smithy too mad.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ The foundation in this old haunted\n ship looks pretty weak. So we try\n not to make Smithy too mad.[await]""",
        DI2061_HEAD_CHEF: """MACHINE MADE: We're making a cake\n to look just like Smithy![await]""",
        DI2062_APPRENTICE_CHEF: """MACHINE MADE: We've gotten REAL\n good with fondant![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """SMITHY: How utterly annoying![await]\n Give me [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """MACHINE MADE: Yo![await][pause] Smithy's busy,\n so come back another time! [await][page]\n [delay]...You sure you wanna just barge\n in like that?[await][pause] Alright buddy, don't\n say I didn't warn you![await]""",
        DI2572_TOWER_HENCHMAN_2: """MACHINE MADE: Man, what's your\n deal?[await][pause] Quit snooping around!\n Smithy'll have a fit![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """SMITHY: So, it's YOU![await]\n Unfortunately for you, there's\n nothing evil in this town that\n demands your attention.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Yo. This inn doesn't charge\n anything for our services.\n Wanna stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Smithy's house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ The shed...?[delay] No, there's nothing in\n there! Take my word for it.[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ What am I doing with this stuff?\n ...None of your business![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n             Get out of here![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ No visitors allowed in the shed!\n Scram![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Grr... What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n   SMITHY: Grr... Leave me alone![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """MACHINE MADE: It's pretty drafty\n in here![await]""",
        DI3073_TOWER_HENCHMAN_3: """\n MACHINE MADE: Oh, no you don't![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Factory-this and Weapon-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """SMITHY: Grr... [delay]You're stronger\n than I thought...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """SMITHY: Grr... [delay]You're stronger\n than I thought...[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """ You're pretty tough, but are you\n ready to fight Smithy?[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """ Oh, wow, you did it![delay] No wonder we\n lost to you...[await]""",
    }

    _item_id: int = 578
