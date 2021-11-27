# Contains most selectors needed for logic/flags.py

import enum
from randomizer.data import music, spells
from json import JSONEncoder

# ****************************** Location enum

class FlagOptions(str, enum.Enum):
    pass


class ShuffleLocationSelector(FlagOptions):
    """Enumeration for enabling and disabling locations"""
    StarterCharacter1 = "Starter character 1"
    StarterCharacter2 = "Starter character 2"
    StarterCharacter3 = "Starter character 3"
    StarterCharacter4 = "Starter character 4"
    StarterCharacter5 = "Starter character 5"
    MariosPadBed = "Invisible Musty Fears Item #1"
    MariosPadStarter1 = "Starter item 1"
    MariosPadStarter2 = "Starter item 2"
    MariosPadStarter3 = "Starter item 3"
    MariosPadStarter4 = "Starter item 4"
    MushroomWay1 = "Mushroom Way first chest"
    MushroomWay2 = "Mushroom Way second chest"
    MushroomWay3 = "Mushroom Way flower jump left chest"
    MushroomWay4 = "Mushroom Way second room right chest"
    ToadRescue1 = "Mushroom Way first Toad reward"
    ToadRescue2 = "Mushroom Way second Toad reward"
    HammerBrosReward = "Mushroom Way boss reward"
    MushroomWayCharacter = "Mushroom Way character join"
    MushroomWayStarPiece = "Mushroom Way boss Star Piece"
    MushroomKingdomHallway = "Mushroom Kingdom castle main hallway chest"
    MushroomKingdomVault1 = "Mushroom Kingdom vault left chest"
    MushroomKingdomVault2 = "Mushroom Kingdom vault right chest"
    MushroomKingdomVault3 = "Mushroom Kingdom vault middle chest"
    InvasionVault1 = "Mushroom Kingdom vault left chest (invasion)"
    InvasionVault2 = "Mushroom Kingdom vault right chest (invasion)"
    InvasionVault3 = "Mushroom Kingdom vault middle chest (invasion)"
    InvasionEasternGuard = "Mushroom Kingdom eastern guard rescue (invasion)"
    WalletGuy1 = "Wallet reward 1"
    WalletGuy2 = "Wallet reward 2"
    MushroomKingdomStore = "Mushroom Kingdom shop free item"
    MushroomKingdomStoreExchange = "Mushroom Kingdom shop Rare Frog Coin exchange"
    MushroomKingdomStoreBasement1 = "Mushroom Kingdom shop basement left chest"
    MushroomKingdomStoreBasement2 = "Mushroom Kingdom shop basement right chest"
    PeachSurprise = "Mushroom Kingdom Toadstool's room chair item"
    InvasionToadRescue = "Mushroom Kingdom Toadstool's room toad rescue item (invasion)"
    InvasionFamily = "Mushroom Kingdom invasion family rescue"
    InvasionGuestRoom = "Mushroom Kingdom invasion guest room"
    InvasionStarPiece = "Mushroom Kingdom invasion boss Star Piece"
    MushroomKingdomInn = "Mushroom Kingdom gameboy kid"
    BanditsWay1 = "Bandit's Way flower chest"
    BanditsWayCoin1 = "Bandit's Way 1st coin"
    BanditsWayCoin2 = "Bandit's Way 2nd coin"
    BanditsWayCoin3 = "Bandit's Way 3rd coin"
    BanditsWay2 = "Bandit's Way long room chest"
    BanditsWayStarChest = "Bandit's Way star chest"
    BanditsWayDogJump = "Bandit's Way dog jump chest"
    BanditsWayCroco = "Bandit's Way Croco chase chest"
    Croco1Reward = "Bandit's Way boss reward 1"
    Croco1Reward2 = "Bandit's Way boss reward 2"
    BanditsWayStarPiece = "Bandit's Way boss Star Piece"
    KeroSewersPandoriteRoom = "Kero Sewers stairway room left chest"
    PandoriteChest = "Kero Sewers stairway room right chest"
    PandoriteReward1 = "Mimic Chest #1 first reward"
    PandoriteReward2 = "Mimic Chest #1 reload reward"
    PandoriteBoss = "Mimic Chest #1 Star Piece"
    KeroSewersStarChest = "Kero Sewers four rat room chest"
    KeroSewersBeforeBelomeLower = "Kero Sewers before boss lower chest"
    KeroSewersBeforeBelomeUpper1 = "Kero Sewers before boss upper chest, before Land's End"
    KeroSewersBeforeBelomeUpper2 = "Kero Sewers before boss upper chest, after Land's End"
    KeroSewersBoss = "Kero Sewers boss Star Piece"
    MidasRiverFirstTime = "Midas River first play reward"
    MidasRiverBottomLeftCave = "Midas River bottom left tunnel freestanding frog coin"
    MidasRiverBottomRightCave = "Midas River bottom right tunnel freestanding flower"
    CricketPieReward = "Tadpole Pond Cricket Pie exchange"
    CricketJamReward = "Tadpole Pond Cricket Jam exchange"
    MelodyBay1 = "Melody Bay song 1 reward"
    MelodyBay2 = "Melody Bay song 2 reward"
    MelodyBay3 = "Melody Bay song 3 reward"
    RoseWayPlatform = "Rose Way swinging Shy Guy chest"
    RoseWayFlower = "Rose Way freestanding flower"
    RoseWayMushroom = "Rose Way freestanding mushroom"
    RoseWayCoin1 = "Rose Way freestanding coin 1"
    RoseWayCoin2 = "Rose Way freestanding coin 2"
    RoseWayCoin3 = "Rose Way freestanding coin 3"
    RoseWayCoin4 = "Rose Way freestanding coin 4"
    RoseWayCoin5 = "Rose Way freestanding coin 5"
    RoseWayFiveChests1 = "Rose Way five-chest area top middle chest"
    RoseWayFiveChests2 = "Rose Way five-chest area bottom left chest"
    RoseWayFiveChests3 = "Rose Way five-chest top right chest"
    RoseWayFiveChests4 = "Rose Way five-chest top left chest"
    RoseWayFiveChests5 = "Rose Way five-chest bottom right chest"
    RoseTownFlag = "Invisible Musty Fears Item #2"
    RoseTownStore1 = "Rose Town shop right chest"
    RoseTownStore2 = "Rose Town shop left chest"
    GardenerCloud1 = "Rose Town gardener right chest"
    GardenerCloud2 = "Rose Town gardener left chest"
    RoseTownToad = "Rose Town Inn Toad gift"
    Gaz = "Rose Town (unoccupied) Gaz gift"
    RoseTownTreasureHouse1 = "Rose Town upper house left chest"
    RoseTownTreasureHouse2 = "Rose Town upper house right chest"
    RoseTownTreasureHouseMazeReward = "Rose Town upper house Maze Secret prize"
    RoseTownTreasureHouse3 = "Rose Town upper house top floor chest"
    ForestMaze1 = "Forest Maze 1st room chest"
    ForestMaze2 = "Forest Maze first chest after underground"
    ForestMazeUnderground1 = "Forest Maze wiggler chest"
    ForestMazeUnderground2 = "Forest Maze bottom right stump chest"
    ForestMazeUnderground3 = "Forest Maze middle left stump chest"
    ForestMazeRedEssence = "Forest Maze before maze chest"
    ForestMazeSecret1 = "Forest Maze secret top right chest"
    ForestMazeSecret2 = "Forest Maze secret bottom right chest"
    ForestMazeSecret3 = "Forest Maze secret top middle chest"
    ForestMazeSecret4 = "Forest Maze secret bottom middle chest"
    ForestMazeSecret5 = "Forest Maze secret left chest"
    ForestMazeCharacter = "Forest Maze character recruit"
    ForestMazeBoss = "Forest Maze boss Star Piece"
    PipeVaultSlide1 = "Pipe Vault slide room back chest"
    PipeVaultSlide2 = "Pipe Vault slide room middle chest"
    PipeVaultSlide3 = "Pipe Vault slide room front chest"
    PipeVaultSlideCoin1 = "Pipe Vault slide room freestanding coin 1"
    PipeVaultSlideCoin2 = "Pipe Vault slide room freestanding coin 2"
    PipeVaultSlideCoin3 = "Pipe Vault slide room freestanding coin 3"
    PipeVaultSlideCoin4 = "Pipe Vault slide room freestanding coin 4"
    PipeVaultSlideCoin5 = "Pipe Vault slide room freestanding coin 5"
    PipeVaultSlideFrogCoin = "Pipe Vault slide room freestanding frog coin"
    PipeVaultNippers1 = "Pipe Vault nipper room first chest"
    PipeVaultNippers2 = "Pipe Vault nipper room second chest"
    GoombaThumping1 = "Pipe Vault Goomba Thumpin first prize"
    GoombaThumping2 = "Pipe Vault Goomba Thumpin second prize"
    YosterIsleEntrance = "Yo'ster Isle entrance chest"
    YosterIsleRaceReward1 = "Yo'ster Isle first race prize item 1"
    YosterIsleRaceReward2 = "Invisible Musty Fears Item #3"
    YosterIsleRaceReward3 = "Yo'ster Isle first race prize item 2"
    YosterIsleFlag = "Yo'ster Isle first race prize item 3"
    BucketGirl = "Moleville bucket girl"
    TreasureSeller1 = "Moleville first treasure shop item"
    TreasureSeller2 = "Moleville second treasure shop item"
    TreasureSeller3 = "Moleville third treasure shop item"
    FireworksShop = "Moleville Mines two-level traintrack room chest"
    MolevilleMinesShyGuy = "Moleville Mines shy guy cart"
    MolevilleMinesStarChest = "Moleville Mines star chest"
    MolevilleMinesCoins = "Moleville Mines near final train tracks chest"
    MolevilleMinesPunchinello1 = "Moleville Mines before boss left chest"
    MolevilleMinesPunchinello2 = "Moleville Mines before boss upper chest"
    MolevilleMinesBoss2 = "Moleville Mines final boss Star Piece"
    MolevilleMinesCharacter = "Moleville Mines character recruit"
    CrocoFlunkie1 = "Moleville Mines trampoline bandit"
    CrocoFlunkie2 = "Moleville Mines left bandit"
    CrocoFlunkie3 = "Moleville Mines right bandit"
    Croco2Item = "Moleville Mines first boss item"
    MolevilleMinesBoss1 = "Moleville Mines first boss Star Piece"
    BoosterPass1 = "Booster Pass main area left chest"
    BoosterPass2 = "Booster Pass main area right chest"
    BoosterPassBush = "Booster Pass main area bush check"
    BoosterPassFlower = "Booster Pass freestanding flower"
    BoosterPassSecret1 = "Booster Pass secret middle chest"
    BoosterPassSecret2 = "Booster Pass secret right chest"
    BoosterPassSecret3 = "Booster Pass secret left chest"
    BoosterTowerSpookum = "Booster Tower first stairway chest"
    BoosterTowerThwomp = "Booster Tower upper thwomp room chest"
    BoosterTowerKnifeGuy = "Booster Tower Knife Guy reward"
    BoosterTowerRoomKey = "Booster Tower checkerboard room item"
    BoosterTowerFrogCoin1 = "Booster Tower checkerboard room freestanding frog coin 1"
    BoosterTowerFrogCoin2 = "Booster Tower checkerboard room freestanding frog coin 2"
    BoosterTowerFrogCoin3 = "Booster Tower checkerboard room freestanding frog coin 3"
    BoosterTowerFrogCoin4 = "Booster Tower checkerboard room freestanding frog coin 4"
    BoosterTowerCoin1 = "Booster Tower checkerboard room freestanding coin 1"
    BoosterTowerCoin2 = "Booster Tower checkerboard room freestanding coin 2"
    BoosterTowerCoin3 = "Booster Tower checkerboard room freestanding coin 3"
    BoosterTowerCoin4 = "Booster Tower checkerboard room freestanding coin 4"
    BoosterTowerCoin5 = "Booster Tower checkerboard room freestanding coin 5"
    BoosterTowerCoin6 = "Booster Tower checkerboard room freestanding coin 6"
    BoosterTowerCoin7 = "Booster Tower checkerboard room freestanding coin 7"
    BoosterTowerCoin8 = "Booster Tower checkerboard room freestanding coin 8"
    BoosterTowerCoin9 = "Booster Tower checkerboard room freestanding coin 9"
    BoosterTowerMasher = "Booster Tower Masher chest"
    BoosterTowerParachute = "Booster Tower parachute room chest"
    BoosterTowerParachuteCrevice = "Booster Tower parachute room stair crevice"
    BoosterTowerZoomShoes = "Booster Tower Room Key chest"
    BoosterTowerTop1 = "Booster Tower top floor lower chest"
    BoosterTowerTop2 = "Booster Tower top floor upper chest"
    BoosterTowerTop3 = "Booster Tower top floor corner chest"
    BoosterTowerRailway = "Booster Tower railway room"
    BoosterTowerPortraits = "Booster Tower portrait prize"
    BoosterTowerChomp = "Booster Tower Elder Key room"
    BoosterTowerCurtainGame = "Booster Tower curtain prize"
    BoosterTowerStarPiece1 = "Booster Tower curtain room boss Star Piece"
    BoosterTowerStarPiece2 = "Booster Tower balcony boss Star Piece"
    MarrymorePrize1 = "Marrymore Suite total stays prize 1"
    MarrymorePrize2 = "Marrymore Suite total stays prize 2"
    MarrymorePrize3 = "Marrymore Suite total stays prize 3"
    MarrymorePrize4 = "Marrymore Suite total stays prize 4"
    MarrymorePrize5 = "Marrymore Suite total stays prize 5"
    MarrymorePrize6 = "Marrymore Suite total stays prize 6"
    MarrymoreInn = "Marrymore Inn regular room chest"
    MarrymoreStarPiece = "Marrymore boss Star Piece"
    MarrymoreCharacter = "Marrymore character join"
    StarHillStarPiece1 = "Star Hill freestanding Star Piece"
    FrogDisciple1 = "Disciple shop first item"
    FrogDisciple2 = "Disciple shop second item"
    FrogDisciple3 = "Disciple shop third item"
    FrogDisciple4 = "Disciple shop fourth item"
    FrogDisciple5 = "Disciple shop fifth item"
    SeasideTownBoss = "Seaside Town boss Star Piece"
    SeasideTownBossPrize = "Seaside Town boss prize"
    SeasideTownRescue = "Seaside Town shed rescue"
    SeaStarChest = "Sea starslap room chest"
    SeaSaveRoom1 = "Sea save room back chest"
    SeaSaveRoom2 = "Sea save room middle chest"
    SeaSaveRoom3 = "Sea save room front chest"
    SeaWhirlpoolChest = "Sea whirlpool room chest"
    SunkenShipRatStairs = "Sunken Ship first stairway chest"
    SunkenShipRatStairsFlower = "Sunken Ship first stairway freestanding flower"
    SunkenShipShop = "Sunken Ship shop area chest"
    SunkenShipCoins1 = "Sunken Ship outside clone room left chest"
    SunkenShipCoins2 = "Sunken Ship outside clone room right chest"
    SunkenShipCloneRoom = "Sunken Ship clone room chest"
    SunkenShipFrogCoinRoom = "Sunken Ship hidden box room chest"
    SunkenShipHidonMushroom = "Sunken Ship Hidon's room left chest"
    HidonChest = "Sunken Ship Hidon's room right chest"
    HidonReward1 = "Mimic Chest #2 first reward"
    HidonReward2 = "Mimic Chest #2 reload reward"
    HidonBoss = "Mimic Chest #2 Star Piece"
    SunkenShipUnderwaterFrogCoin1 = "Sunken Ship underwater freestanding frog coin 1"
    SunkenShipUnderwaterFrogCoin2 = "Sunken Ship underwater freestanding frog coin 2"
    SunkenShipUnderwaterFrogCoin3 = "Sunken Ship underwater freestanding frog coin 3"
    SunkenShipUnderwaterFrogCoin4 = "Sunken Ship underwater freestanding frog coin 4"
    SunkenShipSafetyRing = "Sunken Ship hidden underwater room chest"
    SunkenShipBandanaReds = "Sunken Ship near final boss chest"
    SunkenShipBlooberRoom = "Sunken Ship large pool freestanding frog coin"
    SunkenShipTrampolinePuzzle = "Sunken Ship trampoline puzzle prize"
    SunkenShipTroopaPuzzle = "Sunken Ship troopa cannonball prize"
    SunkenShip3DMaze = "Sunken Ship 3D maze prize"
    SunkenShipCoinSnake = "Sunken Ship coin snake puzzle prize"
    SunkenShipCannonballPuzzle = "Sunken Ship cannonball puzzle prize"
    SunkenShipBarrelPuzzle = "Sunken Ship barrel switch prize"
    SunkenShipMidboss = "Sunken Ship password boss Star Piece"
    SunkenShipBoss = "Sunken Ship final boss Star Piece"
    LandsEndRedEssence = "Land's End first chest"
    LandsEndChowPit1 = "Land's End chow pit left chest"
    LandsEndChowPit2 = "Land's End chow pit right chest"
    LandsEndBeeRoom = "Land's End bee room chest"
    LandsEndSecret1 = "Land's End grotto first chest"
    LandsEndSecret2 = "Land's End grotto corner chest"
    LandsEndShyAway = "Land's End grotto near sewer chest"
    LandsEndStarChest1 = "Land's End whirlpool 1st underground chest"
    LandsEndStarChest2 = "Land's End 1st purchase chest"
    LandsEndStarChest3 = "Land's End 2nd purchase chest"
    TroopaClimb = "Land's End Troopa Climb sub-12 second prize"
    LandsEndStarPiece1 = "Land's End/Belome Temple cloud Star Piece"
    BelomeTempleFortuneTeller = "Belome Temple first fortune-telling room chest"
    BelomeTempleFortune1 = "Belome Temple left-middle-right fortune chest"
    BelomeTempleFortune2 = "Belome Temple left-right-middle fortune chest"
    BelomeTempleFortune3 = "Belome Temple right-left-middle fortune chest"
    BelomeTempleFortune4 = "Belome Temple right-middle-left fortune chest"
    BelomeTempleAfterFortune1 = "Belome Temple after fortune area right chest"
    BelomeTempleAfterFortune2 = "Belome Temple after fortune area lower left chest"
    BelomeTempleAfterFortune3 = "Belome Temple after fortune area middle chest"
    BelomeTempleAfterFortune4 = "Belome Temple after fortune area upper left chest"
    BelomeTempleTreasureFlower1 = "Belome Temple vault flower 1"
    BelomeTempleTreasureFlower2 = "Belome Temple vault flower 2"
    BelomeTempleTreasureFlower3 = "Belome Temple vault flower 3"
    BelomeTempleTreasureFlower4 = "Belome Temple vault flower 4"
    BelomeTempleTreasureFrogCoin1 = "Belome Temple vault frog coin 1"
    BelomeTempleTreasureFrogCoin2 = "Belome Temple vault frog coin 2"
    BelomeTempleTreasureFrogCoin3 = "Belome Temple vault frog coin 3"
    BelomeTempleTreasureFrogCoin4 = "Belome Temple vault frog coin 4"
    BelomeTempleTreasureFrogCoin5 = "Belome Temple vault frog coin 5"
    BelomeTempleTreasureFrogCoin6 = "Belome Temple vault frog coin 6"
    BelomeTempleTreasureFrogCoin7 = "Belome Temple vault frog coin 7"
    BelomeTempleTreasureFrogCoin8 = "Belome Temple vault frog coin 8"
    BelomeTempleTreasure1 = "Belome Temple vault middle item bag"
    BelomeTempleTreasure2 = "Belome Temple vault left item bag"
    BelomeTempleTreasure3 = "Belome Temple vault right item bag"
    BelomeTempleBoss = "Belome Temple boss Star Piece"
    MonstroTownEntrance = "Monstro Town entrance chest"
    MonstroTownThwomp = "Monstro Town thwomp key"
    JinxDojoReward = "Monstro Town dojo prize"
    DojoBoss1 = "Monstro Town dojo first fight Star Piece"
    DojoBoss2 = "Monstro Town dojo second fight Star Piece"
    DojoBoss3 = "Monstro Town dojo third fight Star Piece"
    DojoBoss4 = "Monstro Town dojo fourth fight Star Piece"
    CulexBoss = "Monstro Town sealed door Star Piece"
    CulexReward = "Monstro Town sealed door prize"
    SuperJumps30 = "Monstro Town Super Jump first prize"
    SuperJumps100 = "Monstro Town Super Jump second prize"
    ThreeMustyFears = "Monstro Town flag exchange prize"
    BeanValley1 = "Bean Valley south upper level chest"
    BeanValley2 = "Bean Valley north upper level chest"
    BeanValleyLeftPiranhaPipe = "Bean Valley left piranha pipe chest"
    BeanValleyBottomLeftPiranhaPipe = "Bean Valley bottom left piranha pipe chest"
    BeanValleyBottomRightPiranhaPipeUpper = "Bean Valley bottom right piranha pipe upper chest"
    BeanValleyBottomRightPiranhaPipeLower = "Bean Valley bottom right piranha pipe lower chest"
    BeanValleyBoxBoyRoom1 = "Bean Valley right piranha pipe left chest"
    BoxBoyBoss = "Mimic Chest #3 Star Piece"
    BeanValleyBoxBoyRoom2 = "Bean Valley right piranha pipe right chest"
    BeanValleyBoxBoyRoomHidden = "Bean Valley right piranha pipe hidden stairway item"
    BeanValleyPiranhaPlants = "Bean Valley chest above Box Boy's room"
    BeanValleyMegasmilaxRoom = "Bean Valley boss reward"
    BeanValleyBoss = "Bean Valley boss Star Piece"
    BeanValleyBeanstalk = "Bean Valley clouds solo vine chest"
    BeanValleyBeanstalkFrogCoin = "Bean Valley middle vine room freestanding frog coin"
    BeanValleyBeanstalkCoin1 = "Bean Valley middle vine room lowest freestanding coin"
    BeanValleyBeanstalkCoin2 = "Bean Valley middle vine room middle freestanding coin"
    BeanValleyBeanstalkCoin3 = "Bean Valley middle vine room highest freestanding coin"
    BeanValleyEastBeanstalkCoin1 = "Bean Valley east vine room lowest freestanding coin"
    BeanValleyEastBeanstalkCoin2 = "Bean Valley east vine room lower freestanding coin"
    BeanValleyEastBeanstalkCoin3 = "Bean Valley east vine room middle freestanding coin"
    BeanValleyEastBeanstalkCoin4 = "Bean Valley east vine room higher freestanding coin"
    BeanValleyEastBeanstalkCoin5 = "Bean Valley east vine room highest freestanding coin"
    BeanValleyWestBeanstalkCoin1 = "Bean Valley west vine room lower freestanding coin"
    BeanValleyWestBeanstalkCoin2 = "Bean Valley west vine room middle freestanding coin"
    BeanValleyWestBeanstalkCoin3 = "Bean Valley west vine room upper freestanding coin"
    BeanValleyWestBeanstalkFrogCoin = "Bean Valley west vine room freestanding frog coin"
    BeanValleyCloud1 = "Bean Valley clouds upper left chest"
    BeanValleyCloud2 = "Bean Valley clouds upper right chest"
    BeanValleyFall1 = "Bean Valley clouds lower left chest"
    BeanValleyFall2 = "Bean Valley clouds lower right chest"
    BeanValleyFirstVineRoomFrogCoin = "Bean Valley lowest vine room freestanding frog coin"
    BeanValleyFirstVineRoomMiddleCoin = "Bean Valley lowest vine room middle freestanding coin"
    BeanValleyFirstVineRoomUpperCoin = "Bean Valley lowest vine room upper freestanding coin"
    BeanValleyFirstVineRoomLowerCoin = "Bean Valley lowest vine room lower freestanding coin"
    CasinoGrateGuyPrize = "Grate Guy's Casino LOTW prize"
    NimbusLandShop = "Nimbus Land shop chest"
    NimbusLandInn = "Nimbus Land dream cushion 1st item"
    NimbusLandInn2 = "Nimbus Land dream cushion 2nd item"
    NimbusCastleBeforeBirdetta1 = "Nimbus Castle (occupied) 5-door room chest"
    NimbusCastleBeforeBirdetta2 = "Nimbus Castle west two-level room chest"
    NimbusCastleBirdetta = "Nimbus Castle giant egg prize"
    NimbusCastleStarPiece2 = "Nimbus Land giant egg boss Star Piece"
    NimbusCastleOutOfBounds1 = "Nimbus Castle west stairway room left chest"
    NimbusCastleOutOfBounds2 = "Nimbus Castle west stairway room right chest"
    NimbusCastleSingleGoldBird = "Nimbus Castle single gold bird room chest"
    NimbusCastleAfterEgg1 = "Nimbus Castle east two-level room lower chest"
    NimbusCastleAfterEgg2 = "Nimbus Castle east two-level room upper chest"
    NimbusCastleStarPiece3 = "Nimbus Land final boss Star Piece"
    NimbusCastleStarChest = "Nimbus Castle post-throne chest (occupied)"
    NimbusCastleStarAfterValentina = "Nimbus Castle post-throne chest (unoccupied)"
    NimbusCastleCornerChestAfterValentina = "Nimbus Castle (unoccupied) 5-door room chest"
    NimbusLandRightSide = "Nimbus Land post-invasion off-cloud item"
    DodoReward = "Nimbus Land Dodo's statue game prize"
    NimbusLandStarPiece1 = "Nimbus Land statue keeper boss Star Piece"
    NimbusLandPrisoners = "Nimbus Castle west cellar civilian"
    NimbusLandPrisoners2 = "Nimbus Castle west cellar guard"
    NimbusLandSignalRing = "Nimbus Land post-invasion upper right house"
    NimbusLandCellar = "Nimbus Castle post-invasion north cellar"
    BarrelVolcanoSecret1 = "Barrel Volcano secret room left chest"
    BarrelVolcanoSecret2 = "Barrel Volcano secret room right chest"
    BarrelVolcanoReverse = "Barrel Volcano reverse lava recoil frog coin"
    BarrelVolcanoDonut1 = "Barrel Volcano first donut lift room right freestanding frog coin"
    BarrelVolcanoDonut2 = "Barrel Volcano first donut lift room left freestanding frog coin"
    BarrelVolcanoLavaPool = "Barrel Volcano lava pool freestanding frog coin"
    BarrelVolcanoBeforeStar1 = "Barrel Volcano second arrow sign room left chest"
    BarrelVolcanoBeforeStar2 = "Barrel Volcano second arrow sign room right chest"
    BarrelVolcanoStarRoom = "Barrel Volcano star chest"
    BarrelVolcanoSaveRoom1 = "Barrel Volcano save room lower chest"
    BarrelVolcanoSaveRoom2 = "Barrel Volcano save room upper chest"
    BarrelVolcanoHinopio = "Barrel Volcano Hinopio shop chest"
    BarrelVolcanoBoss1 = "Barrel Volcano first boss Star Piece"
    BarrelVolcanoBoss2 = "Barrel Volcano second boss Star Piece"
    BowsersKeepDarkRoom = "Bowser's Keep dark room chest"
    BowsersKeepCrocoShop1 = "Bowser's Keep near first shop left chest"
    BowsersKeepCrocoShop2 = "Bowser's Keep near first shop right chest"
    BowsersKeepMagikoopa = "Bowser's Keep Magikoopa's room chest"
    BowsersKeepBossChester = "Bowser's Keep battle door Star Piece"
    BowsersKeepBoss1 = "Bowser's Keep first boss Star Piece"
    BowsersKeepInvisibleBridge1 = "Bowser's Keep 6-door invisble bridge bottom chest"
    BowsersKeepInvisibleBridge2 = "Bowser's Keep 6-door invisble bridge right chest"
    BowsersKeepInvisibleBridge3 = "Bowser's Keep 6-door invisble bridge left chest"
    BowsersKeepInvisibleBridge4 = "Bowser's Keep 6-door invisble bridge top chest"
    BowsersKeepInvisibleBridgeCoin1 = "Bowser's Keep 6-door invisble bridge bottom left coin"
    BowsersKeepInvisibleBridgeCoin2 = "Bowser's Keep 6-door invisble bridge bottom right coin"
    BowsersKeepInvisibleBridgeCoin3 = "Bowser's Keep 6-door invisble bridge top left coin"
    BowsersKeepInvisibleBridgeCoin4 = "Bowser's Keep 6-door invisble bridge top right coin"
    BowsersKeepMovingPlatforms1 = "Bowser's Keep X-Y platform room left exit chest"
    BowsersKeepMovingPlatforms2 = "Bowser's Keep X-Y platform room left entrance chest"
    BowsersKeepMovingPlatforms3 = "Bowser's Keep X-Y platform room right entrance chest"
    BowsersKeepMovingPlatforms4 = "Bowser's Keep X-Y platform room right exit chest"
    BowsersKeepElevatorPlatforms = "Bowser's Keep 6-door elevator platform room chest"
    BowsersKeepCannonballRoom1 = "Bowser's Keep cannonball room lower right chest"
    BowsersKeepCannonballRoom2 = "Bowser's Keep cannonball room exit chest"
    BowsersKeepCannonballRoom3 = "Bowser's Keep cannonball room lower left chest"
    BowsersKeepCannonballRoom4 = "Bowser's Keep cannonball room upper right chest"
    BowsersKeepCannonballRoom5 = "Bowser's Keep cannonball room upper left chest"
    BowsersKeepCannonballRoomCoin1 = "Bowser's Keep cannonball room freestanding coin 1"
    BowsersKeepCannonballRoomCoin2 = "Bowser's Keep cannonball room freestanding coin 2"
    BowsersKeepCannonballRoomCoin3 = "Bowser's Keep cannonball room freestanding coin 3"
    BowsersKeepCannonballRoomCoin4 = "Bowser's Keep cannonball room freestanding coin 4"
    BowsersKeepCannonballRoomCoin5 = "Bowser's Keep cannonball room freestanding coin 5"
    BowsersKeepCannonballRoomCoin6 = "Bowser's Keep cannonball room freestanding coin 6"
    BowsersKeepCannonballRoomCoin7 = "Bowser's Keep cannonball room freestanding coin 7"
    BowsersKeepCannonballRoomCoin8 = "Bowser's Keep cannonball room freestanding coin 8"
    BowsersKeepRotatingPlatforms1 = "Bowser's Keep rotating platform room entrance chest"
    BowsersKeepRotatingPlatforms2 = "Bowser's Keep rotating platform lower left chest"
    BowsersKeepRotatingPlatforms3 = "Bowser's Keep rotating platform right chest"
    BowsersKeepRotatingPlatforms4 = "Bowser's Keep rotating platform center chest"
    BowsersKeepRotatingPlatforms5 = "Bowser's Keep rotating platform upper left chest"
    BowsersKeepRotatingPlatforms6 = "Bowser's Keep rotating platform exit chest"
    BowsersKeepDoorReward1 = "Bowser's Keep door prize 1"
    BowsersKeepDoorReward2 = "Bowser's Keep door prize 2"
    BowsersKeepDoorReward3 = "Bowser's Keep door prize 3"
    BowsersKeepDoorReward4 = "Bowser's Keep door prize 4"
    BowsersKeepDoorReward5 = "Bowser's Keep door prize 5"
    BowsersKeepDoorReward6 = "Bowser's Keep door prize 6"
    BowsersKeepBoss2 = "Bowser's Keep second boss Star Piece"
    BowsersKeepBoss3 = "Bowser's Keep third boss Star Piece"
    FactorySaveRoom = "Outer Factory early save room chest"
    FactoryBoltPlatforms = "Outer Factory bot platform chest"
    FactoryBoss1 = "Outer Factory first boss Star Piece"
    FactoryFallingAxems = "Outer Factory falling axem room chest"
    FactoryTreasurePit1 = "Outer Factory pit back chest"
    FactoryTreasurePit2 = "Outer Factory pit front chest"
    FactoryConveyorPlatforms1 = "Outer Factory conveyor room right chest"
    FactoryConveyorPlatforms2 = "Outer Factory conveyor room left chest"
    FactoryBehindSnakes1 = "Outer Factory room behind machine yarid right chest"
    FactoryBehindSnakes2 = "Outer Factory room behind machine yarid left chest"
    FactoryBoss2 = "Outer Factory second boss Star Piece"
    FactoryToadGift = "Inner Factory toad gift"
    InnerFactoryBoss1 = "Inner Factory first boss Star Piece"
    InnerFactoryBoss2 = "Inner Factory second boss Star Piece"
    InnerFactoryBoss3 = "Inner Factory third boss Star Piece"
    InnerFactoryBoss4 = "Inner Factory fourth boss Star Piece"
    InnerFactoryBossFinal = "Factory final boss Star Piece"

regular_checks = [ # excludes key item checks. can't turn those off
    ShuffleLocationSelector.MariosPadStarter1,
    ShuffleLocationSelector.MariosPadStarter2,
    ShuffleLocationSelector.MariosPadStarter3,
    ShuffleLocationSelector.MariosPadStarter4,

    ShuffleLocationSelector.MushroomWay1,
    ShuffleLocationSelector.MushroomWay2,
    ShuffleLocationSelector.MushroomWay3,
    ShuffleLocationSelector.MushroomWay4,
    ShuffleLocationSelector.HammerBrosReward,

    ShuffleLocationSelector.MushroomKingdomHallway,
    ShuffleLocationSelector.PeachSurprise,
    ShuffleLocationSelector.MushroomKingdomVault1,
    ShuffleLocationSelector.MushroomKingdomVault2,
    ShuffleLocationSelector.MushroomKingdomVault3,
    ShuffleLocationSelector.MushroomKingdomStore,
    ShuffleLocationSelector.MushroomKingdomStoreBasement1,
    ShuffleLocationSelector.MushroomKingdomStoreBasement2,
    ShuffleLocationSelector.MushroomKingdomInn,

    ShuffleLocationSelector.BanditsWay1,
    ShuffleLocationSelector.BanditsWay2,
    ShuffleLocationSelector.BanditsWayStarChest,
    ShuffleLocationSelector.BanditsWayDogJump,
    ShuffleLocationSelector.BanditsWayCroco,
    ShuffleLocationSelector.Croco1Reward2,

    ShuffleLocationSelector.PandoriteChest,
    ShuffleLocationSelector.PandoriteReward1,
    ShuffleLocationSelector.PandoriteReward2,
    ShuffleLocationSelector.KeroSewersPandoriteRoom,
    ShuffleLocationSelector.KeroSewersStarChest,
    ShuffleLocationSelector.KeroSewersBeforeBelomeLower,

    ShuffleLocationSelector.MidasRiverFirstTime,

    ShuffleLocationSelector.CricketJamReward,
    ShuffleLocationSelector.CricketPieReward,

    ShuffleLocationSelector.RoseWayFiveChests1,
    ShuffleLocationSelector.RoseWayFiveChests2,
    ShuffleLocationSelector.RoseWayFiveChests3,
    ShuffleLocationSelector.RoseWayFiveChests4,
    ShuffleLocationSelector.RoseWayFiveChests5,
    ShuffleLocationSelector.RoseWayPlatform,

    ShuffleLocationSelector.RoseTownStore1,
    ShuffleLocationSelector.RoseTownStore2,
    ShuffleLocationSelector.RoseTownTreasureHouse1,
    ShuffleLocationSelector.RoseTownTreasureHouse2,
    ShuffleLocationSelector.RoseTownTreasureHouse3,
    ShuffleLocationSelector.RoseTownToad,
    ShuffleLocationSelector.Gaz,
    ShuffleLocationSelector.RoseTownTreasureHouseMazeReward,
    ShuffleLocationSelector.GardenerCloud1,
    ShuffleLocationSelector.GardenerCloud2,

    ShuffleLocationSelector.ForestMaze1,
    ShuffleLocationSelector.ForestMaze2,
    ShuffleLocationSelector.ForestMazeUnderground1,
    ShuffleLocationSelector.ForestMazeUnderground2,
    ShuffleLocationSelector.ForestMazeUnderground3,
    ShuffleLocationSelector.ForestMazeRedEssence,
    ShuffleLocationSelector.ForestMazeSecret1,
    ShuffleLocationSelector.ForestMazeSecret2,
    ShuffleLocationSelector.ForestMazeSecret3,
    ShuffleLocationSelector.ForestMazeSecret4,
    ShuffleLocationSelector.ForestMazeSecret5,

    ShuffleLocationSelector.PipeVaultSlide1,
    ShuffleLocationSelector.PipeVaultSlide2,
    ShuffleLocationSelector.PipeVaultSlide3,
    ShuffleLocationSelector.GoombaThumping1,
    ShuffleLocationSelector.GoombaThumping2,
    ShuffleLocationSelector.PipeVaultNippers1,
    ShuffleLocationSelector.PipeVaultNippers2,

    ShuffleLocationSelector.YosterIsleEntrance,
    ShuffleLocationSelector.YosterIsleRaceReward1,
    ShuffleLocationSelector.YosterIsleRaceReward2,
    ShuffleLocationSelector.YosterIsleRaceReward3,

    ShuffleLocationSelector.MolevilleMinesStarChest,
    ShuffleLocationSelector.MolevilleMinesCoins,
    ShuffleLocationSelector.MolevilleMinesPunchinello1,
    ShuffleLocationSelector.MolevilleMinesPunchinello2,
    ShuffleLocationSelector.TreasureSeller1,
    ShuffleLocationSelector.TreasureSeller2,
    ShuffleLocationSelector.TreasureSeller3,
    ShuffleLocationSelector.BucketGirl,

    ShuffleLocationSelector.BoosterPass1,
    ShuffleLocationSelector.BoosterPass2,
    ShuffleLocationSelector.BoosterPassSecret1,
    ShuffleLocationSelector.BoosterPassSecret2,
    ShuffleLocationSelector.BoosterPassSecret3,

    ShuffleLocationSelector.BoosterTowerSpookum,
    ShuffleLocationSelector.BoosterTowerRailway,
    ShuffleLocationSelector.BoosterTowerMasher,
    ShuffleLocationSelector.BoosterTowerThwomp,
    ShuffleLocationSelector.BoosterTowerParachute,
    ShuffleLocationSelector.BoosterTowerTop1,
    ShuffleLocationSelector.BoosterTowerTop2,
    ShuffleLocationSelector.BoosterTowerTop3,
    
    ShuffleLocationSelector.MarrymoreInn,
    ShuffleLocationSelector.MarrymorePrize1,
    ShuffleLocationSelector.MarrymorePrize2,
    ShuffleLocationSelector.MarrymorePrize3,
    ShuffleLocationSelector.MarrymorePrize4,
    ShuffleLocationSelector.MarrymorePrize5,
    ShuffleLocationSelector.MarrymorePrize6,

    ShuffleLocationSelector.FrogDisciple1,
    ShuffleLocationSelector.FrogDisciple2,
    ShuffleLocationSelector.FrogDisciple3,
    ShuffleLocationSelector.FrogDisciple4,
    ShuffleLocationSelector.FrogDisciple5,
    ShuffleLocationSelector.SeasideTownRescue,

    ShuffleLocationSelector.SeaStarChest,
    ShuffleLocationSelector.SeaSaveRoom1,
    ShuffleLocationSelector.SeaSaveRoom2,
    ShuffleLocationSelector.SeaSaveRoom3,
    ShuffleLocationSelector.SeaWhirlpoolChest,

    ShuffleLocationSelector.SunkenShipRatStairs,
    ShuffleLocationSelector.SunkenShipCannonballPuzzle,
    ShuffleLocationSelector.SunkenShip3DMaze,
    ShuffleLocationSelector.SunkenShipShop,
    ShuffleLocationSelector.SunkenShipCoins1,
    ShuffleLocationSelector.SunkenShipCoins2,
    ShuffleLocationSelector.SunkenShipCloneRoom,
    ShuffleLocationSelector.SunkenShipFrogCoinRoom,
    ShuffleLocationSelector.SunkenShipHidonMushroom,
    ShuffleLocationSelector.HidonChest,
    ShuffleLocationSelector.HidonReward1,
    ShuffleLocationSelector.HidonReward2,
    ShuffleLocationSelector.SunkenShipSafetyRing,
    ShuffleLocationSelector.SunkenShipBandanaReds,

    ShuffleLocationSelector.LandsEndRedEssence,
    ShuffleLocationSelector.LandsEndChowPit1,
    ShuffleLocationSelector.LandsEndChowPit2,
    ShuffleLocationSelector.LandsEndBeeRoom,
    ShuffleLocationSelector.LandsEndSecret1,
    ShuffleLocationSelector.LandsEndSecret2,
    ShuffleLocationSelector.LandsEndShyAway,
    ShuffleLocationSelector.LandsEndStarChest1,
    ShuffleLocationSelector.LandsEndStarChest2,
    ShuffleLocationSelector.LandsEndStarChest3,
    ShuffleLocationSelector.TroopaClimb,

    ShuffleLocationSelector.BelomeTempleFortuneTeller,
    ShuffleLocationSelector.BelomeTempleFortune1,
    ShuffleLocationSelector.BelomeTempleFortune2,
    ShuffleLocationSelector.BelomeTempleFortune3,
    ShuffleLocationSelector.BelomeTempleFortune4,
    ShuffleLocationSelector.BelomeTempleAfterFortune1,
    ShuffleLocationSelector.BelomeTempleAfterFortune2,
    ShuffleLocationSelector.BelomeTempleAfterFortune3,
    ShuffleLocationSelector.BelomeTempleAfterFortune4,
    ShuffleLocationSelector.BelomeTempleTreasure1,
    ShuffleLocationSelector.BelomeTempleTreasure2,
    ShuffleLocationSelector.BelomeTempleTreasure3,

    ShuffleLocationSelector.MonstroTownEntrance,
    ShuffleLocationSelector.JinxDojoReward,
    ShuffleLocationSelector.CulexReward,
    ShuffleLocationSelector.SuperJumps100,
    ShuffleLocationSelector.SuperJumps30,
    ShuffleLocationSelector.ThreeMustyFears,

    ShuffleLocationSelector.BeanValley1,
    ShuffleLocationSelector.BeanValley2,
    ShuffleLocationSelector.BeanValleyLeftPiranhaPipe,
    ShuffleLocationSelector.BeanValleyBottomLeftPiranhaPipe,
    ShuffleLocationSelector.BeanValleyBottomRightPiranhaPipeLower,
    ShuffleLocationSelector.BeanValleyBottomRightPiranhaPipeUpper,
    ShuffleLocationSelector.BeanValleyBoxBoyRoom1,
    ShuffleLocationSelector.BeanValleyBoxBoyRoom2,
    ShuffleLocationSelector.BeanValleyPiranhaPlants,
    ShuffleLocationSelector.BeanValleyBeanstalk,
    ShuffleLocationSelector.BeanValleyCloud1,
    ShuffleLocationSelector.BeanValleyCloud2,
    ShuffleLocationSelector.BeanValleyFall1,
    ShuffleLocationSelector.BeanValleyFall2,

    ShuffleLocationSelector.CasinoGrateGuyPrize,

    ShuffleLocationSelector.NimbusLandInn,
    ShuffleLocationSelector.NimbusLandInn2,
    ShuffleLocationSelector.NimbusLandShop,
    ShuffleLocationSelector.NimbusCastleBeforeBirdetta2,
    ShuffleLocationSelector.NimbusCastleOutOfBounds1,
    ShuffleLocationSelector.NimbusCastleOutOfBounds2,
    ShuffleLocationSelector.NimbusLandPrisoners,
    ShuffleLocationSelector.NimbusCastleSingleGoldBird,
    ShuffleLocationSelector.NimbusCastleAfterEgg1,
    ShuffleLocationSelector.NimbusCastleAfterEgg2,
    ShuffleLocationSelector.NimbusCastleCornerChestAfterValentina,
    ShuffleLocationSelector.NimbusCastleStarAfterValentina,
    ShuffleLocationSelector.NimbusLandCellar,
    ShuffleLocationSelector.NimbusLandSignalRing,
    
    ShuffleLocationSelector.BarrelVolcanoSecret1,
    ShuffleLocationSelector.BarrelVolcanoSecret2,
    ShuffleLocationSelector.BarrelVolcanoBeforeStar1,
    ShuffleLocationSelector.BarrelVolcanoBeforeStar2,
    ShuffleLocationSelector.BarrelVolcanoStarRoom,
    ShuffleLocationSelector.BarrelVolcanoHinopio,
    ShuffleLocationSelector.BarrelVolcanoSaveRoom1,
    ShuffleLocationSelector.BarrelVolcanoSaveRoom2,

    ShuffleLocationSelector.BowsersKeepDarkRoom,
    ShuffleLocationSelector.BowsersKeepCrocoShop1,
    ShuffleLocationSelector.BowsersKeepCrocoShop2,
    ShuffleLocationSelector.BowsersKeepInvisibleBridge1,
    ShuffleLocationSelector.BowsersKeepInvisibleBridge2,
    ShuffleLocationSelector.BowsersKeepInvisibleBridge3,
    ShuffleLocationSelector.BowsersKeepInvisibleBridge4,
    ShuffleLocationSelector.BowsersKeepMovingPlatforms1,
    ShuffleLocationSelector.BowsersKeepMovingPlatforms2,
    ShuffleLocationSelector.BowsersKeepMovingPlatforms3,
    ShuffleLocationSelector.BowsersKeepMovingPlatforms4,
    ShuffleLocationSelector.BowsersKeepElevatorPlatforms,
    ShuffleLocationSelector.BowsersKeepCannonballRoom1,
    ShuffleLocationSelector.BowsersKeepCannonballRoom2,
    ShuffleLocationSelector.BowsersKeepCannonballRoom3,
    ShuffleLocationSelector.BowsersKeepCannonballRoom4,
    ShuffleLocationSelector.BowsersKeepCannonballRoom5,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms1,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms2,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms3,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms4,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms5,
    ShuffleLocationSelector.BowsersKeepRotatingPlatforms6,
    ShuffleLocationSelector.BowsersKeepDoorReward1,
    ShuffleLocationSelector.BowsersKeepDoorReward2,
    ShuffleLocationSelector.BowsersKeepDoorReward3,
    ShuffleLocationSelector.BowsersKeepDoorReward4,
    ShuffleLocationSelector.BowsersKeepDoorReward5,
    ShuffleLocationSelector.BowsersKeepDoorReward6,
    ShuffleLocationSelector.BowsersKeepMagikoopa,

    ShuffleLocationSelector.FactorySaveRoom,
    ShuffleLocationSelector.FactoryBoltPlatforms,
    ShuffleLocationSelector.FactoryFallingAxems,
    ShuffleLocationSelector.FactoryTreasurePit1,
    ShuffleLocationSelector.FactoryTreasurePit2,
    ShuffleLocationSelector.FactoryConveyorPlatforms1,
    ShuffleLocationSelector.FactoryConveyorPlatforms2,
    ShuffleLocationSelector.FactoryBehindSnakes1,
    ShuffleLocationSelector.FactoryBehindSnakes2,

    ShuffleLocationSelector.FactoryToadGift,
]

freestanding_checks = [
    # ShuffleLocationSelector.BanditsWayCoin1,
    # ShuffleLocationSelector.BanditsWayCoin2,
    # ShuffleLocationSelector.BanditsWayCoin3,

    ShuffleLocationSelector.MidasRiverBottomLeftCave,
    ShuffleLocationSelector.MidasRiverBottomRightCave,

    ShuffleLocationSelector.RoseWayMushroom,
    ShuffleLocationSelector.RoseWayFlower,
    # ShuffleLocationSelector.RoseWayCoin1,
    # ShuffleLocationSelector.RoseWayCoin2,
    # ShuffleLocationSelector.RoseWayCoin3,
    # ShuffleLocationSelector.RoseWayCoin4,
    # ShuffleLocationSelector.RoseWayCoin5,

    # ShuffleLocationSelector.PipeVaultSlideCoin1,
    # ShuffleLocationSelector.PipeVaultSlideCoin2,
    # ShuffleLocationSelector.PipeVaultSlideCoin3,
    # ShuffleLocationSelector.PipeVaultSlideCoin4,
    # ShuffleLocationSelector.PipeVaultSlideCoin5,
    ShuffleLocationSelector.PipeVaultSlideFrogCoin,

    ShuffleLocationSelector.MolevilleMinesShyGuy,
    
    ShuffleLocationSelector.BoosterPassBush,
    ShuffleLocationSelector.BoosterPassFlower,

    ShuffleLocationSelector.BoosterTowerParachuteCrevice,
    # ShuffleLocationSelector.BoosterTowerCoin1,
    # ShuffleLocationSelector.BoosterTowerCoin2,
    # ShuffleLocationSelector.BoosterTowerCoin3,
    # ShuffleLocationSelector.BoosterTowerCoin4,
    # ShuffleLocationSelector.BoosterTowerCoin5,
    # ShuffleLocationSelector.BoosterTowerCoin6,
    # ShuffleLocationSelector.BoosterTowerCoin7,
    # ShuffleLocationSelector.BoosterTowerCoin8,
    # ShuffleLocationSelector.BoosterTowerCoin9,
    ShuffleLocationSelector.BoosterTowerFrogCoin1,
    ShuffleLocationSelector.BoosterTowerFrogCoin2,
    ShuffleLocationSelector.BoosterTowerFrogCoin3,
    ShuffleLocationSelector.BoosterTowerFrogCoin4,
    
    ShuffleLocationSelector.SunkenShipRatStairsFlower,
    ShuffleLocationSelector.SunkenShipTroopaPuzzle,
    ShuffleLocationSelector.SunkenShipCoinSnake,
    ShuffleLocationSelector.SunkenShipTrampolinePuzzle,
    ShuffleLocationSelector.SunkenShipBarrelPuzzle,
    ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin1,
    ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin2,
    ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin3,
    ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin4,
    ShuffleLocationSelector.SunkenShipBlooberRoom,

    ShuffleLocationSelector.BelomeTempleTreasureFlower1,
    ShuffleLocationSelector.BelomeTempleTreasureFlower2,
    ShuffleLocationSelector.BelomeTempleTreasureFlower3,
    ShuffleLocationSelector.BelomeTempleTreasureFlower4,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin1,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin2,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin3,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin4,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin5,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin6,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin7,
    ShuffleLocationSelector.BelomeTempleTreasureFrogCoin8,

    ShuffleLocationSelector.BeanValleyBoxBoyRoomHidden,
    ShuffleLocationSelector.BeanValleyFirstVineRoomFrogCoin,
    # ShuffleLocationSelector.BeanValleyFirstVineRoomLowerCoin,
    # ShuffleLocationSelector.BeanValleyFirstVineRoomMiddleCoin,
    # ShuffleLocationSelector.BeanValleyFirstVineRoomUpperCoin,
    # ShuffleLocationSelector.BeanValleyBeanstalkCoin1,
    # ShuffleLocationSelector.BeanValleyBeanstalkCoin2,
    # ShuffleLocationSelector.BeanValleyBeanstalkCoin3,
    ShuffleLocationSelector.BeanValleyBeanstalkFrogCoin,
    # ShuffleLocationSelector.BeanValleyEastBeanstalkCoin1,
    # ShuffleLocationSelector.BeanValleyEastBeanstalkCoin2,
    # ShuffleLocationSelector.BeanValleyEastBeanstalkCoin3,
    # ShuffleLocationSelector.BeanValleyEastBeanstalkCoin4,
    # ShuffleLocationSelector.BeanValleyEastBeanstalkCoin5,
    # ShuffleLocationSelector.BeanValleyWestBeanstalkCoin1,
    # ShuffleLocationSelector.BeanValleyWestBeanstalkCoin2,
    # ShuffleLocationSelector.BeanValleyWestBeanstalkCoin3,
    ShuffleLocationSelector.BeanValleyWestBeanstalkFrogCoin,

    ShuffleLocationSelector.BarrelVolcanoLavaPool,
    ShuffleLocationSelector.BarrelVolcanoDonut1,
    ShuffleLocationSelector.BarrelVolcanoDonut2,
    ShuffleLocationSelector.BarrelVolcanoReverse,

    # ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin1,
    # ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin2,
    # ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin3,
    # ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin4,
    # ShuffleLocationSelector.BowsersKeepCannonballRoomCoin1,
    # ShuffleLocationSelector.BowsersKeepCannonballRoomCoin2,
    # ShuffleLocationSelector.BowsersKeepCannonballRoomCoin3,
    # ShuffleLocationSelector.BowsersKeepCannonballRoomCoin4,
    # ShuffleLocationSelector.BowsersKeepCannonballRoomCoin5,
    # ShuffleLocationSelector.BowsersKeepCannonballRoomCoin6,
    # ShuffleLocationSelector.BowsersKeepCannonballRoomCoin7,
    # ShuffleLocationSelector.BowsersKeepCannonballRoomCoin8,
]

class FireworksOptions(FlagOptions):
    """Enumeration for Fireworks flag option"""
    vanilla = "Vanilla"
    shuffle1 = "Shuffle Fireworks"
    progressive = "Shuffle Progressive Fireworks"


class WinConditions(FlagOptions):
    """Enumeration for win condition options"""
    factory = "Beat the final Factory boss"
    sealed = "Beat Monstro Town sealed door"
    stars = "Collect required Star Pieces"


class PlayableCharacters(FlagOptions):
    """Enumeration for win condition options"""
    mario = "Mario"
    mallow = "Mallow"
    geno = "Geno"
    bowser = "Bowser"
    toadstool = "Toadstool"
    random = "Random"

class EquipmentCharactersOptions(FlagOptions):
    vanilla = "Vanilla"
    v_accessories_all = "Vanilla, except anyone can wear any accessory"
    r_accessories_all = "Random, except anyone can wear any accessory"
    random = "Completely random"
    equip_all = "Anyone can equip anything"


class LearnableSpells(FlagOptions):
    Jump = spells.Jump.base_title
    FireOrb = spells.FireOrb.base_title
    SuperJump = spells.SuperJump.base_title
    SuperFlame = spells.SuperFlame.base_title
    UltraJump = spells.UltraJump.base_title
    UltraFlame = spells.UltraFlame.base_title
    Therapy = spells.Therapy.base_title
    GroupHug = spells.GroupHug.base_title
    SleepyTime = spells.SleepyTime.base_title
    ComeBack = spells.ComeBack.base_title
    Mute = spells.Mute.base_title
    PsychBomb = spells.PsychBomb.base_title
    Terrorize = spells.Terrorize.base_title
    PoisonGas = spells.PoisonGas.base_title
    Crusher = spells.Crusher.base_title
    BowserCrush = spells.BowserCrush.base_title
    GenoBeam = spells.GenoBeam.base_title
    GenoBoost = spells.GenoBoost.base_title
    GenoWhirl = spells.GenoWhirl.base_title
    GenoBlast = spells.GenoBlast.base_title
    GenoFlash = spells.GenoFlash.base_title
    Thunderbolt = spells.Thunderbolt.base_title
    HPRain = spells.HPRain.base_title
    Psychopath = spells.Psychopath.base_title
    Shocker = spells.Shocker.base_title
    Snowy = spells.Snowy.base_title
    StarRain = spells.StarRain.base_title


class EquipmentPropertiesOptions(FlagOptions):
    """Enumeration for win condition options"""
    vanilla = "Vanilla"
    some = "Some buffs added"
    random = "Completely random"


class EXPMultiplierOptions(FlagOptions):
    vanilla = "Default"
    double = "Double"
    triple = "Triple"


class BanditsWayGating(FlagOptions):
    """Enumeration for Bandit's Way gating flag option"""
    mario = "Recruit Mario"
    mallow = "Recruit Mallow"
    geno = "Recruit Geno"
    bowser = "Recruit Bowser"
    toadstool = "Recruit Toadstool"
    mushroomway = "Finish Mushroom Way"
    open = "Always open"


class ForestMazeGating(FlagOptions):
    """Enumeration for Forest Maze gating flag option"""
    mario = "Find Mario"
    mallow = "Find Mallow"
    geno = "Find Geno"
    bowser = "Find Bowser"
    toadstool = "Find Toadstool"
    pie = "Exchange Cricket Pie"
    open = "Always open"


class PipeVaultGating(FlagOptions):
    """Enumeration for Pipe Vault gating flag option"""
    mario = "Recruit Mario"
    mallow = "Recruit Mallow"
    geno = "Recruit Geno"
    bowser = "Recruit Bowser"
    toadstool = "Recruit Toadstool"
    forest = "Finish Forest Maze"
    open = "Always open"


class BoosterTowerGating(FlagOptions):
    """Enumeration for Booster Tower gating flag option"""
    mario = "Recruit Mario"
    mallow = "Recruit Mallow"
    geno = "Recruit Geno"
    bowser = "Recruit Bowser"
    toadstool = "Recruit Toadstool"
    mines = "Finish Moleville Mines"
    open = "Always open"


class MarrymoreGating(FlagOptions):
    """Enumeration for Marrymore gating flag option"""
    hill = "Finish Booster Hill"
    tower = "Finish Booster Tower"
    open = "Always open"


class SeaGating(FlagOptions):
    """Enumeration for Sea & Sunken Ship gating flag option"""
    mario = "Recruit Mario"
    mallow = "Recruit Mallow"
    geno = "Recruit Geno"
    bowser = "Recruit Bowser"
    toadstool = "Recruit Toadstool"
    star1 = "Collect 1 Star Piece"
    star2 = "Collect 2 Star Pieces"
    star3 = "Collect 3 Star Pieces"
    star4 = "Collect 4 Star Pieces"
    star5 = "Collect 5 Star Pieces"
    star6 = "Collect 6 Star Pieces"
    open = "Always open"


class YaridovichGating(FlagOptions):
    """Enumeration for Seaside boss gating flag option"""
    ship = "Finish Sunken Ship"
    open = "Always available"


class BelomeTempleGating(FlagOptions):
    """Enumeration for Belome Temple gating flag option"""
    seaside = "Finish Seaside Town"
    open = "Always open"



class MonstroTownGating(FlagOptions):
    """Enumeration for Monstro Town gating flag option"""
    landsend = "Finish Land's End"
    open = "Always open"


class BarrelVolcanoGating(FlagOptions):
    """Enumeration for Barrel Volcano gating flag option"""
    nimbus = "Finish Nimbus Land"
    open = "Always open"


class BowsersKeepGating(FlagOptions):
    """Enumeration for Bowser's Keep gating flag option"""
    star1 = "Collect 1 Star Piece"
    star2 = "Collect 2 Star Pieces"
    star3 = "Collect 3 Star Pieces"
    star4 = "Collect 4 Star Pieces"
    star5 = "Collect 5 Star Pieces"
    star6 = "Collect 6 Star Pieces"
    volcano = "Finish Barrel Volcano"
    open = "Always open"


class FactoryGating(FlagOptions):
    """Enumeration for Factory gating flag option"""
    open = "Open when Bowser's Keep is opened"
    keep = "Finish Bowser's Keep"
    star1 = "Collect 1 Star Piece"
    star2 = "Collect 2 Star Pieces"
    star3 = "Collect 3 Star Pieces"
    star4 = "Collect 4 Star Pieces"
    star5 = "Collect 5 Star Pieces"
    star6 = "Collect 6 Star Pieces"


class EXPChallengeOptions(FlagOptions):
    vanilla = "Vanilla"
    easystars = "Star Pieces (easy)"
    hardstars = "Star Pieces (hard)"
    easybosses = "Bosses (easy)"
    hardbosses = "Bosses (hard)"
    none = "None"


class ItemQualities(FlagOptions):
    """Enumeration for item shuffle quality option"""
    original = "Original item pool"
    t4 = "Completely random, unrestricted"
    t3 = "Completely random, exclude top-tier items"
    t2 = "Completely random, include some good items"
    t1 = "Completely random, bad items only"
    empty = "Completely empty"


class ShopQualities(FlagOptions):
    """Enumeration for shop shuffle quality option"""
    original = "Original shop pool"
    t4 = "Completely random, unrestricted"
    t3 = "Completely random, exclude top-tier items"
    t2 = "Completely random, include some good items"
    t1 = "Completely random, bad items only"
    empty = "Completely empty"


class AvailableMusic(FlagOptions):
    normal = music.NormalBattleMusic.name
    boss1 = music.MidbossMusic.name
    boss2 = music.BossMusic.name
    smithy = music.Smithy1Music.name
    culex = music.CulexMusic.name
    corn = music.CorndillyMusic.name


class SequenceType(enum.Enum):
    Sequence = enum.auto()
    Mold = enum.auto()