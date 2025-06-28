from django.core.management.base import BaseCommand
from randomizer.data.npcs import npcs
from randomizer.data.rooms.room import (
    Buffer,
    Partition,
    DestinationProps,
    RoomExit,
    MapExit,
    Event,
    BattlePackNPC,
    RegularNPC,
    ChestNPC,
    BattlePackClone,
    RegularClone,
    ChestClone,
    Room,
)
from randomizer.helpers.roomobjecttables import (
    object_type,
    event_initiator,
    post_battle_behaviour,
    radial_direction_table,
    music_table,
    edge_table,
    exit_type_table,
    location_table,
    room_table,
    partition_space_table,
    partition_buffer_table,
    ExitType,
)
from randomizer.logic.utils import isclass_or_instance

from randomizer.management.disassembler_common import (
    shortify,
    bit,
    dbyte,
    hbyte,
    named,
    con,
    byte,
    byte_int,
    short,
    short_int,
    build_table,
    use_table_name,
    get_flag_string,
    flags,
    con_int,
    flags_short,
    writeline,
    bit_bool_from_num,
)
from randomizer.helpers.npcmodeltables import (
    sprite_name_table,
    vram_store_table,
    shadow_size_table,
)


start = 0x148400
end = 0x14FFFF
ptrstart = 0x148000
ptrend = 0x1483FF

roomevent_start = 0x20E400
roomevent_end = 0x20FFFF  # might be 0x20FDC7
roomevent_ptrstart = 0x20E000
roomevent_ptrend = 0x20E3FF

roomexit_start = 0x1D3166
roomexit_end = 0x1D4904
roomexit_ptrstart = 0x1D2D64
roomexit_ptrend = 0x1D3165

partitionstart = 0x1DDE00
partitionend = 0x1DDFFF  # bumped up from 0x1DDFDF

npctable_start = 0x1DB800
npctable_end = 0x1DDDFF

ELIGIBLE_NPCS = [
    npcs.Mario,
    npcs.Toadstool,
    npcs.Bowser,
    npcs.Mallow,
    npcs.Geno,
    npcs.YellowYoshi,
    npcs.PinkYoshi,
    npcs.Boshi,
    npcs.Croco,
    npcs.RideYoshi,
    npcs.Booster,
    npcs.GreenYoshi,
    npcs.KingNimbus,
    npcs.QueenNimbus,
    npcs.JohnnySmall,
    npcs.ValentinaSmall,
    npcs.MagikoopaSmall,
    npcs.Frogfucius,
    npcs.Tadpole,
    npcs.Thwomp,
    npcs.BigThwomp,
    npcs.NimbusLandStatue,
    npcs.RedSmallToad,
    npcs.BlueToad,
    npcs.PinkToad,
    npcs.OldBlueToad,
    npcs.OldRedToad,
    npcs.GreenSmallToad,
    npcs.Chancellor,
    npcs.PaMole,
    npcs.MaMole,
    npcs.PinkMole,
    npcs.YellowMole,
    npcs.BlueNimbite,
    npcs.RedNimbite,
    npcs.BrownNimbite,
    npcs.GreenNimbite,
    npcs.NimbusGuard,
    npcs.Toadofsky,
    npcs.MallowDoll,
    npcs.BlueStarPiece,
    npcs.PurpleStarPiece,
    npcs.RedStarPiece,
    npcs.OrangeStarPiece,
    npcs.GreenStarPiece,
    npcs.IndigoStarPiece,
    npcs.YellowStarPiece,
    npcs.BowserDoll,
    npcs.ToadstoolDoll,
    npcs.TreasureChest,
    npcs.MidasRiverMario,
    npcs.Parachute,
    npcs.Barrel,
    npcs.WarpTrampoline,
    npcs.JumpTrampoline,
    npcs.Seesaw,
    npcs.SavePoint,
    npcs.Corkpedite,
    npcs.JBlock,
    npcs.YellowPlatform,
    npcs.WhirlpoolBubble,
    npcs.Hinopio,
    npcs.FactoryNut,
    npcs.GreenSwitch,
    npcs.RedToad,
    npcs.GreenToad,
    npcs.YellowToad,
    npcs.TurquoiseToad,
    npcs.PinkSmallToad,
    npcs.BlueSmallToad,
    npcs.OldBrownToad,
    npcs.OldGreenToad,
    npcs.OldDarkGreenToad,
    npcs.OldPinkToad,
    npcs.FatYoshi,
    npcs.PurpleSmallToad,
    npcs.FrogDisciple,
    npcs.ChompBehind,
    npcs.WigglerHead,
    npcs.BlockShadow,
    npcs.RedMagikoopa,
    npcs.WigglerBody,
    npcs.ParsonDodo,
    npcs.KnifeGuySmall,
    npcs.KnifeGuySmall2,
    npcs.Minecart,
    npcs.FlatFireball,
    npcs.PipePiranhaPlant,
    npcs.ThumpGoomba,
    npcs.BulletBill,
    npcs.GoldenBulletBill,
    npcs.ClerkSmall,
    npcs.LandsEndCannon,
    npcs.CommanderTroopa,
    npcs.BelomeStatue,
    npcs.ShyGuyClownCar,
    npcs.MachineBowyer,
    npcs.MachineYaridOverworld,
    npcs.GunyolkTop,
    npcs.GunyolkOuter,
    npcs.Crane,
    npcs.SpinningStarPiece,
    npcs.SmithyHammer,
    npcs.SmithyBodyOverworld,
    npcs.PoisonGas,
    npcs.DynaMite,
    npcs.FakeToad,
    npcs.FakeElder,
    npcs.Elder,
    npcs.Monstromama,
    npcs.NimbusGuardPurple,
    npcs.ManagerSmall,
    npcs.DirectorSmall,
    npcs.BoomerOverworld,
    npcs.DrTopper,
    npcs.StarPieceSparkle,
    npcs.GenoDoll,
    npcs.SmelterSection,
    npcs.AeroShot,
    npcs.GoldenChompBehind,
    npcs.GrateGuySmall,
    npcs.BlueStripedToad,
    npcs.RedStripedToad,
    npcs.PinkStripedToad,
    npcs.YellowStripedToad,
    npcs.OldBlueStripedToad,
    npcs.OldRedStripedToad,
    npcs.RedStripedSmallToad,
    npcs.PinkStripedSmallToad,
    npcs.Cannonball,
    npcs.Croco2,
    npcs.Jinx2,
    npcs.BigCoin,
    npcs.SmallCoin,
    npcs.FrogCoin,
    npcs.Ring,
    npcs.SparkleSideways,
    npcs.SparkleDown,
    npcs.FryingPan,
    npcs.Explosion,
    npcs.MokuraCloud,
    npcs.Shoes,
    npcs.MicroBombItem,
    npcs.Card,
    npcs.Brooch,
    npcs.Hammer,
    npcs.FroggieStick,
    npcs.ChompItem,
    npcs.Fan,
    npcs.RedMushroom,
    npcs.Teleport,
    npcs.GreenMushroom,
    npcs.YellowMushroom,
    npcs.Crown,
    npcs.GreenCandy,
    npcs.BlueCandy,
    npcs.RedSyrup,
    npcs.GreenSyrup,
    npcs.YellowSyrup,
    npcs.Banana,
    npcs.BlueSyrup,
    npcs.RedBomb,
    npcs.TinyStar,
    npcs.GreenBomb,
    npcs.YellowBomb,
    npcs.BlueBomb,
    npcs.GreenJuice,
    npcs.Egg,
    npcs.RedJuice,
    npcs.RDrink,
    npcs.DDrink,
    npcs.PDrink,
    npcs.FrogDrink,
    npcs.YellowMusicDrink,
    npcs.BlueMusicDrink,
    npcs.RedMusicDrink,
    npcs.StarDrink,
    npcs.RedShell,
    npcs.GreenShell,
    npcs.Parasol,
    npcs.Feather,
    npcs.Berry,
    npcs.Cookie,
    npcs.Beetle,
    npcs.Terrapin,
    npcs.Spikey,
    npcs.SkyTroopa,
    npcs.MadMallet,
    npcs.Shaman,
    npcs.Crook,
    npcs.Goomba,
    npcs.PiranhaPlant,
    npcs.Amanita,
    npcs.Goby,
    npcs.Bloober,
    npcs.BandanaRed,
    npcs.Lakitu,
    npcs.Birdy,
    npcs.Pinwheel,
    npcs.RatFunk,
    npcs.K9,
    npcs.Magmite,
    npcs.BigBoo,
    npcs.DryBones,
    npcs.Greaper,
    npcs.RedFireball,
    npcs.Chomp,
    npcs.PandoriteLarge,
    npcs.BobOmb,
    npcs.Spookum,
    npcs.HammerBroLarge,
    npcs.Buzzer,
    npcs.Ameboid,
    npcs.Gecko,
    npcs.Wiggler,
    npcs.Jawful,
    npcs.Guerrilla,
    npcs.Shogun,
    npcs.HeavyTropa,
    npcs.ClerkLarge,
    npcs.BoomerLarge,
    npcs.DodoLarge,
    npcs.TerraCotta,
    npcs.Spikester,
    npcs.Malakoopa,
    npcs.Pounder,
    npcs.Poundette,
    npcs.Sackit,
    npcs.GuGoomba,
    npcs.Chewy,
    npcs.BlueFireball,
    npcs.MrKipper,
    npcs.FactoryChief,
    npcs.BandanaBlue,
    npcs.ManagerLarge,
    npcs.Bluebird,
    npcs.AlleyRat,
    npcs.Chow,
    npcs.Magmus,
    npcs.LilBoo,
    npcs.Vomer,
    npcs.GlumReaper,
    npcs.HidonLarge,
    npcs.SlingShy,
    npcs.RobOmb,
    npcs.ShyGuy,
    npcs.Ninja,
    npcs.Stinger,
    npcs.Geckit,
    npcs.Jabit,
    npcs.MagikoopaLarge,
    npcs.DirectorLarge,
    npcs.Apprentice,
    npcs.GenoRedemption,
    npcs.BoxBoyLarge,
    npcs.Oerlikon,
    npcs.ChesterLarge,
    npcs.Torte,
    npcs.ShyAway,
    npcs.MachineShyster,
    npcs.MachineDrillBit,
    npcs.MarioClone,
    npcs.PeachClone,
    npcs.BowserClone,
    npcs.GenoClone,
    npcs.MallowClone,
    npcs.Shyster,
    npcs.HanginShy,
    npcs.MachineMack,
    npcs.MachineAxemPink,
    npcs.MachineAxemBlack,
    npcs.MachineAxemRed,
    npcs.MachineAxemYellow,
    npcs.MachineAxemGreen,
    npcs.Starslap,
    npcs.Mukumuku,
    npcs.Zeostar,
    npcs.Chompweed,
    npcs.Microbomb,
    npcs.Helio,
    npcs.KnifeGuyLarge,
    npcs.GrateGuyLarge,
    npcs.BundtLarge,
    npcs.Belome1Large,
    npcs.Smilax,
    npcs.Thrax,
    npcs.Megasmilax,
    npcs.BirdettaLarge,
    npcs.Eggbert,
    npcs.AxemYellow,
    npcs.PunchinelloLarge,
    npcs.AxemRed,
    npcs.AxemGreen,
    npcs.BundtSmall,
    npcs.CloakerLarge,
    npcs.MackLarge,
    npcs.YaridovichLarge,
    npcs.DrillBit,
    npcs.AxemPink,
    npcs.AxemBlack,
    npcs.BowyerLarge,
    npcs.AeroUpright,
    npcs.Snifit,
    npcs.JohnnyLarge,
    npcs.ValentinaLarge,
    npcs.CulexLarge,
    npcs.CountDownGridplane,
    npcs.MokuraLarge,
    npcs.PandoriteSmall,
    npcs.HidonSmall,
    npcs.ChesterSmall,
    npcs.BoxBoySmall,
    npcs.HammerBroSmall,
    npcs.MackSmall,
    npcs.Belome1Small,
    npcs.Belome2Small,
    npcs.BowyerSmall,
    npcs.PunchinelloSmall,
    npcs.DodoSmall,
    npcs.BirdettaSmall,
    npcs.CzarDragonSmall,
    npcs.BoomerSmall,
    npcs.ExorSmall,
    npcs.DominoSmall,
    npcs.SmithySmall,
    npcs.MarioDoll,
    npcs.GoldGoomba,
    npcs.BigFlower,
    npcs.SmallFrogCoin,
    npcs.Jinx1,
    npcs.Jinx3,
    npcs.TerrapinEnding,
    npcs.StumpetHead,
    npcs.StumpetRoot,
    npcs.CzarBody,
    npcs.VineBeanstalk,
    npcs.BrownBrick,
    npcs.SandWhirlpool,
    npcs.Letter,
    npcs.YaridOverworld,
    npcs.TentacleExtending,
    npcs.BackSnifit,
    npcs.DonutLift,
    npcs.NESProtagonist,
    npcs.SplashWaterDroplets,
    npcs.Fish,
    npcs.Geyser,
    npcs.BowyerOverworld,
    npcs.MushroomLamp,
    npcs.Link,
    npcs.Samus,
    npcs.GreyBlock,
    npcs.PlaneModel,
    npcs.GreyBrick,
    npcs.CulexSmall,
    npcs.CircularSparkle,
    npcs.Flower,
    npcs.RecoveryMushroom,
    npcs.Key,
    npcs.ItemBag,
    npcs.Music,
    npcs.TinyMushroom,
    npcs.DingalingGridplane,
    npcs.EggbertGridplane,
    npcs.FireCrystal,
    npcs.WaterCrystal,
    npcs.EarthCrystal,
    npcs.WindCrystal,
    npcs.GenoBullet,
    npcs.MackMedium,
    npcs.KnifeGuyGridplane,
    npcs.TinyBloober,
    npcs.TinyBird,
    npcs.SmithyLarge,
    npcs.Goombette,
    npcs.Empty,
]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

        parser.add_argument(
            "-d",
            "--debug",
            action="store_true",
            help="If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer",
        )

    def handle(self, *args, **options):
        debug = options["debug"]

        dest = "randomizer/data/rooms"
        if debug:
            dest = "randomizer/management/commands/output/disassembler/room"

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        rooms_raw_data = []
        roomevent_raw_data = []
        roomexit_raw_data = []
        partitions = []

        ptrs = []
        roomevent_ptrs = []
        roomexit_ptrs = []

        table_npcs = []

        for offset in range(npctable_start, npctable_end + 1, 7):
            if offset + 7 > npctable_end:
                break
            raw_data = rom[offset : (offset + 7)]
            if raw_data == bytearray([0xFF] * 7):
                continue
            sprite_val = ((raw_data[1] << 8) | raw_data[0]) & 0x03FF
            vram_store_val = (raw_data[1] >> 2) & 0x07
            vram_size = raw_data[1] >> 5
            priority0 = (raw_data[2] & 0x20) == 0x20  # bit 5
            priority1 = (raw_data[2] & 0x40) == 0x40  # bit 6
            priority2 = (raw_data[2] & 0x80) == 0x80  # bit 7
            byte2_bit0 = (raw_data[2] & 0x01) == 0x01  # bit 0
            byte2_bit1 = (raw_data[2] & 0x02) == 0x02  # bit 1
            byte2_bit2 = (raw_data[2] & 0x04) == 0x04  # bit 2
            byte2_bit3 = (raw_data[2] & 0x08) == 0x08  # bit 3
            byte2_bit4 = (raw_data[2] & 0x10) == 0x10  # bit 4
            y_pixel_shift = raw_data[3] & 0x0F
            shift_16_px_down = (raw_data[3] & 0x10) == 0x10  # bit 4
            shadow_val = (raw_data[3] & 0x60) >> 5
            cannot_clone = (raw_data[3] & 0x80) == 0x80  # bit 7
            acute_axis = raw_data[4] & 0x0F
            obtuse_axis = (raw_data[4] & 0xF0) >> 4

            height = raw_data[5] & 0x1F
            show_shadow = (raw_data[5] & 0x20) == 0x20  # bit 5
            byte5_bit6 = (raw_data[5] & 0x40) == 0x40  # bit 6
            byte5_bit7 = (raw_data[5] & 0x80) == 0x80  # bit 7

            byte6_bit2 = (raw_data[6] & 0x04) == 0x04  # bit 2

            y_pixel_shift = y_pixel_shift + (-16 if shift_16_px_down else 0)

            table_npcs.append(
                npcs.TableNPC(
                    sprite_val,
                    priority0,
                    priority1,
                    priority2,
                    show_shadow,
                    shadow_val,
                    y_pixel_shift,
                    acute_axis,
                    obtuse_axis,
                    height,
                    vram_store_val,
                    vram_size,
                    cannot_clone,
                    byte2_bit0,
                    byte2_bit1,
                    byte2_bit2,
                    byte2_bit3,
                    byte2_bit4,
                    byte5_bit6,
                    byte5_bit7,
                    byte6_bit2,
                )
            )

        for i in range(partitionstart, partitionend, 4):
            partition_data = rom[i : i + 4]
            allow_extra_sprite_buffer = partition_data[0] & 0x10 == 0x10
            full_palette_buffer = partition_data[0] & 0x80 == 0x80
            ally_sprite_buffer_size = (partition_data[0] & 0x60) >> 5
            extra_sprite_buffer_size = partition_data[0] & 0x0F
            clone_buffer_a_type = partition_data[1] & 0x07
            clone_buffer_a_space = (partition_data[1] & 0x70) >> 4
            clone_buffer_a_index_in_main = partition_data[1] & 0x80 == 0x80
            clone_buffer_b_type = partition_data[2] & 0x07
            clone_buffer_b_space = (partition_data[2] & 0x70) >> 4
            clone_buffer_b_index_in_main = partition_data[2] & 0x80 == 0x80
            clone_buffer_c_type = partition_data[3] & 0x07
            clone_buffer_c_space = (partition_data[3] & 0x70) >> 4
            clone_buffer_c_index_in_main = partition_data[3] & 0x80 == 0x80
            partitions.append(
                Partition(
                    ally_sprite_buffer_size,
                    allow_extra_sprite_buffer,
                    extra_sprite_buffer_size,
                    [
                        Buffer(
                            clone_buffer_a_type,
                            clone_buffer_a_space,
                            clone_buffer_a_index_in_main,
                        ),
                        Buffer(
                            clone_buffer_b_type,
                            clone_buffer_b_space,
                            clone_buffer_b_index_in_main,
                        ),
                        Buffer(
                            clone_buffer_c_type,
                            clone_buffer_c_space,
                            clone_buffer_c_index_in_main,
                        ),
                    ],
                    full_palette_buffer,
                )
            )

        for i in range(ptrstart, ptrend, 2):
            ptrs.append((0x14 << 16) | (shortify(rom, i)))
        for i in range(roomevent_ptrstart, roomevent_ptrend, 2):
            roomevent_ptrs.append((0x20 << 16) | (shortify(rom, i)))
        for i in range(roomexit_ptrstart, roomexit_ptrend, 2):
            roomexit_ptrs.append((0x1D << 16) | (shortify(rom, i)))
        lengths = []
        roomevent_lengths = []
        roomexit_lengths = []

        # get raw data per room
        for i in range(len(ptrs)):
            if i < len(ptrs) - 1:
                lengths.append(ptrs[i + 1] - ptrs[i])
                rooms_raw_data.append(rom[ptrs[i] : ptrs[i + 1]])
            else:
                lengths.append(end - ptrs[i])
                rooms_raw_data.append(rom[ptrs[i] : end])
        for i in range(len(roomevent_ptrs)):
            if i < len(roomevent_ptrs) - 1:
                roomevent_lengths.append(roomevent_ptrs[i + 1] - roomevent_ptrs[i])
                roomevent_raw_data.append(
                    rom[roomevent_ptrs[i] : roomevent_ptrs[i + 1]]
                )
            else:
                roomevent_lengths.append(roomevent_ptrend - roomevent_ptrs[i])
                roomevent_raw_data.append(rom[roomevent_ptrs[i] : roomevent_ptrend])
        for i in range(len(roomexit_ptrs)):
            if i < len(roomexit_ptrs) - 1:
                roomexit_lengths.append(roomexit_ptrs[i + 1] - roomexit_ptrs[i])
                roomexit_raw_data.append(rom[roomexit_ptrs[i] : roomexit_ptrs[i + 1]])
            else:
                roomexit_lengths.append(roomexit_end - roomexit_ptrs[i])
                roomexit_raw_data.append(rom[roomexit_ptrs[i] : roomexit_end])

        if len(rooms_raw_data) < 511:
            raise Exception(
                "npc pointer table had %i entries (needs at least 509)"
                % len(rooms_raw_data)
            )
        if len(roomevent_raw_data) < 511:
            raise Exception(
                "event tile pointer table had %i entries (needs at least 509)"
                % len(roomexit_raw_data)
            )
        if len(roomexit_raw_data) < 511:
            raise Exception(
                "exit field pointer table had %i entries (needs at least 509)"
                % len(roomexit_raw_data)
            )
        for i in range(len(rooms_raw_data)):
            d = rooms_raw_data[i]
            r = roomevent_raw_data[i]
            e = roomexit_raw_data[i]
            if i > 511:
                break
            if i > 509:
                d = []
                e = []

            file = open("%s/room_%i.py" % (dest, i), "w")

            writeline(file, "# AUTOGENERATED DO NOT EDIT!!")
            writeline(
                file, "# Run the following command if you need to rebuild the table"
            )
            writeline(file, "# python manage.py objectdisassembler --rom ROM")
            writeline(
                file,
                "from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace",
            )
            writeline(
                file,
                "from randomizer.data.rooms.room import Buffer, Partition, DestinationProps, RoomExit, MapExit, Event, BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone, Room",
            )
            writeline(file, "from randomizer.data import npcs")
            writeline(
                file,
                "from randomizer.helpers.npcmodeltables import SpriteName, VramStore, ShadowSize",
            )

            if len(d) == 0 and len(r) == 0 and len(e) == 0:
                writeline(file, "room = None")
                file.close()
                continue
            writeline(file, "room = Room(")

            # partition

            if len(d) == 0:
                partition = Partition()
            else:
                partition = partitions[d[0]]
            writeline(file, "    partition=Partition(")
            writeline(
                file,
                "        ally_sprite_buffer_size=%i,"
                % partition.ally_sprite_buffer_size,
            )
            writeline(
                file,
                "        allow_extra_sprite_buffer=%r,"
                % partition.allow_extra_sprite_buffer,
            )
            writeline(
                file,
                "        extra_sprite_buffer_size=%i,"
                % partition.extra_sprite_buffer_size,
            )
            writeline(file, "        buffers = [")
            writeline(file, "            Buffer(")
            buffer_type, _ = byte(
                prefix="PartitionBufferTypes", table=partition_buffer_table
            )([partition.buffers[0].buffer_type])
            writeline(file, "                buffer_type=%s," % buffer_type)
            main_buffer_space, _ = byte(
                prefix="PartitionMainSpace", table=partition_space_table
            )([partition.buffers[0].main_buffer_space])
            writeline(file, "                main_buffer_space=%s," % main_buffer_space)
            writeline(
                file,
                "                index_in_main_buffer=%r"
                % partition.buffers[0].index_in_main_buffer,
            )
            writeline(file, "            ),")
            writeline(file, "            Buffer(")
            buffer_type, _ = byte(
                prefix="PartitionBufferTypes", table=partition_buffer_table
            )([partition.buffers[1].buffer_type])
            writeline(file, "                buffer_type=%s," % buffer_type)
            main_buffer_space, _ = byte(
                prefix="PartitionMainSpace", table=partition_space_table
            )([partition.buffers[1].main_buffer_space])
            writeline(file, "                main_buffer_space=%s," % main_buffer_space)
            writeline(
                file,
                "                index_in_main_buffer=%r"
                % partition.buffers[1].index_in_main_buffer,
            )
            writeline(file, "            ),")
            writeline(file, "            Buffer(")
            buffer_type, _ = byte(
                prefix="PartitionBufferTypes", table=partition_buffer_table
            )([partition.buffers[2].buffer_type])
            writeline(file, "                buffer_type=%s," % buffer_type)
            main_buffer_space, _ = byte(
                prefix="PartitionMainSpace", table=partition_space_table
            )([partition.buffers[2].main_buffer_space])
            writeline(file, "                main_buffer_space=%s," % main_buffer_space)
            writeline(
                file,
                "                index_in_main_buffer=%r"
                % partition.buffers[2].index_in_main_buffer,
            )
            writeline(file, "            )")
            writeline(file, "        ],")
            writeline(
                file, "        full_palette_buffer=%r" % partition.full_palette_buffer
            )
            writeline(file, "    ),")

            # events

            if len(r) > 0:
                music, _ = byte(prefix="Music", table=music_table)([r[0]])
                writeline(file, "    music=%s," % music)
                loading_event = (r[2] << 8) + r[1]
                writeline(file, "    entrance_event=%i," % loading_event)

                j = 3
                event_triggers = []
                while j < len(r):
                    length_determinant = r[j + 1] & 0x80 == 0x80
                    if length_determinant == 0:
                        trigger_data = r[j : j + 5]
                        length = 1
                        f_bit = 0
                        byte_8_bit_4 = 0
                        j += 5
                    else:
                        trigger_data = r[j : j + 6]
                        length = 1 + (trigger_data[5] & 0x0F)
                        f_bit = (trigger_data[5] & 0x80) >> 7
                        byte_8_bit_4 = (trigger_data[5] & 0x10) >> 4
                        j += 6
                    event_triggers.append(
                        Event(
                            event=((trigger_data[1] & 0x7F) << 8) + trigger_data[0],
                            x=trigger_data[2] & 0x7F,
                            y=trigger_data[3] & 0x7F,
                            z=trigger_data[4] & 0x1F,
                            f=f_bit,
                            length=length,
                            height=(trigger_data[4] & 0xF0) >> 5,
                            nw_se_edge_active=trigger_data[2] & 0x80 == 0x80,
                            ne_sw_edge_active=trigger_data[3] & 0x80 == 0x80,
                            byte_8_bit_4=byte_8_bit_4 == 1,
                        )
                    )
                if len(event_triggers) > 0:
                    writeline(file, "    event_tiles=[")
                    for event in event_triggers:
                        writeline(file, "        Event(")
                        writeline(file, "            event=%i," % event.event)
                        writeline(file, "            x=%i," % event.x)
                        writeline(file, "            y=%i," % event.y)
                        writeline(file, "            z=%i," % event.z)
                        f, _ = byte(prefix="Edge", table=edge_table)([event.f])
                        if i == 284:
                            print(f)
                        writeline(file, "            f=%s," % f)
                        writeline(file, "            height=%i," % event.height)
                        writeline(file, "            length=%i," % event.length)
                        writeline(
                            file,
                            "            nw_se_edge_active=%r,"
                            % event.nw_se_edge_active,
                        )
                        writeline(
                            file,
                            "            ne_sw_edge_active=%r,"
                            % event.ne_sw_edge_active,
                        )
                        writeline(
                            file, "            byte_8_bit_4=%r," % event.byte_8_bit_4
                        )
                        writeline(file, "        ),")
                    writeline(file, "    ],")

            # exits

            if len(e) > 0:
                exit_fields = []
                j = 0
                while j < len(e):
                    offset = 0
                    field_data = e[j:]
                    exit_type = (field_data[1] & 0x60) >> 6
                    byte_2_bit_0 = field_data[1] & 0x01
                    byte_2_bit_1 = (field_data[1] & 0x02) >> 1
                    byte_2_bit_2 = (field_data[1] & 0x04) >> 2

                    length_determinant = field_data[1] & 0x80 == 0x80
                    dst = ((field_data[1] << 8) + field_data[0]) & 0x1FF

                    offset += 5
                    if exit_type == 0:  # room
                        offset += 3
                    if length_determinant == 0:
                        length = 1
                        f_bit = 0
                    else:
                        length = 1 + (field_data[offset] & 0x0F)
                        f_bit = (field_data[offset] & 0x80) >> 7
                        offset += 1
                    if exit_type == 0:  # room
                        dst_f_val = (field_data[7] & 0xF0) >> 5
                        exit_fields.append(
                            RoomExit(
                                x=field_data[2] & 0x7F,
                                y=field_data[3] & 0x7F,
                                z=field_data[4] & 0x1F,
                                f=f_bit,
                                length=length,
                                height=(field_data[4] & 0xF0) >> 5,
                                nw_se_edge_active=field_data[2] & 0x80 == 0x80,
                                ne_sw_edge_active=field_data[3] & 0x80 == 0x80,
                                byte_2_bit_2=byte_2_bit_2 == 1,
                                destination=dst,
                                show_message=(field_data[1] & 0x08) == 0x08,
                                dst_x=field_data[5] & 0x7F,
                                dst_y=field_data[6] & 0x7F,
                                dst_z=field_data[7] & 0x1F,
                                dst_z_half=(field_data[6] & 0x80) == 0x80,
                                dst_f=dst_f_val,
                                x_bit_7=(field_data[5] & 0x80) == 0x80,
                            )
                        )
                    else:  # world map location
                        dst &= 0xFF
                        exit_fields.append(
                            MapExit(
                                x=field_data[2] & 0x7F,
                                y=field_data[3] & 0x7F,
                                z=field_data[4] & 0x1F,
                                f=f_bit,
                                length=length,
                                height=(field_data[4] & 0xF0) >> 5,
                                nw_se_edge_active=field_data[2] & 0x80 == 0x80,
                                ne_sw_edge_active=field_data[3] & 0x80 == 0x80,
                                byte_2_bit_2=byte_2_bit_2 == 1,
                                destination=dst,
                                show_message=(field_data[1] & 0x08) == 0x08,
                                byte_2_bit_1=byte_2_bit_1 == 1,
                                byte_2_bit_0=byte_2_bit_0 == 1,
                            )
                        )
                    j += offset

                if len(exit_fields) > 0:
                    writeline(file, "    exit_fields=[")
                    for ex in exit_fields:
                        if ex.destination_type == ExitType.ROOM:
                            writeline(file, "        RoomExit(")
                        else:
                            writeline(file, "        MapExit(")
                        writeline(file, "            x=%i," % ex.x)
                        writeline(file, "            y=%i," % ex.y)
                        writeline(file, "            z=%i," % ex.z)
                        f, _ = byte(prefix="Edge", table=edge_table)([ex.f])
                        writeline(file, "            f=%s," % f)
                        writeline(file, "            length=%i," % ex.length)
                        writeline(file, "            height=%i," % ex.height)
                        writeline(
                            file,
                            "            nw_se_edge_active=%r," % ex.nw_se_edge_active,
                        )
                        writeline(
                            file,
                            "            ne_sw_edge_active=%r," % ex.ne_sw_edge_active,
                        )
                        writeline(
                            file, "            byte_2_bit_2=%r," % ex.byte_2_bit_2
                        )
                        if ex.destination_type == ExitType.ROOM:
                            dst, _ = byte(prefix="Rooms", table=room_table)(
                                [ex.destination]
                            )
                        else:
                            dst, _ = byte(prefix="Locations", table=location_table)(
                                [ex.destination]
                            )
                        writeline(file, "            destination=%s," % dst)
                        writeline(
                            file, "            show_message=%r," % ex.show_message
                        )
                        if ex.destination_type == ExitType.ROOM:
                            writeline(
                                file, "            dst_x=%i," % ex.destination_props.x
                            )
                            writeline(
                                file, "            dst_y=%i," % ex.destination_props.y
                            )
                            writeline(
                                file, "            dst_z=%i," % ex.destination_props.z
                            )
                            writeline(
                                file,
                                "            dst_z_half=%i,"
                                % ex.destination_props.z_half,
                            )
                            dst_f, _ = byte(
                                prefix="RadialDirection", table=radial_direction_table
                            )([ex.destination_props.f])
                            writeline(file, "            dst_f=%s," % dst_f)
                            writeline(
                                file,
                                "            x_bit_7=%r,"
                                % ex.destination_props.x_bit_7,
                            )
                        else:
                            writeline(
                                file, "            byte_2_bit_1=%r," % ex.byte_2_bit_1
                            )
                            writeline(
                                file, "            byte_2_bit_0=%r," % ex.byte_2_bit_0
                            )

                        writeline(file, "        ),")
                    writeline(file, "    ],")

            if len(d) > 0:
                room_objects = []
                offset = 1
                n = 0
                while offset < len(d):
                    l = 12
                    otype = d[offset] >> 4
                    speed = d[offset + 1] & 0x07
                    base_assigned_npc = ((d[offset + 4] & 0x0F) << 6) + (
                        d[offset + 3] >> 2
                    )
                    base_action_script = ((d[offset + 5] & 0x3F) << 4) + (
                        (d[offset + 4] & 0xFF) >> 4
                    )
                    initiator = d[offset + 7] >> 4
                    if otype == 0:  # regular
                        base_event = ((d[offset + 7] & 0x0F) << 8) + d[offset + 6]
                        event = base_event + (d[offset + 8] >> 5)
                        assigned_npc = base_assigned_npc + (d[offset + 8] & 0x07)
                        action_script = base_action_script + (
                            (d[offset + 8] & 0x1F) >> 3
                        )
                    elif otype == 1:  # chest
                        base_event = ((d[offset + 7] & 0x0F) << 8) + d[offset + 6]
                        event = base_event
                        assigned_npc = base_assigned_npc
                        action_script = base_action_script
                        upper_70a7 = d[offset + 8] >> 4
                        lower_70a7 = d[offset + 8] & 0x0F
                    else:  # battle
                        assigned_npc = base_assigned_npc
                        action_script = base_action_script + (d[offset + 8] & 0x0F)
                        after_battle = d[offset + 7] & 0x0F
                        base_pack = d[offset + 6]
                        pack = base_pack + (d[offset + 8] >> 4)
                    visible = bit_bool_from_num(d[offset + 9], 7)
                    x = d[offset + 9] & 0x7F
                    y = d[offset + 10] & 0x7F
                    z = d[offset + 11] & 0x1F
                    z_half = bit_bool_from_num(d[offset + 10], 7)
                    direction = d[offset + 11] >> 5
                    face_on_trigger = bit_bool_from_num(d[offset + 1], 3)
                    cant_enter_doors = bit_bool_from_num(d[offset + 1], 4)
                    byte2_bit5 = bit_bool_from_num(d[offset + 1], 5)
                    set_sequence_playback = bit_bool_from_num(d[offset + 1], 6)
                    cant_float = bit_bool_from_num(d[offset + 1], 7)
                    cant_walk_up_stairs = bit_bool_from_num(d[offset + 2], 0)
                    cant_walk_under = bit_bool_from_num(d[offset + 2], 1)
                    cant_pass_walls = bit_bool_from_num(d[offset + 2], 2)
                    cant_jump_through = bit_bool_from_num(d[offset + 2], 3)
                    cant_pass_npcs = bit_bool_from_num(d[offset + 2], 4)
                    byte3_bit5 = bit_bool_from_num(d[offset + 2], 5)
                    cant_walk_through = bit_bool_from_num(d[offset + 2], 6)
                    byte3_bit7 = bit_bool_from_num(d[offset + 2], 7)
                    slidable_along_walls = bit_bool_from_num(d[offset + 3], 0)
                    cant_move_if_in_air = bit_bool_from_num(d[offset + 3], 1)
                    byte7_upper2 = d[offset + 5] >> 6

                    npc_from_table = table_npcs[assigned_npc]
                    sprite_match = npc_from_table.sprite_id

                    npc_class = next(
                        (x for x in ELIGIBLE_NPCS if x.sprite_id == sprite_match), None
                    )
                    if npc_class is None:
                        raise Exception(
                            "could not find a NPC matching sprite with ID %i in room %i"
                            % (sprite_match, i),
                        )

                    ending_args = [
                        speed,
                        visible,
                        x,
                        y,
                        z,
                        z_half,
                        direction,
                        face_on_trigger,
                        cant_enter_doors,
                        byte2_bit5,
                        set_sequence_playback,
                        cant_float,
                        cant_walk_up_stairs,
                        cant_walk_under,
                        cant_pass_walls,
                        cant_jump_through,
                        cant_pass_npcs,
                        byte3_bit5,
                        cant_walk_through,
                        byte3_bit7,
                        slidable_along_walls,
                        cant_move_if_in_air,
                        byte7_upper2,
                        npc_from_table.priority_0,
                        npc_from_table.priority_1,
                        npc_from_table.priority_2,
                        None
                        if npc_class.show_shadow == npc_from_table.show_shadow
                        else npc_from_table.show_shadow,
                        None
                        if npc_class.acute_axis == npc_from_table.acute_axis
                        else npc_from_table.acute_axis,
                        None
                        if npc_class.obtuse_axis == npc_from_table.obtuse_axis
                        else npc_from_table.obtuse_axis,
                        None
                        if npc_class.height == npc_from_table.height
                        else npc_from_table.height,
                        None
                        if npc_class.directions == npc_from_table.directions
                        else npc_from_table.directions,
                        None
                        if npc_class.min_vram_size == npc_from_table.vram_size
                        else npc_from_table.vram_size,
                        npc_from_table.cannot_clone,
                        None
                        if npc_class.byte2_bit0 == npc_from_table.byte2_bit0
                        else npc_from_table.byte2_bit0,
                        None
                        if npc_class.byte2_bit1 == npc_from_table.byte2_bit1
                        else npc_from_table.byte2_bit1,
                        None
                        if npc_class.byte2_bit2 == npc_from_table.byte2_bit2
                        else npc_from_table.byte2_bit2,
                        None
                        if npc_class.byte2_bit3 == npc_from_table.byte2_bit3
                        else npc_from_table.byte2_bit3,
                        None
                        if npc_class.byte2_bit4 == npc_from_table.byte2_bit4
                        else npc_from_table.byte2_bit4,
                        None
                        if npc_class.byte5_bit6 == npc_from_table.byte5_bit6
                        else npc_from_table.byte5_bit6,
                        None
                        if npc_class.byte5_bit7 == npc_from_table.byte5_bit7
                        else npc_from_table.byte5_bit7,
                        None
                        if npc_class.byte6_bit2 == npc_from_table.byte6_bit2
                        else npc_from_table.byte6_bit2,
                        None
                        if npc_class.y_shift == npc_from_table.y_shift
                        else npc_from_table.y_shift,
                    ]

                    # start comparing properties of npc_from_table vs npc_class
                    if otype == 0:  # regular
                        npcType = RegularNPC
                        args = [
                            npc_class,
                            initiator,
                            event,
                            action_script,
                        ] + ending_args
                    elif otype == 1:  # chest
                        npcType = ChestNPC
                        args = [
                            npc_class,
                            initiator,
                            event,
                            action_script,
                            upper_70a7,
                            lower_70a7,
                        ] + ending_args
                    else:  # battle
                        npcType = BattlePackNPC
                        args = [
                            npc_class,
                            initiator,
                            after_battle,
                            pack,
                            action_script,
                        ] + ending_args
                    thisNPC = npcType(*args)

                    room_objects.append(thisNPC)

                    n += 1

                    extra_length = d[offset] & 0x0F
                    if extra_length > 0:
                        l += extra_length * 4
                        for o in range(offset + 12, offset + l - 1, 4):

                            if otype == 0:  # regular
                                npcType = RegularClone
                                assigned_npc = base_assigned_npc + (d[o] & 0x07)
                                event = base_event + (d[o] >> 5)
                                action_script = base_action_script + (
                                    (d[o] & 0x1F) >> 3
                                )
                            elif otype == 1:  # chest
                                npcType = ChestClone
                                upper_70a7 = d[o] >> 4
                                lower_70a7 = d[o] & 0x0F
                            else:  # battle
                                npcType = BattlePackClone
                                action_script = base_action_script + (d[o] & 0x0F)
                                pack = base_pack + (d[o] >> 4)

                            npc_from_table = table_npcs[assigned_npc]
                            sprite_match = npc_from_table.sprite_id

                            npc_class = next(
                                (
                                    x
                                    for x in ELIGIBLE_NPCS
                                    if x.sprite_id == sprite_match
                                ),
                                None,
                            )
                            if npc_class is None:
                                raise Exception(
                                    "could not find a NPC matching sprite with ID %i in room %i",
                                    (sprite_match, i),
                                )

                            # print(npc_from_table.cannot_clone)

                            ending_args = [
                                bit_bool_from_num(d[o + 1], 7),
                                (d[o + 1] & 0x7F),
                                (d[o + 2] & 0x7F),
                                (d[o + 3] & 0x1F),
                                bit_bool_from_num(d[o + 2], 7),
                                (d[o + 3] >> 5),
                                npc_from_table.priority_0,
                                npc_from_table.priority_1,
                                npc_from_table.priority_2,
                                None
                                if npc_class.show_shadow == npc_from_table.show_shadow
                                else npc_from_table.show_shadow,
                                None
                                if npc_class.y_shift == npc_from_table.y_shift
                                else npc_from_table.y_shift,
                                None
                                if npc_class.acute_axis == npc_from_table.acute_axis
                                else npc_from_table.acute_axis,
                                None
                                if npc_class.obtuse_axis == npc_from_table.obtuse_axis
                                else npc_from_table.obtuse_axis,
                                None
                                if npc_class.height == npc_from_table.height
                                else npc_from_table.height,
                                None
                                if npc_class.directions == npc_from_table.directions
                                else npc_from_table.directions,
                                None
                                if npc_class.min_vram_size == npc_from_table.vram_size
                                else npc_from_table.vram_size,
                                npc_from_table.cannot_clone,
                                None
                                if npc_class.byte2_bit0 == npc_from_table.byte2_bit0
                                else npc_from_table.byte2_bit0,
                                None
                                if npc_class.byte2_bit1 == npc_from_table.byte2_bit1
                                else npc_from_table.byte2_bit1,
                                None
                                if npc_class.byte2_bit2 == npc_from_table.byte2_bit2
                                else npc_from_table.byte2_bit2,
                                None
                                if npc_class.byte2_bit3 == npc_from_table.byte2_bit3
                                else npc_from_table.byte2_bit3,
                                None
                                if npc_class.byte2_bit4 == npc_from_table.byte2_bit4
                                else npc_from_table.byte2_bit4,
                                None
                                if npc_class.byte5_bit6 == npc_from_table.byte5_bit6
                                else npc_from_table.byte5_bit6,
                                None
                                if npc_class.byte5_bit7 == npc_from_table.byte5_bit7
                                else npc_from_table.byte5_bit7,
                                None
                                if npc_class.byte6_bit2 == npc_from_table.byte6_bit2
                                else npc_from_table.byte6_bit2,
                            ]

                            if otype == 0:  # regular
                                args = [npc_class, event, action_script] + ending_args
                            elif otype == 1:  # chest
                                args = [npc_class, lower_70a7, upper_70a7] + ending_args
                            else:  # battle
                                args = [npc_class, pack, action_script] + ending_args
                            thisNPC = npcType(*args)

                            room_objects.append(thisNPC)
                    offset += l

                writeline(file, "    objects=[")
                for index, obj in enumerate(room_objects):
                    if isclass_or_instance(obj, BattlePackNPC):
                        writeline(file, "        BattlePackNPC( # %i" % index)
                    elif isclass_or_instance(obj, RegularNPC):
                        writeline(file, "        RegularNPC( # %i" % index)
                    elif isclass_or_instance(obj, ChestNPC):
                        writeline(file, "        ChestNPC( # %i" % index)
                    elif isclass_or_instance(obj, BattlePackClone):
                        writeline(file, "        BattlePackClone( # %i" % index)
                    elif isclass_or_instance(obj, RegularClone):
                        writeline(file, "        RegularClone( # %i" % index)
                    elif isclass_or_instance(obj, ChestClone):
                        writeline(file, "        ChestClone( # %i" % index)
                    else:
                        raise Exception("unknown class")
                    writeline(
                        file,
                        "            occupant=npcs.%s," % obj.model.occupant.__name__,
                    )
                    if (
                        isclass_or_instance(obj, BattlePackNPC)
                        or isclass_or_instance(obj, RegularNPC)
                        or isclass_or_instance(obj, ChestNPC)
                    ):
                        initiator, _ = byte(prefix="Initiator", table=event_initiator)(
                            [obj.initiator]
                        )
                        writeline(file, "            initiator=%s," % initiator)
                    if isclass_or_instance(obj, BattlePackNPC):
                        postbattle, _ = byte(
                            prefix="PostBattle", table=post_battle_behaviour
                        )([obj.after_battle])
                        writeline(file, "            after_battle=%s," % postbattle)
                    if isclass_or_instance(obj, BattlePackNPC) or isclass_or_instance(
                        obj, BattlePackClone
                    ):
                        writeline(file, "            battle_pack=%i," % obj.battle_pack)
                    if (
                        isclass_or_instance(obj, RegularNPC)
                        or isclass_or_instance(obj, RegularClone)
                        or isclass_or_instance(obj, ChestNPC)
                    ):
                        writeline(
                            file, "            event_script=%i," % obj.event_script
                        )
                    if (
                        isclass_or_instance(obj, RegularNPC)
                        or isclass_or_instance(obj, BattlePackNPC)
                        or isclass_or_instance(obj, ChestNPC)
                        or isclass_or_instance(obj, RegularClone)
                        or isclass_or_instance(obj, BattlePackClone)
                    ):
                        writeline(
                            file, "            action_script=%i," % obj.action_script
                        )
                    if isclass_or_instance(obj, ChestNPC) or isclass_or_instance(
                        obj, ChestClone
                    ):
                        writeline(file, "            lower_70a7=%i," % obj.lower_70a7)
                        writeline(file, "            upper_70a7=%i," % obj.upper_70a7)
                    if (
                        isclass_or_instance(obj, BattlePackNPC)
                        or isclass_or_instance(obj, RegularNPC)
                        or isclass_or_instance(obj, ChestNPC)
                    ):
                        if obj.speed != 0:
                            writeline(file, "            speed=%i," % obj.speed)
                    writeline(file, "            visible=%r," % obj.visible)
                    writeline(file, "            x=%i," % obj.x)
                    writeline(file, "            y=%i," % obj.y)
                    writeline(file, "            z=%i," % obj.z)
                    writeline(file, "            z_half=%r," % obj.z_half)
                    direction, _ = byte(
                        prefix="RadialDirection", table=radial_direction_table
                    )([obj.direction])
                    writeline(file, "            direction=%s," % direction)
                    if (
                        isclass_or_instance(obj, BattlePackNPC)
                        or isclass_or_instance(obj, RegularNPC)
                        or isclass_or_instance(obj, ChestNPC)
                    ):
                        writeline(
                            file,
                            "            face_on_trigger=%r," % obj.face_on_trigger,
                        )
                        writeline(
                            file,
                            "            cant_enter_doors=%r," % obj.cant_enter_doors,
                        )
                        writeline(file, "            byte2_bit5=%r," % obj.byte2_bit5)
                        writeline(
                            file,
                            "            set_sequence_playback=%r,"
                            % obj.set_sequence_playback,
                        )
                        writeline(file, "            cant_float=%r," % obj.cant_float)
                        writeline(
                            file,
                            "            cant_walk_up_stairs=%r,"
                            % obj.cant_walk_up_stairs,
                        )
                        writeline(
                            file,
                            "            cant_walk_under=%r," % obj.cant_walk_under,
                        )
                        writeline(
                            file,
                            "            cant_pass_walls=%r," % obj.cant_pass_walls,
                        )
                        writeline(
                            file,
                            "            cant_jump_through=%r," % obj.cant_jump_through,
                        )
                        writeline(
                            file, "            cant_pass_npcs=%r," % obj.cant_pass_npcs
                        )
                        writeline(file, "            byte3_bit5=%r," % obj.byte3_bit5)
                        writeline(
                            file,
                            "            cant_walk_through=%r," % obj.cant_walk_through,
                        )
                        writeline(file, "            byte3_bit7=%r," % obj.byte3_bit7)
                        writeline(
                            file,
                            "            slidable_along_walls=%r,"
                            % obj.slidable_along_walls,
                        )
                        writeline(
                            file,
                            "            cant_move_if_in_air=%r,"
                            % obj.cant_move_if_in_air,
                        )
                        writeline(
                            file, "            byte7_upper2=%r," % obj.byte7_upper2
                        )
                    writeline(file, "            priority_0=%r," % obj.model.priority_0)
                    writeline(file, "            priority_1=%r," % obj.model.priority_1)
                    writeline(file, "            priority_2=%r," % obj.model.priority_2)
                    if obj.model._show_shadow is not None:
                        writeline(
                            file, "            show_shadow=%r," % obj.model.show_shadow
                        )
                    if obj.model._acute_axis is not None:
                        writeline(
                            file, "            acute_axis=%i," % obj.model.acute_axis
                        )
                    if obj.model._obtuse_axis is not None:
                        writeline(
                            file, "            obtuse_axis=%i," % obj.model.obtuse_axis
                        )
                    if obj.model._height is not None:
                        writeline(file, "            height=%i," % obj.model.height)
                    if obj.model._vram_size is not None:
                        writeline(
                            file, "            vram_size=%i," % obj.model.vram_size
                        )
                    if obj.model._directions is not None:
                        vram_store, _ = byte(
                            prefix="VramStore", table=vram_store_table
                        )([obj.model.directions])
                        writeline(file, "            directions=%s," % vram_store)
                    writeline(
                        file, "            cannot_clone=%r," % obj.model.cannot_clone
                    )
                    if obj.model._byte2_bit0 is not None:
                        writeline(
                            file, "            byte2_bit0=%r," % obj.model.byte2_bit0
                        )
                    if obj.model._byte2_bit1 is not None:
                        writeline(
                            file, "            byte2_bit1=%r," % obj.model.byte2_bit1
                        )
                    if obj.model._byte2_bit2 is not None:
                        writeline(
                            file, "            byte2_bit2=%r," % obj.model.byte2_bit2
                        )
                    if obj.model._byte2_bit3 is not None:
                        writeline(
                            file, "            byte2_bit3=%r," % obj.model.byte2_bit3
                        )
                    if obj.model._byte2_bit4 is not None:
                        writeline(
                            file, "            byte2_bit4=%r," % obj.model.byte2_bit4
                        )
                    if obj.model._byte5_bit6 is not None:
                        writeline(
                            file, "            byte5_bit6=%r," % obj.model.byte5_bit6
                        )
                    if obj.model._byte5_bit7 is not None:
                        writeline(
                            file, "            byte5_bit7=%r," % obj.model.byte5_bit7
                        )
                    if obj.model._byte6_bit2 is not None:
                        writeline(
                            file, "            byte6_bit2=%r," % obj.model.byte6_bit2
                        )
                    if obj.model._y_shift is not None:
                        writeline(file, "            y_shift=%i," % obj.model.y_shift)
                    writeline(file, "        ),")

                writeline(file, "    ]")

            writeline(file, ")")
            file.close()

        file = open("%s/rooms.py" % dest, "w", encoding="utf-8")
        for i in range(512):
            writeline(
                file,
                "from randomizer.data.rooms.room_%i import room as room_%i" % (i, i),
            )
        writeline(file, "rooms = [None]*512")
        for i in range(512):
            writeline(file, "rooms[%i] = room_%i" % (i, i))
        file.close()
