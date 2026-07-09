from PIL import Image
from enum import Enum

inv_slot_width = 112
inv_slot_height = 112

im = Image.open("assets/ui0100_iam.texout.png")

def crop_image(i, j, fat=False):
    if fat:
        return im.crop((j*inv_slot_width, i*inv_slot_height, (j+2)*inv_slot_width, (i+1)*inv_slot_height))
    return im.crop((j*inv_slot_width, i*inv_slot_height, (j+1)*inv_slot_width, (i+1)*inv_slot_height))

class ItemEnumeration(Enum):
    First_Aid_Spray = 0x0001
    Green_Herb = 0x0002
    Red_Herb = 0x0003
    Mixed_Herb_GG = 0x0005
    Mixed_Herb_GR = 0x0006
    Mixed_Herb_GGG = 0x0009
    Green_Herb2 = 0x0016
    Red_Herb2 = 0x0017
    Handgun_Ammo = 0x001F
    Shotgun_Shells = 0x0020
    Assault_Rifle_Ammo = 0x0021
    MAG_Ammo = 0x0022
    Mine_Rounds = 0x0024
    Explosive_Rounds = 0x0025
    Acid_Rounds = 0x0026
    Flame_Rounds = 0x0027
    Gunpowder = 0x003D
    HighGrade_Gunpowder = 0x003E
    Explosive_A = 0x003F
    Explosive_B = 0x0040
    Moderator_Handgun = 0x004C
    Dot_Sight_Handgun = 0x004D
    Extended_Magazine_Handgun = 0x004E
    SemiAuto_Barrel_Shotgun = 0x005B
    Tactical_Stock_Shotgun = 0x005C
    Shell_Holder_Shotgun = 0x005D
    Scope_Assault_Rifle = 0x0060
    Dual_Magazine_Assault_Rifle = 0x0061
    Tactical_Grip_Assault_Rifle = 0x0062
    Extended_Barrel_MAG = 0x0065
    Audiocassette_Tape = 0x0083
    Lock_Pick = 0x0097
    Bolt_Cutters = 0x0098
    Battery = 0x00A1
    Safety_Deposit_Key = 0x00A2
    Brads_ID_Card = 0x00A4
    Detonator_No_Battery = 0x00A5
    Detonator = 0x00A6
    Fire_Hose = 0x00B5
    Kendos_Gate_Key = 0x00B6
    Case_Lock_Pick = 0x00B9
    Battery_Pack = 0x00BA
    Green_Jewel = 0x00BB
    Blue_Jewel = 0x00BC
    Red_Jewel = 0x00BD
    Fancy_Box_Green_Jewel = 0x00C0
    Fancy_Box_Blue_Jewel = 0x00C1
    Fancy_Box_Red_Jewel = 0x00C2
    Hospital_ID_Card = 0x00D3
    Tape_Player_Tape_Inserted = 0x00D4
    Audiocassette_Tape2 = 0x00D5
    Tape_Player = 0x00D6
    Vaccine_Sample = 0x00D7
    Detonator2 = 0x00D9
    Locker_Room_Key = 0x00DA
    Fuse3 = 0x00DE
    Fuse2 = 0x00DF
    Fuse1 = 0x00E0
    Wristband = 0x00E7
    Override_Key = 0x00E8
    Vaccine = 0x00E9
    Culture_Sample = 0x00EA
    Liquidfilled_Test_Tube = 0x00EB
    Vaccine_Base = 0x00EC
    Hip_Pouch = 0x0105
    Fire_Hose2 = 0x0108
    Iron_Defense_Coin = 0x012D
    Assault_Coin = 0x012E
    Recovery_Coin = 0x012F
    Crafting_Companion = 0x0130
    STARS_Field_Combat_Manual = 0x0131
    Supply_Crate_Extended_Magazine_Handgun = 0x0137
    Supply_Crate_Moderator_Handgun = 0x0138
    Supply_Crate_Shotgun_Shells = 0x0139
    Supply_Crate_Acid_Rounds = 0x013A
    Supply_Crate_Flame_Rounds = 0x013B
    Supply_Crate_Extended_Barrel_MAG = 0x013C

item_images = {}

col = 0
item_images[ItemEnumeration.First_Aid_Spray] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Green_Herb] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Red_Herb] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Mixed_Herb_GG] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Mixed_Herb_GR] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Mixed_Herb_GGG] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Green_Herb2] = crop_image(0,col); col += 1;
item_images[ItemEnumeration.Red_Herb2] = crop_image(0,col); col += 1;

col = 0
item_images[ItemEnumeration.Handgun_Ammo] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Shotgun_Shells] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Assault_Rifle_Ammo] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.MAG_Ammo] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Acid_Rounds] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Flame_Rounds] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Explosive_Rounds] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Mine_Rounds] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Gunpowder] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.HighGrade_Gunpowder] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Explosive_A] = crop_image(1,col); col += 1;
item_images[ItemEnumeration.Explosive_B] = crop_image(1,col); col += 1;

col = 0
item_images[ItemEnumeration.Moderator_Handgun] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Dot_Sight_Handgun] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Extended_Magazine_Handgun] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.SemiAuto_Barrel_Shotgun] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Tactical_Stock_Shotgun] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Shell_Holder_Shotgun] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Scope_Assault_Rifle] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Dual_Magazine_Assault_Rifle] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Tactical_Grip_Assault_Rifle] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Extended_Barrel_MAG] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Supply_Crate_Acid_Rounds] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Supply_Crate_Extended_Barrel_MAG] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Supply_Crate_Extended_Magazine_Handgun] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Supply_Crate_Flame_Rounds] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Supply_Crate_Moderator_Handgun] = crop_image(2,col); col += 1;
item_images[ItemEnumeration.Supply_Crate_Shotgun_Shells] = crop_image(2,col); col += 1;

col = 0
item_images[ItemEnumeration.Battery] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Safety_Deposit_Key] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Detonator_No_Battery] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Brads_ID_Card] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Detonator] = crop_image(3,col);
item_images[ItemEnumeration.Detonator2] = crop_image(3,col); col = 8;
item_images[ItemEnumeration.Lock_Pick] = crop_image(3,col); col += 1;
item_images[ItemEnumeration.Bolt_Cutters] = crop_image(3,col); col += 1;

col = 0
item_images[ItemEnumeration.Fire_Hose] = crop_image(4,col);
item_images[ItemEnumeration.Fire_Hose2] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Kendos_Gate_Key] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Battery_Pack] = crop_image(4,col, True); col += 2;
item_images[ItemEnumeration.Case_Lock_Pick] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Green_Jewel] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Blue_Jewel] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Red_Jewel] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Fancy_Box_Green_Jewel] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Fancy_Box_Blue_Jewel] = crop_image(4,col); col += 1;
item_images[ItemEnumeration.Fancy_Box_Red_Jewel] = crop_image(4,col); col += 1;

col = 0
item_images[ItemEnumeration.Hospital_ID_Card] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Audiocassette_Tape] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Vaccine_Sample] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Fuse1] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Fuse2] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Fuse3] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Audiocassette_Tape2] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Tape_Player] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Tape_Player_Tape_Inserted] = crop_image(5,col); col += 1;
item_images[ItemEnumeration.Locker_Room_Key] = crop_image(5,col); col += 1;

col = 0
item_images[ItemEnumeration.Override_Key] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.Vaccine] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.Culture_Sample] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.Liquidfilled_Test_Tube] = crop_image(6,col); col += 1;
item_images[ItemEnumeration.Vaccine_Base] = crop_image(6,col); col += 1;

item_images[ItemEnumeration.Hip_Pouch] = crop_image(7,1); col = 5
item_images[ItemEnumeration.Iron_Defense_Coin] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.Assault_Coin] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.Recovery_Coin] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.Crafting_Companion] = crop_image(7,col); col += 1;
item_images[ItemEnumeration.STARS_Field_Combat_Manual] = crop_image(7,col); col += 1;

class WeaponEnumeration(Enum):
    G19_Handgun = 0x01
    G18_Burst_Handgun = 0x02
    G18_Handgun = 0x03
    Samurai_Edge = 0x04
    Infinite_MUP_Handgun = 0x07
    Shotgun = 0x0B
    CQBR_Assault_Rifle = 0x15
    Infinite_CQBR_Assault_Rifle = 0x16
    Lightning_Hawk = 0x1F
    RAIDEN = 0x20
    Grenade_Launcher = 0x2A
    Combat_Knife_Carlos = 0x2E
    Survival_Knife_Jill = 0x2F
    HOT_DOGGER = 0x30
    Infinite_Rocket_Launcher = 0x31
    Hand_Grenade = 0x41
    Flash_Grenade = 0x42

class AttachmentsFlag(Enum):
    Nothing = 0x00
    First = 0x01 # fat
    Second = 0x02
    Third = 0x04

im = Image.open("assets/ui0100_wp_iam.texout.png")

weapon_images = {}

col = 0
weapon_images[(WeaponEnumeration.G19_Handgun, AttachmentsFlag.Nothing.value)] = crop_image(0, col); col += 1;
weapon_images[(WeaponEnumeration.G19_Handgun, AttachmentsFlag.First.value)] = crop_image(0, col, True); col += 2;
weapon_images[(WeaponEnumeration.G19_Handgun, AttachmentsFlag.First.value | AttachmentsFlag.Third.value)] = crop_image(0, col, True); col += 2;
weapon_images[(WeaponEnumeration.G19_Handgun, AttachmentsFlag.First.value | AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(0, col, True); col += 2;
weapon_images[(WeaponEnumeration.G19_Handgun, AttachmentsFlag.Third.value)] = crop_image(0, col); col += 1;
weapon_images[(WeaponEnumeration.G19_Handgun, AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(0, col); col += 1;
weapon_images[(WeaponEnumeration.G19_Handgun, AttachmentsFlag.Second.value)] = crop_image(0, col); col += 1;
weapon_images[(WeaponEnumeration.G19_Handgun, AttachmentsFlag.First.value | AttachmentsFlag.Second.value)] = crop_image(0, col, True); col += 2;
weapon_images[(WeaponEnumeration.Samurai_Edge, AttachmentsFlag.Nothing.value)] = crop_image(0, col); col  = 16;
weapon_images[(WeaponEnumeration.G18_Handgun, AttachmentsFlag.Nothing.value)] = crop_image(0, col); col += 1;
weapon_images[(WeaponEnumeration.G18_Burst_Handgun, AttachmentsFlag.Nothing.value)] = crop_image(0, col); col += 1;

col = 0
weapon_images[(WeaponEnumeration.Shotgun, AttachmentsFlag.Nothing.value)] = crop_image(1, col); col += 1;
weapon_images[(WeaponEnumeration.Shotgun, AttachmentsFlag.First.value)] = crop_image(1, col, True); col += 2;
weapon_images[(WeaponEnumeration.Shotgun, AttachmentsFlag.First.value | AttachmentsFlag.Third.value)] = crop_image(1, col, True); col += 2;
weapon_images[(WeaponEnumeration.Shotgun, AttachmentsFlag.First.value | AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(1, col, True); col += 2;
weapon_images[(WeaponEnumeration.Shotgun, AttachmentsFlag.Third.value)] = crop_image(1, col); col += 1;
weapon_images[(WeaponEnumeration.Shotgun, AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(1, col); col += 1;
weapon_images[(WeaponEnumeration.Shotgun, AttachmentsFlag.Second.value)] = crop_image(1, col); col += 1;
weapon_images[(WeaponEnumeration.Shotgun, AttachmentsFlag.First.value | AttachmentsFlag.Second.value)] = crop_image(1, col, True); col += 2;
weapon_images[(WeaponEnumeration.Lightning_Hawk, AttachmentsFlag.Nothing.value)] = crop_image(1, col); col += 1;
weapon_images[(WeaponEnumeration.Lightning_Hawk, AttachmentsFlag.Second.value)] = crop_image(1, col); col += 1;

col = 0
weapon_images[(WeaponEnumeration.CQBR_Assault_Rifle, AttachmentsFlag.Nothing.value)] = crop_image(2, col, True); col += 2;
weapon_images[(WeaponEnumeration.CQBR_Assault_Rifle, AttachmentsFlag.First.value)] = crop_image(2, col, True); col += 2;
weapon_images[(WeaponEnumeration.CQBR_Assault_Rifle, AttachmentsFlag.First.value | AttachmentsFlag.Third.value)] = crop_image(2, col, True); col += 2;
weapon_images[(WeaponEnumeration.CQBR_Assault_Rifle, AttachmentsFlag.First.value | AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(2, col, True); col += 2;
weapon_images[(WeaponEnumeration.CQBR_Assault_Rifle, AttachmentsFlag.Third.value)] = crop_image(2, col, True); col += 2;
weapon_images[(WeaponEnumeration.CQBR_Assault_Rifle, AttachmentsFlag.Second.value | AttachmentsFlag.Third.value)] = crop_image(2, col, True); col += 2;
weapon_images[(WeaponEnumeration.CQBR_Assault_Rifle, AttachmentsFlag.Second.value)] = crop_image(2, col, True); col += 2;
weapon_images[(WeaponEnumeration.CQBR_Assault_Rifle, AttachmentsFlag.First.value | AttachmentsFlag.Second.value)] = crop_image(2, col, True)

col = 6
weapon_images[(WeaponEnumeration.Infinite_Rocket_Launcher, AttachmentsFlag.Nothing.value)] = crop_image(3, col, True); col += 2;
weapon_images[(WeaponEnumeration.Infinite_CQBR_Assault_Rifle, AttachmentsFlag.Nothing.value)] = crop_image(3, col, True)

col = 0
weapon_images[(WeaponEnumeration.Combat_Knife_Carlos, AttachmentsFlag.Nothing.value)] = crop_image(4, col); col += 1;
weapon_images[(WeaponEnumeration.Survival_Knife_Jill, AttachmentsFlag.Nothing.value)] = crop_image(4, col); col = 4;
weapon_images[(WeaponEnumeration.Infinite_MUP_Handgun, AttachmentsFlag.Nothing.value)] = crop_image(4, col); col += 1;
weapon_images[(WeaponEnumeration.RAIDEN, AttachmentsFlag.Nothing.value)] = crop_image(4, col, True); col += 2;
weapon_images[(WeaponEnumeration.HOT_DOGGER, AttachmentsFlag.Nothing.value)] = crop_image(4, col); col += 2;
weapon_images[(WeaponEnumeration.Hand_Grenade, AttachmentsFlag.Nothing.value)] = crop_image(4, col); col += 1;
weapon_images[(WeaponEnumeration.Flash_Grenade, AttachmentsFlag.Nothing.value)] = crop_image(4, col); col += 1;
weapon_images[(WeaponEnumeration.Grenade_Launcher, AttachmentsFlag.Nothing.value)] = crop_image(4, col, True)

for k,i in item_images.items():
    i.save(f"assets/items/{k.value}.png")

for k,i in weapon_images.items():
    i.save(f"assets/weapons/{k[0].value},{k[1]}.png")
