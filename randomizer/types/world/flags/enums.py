"""Enums used to form constants used to populate setting values."""

import enum

from randomizer.types.battles import (
    BossMusic,
    CorndillyMusic,
    CulexMusic,
    MidbossMusic,
    NormalBattleMusic,
    Smithy1Music,
)

from randomizer.entities.spells.spells import (
    Jump,
    FireOrb,
    SuperJump,
    SuperFlame,
    UltraJump,
    UltraFlame,
    Therapy,
    GroupHug,
    SleepyTime,
    ComeBack,
    Mute,
    PsychBomb,
    Terrorize,
    PoisonGas,
    Crusher,
    BowserCrush,
    GenoBeam,
    GenoBoost,
    GenoWhirl,
    GenoBlast,
    GenoFlash,
    Thunderbolt,
    HPRain,
    Psychopath,
    Shocker,
    Snowy,
    StarRain,
)


class FlagOptions(str, enum.Enum):
    """Base class for options that can belong to a setting"""


class FlagTypes(str, enum.Enum):
    """Enum for the different input types of settings"""

    CATEGORIZATION = "categorization"
    SELECT_ONE = "select_one"
    BOOLEAN = "boolean"
    NUMBER = "number"


class ShuffleLocationSelector(FlagOptions):
    """Enumeration for enabling and disabling locations"""

    STARTER_CHARACTER_1 = "Starter character 1"
    STARTER_CHARACTER_2 = "Starter character 2"
    STARTER_CHARACTER_3 = "Starter character 3"
    STARTER_CHARACTER_4 = "Starter character 4"
    STARTER_CHARACTER_5 = "Starter character 5"
    MARIOS_PAD_BED = "Mario's Pad Invisible Item"
    MARIOS_PAD_STARTER_1 = "Starter item 1"
    MARIOS_PAD_STARTER_2 = "Starter item 2"
    MARIOS_PAD_STARTER_3 = "Starter item 3"
    MARIOS_PAD_STARTER_4 = "Starter item 4"
    POSTGAME_VOUCHER = "Toad's postgame item grant (remake)"
    MUSHROOM_WAY_1 = "Mushroom Way first chest"
    MUSHROOM_WAY_2 = "Mushroom Way second chest"
    MUSHROOM_WAY_3 = "Mushroom Way flower jump left chest"
    MUSHROOM_WAY_4 = "Mushroom Way second room right chest"
    REMAKE_1 = "Mushroom Way left freestanding item (remake)"
    REMAKE_2 = "Mushroom Way right freestanding item (remake)"
    TOAD_RESCUE_1 = "Mushroom Way first Toad reward"
    TOAD_RESCUE_2 = "Mushroom Way second Toad reward"
    HAMMER_BROS_REWARD = "Mushroom Way boss reward"
    MUSHROOM_WAY_CHARACTER = "Mushroom Way character join"
    MUSHROOM_WAY_STAR_PIECE = "Mushroom Way boss Star Piece"
    MUSHROOM_KINGDOM_HALLWAY = "Mushroom Kingdom castle main hallway chest"
    MUSHROOM_KINGDOM_VAULT_1 = "Mushroom Kingdom vault left chest"
    MUSHROOM_KINGDOM_VAULT_2 = "Mushroom Kingdom vault right chest"
    MUSHROOM_KINGDOM_VAULT_3 = "Mushroom Kingdom vault middle chest"
    INVASION_VAULT_1 = "Mushroom Kingdom vault left chest (invasion)"
    INVASION_VAULT_2 = "Mushroom Kingdom vault right chest (invasion)"
    INVASION_VAULT_3 = "Mushroom Kingdom vault middle chest (invasion)"
    INVASION_EASTERN_GUARD = "Mushroom Kingdom eastern guard rescue (invasion)"
    WALLET_GUY_1 = "Wallet reward 1"
    WALLET_GUY_2 = "Wallet reward 2"
    MUSHROOM_KINGDOM_STORE = "Mushroom Kingdom shop free item"
    MUSHROOM_KINGDOM_STORE_EXCHANGE = "Mushroom Kingdom shop Rare Frog Coin exchange"
    MUSHROOM_KINGDOM_STORE_BASEMENT_1 = "Mushroom Kingdom shop basement left chest"
    MUSHROOM_KINGDOM_STORE_BASEMENT_2 = "Mushroom Kingdom shop basement right chest"
    PEACH_SURPRISE = "Mushroom Kingdom Toadstool's room chair item"
    INVASION_TOAD_RESCUE = (
        "Mushroom Kingdom Toadstool's room toad rescue item (invasion)"
    )
    INVASION_FAMILY = "Mushroom Kingdom invasion family rescue"
    INVASION_GUEST_ROOM = "Mushroom Kingdom invasion guest room"
    INVASION_STAR_PIECE = "Mushroom Kingdom invasion boss Star Piece"
    MUSHROOM_KINGDOM_INN = "Mushroom Kingdom gameboy kid"
    BANDITS_WAY_1 = "Bandit's Way flower chest"
    BANDITS_WAY_COIN_1 = "Bandit's Way 1st coin"
    BANDITS_WAY_COIN_2 = "Bandit's Way 2nd coin"
    BANDITS_WAY_COIN_3 = "Bandit's Way 3rd coin"
    BANDITS_WAY_2 = "Bandit's Way long room chest"
    BANDITS_WAY_STAR_CHEST = "Bandit's Way star chest"
    BANDITS_WAY_DOG_JUMP = "Bandit's Way dog jump chest"
    BANDITS_WAY_CROCO = "Bandit's Way Croco chase chest"
    CROCO_1_REWARD = "Bandit's Way boss reward 1"
    CROCO_1_REWARD_2 = "Bandit's Way boss reward 2"
    BANDITS_WAY_STAR_PIECE = "Bandit's Way boss Star Piece"
    KERO_SEWERS_PANDORITE_ROOM = "Kero Sewers stairway room left chest"
    PANDORITE_CHEST = "Kero Sewers stairway room right chest"
    PANDORITE_REWARD_1 = "Mimic Chest #1 first reward"
    PANDORITE_REWARD_2 = "Mimic Chest #1 reload reward"
    PANDORITE_BOSS = "Mimic Chest #1 Star Piece"
    KERO_SEWERS_STAR_CHEST = "Kero Sewers four rat room chest"
    KERO_SEWERS_BEFORE_BELOME_LOWER = "Kero Sewers before boss lower chest"
    KERO_SEWERS_BEFORE_BELOME_UPPER_1 = (
        "Kero Sewers before boss upper chest, before Land's End"
    )
    KERO_SEWERS_BEFORE_BELOME_UPPER_2 = (
        "Kero Sewers before boss upper chest, after Land's End"
    )
    KERO_SEWERS_BOSS = "Kero Sewers boss Star Piece"
    MIDAS_RIVER_FIRST_TIME = "Midas River first play reward"
    MIDAS_RIVER_BOTTOM_LEFT_CAVE = (
        "Midas River bottom left tunnel freestanding frog coin"
    )
    MIDAS_RIVER_BOTTOM_RIGHT_CAVE = (
        "Midas River bottom right tunnel freestanding flower"
    )
    CRICKET_PIE_REWARD = "Tadpole Pond Cricket Pie exchange"
    CRICKET_JAM_REWARD = "Tadpole Pond Cricket Jam exchange"
    MELODY_BAY_1 = "Melody Bay song 1 reward"
    MELODY_BAY_2 = "Melody Bay song 2 reward"
    MELODY_BAY_3 = "Melody Bay song 3 reward"
    ROSE_WAY_PLATFORM = "Rose Way swinging Shy Guy chest"
    ROSE_WAY_FLOWER = "Rose Way freestanding flower"
    ROSE_WAY_MUSHROOM = "Rose Way freestanding mushroom"
    ROSE_WAY_COIN_1 = "Rose Way freestanding coin 1"
    ROSE_WAY_COIN_2 = "Rose Way freestanding coin 2"
    ROSE_WAY_COIN_3 = "Rose Way freestanding coin 3"
    ROSE_WAY_COIN_4 = "Rose Way freestanding coin 4"
    ROSE_WAY_COIN_5 = "Rose Way freestanding coin 5"
    ROSE_WAY_FIVE_CHESTS_1 = "Rose Way five-chest area top middle chest"
    ROSE_WAY_FIVE_CHESTS_2 = "Rose Way five-chest area bottom left chest"
    ROSE_WAY_FIVE_CHESTS_3 = "Rose Way five-chest top right chest"
    ROSE_WAY_FIVE_CHESTS_4 = "Rose Way five-chest top left chest"
    ROSE_WAY_FIVE_CHESTS_5 = "Rose Way five-chest bottom right chest"
    ROSE_TOWN_FLAG = "Rose Town Invisible Item"
    ROSE_TOWN_STORE_1 = "Rose Town shop right chest"
    ROSE_TOWN_STORE_2 = "Rose Town shop left chest"
    GARDENER_CLOUD_1 = "Rose Town gardener right chest"
    GARDENER_CLOUD_2 = "Rose Town gardener left chest"
    ROSE_TOWN_TOAD = "Rose Town Inn Toad gift"
    GAZ = "Rose Town (unoccupied) Gaz gift"
    ROSE_TOWN_TREASURE_HOUSE_1 = "Rose Town upper house left chest"
    ROSE_TOWN_TREASURE_HOUSE_2 = "Rose Town upper house right chest"
    ROSE_TOWN_TREASURE_HOUSE_MAZE_REWARD = "Rose Town upper house Maze Secret prize"
    ROSE_TOWN_TREASURE_HOUSE_3 = "Rose Town upper house top floor chest"
    FOREST_MAZE_1 = "Forest Maze 1st room chest"
    FOREST_MAZE_2 = "Forest Maze first chest after underground"
    FOREST_MAZE_UNDERGROUND_1 = "Forest Maze wiggler chest"
    FOREST_MAZE_UNDERGROUND_2 = "Forest Maze bottom right stump chest"
    FOREST_MAZE_UNDERGROUND_3 = "Forest Maze middle left stump chest"
    FOREST_MAZE_RED_ESSENCE = "Forest Maze before maze chest"
    FOREST_MAZE_SECRET_1 = "Forest Maze secret top right chest"
    FOREST_MAZE_SECRET_2 = "Forest Maze secret bottom right chest"
    FOREST_MAZE_SECRET_3 = "Forest Maze secret top middle chest"
    FOREST_MAZE_SECRET_4 = "Forest Maze secret bottom middle chest"
    FOREST_MAZE_SECRET_5 = "Forest Maze secret left chest"
    FOREST_MAZE_CHARACTER = "Forest Maze character recruit"
    FOREST_MAZE_BOSS = "Forest Maze boss Star Piece"
    PIPE_VAULT_SLIDE_1 = "Pipe Vault slide room back chest"
    PIPE_VAULT_SLIDE_2 = "Pipe Vault slide room middle chest"
    PIPE_VAULT_SLIDE_3 = "Pipe Vault slide room front chest"
    PIPE_VAULT_SLIDE_COIN_1 = "Pipe Vault slide room freestanding coin 1"
    PIPE_VAULT_SLIDE_COIN_2 = "Pipe Vault slide room freestanding coin 2"
    PIPE_VAULT_SLIDE_COIN_3 = "Pipe Vault slide room freestanding coin 3"
    PIPE_VAULT_SLIDE_COIN_4 = "Pipe Vault slide room freestanding coin 4"
    PIPE_VAULT_SLIDE_COIN_5 = "Pipe Vault slide room freestanding coin 5"
    PIPE_VAULT_SLIDE_FROG_COIN = "Pipe Vault slide room freestanding frog coin"
    PIPE_VAULT_NIPPERS_1 = "Pipe Vault nipper room first chest"
    PIPE_VAULT_NIPPERS_2 = "Pipe Vault nipper room second chest"
    GOOMBA_THUMPING_1 = "Pipe Vault Goomba Thumpin first prize"
    GOOMBA_THUMPING_2 = "Pipe Vault Goomba Thumpin second prize"
    YOSTER_ISLE_ENTRANCE = "Yo'ster Isle entrance chest"
    YOSTER_ISLE_RACE_REWARD_1 = "Yo'ster Isle first race prize item 1"
    YOSTER_ISLE_RACE_REWARD_2 = "Yo'ster Isle Invisible Item"
    YOSTER_ISLE_RACE_REWARD_3 = "Yo'ster Isle first race prize item 2"
    YOSTER_ISLE_FLAG = "Yo'ster Isle first race prize item 3"
    CROCO_FLUNKIE_1 = "Moleville Mines trampoline bandit"
    CROCO_FLUNKIE_2 = "Moleville Mines left bandit"
    CROCO_FLUNKIE_3 = "Moleville Mines right bandit"
    CROCO_2_ITEM = "Moleville Mines first boss item"
    MOLEVILLE_MINES_BOSS_1 = "Moleville Mines first boss Star Piece"
    MOLEVILLE_MINES_SHY_GUY = "Moleville Mines shy guy cart"
    MOLEVILLE_MINES_STAR_CHEST = "Moleville Mines two-level traintrack room chest"
    MOLEVILLE_MINES_COINS = "Moleville Mines near final train tracks chest"
    MOLEVILLE_MINES_PUNCHINELLO_1 = "Moleville Mines before boss left chest"
    MOLEVILLE_MINES_PUNCHINELLO_2 = "Moleville Mines before boss upper chest"
    MOLEVILLE_MINES_BOSS_2 = "Moleville Mines final boss Star Piece"
    MOLEVILLE_MINES_CHARACTER = "Moleville Mines character recruit"
    BUCKET_GIRL = "Moleville bucket girl"
    TREASURE_SELLER_1 = "Moleville first treasure shop item"
    TREASURE_SELLER_2 = "Moleville second treasure shop item"
    TREASURE_SELLER_3 = "Moleville third treasure shop item"
    FIREWORKS_SHOP = "Moleville fireworks shop first item"
    BOOSTER_PASS_1 = "Booster Pass main area left chest"
    BOOSTER_PASS_2 = "Booster Pass main area right chest"
    BOOSTER_PASS_BUSH = "Booster Pass main area bush check"
    BOOSTER_PASS_FLOWER = "Booster Pass freestanding flower"
    BOOSTER_PASS_SECRET_1 = "Booster Pass secret middle chest"
    BOOSTER_PASS_SECRET_2 = "Booster Pass secret right chest"
    BOOSTER_PASS_SECRET_3 = "Booster Pass secret left chest"
    BOOSTER_TOWER_SPOOKUM = "Booster Tower first stairway chest"
    BOOSTER_TOWER_THWOMP = "Booster Tower upper thwomp room chest"
    BOOSTER_TOWER_KNIFE_GUY = "Booster Tower Knife Guy reward"
    BOOSTER_TOWER_ROOM_KEY = "Booster Tower checkerboard room item"
    BOOSTER_TOWER_FROG_COIN_1 = (
        "Booster Tower checkerboard room freestanding frog coin 1"
    )
    BOOSTER_TOWER_FROG_COIN_2 = (
        "Booster Tower checkerboard room freestanding frog coin 2"
    )
    BOOSTER_TOWER_FROG_COIN_3 = (
        "Booster Tower checkerboard room freestanding frog coin 3"
    )
    BOOSTER_TOWER_FROG_COIN_4 = (
        "Booster Tower checkerboard room freestanding frog coin 4"
    )
    BOOSTER_TOWER_COIN_1 = "Booster Tower checkerboard room freestanding coin 1"
    BOOSTER_TOWER_COIN_2 = "Booster Tower checkerboard room freestanding coin 2"
    BOOSTER_TOWER_COIN_3 = "Booster Tower checkerboard room freestanding coin 3"
    BOOSTER_TOWER_COIN_4 = "Booster Tower checkerboard room freestanding coin 4"
    BOOSTER_TOWER_COIN_5 = "Booster Tower checkerboard room freestanding coin 5"
    BOOSTER_TOWER_COIN_6 = "Booster Tower checkerboard room freestanding coin 6"
    BOOSTER_TOWER_COIN_7 = "Booster Tower checkerboard room freestanding coin 7"
    BOOSTER_TOWER_COIN_8 = "Booster Tower checkerboard room freestanding coin 8"
    BOOSTER_TOWER_COIN_9 = "Booster Tower checkerboard room freestanding coin 9"
    BOOSTER_TOWER_MASHER = "Booster Tower Masher chest"
    BOOSTER_TOWER_PARACHUTE = "Booster Tower parachute room chest"
    BOOSTER_TOWER_PARACHUTE_CREVICE = "Booster Tower parachute room stair crevice"
    BOOSTER_TOWER_ZOOM_SHOES = "Booster Tower Room Key chest"
    BOOSTER_TOWER_TOP_1 = "Booster Tower top floor lower chest"
    BOOSTER_TOWER_TOP_2 = "Booster Tower top floor upper chest"
    BOOSTER_TOWER_TOP_3 = "Booster Tower top floor corner chest"
    BOOSTER_TOWER_RAILWAY = "Booster Tower railway room"
    BOOSTER_TOWER_PORTRAITS = "Booster Tower portrait prize"
    BOOSTER_TOWER_CHOMP = "Booster Tower Elder Key room"
    BOOSTER_TOWER_CURTAIN_GAME = "Booster Tower curtain prize"
    BOOSTER_TOWER_STAR_PIECE_1 = "Booster Tower curtain room boss Star Piece"
    BOOSTER_TOWER_STAR_PIECE_2 = "Booster Tower balcony boss Star Piece"
    MARRYMORE_PRIZE_1 = "Marrymore Suite total stays prize 1"
    MARRYMORE_PRIZE_2 = "Marrymore Suite total stays prize 2"
    MARRYMORE_PRIZE_3 = "Marrymore Suite total stays prize 3"
    MARRYMORE_PRIZE_4 = "Marrymore Suite total stays prize 4"
    MARRYMORE_PRIZE_5 = "Marrymore Suite total stays prize 5"
    MARRYMORE_PRIZE_6 = "Marrymore Suite total stays prize 6"
    MARRYMORE_BIG_TIP = "Marrymore Inn elderly guest's major tip"
    MARRYMORE_INN = "Marrymore Inn regular room chest"
    MARRYMORE_SNIFIT_1 = "Marrymore Snifit 1 chapel item"
    MARRYMORE_SNIFIT_2 = "Marrymore Snifit 2 chapel item"
    MARRYMORE_SNIFIT_3 = "Marrymore Snifit 3 chapel item"
    MARRYMORE_ALTAR = "Marrymore altar chapel item"
    MARRYMORE_STAR_PIECE = "Marrymore boss Star Piece"
    MARRYMORE_CHARACTER = "Marrymore character join"
    STAR_HILL_STAR_PIECE_1 = "Star Hill freestanding Star Piece"
    FROG_DISCIPLE_1 = "Disciple shop first item"
    FROG_DISCIPLE_2 = "Disciple shop second item"
    FROG_DISCIPLE_3 = "Disciple shop third item"
    FROG_DISCIPLE_4 = "Disciple shop fourth item"
    FROG_DISCIPLE_5 = "Disciple shop fifth item"
    SEASIDE_TOWN_BOSS = "Seaside Town boss Star Piece"
    SEASIDE_TOWN_BOSS_PRIZE = "Seaside Town boss prize"
    SEASIDE_TOWN_RESCUE = "Seaside Town shed rescue"
    SEA_STAR_CHEST = "Sea starslap room chest"
    SEA_SAVE_ROOM_1 = "Sea save room back chest"
    SEA_SAVE_ROOM_2 = "Sea save room middle chest"
    SEA_SAVE_ROOM_3 = "Sea save room front chest"
    SEA_WHIRLPOOL_CHEST = "Sea whirlpool room chest"
    SUNKEN_SHIP_RAT_STAIRS = "Sunken Ship first stairway chest"
    SUNKEN_SHIP_RAT_STAIRS_FLOWER = "Sunken Ship first stairway freestanding flower"
    SUNKEN_SHIP_SHOP = "Sunken Ship shop area chest"
    SUNKEN_SHIP_COINS_1 = "Sunken Ship outside clone room left chest"
    SUNKEN_SHIP_COINS_2 = "Sunken Ship outside clone room right chest"
    SUNKEN_SHIP_CLONE_ROOM = "Sunken Ship clone room chest"
    SUNKEN_SHIP_FROG_COIN_ROOM = "Sunken Ship hidden box room chest"
    SUNKEN_SHIP_HIDON_MUSHROOM = "Sunken Ship Hidon's room left chest"
    HIDON_CHEST = "Sunken Ship Hidon's room right chest"
    HIDON_REWARD_1 = "Mimic Chest #2 first reward"
    HIDON_REWARD_2 = "Mimic Chest #2 reload reward"
    HIDON_BOSS = "Mimic Chest #2 Star Piece"
    SUNKEN_SHIP_UNDERWATER_FROG_COIN_1 = (
        "Sunken Ship underwater freestanding frog coin 1"
    )
    SUNKEN_SHIP_UNDERWATER_FROG_COIN_2 = (
        "Sunken Ship underwater freestanding frog coin 2"
    )
    SUNKEN_SHIP_UNDERWATER_FROG_COIN_3 = (
        "Sunken Ship underwater freestanding frog coin 3"
    )
    SUNKEN_SHIP_UNDERWATER_FROG_COIN_4 = (
        "Sunken Ship underwater freestanding frog coin 4"
    )
    SUNKEN_SHIP_SAFETY_RING = "Sunken Ship hidden underwater room chest"
    SUNKEN_SHIP_BANDANA_REDS = "Sunken Ship near final boss chest"
    SUNKEN_SHIP_BLOOBER_ROOM = "Sunken Ship large pool freestanding frog coin"
    SUNKEN_SHIP_TRAMPOLINE_PUZZLE = "Sunken Ship trampoline puzzle prize"
    SUNKEN_SHIP_TROOPA_PUZZLE = "Sunken Ship troopa cannonball prize"
    SUNKEN_SHIP_3D_MAZE = "Sunken Ship 3D maze prize"
    SUNKEN_SHIP_COIN_SNAKE = "Sunken Ship coin snake puzzle prize"
    SUNKEN_SHIP_CANNONBALL_PUZZLE = "Sunken Ship cannonball puzzle prize"
    SUNKEN_SHIP_BARREL_PUZZLE = "Sunken Ship barrel switch prize"
    SUNKEN_SHIP_MIDBOSS = "Sunken Ship password boss Star Piece"
    SUNKEN_SHIP_BOSS = "Sunken Ship final boss Star Piece"
    LANDS_END_RED_ESSENCE = "Land's End first chest"
    LANDS_END_CHOW_PIT_1 = "Land's End chow pit left chest"
    LANDS_END_CHOW_PIT_2 = "Land's End chow pit right chest"
    LNDS_END_BEE_ROOM = "Land's End bee room chest"
    REMAKE_3 = "Land's End bridge room freestanding item (remake)"
    LANDS_END_SECRET_1 = "Land's End grotto first chest"
    LANDS_END_SECRET_2 = "Land's End grotto corner chest"
    LANDS_END_SHY_AWAY = "Land's End grotto near sewer chest"
    LANDS_END_STAR_CHEST_1 = "Land's End whirlpool 1st underground chest"
    LANDS_END_STAR_CHEST_2 = "Land's End 1st purchase chest"
    LANDS_END_STAR_CHEST_3 = "Land's End 2nd purchase chest"
    TROOPA_CLIMB = "Land's End Troopa Climb sub-12 second prize"
    LANDS_END_STAR_PIECE_1 = "Land's End/Belome Temple cloud Star Piece"
    BELOME_TEMPLE_FORTUNE_TELLER = "Belome Temple first fortune-telling room chest"
    BELOME_TEMPLE_FORTUNE_1 = "Belome Temple left-middle-right fortune chest"
    BELOME_TEMPLE_FORTUNE_2 = "Belome Temple left-right-middle fortune chest"
    BELOME_TEMPLE_FORTUNE_3 = "Belome Temple right-left-middle fortune chest"
    BELOME_TEMPLE_FORTUNE_4 = "Belome Temple right-middle-left fortune chest"
    BELOME_TEMPLE_AFTER_FORTUNE_1 = "Belome Temple after fortune area right chest"
    BELOME_TEMPLE_AFTER_FORTUNE_2 = "Belome Temple after fortune area lower left chest"
    BELOME_TEMPLE_AFTER_FORTUNE_3 = "Belome Temple after fortune area middle chest"
    BELOME_TEMPLE_AFTER_FORTUNE_4 = "Belome Temple after fortune area upper left chest"
    BELOME_TEMPLE_TREASURE_FLOWER_1 = "Belome Temple vault flower 1"
    BELOME_TEMPLE_TREASURE_FLOWER_2 = "Belome Temple vault flower 2"
    BELOME_TEMPLE_TREASURE_FLOWER_3 = "Belome Temple vault flower 3"
    BELOME_TEMPLE_TREASURE_FLOWER_4 = "Belome Temple vault flower 4"
    BELOME_TEMPLE_TREASURE_FROG_COIN_1 = "Belome Temple vault frog coin 1"
    BELOME_TEMPLE_TREASURE_FROG_COIN_2 = "Belome Temple vault frog coin 2"
    BELOME_TEMPLE_TREASURE_FROG_COIN_3 = "Belome Temple vault frog coin 3"
    BELOME_TEMPLE_TREASURE_FROG_COIN_4 = "Belome Temple vault frog coin 4"
    BELOME_TEMPLE_TREASURE_FROG_COIN_5 = "Belome Temple vault frog coin 5"
    BELOME_TEMPLE_TREASURE_FROG_COIN_6 = "Belome Temple vault frog coin 6"
    BELOME_TEMPLE_TREASURE_FROG_COIN_7 = "Belome Temple vault frog coin 7"
    BELOME_TEMPLE_TREASURE_FROG_COIN_8 = "Belome Temple vault frog coin 8"
    BELOME_TEMPLE_TREASURE_1 = "Belome Temple vault middle item bag"
    BELOME_TEMPLE_TREASURE_2 = "Belome Temple vault left item bag"
    BELOME_TEMPLE_TREASURE_3 = "Belome Temple vault right item bag"
    BELOME_TEMPLE_BOSS = "Belome Temple boss Star Piece"
    MONSTRO_TOWN_ENTRANCE = "Monstro Town entrance chest"
    MONSTRO_TOWN_THWOMP = "Monstro Town thwomp key"
    JINX_DOJO_REWARD = "Monstro Town dojo prize"
    DOJO_BOSS_1 = "Monstro Town dojo first fight Star Piece"
    DOJO_BOSS_2 = "Monstro Town dojo second fight Star Piece"
    DOJO_BOSS_3 = "Monstro Town dojo third fight Star Piece"
    DOJO_BOSS_4 = "Monstro Town dojo fourth fight Star Piece"
    CULEX_BOSS = "Monstro Town sealed door Star Piece"
    CULEX_REWARD = "Monstro Town sealed door prize"
    SUPER_JUMPS_30 = "Monstro Town Super Jump first prize"
    SUPER_JUMPS_100 = "Monstro Town Super Jump second prize"
    THREE_MUSTY_FEARS = "Monstro Town flag exchange prize"
    BEAN_VALLEY_1 = "Bean Valley south upper level chest"
    BEAN_VALLEY_2 = "Bean Valley north upper level chest"
    BEAN_VALLEY_LEFT_PIRANHA_PIPE = "Bean Valley left piranha pipe chest"
    BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE = "Bean Valley bottom left piranha pipe chest"
    BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER = (
        "Bean Valley bottom right piranha pipe upper chest"
    )
    BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER = (
        "Bean Valley bottom right piranha pipe lower chest"
    )
    BEAN_VALLEY_BOX_BOY_ROOM_1 = "Bean Valley right piranha pipe left chest"
    BOX_BOY_BOSS = "Mimic Chest #3 Star Piece"
    BEAN_VALLEY_BOX_BOY_ROOM_2 = "Bean Valley right piranha pipe right chest"
    BEAN_VALLEY_BOX_BOY_ROOM_HIDDEN = (
        "Bean Valley right piranha pipe hidden stairway item"
    )
    BEAN_VALLEY_PIRANHA_PLANTS = "Bean Valley chest above Box Boy's room"
    BEAN_VALLEY_MEGASMILAX_ROOM = "Bean Valley boss reward"
    BEAN_VALLEY_BOSS = "Bean Valley boss Star Piece"
    BEAN_VALLEY_BEANSTALK = "Bean Valley clouds solo vine chest"
    BEAN_VALLEY_BEANSTALK_FROG_COIN = (
        "Bean Valley middle vine room freestanding frog coin"
    )
    BEAN_VALLEY_BEANSTALK_COIN_1 = (
        "Bean Valley middle vine room lowest freestanding coin"
    )
    BEAN_VALLEY_BEANSTALK_COIN_2 = (
        "Bean Valley middle vine room middle freestanding coin"
    )
    BEAN_VALLEY_BEANSTALK_COIN_3 = (
        "Bean Valley middle vine room highest freestanding coin"
    )
    BEAN_VALLEY_EAST_BEANSTALK_COIN_1 = (
        "Bean Valley east vine room lowest freestanding coin"
    )
    BEAN_VALLEY_EAST_BEANSTALK_COIN_2 = (
        "Bean Valley east vine room lower freestanding coin"
    )
    BEAN_VALLEY_EAST_BEANSTALK_COIN_3 = (
        "Bean Valley east vine room middle freestanding coin"
    )
    BEAN_VALLEY_EAST_BEANSTALK_COIN_4 = (
        "Bean Valley east vine room higher freestanding coin"
    )
    BEAN_VALLEY_EAST_BEANSTALK_COIN_5 = (
        "Bean Valley east vine room highest freestanding coin"
    )
    BEAN_VALLEY_WEST_BEANSTALK_COIN_1 = (
        "Bean Valley west vine room lower freestanding coin"
    )
    BEAN_VALLEY_WEST_BEANSTALK_COIN_2 = (
        "Bean Valley west vine room middle freestanding coin"
    )
    BEAN_VALLEY_WEST_BEANSTALK_COIN_3 = (
        "Bean Valley west vine room upper freestanding coin"
    )
    BEAN_VALLEY_WEST_BEANSTALK_FROG_COIN = (
        "Bean Valley west vine room freestanding frog coin"
    )
    BEAN_VALLEY_CLOUD_1 = "Bean Valley clouds upper left chest"
    BEAN_VALLEY_CLOUD_2 = "Bean Valley clouds upper right chest"
    BEAN_VALLEY_FALL_1 = "Bean Valley clouds lower left chest"
    BEAN_VALLEY_FALL_2 = "Bean Valley clouds lower right chest"
    BEAN_VALLEY_FIRST_VINE_ROOM_FROG_COIN = (
        "Bean Valley lowest vine room freestanding frog coin"
    )
    BEAN_VALLEY_FIRST_VINE_ROOM_MIDDLE_COIN = (
        "Bean Valley lowest vine room middle freestanding coin"
    )
    BEAN_VALLEY_FIRST_VINE_ROOM_UPPER_COIN = (
        "Bean Valley lowest vine room upper freestanding coin"
    )
    BEAN_VALLEY_FIRST_VINE_ROOM_LOWER_COIN = (
        "Bean Valley lowest vine room lower freestanding coin"
    )
    CASINO_GRATE_GUY_PRIZE = "Grate Guy's Casino LOTW prize"
    NIMBUS_LAND_SHOP = "Nimbus Land shop chest"
    NIMBUS_LAND_INN = "Nimbus Land dream cushion 1st item"
    NIMBUS_LAND_INN_2 = "Nimbus Land dream cushion 2nd item"
    NIMBUS_LAND_BEFORE_BIRDETTA_1 = "Nimbus Castle (occupied) 5-door room chest"
    NIMBUS_LAND_BEFORE_BIRDETTA_2 = "Nimbus Castle west two-level room chest"
    NIMBUS_CASTLE_BIRDETTA = "Nimbus Castle giant egg prize"
    NIMBUS_CASTLE_STAR_PIECE_2 = "Nimbus Land giant egg boss Star Piece"
    NIMBUS_CASTLE_OUT_OF_BOUNDS_1 = "Nimbus Castle west stairway room left chest"
    NIMBUS_CASTLE_OUT_OF_BOUNDS_2 = "Nimbus Castle west stairway room right chest"
    NIMBUS_CASTLE_SINGLE_GOLD_BIRD = "Nimbus Castle single gold bird room chest"
    NIMBUS_CASTLE_AFTER_EGG_1 = "Nimbus Castle east two-level room lower chest"
    NIMBUS_CASTLE_AFTER_EGG_2 = "Nimbus Castle east two-level room upper chest"
    NIMBUS_CASTLE_STAR_PIECE_3 = "Nimbus Land final boss Star Piece"
    NIMBUS_CASTLE_STAR_CHEST = "Nimbus Castle post-throne chest (occupied)"
    NIMBUS_CASTLE_STAR_AFTER_VALENTINA = "Nimbus Castle post-throne chest (unoccupied)"
    NIMBUS_CASTLE_CORNER_CHEST_AFTER_VALENTINA = (
        "Nimbus Castle (unoccupied) 5-door room chest"
    )
    NIMBUS_LAND_RIGHT_SIDE = "Nimbus Land post-invasion off-cloud item"
    DODO_REWARD = "Nimbus Land Dodo's statue game prize"
    NIMBUS_LAND_STAR_PIECE_1 = "Nimbus Land statue keeper boss Star Piece"
    NIMBUS_LAND_PRISONERS = "Nimbus Castle west cellar civilian"
    NIMBUS_LAND_PRISONERS_2 = "Nimbus Castle west cellar guard"
    NIMBUS_LAND_SIGNAL_RING = "Nimbus Land post-invasion upper right house"
    NIMBUS_LAND_CELLAR = "Nimbus Castle post-invasion north cellar"
    BARREL_VOLCANO_SECRET_1 = "Barrel Volcano secret room left chest"
    BARREL_VOLCANO_SECRET_2 = "Barrel Volcano secret room right chest"
    BARREL_VOLCANO_REVERSE = "Barrel Volcano reverse lava recoil frog coin"
    BARREL_VOLCANO_DONUT_1 = (
        "Barrel Volcano first donut lift room right freestanding frog coin"
    )
    BARREL_VOLCANO_DONUT_2 = (
        "Barrel Volcano first donut lift room left freestanding frog coin"
    )
    BARREL_VOLCANO_LAVA_POOL = "Barrel Volcano lava pool freestanding frog coin"
    BARREL_VOLCANO_BEFORE_STAR_1 = "Barrel Volcano second arrow sign room left chest"
    BARREL_VOLCANO_BEFORE_STAR_2 = "Barrel Volcano second arrow sign room right chest"
    BARREL_VOLCANO_STAR_ROOM = "Barrel Volcano star chest"
    BARREL_VOLCANO_SAVE_ROOM_1 = "Barrel Volcano save room lower chest"
    BARREL_VOLCANO_SAVE_ROOM_2 = "Barrel Volcano save room upper chest"
    BARREL_VOLCANO_HINOPIO = "Barrel Volcano Hinopio shop chest"
    BARREL_VOLCANO_BOSS_1 = "Barrel Volcano first boss Star Piece"
    BARREL_VOLCANO_BOSS_2 = "Barrel Volcano second boss Star Piece"
    BOWSERS_KEEP_DARK_ROOM = "Bowser's Keep dark room chest"
    BOWSERS_KEEP_CROCO_SHOP_1 = "Bowser's Keep near first shop left chest"
    BOWSERS_KEEP_CROCO_SHOP_2 = "Bowser's Keep near first shop right chest"
    BOWSERS_KEEP_MAGIKOOPA = "Bowser's Keep Magikoopa's room chest"
    BOWSERS_KEEP_BOSS_CHESTER = "Bowser's Keep battle door Star Piece"
    BOWSERS_KEEP_BOSS_1 = "Bowser's Keep first boss Star Piece"
    BOWSERS_KEEP_INVISIBLE_BRIDGE_1 = (
        "Bowser's Keep 6-door invisble bridge bottom chest"
    )
    BOWSERS_KEEP_INVISIBLE_BRIDGE_2 = "Bowser's Keep 6-door invisble bridge right chest"
    BOWSERS_KEEP_INVISIBLE_BRIDGE_3 = "Bowser's Keep 6-door invisble bridge left chest"
    BOWSERS_KEEP_INVISIBLE_BRIDGE_4 = "Bowser's Keep 6-door invisble bridge top chest"
    BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_1 = (
        "Bowser's Keep 6-door invisble bridge bottom left coin"
    )
    BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_2 = (
        "Bowser's Keep 6-door invisble bridge bottom right coin"
    )
    BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_3 = (
        "Bowser's Keep 6-door invisble bridge top left coin"
    )
    BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_4 = (
        "Bowser's Keep 6-door invisble bridge top right coin"
    )
    BOWSERS_KEEP_MOVING_PLATFORMS_1 = "Bowser's Keep X-Y platform room left exit chest"
    BOWSERS_KEEP_MOVING_PLATFORMS_2 = (
        "Bowser's Keep X-Y platform room left entrance chest"
    )
    BOWSERS_KEEP_MOVING_PLATFORMS_3 = (
        "Bowser's Keep X-Y platform room right entrance chest"
    )
    BOWSERS_KEEP_MOVING_PLATFORMS_4 = "Bowser's Keep X-Y platform room right exit chest"
    BOWSERS_KEEP_ELEVATOR_PLATFORMS = (
        "Bowser's Keep 6-door elevator platform room chest"
    )
    BOWSERS_KEEP_CANNONBALL_ROOM_1 = "Bowser's Keep cannonball room lower right chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_2 = "Bowser's Keep cannonball room exit chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_3 = "Bowser's Keep cannonball room lower left chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_4 = "Bowser's Keep cannonball room upper right chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_5 = "Bowser's Keep cannonball room upper left chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_COIN_1 = (
        "Bowser's Keep cannonball room freestanding coin 1"
    )
    BOWSERS_KEEP_CANNONBALL_ROOM_COIN_2 = (
        "Bowser's Keep cannonball room freestanding coin 2"
    )
    BOWSERS_KEEP_CANNONBALL_ROOM_COIN_3 = (
        "Bowser's Keep cannonball room freestanding coin 3"
    )
    BOWSERS_KEEP_CANNONBALL_ROOM_COIN_4 = (
        "Bowser's Keep cannonball room freestanding coin 4"
    )
    BOWSERS_KEEP_CANNONBALL_ROOM_COIN_5 = (
        "Bowser's Keep cannonball room freestanding coin 5"
    )
    BOWSERS_KEEP_CANNONBALL_ROOM_COIN_6 = (
        "Bowser's Keep cannonball room freestanding coin 6"
    )
    BOWSERS_KEEP_CANNONBALL_ROOM_COIN_7 = (
        "Bowser's Keep cannonball room freestanding coin 7"
    )
    BOWSERS_KEEP_CANNONBALL_ROOM_COIN_8 = (
        "Bowser's Keep cannonball room freestanding coin 8"
    )
    BOWSERS_KEEP_ROTATING_PLATFORMS_1 = (
        "Bowser's Keep rotating platform room entrance chest"
    )
    BOWSERS_KEEP_ROTATING_PLATFORMS_2 = (
        "Bowser's Keep rotating platform lower left chest"
    )
    BOWSERS_KEEP_ROTATING_PLATFORMS_3 = "Bowser's Keep rotating platform right chest"
    BOWSERS_KEEP_ROTATING_PLATFORMS_4 = "Bowser's Keep rotating platform center chest"
    BOWSERS_KEEP_ROTATING_PLATFORMS_5 = (
        "Bowser's Keep rotating platform upper left chest"
    )
    BOWSERS_KEEP_ROTATING_PLATFORMS_6 = "Bowser's Keep rotating platform exit chest"
    BOWSERS_KEEP_DOOR_REWARD_1 = "Bowser's Keep door prize 1"
    BOWSERS_KEEP_DOOR_REWARD_2 = "Bowser's Keep door prize 2"
    BOWSERS_KEEP_DOOR_REWARD_3 = "Bowser's Keep door prize 3"
    BOWSERS_KEEP_DOOR_REWARD_4 = "Bowser's Keep door prize 4"
    BOWSERS_KEEP_DOOR_REWARD_5 = "Bowser's Keep door prize 5"
    BOWSERS_KEEP_DOOR_REWARD_6 = "Bowser's Keep door prize 6"
    BOWSERS_KEEP_BOSS_2 = "Bowser's Keep second boss Star Piece"
    BOWSERS_KEEP_BOSS_3 = "Bowser's Keep third boss Star Piece"
    FACTORY_SAVE_ROOM = "Outer Factory early save room chest"
    FACTORY_BOLT_PLATFORMS = "Outer Factory bot platform chest"
    FACTORY_BOSS_1 = "Outer Factory first boss Star Piece"
    FACTORY_FALLING_AXEMS = "Outer Factory falling axem room chest"
    FACTORY_TREASURE_PIT_1 = "Outer Factory pit back chest"
    FACTORY_TREASURE_PIT_2 = "Outer Factory pit front chest"
    FACTORY_CONVEYOR_PLATFORMS_1 = "Outer Factory conveyor room right chest"
    FACTORY_CONVEYOR_PLATFORMS_2 = "Outer Factory conveyor room left chest"
    FACTORY_BEHIND_SNAKES_1 = "Outer Factory room behind machine yarid right chest"
    FACTORY_BEHIND_SNAKES_2 = "Outer Factory room behind machine yarid left chest"
    FACTORY_BOSS_2 = "Outer Factory second boss Star Piece"
    FACTORY_TOAD_GIFT = "Inner Factory toad gift"
    INNER_FACTORY_BOSS_1 = "Inner Factory first boss Star Piece"
    INNER_FACTORY_BOSS_2 = "Inner Factory second boss Star Piece"
    INNER_FACTORY_BOSS_3 = "Inner Factory third boss Star Piece"
    INNER_FACTORY_BOSS_4 = "Inner Factory fourth boss Star Piece"
    INNER_FACTORY_BOSS_FINAL = "Factory final boss Star Piece"


# ****************************** Location enum


class FireworksOptions(FlagOptions):
    """Enumeration for Fireworks flag option"""

    VANILLA = "Vanilla"
    SHUFFLE_ONE = "Shuffle Fireworks"
    PROGRESSIVE = "Shuffle Progressive Fireworks"


class WinConditions(FlagOptions):
    """Enumeration for win condition options"""

    FACTORY = "Beat the final Factory boss"
    SMITHY = "Beat Smithy"
    STARS = "Collect required Star Pieces"
    SEALED = "Beat Monstro Town sealed door"


class PlayableCharacters(FlagOptions):
    """Enumeration for character avilability options"""

    MARIO = "Mario"
    MALLOW = "Mallow"
    GENO = "Geno"
    BOWSER = "Bowser"
    TOADSTOOL = "Toadstool"
    RANDOM = "Random"


class EquipmentCharactersOptions(FlagOptions):
    """Enumeration for character equipment guidelines"""

    VANILLA = "Vanilla"
    VANILLA_ACCESSORIES_ALL = "Vanilla, except anyone can wear any accessory"
    RANDOM_ACCESSORIES_ALL = "Random, except anyone can wear any accessory"
    RANDOM = "Completely random"
    EQUIP_ALL = "Anyone can equip anything"


class EquipmentPropertiesOptions(FlagOptions):
    """Enumeration for win condition options"""

    VANILLA = "Vanilla"
    SOME = "Some buffs added"
    RANDOM = "Completely random"


class EXPMultiplierOptions(FlagOptions):
    """Enumeration for EXP scaling from enemy battles"""

    VANILLA = "Default"
    DOUBLE = "Double"
    TRIPLE = "Triple"


class BanditsWayGating(FlagOptions):
    """Enumeration for Bandit's Way gating flag option"""

    MALLOW = "Recruit Mallow"
    MUSHROOM_WAY = "Finish Mushroom Way"
    HAMMER_BRO = "Defeat Hammer Bros"
    OPEN = "Always open"


class ForestMazeGating(FlagOptions):
    """Enumeration for Forest Maze gating flag option"""

    GENO = "Find Geno"
    PIE = "Exchange Cricket Pie"
    OPEN = "Always open"


class Moleville1Gating(FlagOptions):
    """Enumeration for Pipe Vault gating flag option"""

    GENO = "Recruit Geno"
    FOREST = "Finish Forest Maze"
    BOWYER = "Defeat Bowyer"
    OPEN = "Always open"


class PipeVaultGating(FlagOptions):
    """Enumeration for Pipe Vault gating flag option"""

    GENO = "Recruit Geno"
    FOREST = "Finish Forest Maze"
    BOWYER = "Defeat Bowyer"
    OPEN = "Always open"


class BoosterTowerGating(FlagOptions):
    """Enumeration for Booster Tower gating flag option"""

    MARIO = "Recruit Mario"
    MALLOW = "Recruit Mallow"
    GENO = "Recruit Geno"
    BOWSER = "Recruit Bowser"
    TOADSTOOL = "Recruit Toadstool"
    MINES = "Finish Moleville Mines"
    PUNCHINELLO = "Defeat Punchinello"
    OPEN = "Always open"


class MarrymoreGating(FlagOptions):
    """Enumeration for Marrymore gating flag option"""

    HILL = "Finish Booster Hill"
    TOWER = "Finish Booster Tower"
    KGGG = "Defeat Knife Guy & Grate Guy"
    OPEN = "Always open"


class SeaGating(FlagOptions):
    """Enumeration for Sea & Sunken Ship gating flag option"""

    TOADSTOOL = "Recruit Toadstool"
    STAR_4 = "Collect 4 Star Pieces"
    BUNDT = "Defeat Bundt"
    OPEN = "Always open"


class YaridovichGating(FlagOptions):
    """Enumeration for Seaside boss gating flag option"""

    SHIP = "Finish Sunken Ship"
    JOHNNY = "Defeat Johnny"
    OPEN = "Always available"


class BelomeTempleGating(FlagOptions):
    """Enumeration for Belome Temple gating flag option"""

    SEASIDE = "Finish Seaside Town"
    YARID = "Defeat Yaridovich"
    OPEN = "Always open"


class MonstroTownGating(FlagOptions):
    """Enumeration for Monstro Town gating flag option"""

    LANDS_END = "Finish Land's End"
    BELOME_2 = "Defeat Belome 2"
    OPEN = "Always open"


class BarrelVolcanoGating(FlagOptions):
    """Enumeration for Barrel Volcano gating flag option"""

    NIMBUS = "Finish Nimbus Land"
    VALENTINA = "Defeat Valentina"
    OPEN = "Always open"


class BowsersKeepGating(FlagOptions):
    """Enumeration for Bowser's Keep gating flag option"""

    STAR_6 = "Collect 6 Star Pieces"
    VOLCANO = "Finish Barrel Volcano"
    AXEM = "Defeat Axem Rangers"
    OPEN = "Always open"


class FactoryGating(FlagOptions):
    """Enumeration for Factory gating flag option"""

    OPEN = "Open when Bowser's Keep is opened"
    KEEP = "Finish Bowser's Keep"
    STAR_6 = "Collect 6 Star Pieces"
    EXOR = "Defeat Exor"


class EXPChallengeOptions(FlagOptions):
    """Enumeration for exp star quality scaling option"""

    VANILLA = "Vanilla"
    EASY_STARS = "Star Pieces (easy)"
    HARD_STARS = "Star Pieces (hard)"
    EASY_BOSSES = "Bosses (easy)"
    HARD_BOSSES = "Bosses (hard)"
    NONE = "None"


class ItemQualities(FlagOptions):
    """Enumeration for item shuffle quality option"""

    ORIGINAL = "Original item pool"
    TIER_4 = "Completely random, unrestricted"
    TIER_3 = "Completely random, exclude top-tier items"
    TIER_2 = "Completely random, include some good items"
    TIER_1 = "Completely random, bad items only"
    EMPTY = "Completely empty"


class ShopQualities(FlagOptions):
    """Enumeration for shop shuffle quality option"""

    ORIGINAL = "Original shop pool"
    TIER_4 = "Completely random, unrestricted"
    TIER_3 = "Completely random, exclude top-tier items"
    TIER_2 = "Completely random, include some good items"
    TIER_1 = "Completely random, bad items only"
    EMPTY = "Completely empty"


class BossScaleOptions(FlagOptions):
    """Enumeration for shuffled boss stat scaling"""

    VANILLA = "Do not scale"
    MATCH = "Match to area"
    RANDOM = "Completely random"


class AvailableMusic(FlagOptions):
    """Enumeration for available music"""

    NORMAL = NormalBattleMusic.name
    BOSS_1 = MidbossMusic.name
    BOSS_2 = BossMusic.name
    SMITHY = Smithy1Music.name
    CULEX = CulexMusic.name
    CORN = CorndillyMusic.name


class LearnableSpells(FlagOptions):
    """Enum of learnable spell names, excluding clones and swapped elements"""

    JUMP = Jump().title
    FIRE_ORB = FireOrb().title
    SUPER_JUMP = SuperJump().title
    SUPER_FLAME = SuperFlame().title
    ULTRA_JUMP = UltraJump().title
    ULTRA_FLAME = UltraFlame().title
    THERAPY = Therapy().title
    GROUP_HUG = GroupHug().title
    SLEEPY_TIME = SleepyTime().title
    COME_BACK = ComeBack().title
    MUTE = Mute().title
    PSYCH_BOMB = PsychBomb().title
    TERRORIZE = Terrorize().title
    POISON_GAS = PoisonGas().title
    CRUSHER = Crusher().title
    BOWSER_CRUSH = BowserCrush().title
    GENO_BEAM = GenoBeam().title
    GENO_BOOST = GenoBoost().title
    GENO_WHIRL = GenoWhirl().title
    GENO_BLAST = GenoBlast().title
    GENO_FLASH = GenoFlash().title
    THUNDERBOLT = Thunderbolt().title
    HP_RAIN = HPRain().title
    PSYCHOPATH = Psychopath().title
    SHOCKER = Shocker().title
    SNOWY = Snowy().title
    STAR_RAIN = StarRain().title
