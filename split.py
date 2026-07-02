from PIL import Image
from enum import Enum

inv_slot_width = 112
inv_slot_height = 112

im = Image.open("ui0100_iam.texout.png")

def crop_image(i, j, fat=False):
    if fat:
        return im.crop((j*inv_slot_width, i*inv_slot_height, (j+2)*inv_slot_width, (i+1)*inv_slot_height))
    return im.crop((j*inv_slot_width, i*inv_slot_height, (j+1)*inv_slot_width, (i+1)*inv_slot_height))

class ItemEnumeration(Enum):
    FirstAidSpray = 0x01
    Herb_Green1 = 0x02
    Herb_Red1 = 0x03
    Herb_Blue1 = 0x04
    Herb_Mixed_GG = 0x05
    Herb_Mixed_GR = 0x06
    Herb_Mixed_GB = 0x07
    Herb_Mixed_GGB = 0x08
    Herb_Mixed_GGG = 0x09
    Herb_Mixed_GRB = 0x0A
    Herb_Mixed_RB = 0x0B
    Herb_Green2 = 0x0C
    Herb_Red2 = 0x0D
    Herb_Blue2 = 0x0E
    HandgunBullets = 0x0F
    ShotgunShells = 0x10
    SubmachineGunAmmo = 0x11
    MAGAmmo = 0x12
    GrenadeAcidRounds = 0x16
    GrenadeFlameRounds = 0x17
    NeedleCartridges = 0x18
    Fuel = 0x19
    HandgunLargeCaliberAmmo = 0x1A
    SLS60HighPoweredRounds = 0x1B
    Detonator = 0x1F
    InkRibbon = 0x20
    WoodenBoard = 0x21
    ElectronicGadget = 0x22
    Battery9Volt = 0x23
    Gunpowder = 0x24
    GunpowderLarge = 0x25
    GunpowderHighGradeYellow = 0x26
    GunpowderHighGradeWhite = 0x27
    MatildaHighCapacityMagazine = 0x30
    MatildaMuzzleBrake = 0x31
    MatildaGunStock = 0x32
    SLS60SpeedLoader = 0x33
    JMBHp3LaserSight = 0x34
    SLS60ReinforcedFrame = 0x35
    JMBHp3HighCapacityMagazine = 0x36
    W870ShotgunStock = 0x37
    W870LongBarrel = 0x38
    MQ11HighCapacityMagazine = 0x3A
    MQ11Suppressor = 0x3C
    LightningHawkRedDotSight = 0x3D
    LightningHawkLongBarrel = 0x3E
    GM79ShoulderStock = 0x40
    FlamethrowerRegulator = 0x41
    SparkShotHighVoltageCondenser = 0x42
    Film_HidingPlace = 0x48
    Film_RisingRookie = 0x49
    Film_Commemorative = 0x4A
    Film_3FLocker = 0x4B
    Film_LionStatue = 0x4C
    KeyStorageRoom = 0x4D
    JackHandle = 0x4F
    SquareCrank = 0x50
    MedallionUnicorn = 0x51
    KeySpade = 0x52
    KeyCardParkingGarage = 0x53
    KeyCardWeaponsLocker = 0x54
    ValveHandle = 0x56
    STARSBadge = 0x57
    Scepter = 0x58
    RedJewel = 0x5A
    BejeweledBox = 0x5B
    PlugBishop = 0x5D
    PlugRook = 0x5E
    PlugKing = 0x5F
    PictureBlock = 0x62
    USBDongleKey = 0x66
    SpareKey = 0x70
    RedBook = 0x72
    StatuesLeftArm = 0x73
    StatuesLeftArmWithRedBook = 0x74
    MedallionLion = 0x76
    KeyDiamond = 0x77
    KeyCar = 0x78
    MedallionMaiden = 0x7C
    PowerPanelPart1 = 0x7E
    PowerPanelPart2 = 0x7F
    LoversRelief = 0x80
    GearSmall = 0x81
    GearLarge = 0x82
    KeyCourtyard = 0x83
    PlugKnight = 0x84
    PlugPawn = 0x85
    PlugQueen = 0x86
    BoxedElectronicPart1 = 0x87
    BoxedElectronicPart2 = 0x88
    KeyOrphanage = 0x9F
    KeyClub = 0xA0
    KeyHeart = 0xA9
    USSDigitalVideoCassette = 0xAA
    TBarValveHandle = 0xB0
    DispersalCartridgeEmpty = 0xB3
    DispersalCartridgeSolution = 0xB4
    DispersalCartridgeHerbicide = 0xB5
    JointPlug = 0xB7
    UpgradeChipAdministrator = 0xBA
    IDWristbandAdministrator = 0xBB
    ElectronicChip = 0xBC
    SignalModulator = 0xBD
    Trophy1 = 0xBE
    Trophy2 = 0xBF
    KeySewers = 0xC2
    IDWristbandVisitor1 = 0xC3
    IDWristbandGeneralStaff1 = 0xC4
    IDWristbandSeniorStaff1 = 0xC5
    UpgradeChipGeneralStaff = 0xC6
    UpgradeChipSeniorStaff = 0xC7
    IDWristbandVisitor2 = 0xC8
    IDWristbandGeneralStaff2 = 0xC9
    IDWristbandSeniorStaff2 = 0xCA
    LabDigitalVideoCassette = 0xCB
    Briefcase = 0xE6
    FuseMainHall = 0xF0
    FuseBreakRoom = 0xF1
    Scissors = 0xF3
    BoltCutter = 0xF4
    StuffedDoll = 0xF5
    HipPouch = 0x0106
    OldKey = 0x011E
    PortableSafe = 0x0123
    TinStorageBox1 = 0x0125
    WoodenBox1 = 0x0126
    WoodenBox2 = 0x0127
    TinStorageBox2 = 0x0128

item_images = {}

col = 0
item_images[ItemEnumeration.FirstAidSpray] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Green2] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Red2] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Blue2] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Mixed_GG] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Mixed_GR] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Mixed_GB] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Mixed_GGB] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Mixed_GGG] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Mixed_GRB] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Mixed_RB] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Green1] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Red1] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Herb_Blue1] = crop_image(0,col); col += 1;

col = 0
item_images[ItemEnumeration.HandgunBullets] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.ShotgunShells] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.SubmachineGunAmmo] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.MAGAmmo] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.HandgunLargeCaliberAmmo] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.SLS60HighPoweredRounds] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.GrenadeAcidRounds] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.GrenadeFlameRounds] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.NeedleCartridges] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Fuel] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.InkRibbon] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.WoodenBoard] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Gunpowder] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.GunpowderLarge] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.GunpowderHighGradeYellow] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.GunpowderHighGradeWhite] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.HipPouch] = crop_image(1,col); col += 1;

col = 0
item_images[ItemEnumeration.MatildaHighCapacityMagazine] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.MatildaMuzzleBrake] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.MatildaGunStock] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.SLS60SpeedLoader] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.JMBHp3LaserSight] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.SLS60ReinforcedFrame] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.JMBHp3HighCapacityMagazine] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.W870ShotgunStock] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.W870LongBarrel] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.MQ11HighCapacityMagazine] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.MQ11Suppressor] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.LightningHawkRedDotSight] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.LightningHawkLongBarrel] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.GM79ShoulderStock] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.FlamethrowerRegulator] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.SparkShotHighVoltageCondenser] = crop_image(2,col); col += 1;

col = 9
item_images[ItemEnumeration.Film_HidingPlace] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Film_RisingRookie] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Film_Commemorative] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Film_3FLocker] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Film_LionStatue] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.PortableSafe] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.TinStorageBox1] = crop_image(3,col);
item_images[ItemEnumeration.TinStorageBox2] = crop_image(3,col);

col = 0
item_images[ItemEnumeration.Detonator] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.ElectronicGadget] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Battery9Volt] = crop_image(4,col);
item_images[ItemEnumeration.KeyStorageRoom] = crop_image(4,4);
col = 6
item_images[ItemEnumeration.JackHandle] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.SquareCrank] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.MedallionUnicorn] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.KeySpade] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.KeyCardParkingGarage] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.KeyCardWeaponsLocker] = crop_image(4,col); col += 1;
col = 13
item_images[ItemEnumeration.ValveHandle] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.STARSBadge] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Scepter] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.RedJewel] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.BejeweledBox] = crop_image(4,col); col += 1;

col = 1
item_images[ItemEnumeration.PlugBishop] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.PlugRook] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.PlugKing] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.PictureBlock] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.USBDongleKey] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.SpareKey] = crop_image(5,col); col += 1;
col = 8
item_images[ItemEnumeration.RedBook] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.StatuesLeftArm] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.StatuesLeftArmWithRedBook] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.MedallionLion] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.KeyDiamond] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.KeyCar] = crop_image(5,col); col += 1;
col = 15
item_images[ItemEnumeration.MedallionMaiden] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.PowerPanelPart1] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.PowerPanelPart2] = crop_image(5,col); col += 1;

col = 0
item_images[ItemEnumeration.LoversRelief] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.KeyOrphanage] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.KeyClub] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.KeyHeart] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.USSDigitalVideoCassette] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.TBarValveHandle] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.SignalModulator] = crop_image(6,col); col += 1;
col = 8
item_images[ItemEnumeration.KeySewers] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.IDWristbandVisitor1] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.IDWristbandGeneralStaff1] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.IDWristbandSeniorStaff1] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.UpgradeChipGeneralStaff] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.UpgradeChipSeniorStaff] = crop_image(6,col); col += 1;
col = 15
item_images[ItemEnumeration.FuseMainHall] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.Scissors] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.BoltCutter] = crop_image(6,col); col += 1;

item_images[ItemEnumeration.StuffedDoll] = crop_image(7,0);
col = 2
item_images[ItemEnumeration.IDWristbandVisitor2] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.IDWristbandGeneralStaff2] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.IDWristbandSeniorStaff2] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.LabDigitalVideoCassette] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.DispersalCartridgeEmpty] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.DispersalCartridgeSolution] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.DispersalCartridgeHerbicide] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.JointPlug] = crop_image(7,10, fat=True)
col = 12
item_images[ItemEnumeration.Trophy1] = crop_image(7,col);
item_images[ItemEnumeration.Trophy2] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.GearSmall] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.GearLarge] = crop_image(7,14, fat=True)
item_images[ItemEnumeration.PlugKnight] = crop_image(7,16)
item_images[ItemEnumeration.PlugPawn] = crop_image(7,17)

item_images[ItemEnumeration.PlugQueen] = crop_image(8,0)
item_images[ItemEnumeration.BoxedElectronicPart1] = crop_image(8,2)
item_images[ItemEnumeration.BoxedElectronicPart2] = crop_image(8,3)
col = 5
item_images[ItemEnumeration.UpgradeChipAdministrator] = crop_image(8,col); col += 1;
item_images[ItemEnumeration.IDWristbandAdministrator] = crop_image(8,col); col += 1;
item_images[ItemEnumeration.KeyCourtyard] = crop_image(8,col); col += 1;
item_images[ItemEnumeration.FuseBreakRoom] = crop_image(8,col); col += 1;

item_images[ItemEnumeration.WoodenBox1] = crop_image(14, 9)
item_images[ItemEnumeration.WoodenBox2] = crop_image(14, 10)

item_images[ItemEnumeration.OldKey] = Image.open("40d.texout.png").resize((inv_slot_width, inv_slot_height))


class WeaponEnumeration(Enum):
    Handgun_Matilda = 0x01
    Handgun_M19 = 0x02
    Handgun_JMB_Hp3 = 0x03
    Handgun_Quickdraw_Army = 0x04
    Handgun_MUP = 0x07
    Handgun_BroomHc = 0x08
    Handgun_SLS60 = 0x09
    Shotgun_W870 = 0x0B
    SMG_MQ11 = 0x15
    SMG_LE5_Infinite = 0x17
    Handgun_LightningHawk = 0x1F
    EMF_Visualizer = 0x29
    GrenadeLauncher_GM79 = 0x2A
    ChemicalFlamethrower = 0x2B
    SparkShot = 0x2C
    ATM4 = 0x2D
    CombatKnife = 0x2E
    CombatKnife_Infinite = 0x2F
    AntiTankRocketLauncher = 0x31
    Minigun = 0x32
    HandGrenade = 0x41
    FlashGrenade = 0x42
    Handgun_SamuraiEdge_Infinite = 0x52
    Handgun_SamuraiEdge_ChrisRedfield = 0x53
    Handgun_SamuraiEdge_JillValentine = 0x54
    Handgun_SamuraiEdge_AlbertWesker = 0x55
    ATM4_Infinite = 0xDE
    AntiTankRocketLauncher_Infinite = 0xF2
    Minigun_Infinite = 0xFC

class AttachmentsFlag(Enum):
    Nothing = 0x00
    First = 0x01 # fat
    Second = 0x02
    Third = 0x04

weapon_images = {}

# NOTE: some weapons are fat by default, some need attachment flag to be odd to be fat

col = 0
weapon_images[(WeaponEnumeration.Handgun_Matilda, AttachmentsFlag.Nothing.value)] = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_Matilda, AttachmentsFlag.First.value)] = crop_image(9,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.Handgun_Matilda, AttachmentsFlag.Second.value)] = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_Matilda, AttachmentsFlag.Third.value)] = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_Matilda, AttachmentsFlag.First.value | AttachmentsFlag.Second.value)] = crop_image(9,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.Handgun_Matilda, AttachmentsFlag.First.value | AttachmentsFlag.Third.value)] = crop_image(9,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.Handgun_Matilda, AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_Matilda, AttachmentsFlag.First.value | AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(9,col,fat=True); col += 2;
weapon_images[(WeaponEnumeration.Handgun_JMB_Hp3, AttachmentsFlag.Nothing.value)] = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_JMB_Hp3, AttachmentsFlag.Second.value)] = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_JMB_Hp3, AttachmentsFlag.Third.value)]  = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_JMB_Hp3, AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_MUP, AttachmentsFlag.Nothing.value)] = crop_image(9,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_BroomHc, AttachmentsFlag.Nothing.value)] = crop_image(9,col); col += 1;

col = 0
weapon_images[(WeaponEnumeration.Handgun_SLS60, AttachmentsFlag.Nothing.value)]  = crop_image(10,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_SLS60, AttachmentsFlag.Third.value)]  = crop_image(10,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_M19, AttachmentsFlag.Nothing.value)]  = crop_image(10,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_SLS60, AttachmentsFlag.Second.value)]  = crop_image(10,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_SLS60, AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)]  = crop_image(10,col); col += 2;
weapon_images[(WeaponEnumeration.Shotgun_W870, AttachmentsFlag.Nothing.value)]  = crop_image(10,col); col += 1;
weapon_images[(WeaponEnumeration.Shotgun_W870, AttachmentsFlag.First.value)]  = crop_image(10,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.Shotgun_W870, AttachmentsFlag.Second.value)]  = crop_image(10,col); col += 1;
weapon_images[(WeaponEnumeration.Shotgun_W870, AttachmentsFlag.First.value | AttachmentsFlag.Second.value)]  = crop_image(10,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.SMG_MQ11, AttachmentsFlag.Nothing.value)]  = crop_image(10,col); col += 1;
weapon_images[(WeaponEnumeration.SMG_MQ11, AttachmentsFlag.First.value)]  = crop_image(10,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.SMG_MQ11, AttachmentsFlag.Second.value)]  = crop_image(10,col); col += 1;
weapon_images[(WeaponEnumeration.SMG_MQ11, AttachmentsFlag.First.value | AttachmentsFlag.Second.value)]  = crop_image(10,col, fat=True); col += 2;

col = 1
weapon_images[(WeaponEnumeration.Handgun_LightningHawk, AttachmentsFlag.Nothing.value)]  = crop_image(11,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_LightningHawk, AttachmentsFlag.First.value)]  = crop_image(11,col,fat=True); col += 2;
weapon_images[(WeaponEnumeration.Handgun_LightningHawk, AttachmentsFlag.Second.value)]  = crop_image(11,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_LightningHawk, AttachmentsFlag.First.value | AttachmentsFlag.Second.value)]  = crop_image(11,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.GrenadeLauncher_GM79, AttachmentsFlag.Nothing.value)]  = crop_image(11,col); col += 1;
weapon_images[(WeaponEnumeration.GrenadeLauncher_GM79, AttachmentsFlag.First.value)]  = crop_image(11,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.ChemicalFlamethrower, AttachmentsFlag.Nothing.value)]  = crop_image(11,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.ChemicalFlamethrower, AttachmentsFlag.Second.value)]  = crop_image(11,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.SparkShot, AttachmentsFlag.Nothing.value)]  = crop_image(11,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.SparkShot, AttachmentsFlag.Second.value)]  = crop_image(11,col, fat=True); col += 2;

col = 0
weapon_images[(WeaponEnumeration.ATM4, AttachmentsFlag.Nothing.value)] = crop_image(12,col, fat=True);
weapon_images[(WeaponEnumeration.ATM4_Infinite, AttachmentsFlag.Nothing.value)] = crop_image(12,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.AntiTankRocketLauncher, AttachmentsFlag.Nothing.value)] = crop_image(12,col, fat=True);
weapon_images[(WeaponEnumeration.AntiTankRocketLauncher_Infinite, AttachmentsFlag.Nothing.value)] = crop_image(12,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.Minigun, AttachmentsFlag.Nothing.value)] = crop_image(12,col, fat=True);
weapon_images[(WeaponEnumeration.Minigun_Infinite, AttachmentsFlag.Nothing.value)] = crop_image(12,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.EMF_Visualizer, AttachmentsFlag.Nothing.value)] = crop_image(12,col); col += 1;
weapon_images[(WeaponEnumeration.Handgun_Quickdraw_Army, AttachmentsFlag.Nothing.value)] = crop_image(12,col); col += 2;
weapon_images[(WeaponEnumeration.SMG_LE5_Infinite, AttachmentsFlag.Nothing.value)] = crop_image(12,col, fat=True); col += 2;
weapon_images[(WeaponEnumeration.Handgun_SamuraiEdge_Infinite, AttachmentsFlag.Nothing.value)] = crop_image(12,col)
weapon_images[(WeaponEnumeration.Handgun_SamuraiEdge_AlbertWesker, AttachmentsFlag.Nothing.value)] = crop_image(12,col)
weapon_images[(WeaponEnumeration.Handgun_SamuraiEdge_ChrisRedfield, AttachmentsFlag.Nothing.value)] = crop_image(12,col)
weapon_images[(WeaponEnumeration.Handgun_SamuraiEdge_JillValentine, AttachmentsFlag.Nothing.value)] = crop_image(12,col)

weapon_images[(WeaponEnumeration.CombatKnife, AttachmentsFlag.Nothing.value)] = crop_image(13, 0)
weapon_images[(WeaponEnumeration.CombatKnife_Infinite, AttachmentsFlag.Nothing.value)] = crop_image(13, 1)
weapon_images[(WeaponEnumeration.HandGrenade, AttachmentsFlag.Nothing.value)] = crop_image(13, 9)
weapon_images[(WeaponEnumeration.FlashGrenade, AttachmentsFlag.Nothing.value)] = crop_image(13, 10)



for k,i in item_images.items():
    i.save(f"images/items/{k.value}.png")

for k,i in weapon_images.items():
    i.save(f"images/weapons/{k[0].value},{k[1]}.png")
