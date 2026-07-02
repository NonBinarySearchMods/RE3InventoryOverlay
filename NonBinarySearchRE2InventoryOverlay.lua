local known_typeofs = {}
local function get_component(game_object, type_name)
    local t = known_typeofs[type_name] or sdk.typeof(type_name)

    if t == nil then 
        return nil
    end

    known_typeofs[type_name] = t
    return game_object:call("getComponent(System.Type)", t)
end

local function get_inventory()
    local playman = sdk.get_managed_singleton(sdk.game_namespace("PlayerManager"))
    if not playman then
        return nil
    end

	local player = playman:call("get_CurrentPlayer")
    if not player then
        return nil
    end

    return get_component(player, sdk.game_namespace("survivor.Inventory"))
end

local function get_game_state()
	local flowmanager = sdk.get_managed_singleton(sdk.game_namespace("gamemastering.MainFlowManager"))
	if not flowmanager then
		return false, false
	end

	return flowmanager:call("get_IsInGame"), flowmanager:call("get_IsInPause")
end

local items = {
	"1",
	"10",
	"102",
	"11",
	"112",
	"114",
	"115",
	"116",
	"118",
	"119",
	"12",
	"120",
	"124",
	"126",
	"127",
	"128",
	"129",
	"13",
	"130",
	"131",
	"132",
	"133",
	"134",
	"135",
	"136",
	"14",
	"15",
	"159",
	"16",
	"160",
	"169",
	"17",
	"170",
	"176",
	"179",
	"18",
	"180",
	"181",
	"183",
	"186",
	"187",
	"189",
	"190",
	"191",
	"194",
	"195",
	"196",
	"197",
	"198",
	"199",
	"2",
	"200",
	"201",
	"202",
	"203",
	"22",
	"23",
	"24",
	"240",
	"241",
	"243",
	"244",
	"245",
	"25",
	"26",
	"262",
	"27",
	"286",
	"291",
	"293",
	"294",
	"295",
	"296",
	"3",
	"31",
	"32",
	"33",
	"34",
	"35",
	"36",
	"37",
	"38",
	"39",
	"4",
	"48",
	"49",
	"5",
	"50",
	"51",
	"52",
	"53",
	"54",
	"55",
	"56",
	"58",
	"6",
	"60",
	"61",
	"62",
	"64",
	"65",
	"66",
	"7",
	"72",
	"73",
	"74",
	"75",
	"76",
	"77",
	"79",
	"8",
	"80",
	"81",
	"82",
	"83",
	"84",
	"86",
	"87",
	"88",
	"9",
	"90",
	"91",
	"93",
	"94",
	"95",
	"98"
}

local weapons = {
	"1,0",
	"1,1",
	"1,2",
	"1,3",
	"1,4",
	"1,5",
	"1,6",
	"1,7",
	"11,0",
	"11,1",
	"11,2",
	"11,3",
	"2,0",
	"21,0",
	"21,1",
	"21,2",
	"21,3",
	"222,0",
	"23,0",
	"242,0",
	"252,0",
	"3,0",
	"3,2",
	"3,4",
	"3,6",
	"31,0",
	"31,1",
	"31,2",
	"31,3",
	"4,0",
	"41,0",
	"42,0",
	"42,1",
	"43,0",
	"43,2",
	"44,0",
	"44,2",
	"45,0",
	"46,0",
	"47,0",
	"49,0",
	"50,0",
	"65,0",
	"66,0",
	"7,0",
	"8,0",
	"82,0",
	"83,0",
	"84,0",
	"85,0",
	"9,0",
	"9,2",
	"9,4",
	"9,6"
}

-- settings
local settings = {
	scaling = 1,
	padding = 10,
	margin_top = 220,
	margin_left = 40,
	textsize = 16
}
local settingsfile = "NonBinarySearchRE2InventoryOverlay.json"

local function rt(t, k, d)
    if t[k] ~= nil then
        return t[k]
    end
    return d
end

local function save_settings()
    json.dump_file(settingsfile, settings)
end

local function load_settings()
    local sf = json.load_file(settingsfile)
    if sf then
        settings.scaling = rt(sf, "scaling", settings.scaling)
        settings.padding = rt(sf, "padding", settings.padding)
        settings.margin_top = rt(sf, "margin_top", settings.margin_top)
        settings.margin_left = rt(sf, "margin_left", settings.margin_left)
        settings.textsize = rt(sf, "textsize", settings.textsize)
    else
        save_settings()
    end
end

load_settings()

-- states
local margin_top = nil
local margin_left = nil
local padding = nil
local uiscale = nil
local initialized = false
local image_loading_error = false
local screen_size = { w = 0, h = 0 }
local images = {}
local path_prefix = "NonBinarySearchInventoryOverlay"
local font = nil
local unit_without_scaling = 112
local fontsize = nil
local unit = nil

local function load_item_images()
	for k,v in pairs(items) do
		local path = string.format("%s/items/%s.png", path_prefix, v)
		local image = d2d.Image.new(path)
		if image == nil then
			image_loading_error = true
			break
		end
		images[string.format("items/%s", v)] = image
	end
end

local function load_weapon_images()
	for k,v in pairs(weapons) do
		local path = string.format("%s/weapons/%s.png", path_prefix, v)
		local image = d2d.Image.new(path)
		if image == nil then
			image_loading_error = true
			break
		end
		images[string.format("weapons/%s", v)] = image
	end
end

local function inventory_overlay_d2d_initialize()
    screen_size.w, screen_size.h = d2d.surface_size()

	load_item_images()
	if image_loading_error then
		initialized = true
		return
	end

	load_weapon_images()
	if image_loading_error then
		initialized = true
		return
	end

    uiscale = (screen_size.h / 1080) * 0.6 * settings.scaling

	padding = settings.padding
	margin_top = settings.margin_top
	margin_left = settings.margin_left

	fontsize = math.floor(settings.textsize * uiscale)
    font = d2d.Font.new("NotoSansMono-SemiBold.ttf", fontsize)
	unit = math.floor(unit_without_scaling * uiscale)

	initialized = true
end

local function draw_text_shadowed(s, x, y)
	local fc = rgba(255, 255, 255, 240)
	local sc = rgba(0, 0, 0, 240)
	local shadowoffset = math.max(math.floor(uiscale * 0.8), 1)
	d2d.text(font, s, x + shadowoffset, y + shadowoffset, sc)
	d2d.text(font, s, x + (shadowoffset * 2), y + (shadowoffset * 2), sc)
	d2d.text(font, s, x, y, fc)
end

local function get_base_coord(col, row)
	-- top left
	return margin_left + col * unit, margin_top + row * unit + (row - 1) * padding
end

local function draw_image(image, col, row)
	local w,h = image:size()
	local adjusted_w = math.floor(w * uiscale)
	local adjusted_h = math.floor(h * uiscale)
	local x,y = get_base_coord(col, row)
	d2d.image(
		image,
		x, y,
		adjusted_w, adjusted_h
	)
	return x,y,adjusted_w, adjusted_h
end

local function draw_text_below_image(s, x, y, w, h)
	text_height = fontsize * 0.65
	text_width = string.len(s) * fontsize * 0.55
	draw_text_shadowed(
		s,
		x + math.floor(w/2 - text_width/2), y + h - math.floor(text_height + 5 * uiscale)
	)
end

local function draw_item(image, col, row, item_number)
	local x,y,w,h = draw_image(image, col, row)
	if item_number > 1 then
		draw_text_below_image(tostring(item_number),x,y,w,h)
	end
end

local function draw_weapon(image, col, row, current_ammo, max_ammo)
	local x,y,w,h = draw_image(image, col, row)
	if max_ammo < 0 and current_ammo < 0 then
		draw_text_below_image(
			"inf",
			x,y,w,h
		)
	elseif max_ammo < 0 then
		draw_text_below_image(
			string.format("%d/inf", current_ammo),
			x,y,w,h
		)
	else
		draw_text_below_image(
			string.format("%d/%d", current_ammo, max_ammo),
			x,y,w,h
		)
	end
end

local function draw_border(col, row, is_fat)
	local fc = rgba(255, 255, 255, 240)
	local sc = rgba(0, 0, 0, 240)
	local shadowoffset = math.max(math.floor(uiscale * 0.8), 1)
	local x,y = get_base_coord(col, row)
	local w = unit
	if is_fat then
		w = unit * 2
	end
	local h = unit + padding
	local thickness = 1

	d2d.outline_rect(x + shadowoffset, y + shadowoffset, w, h, thickness, sc)
	d2d.outline_rect(x + (shadowoffset * 2), y + (shadowoffset * 2), w, h, thickness, sc)
	d2d.outline_rect(x, y, w, h, thickness, fc)
end

local function inventory_overlay_d2d_draw()
	local is_playing, is_paused = get_game_state()
	if not is_playing or is_paused then
		return
	end

	local inventory = get_inventory()
	if not inventory then
		return
	end

	local index = 0
	local slotSize = inventory:call("get_CurrentSlotSize()")
	local nrows = math.ceil(slotSize / 4.0)

	for row=0,nrows-1 do
		local ncols = 4
		if row == nrows-1 then
			ncols = slotSize - (nrows - 1) * 4
		end

		for col=0,ncols-1 do
			local slot = inventory:call("getSlot", index)
			if slot:call("get_IsItem") then
				local item_id = slot:call("get_ItemID")
				local item_number = slot:call("get_Number")
				draw_item(images[string.format("items/%d", item_id)], col, row, item_number)
			elseif slot:call("get_IsWeapon") then
				local weapon_id = slot:call("get_WeaponType")
				local attachments = slot:call("get_WeaponParts")
				local current_ammo = slot:call("get_Number")
				local max_ammo = slot:call("get_MaxNumber")
				if slot:call("get_AlwaysReloadable") then
					max_ammo = -1
				end
				draw_weapon(images[string.format("weapons/%d,%d", weapon_id, attachments)], col, row, current_ammo, max_ammo)
			end

			if slot:call("get_IsFatSlot") then
				draw_border(col, row, true)
			elseif not slot:call("get_IsDeadSlot") then
				draw_border(col, row, false)
			end

			index = index + 1
		end
	end

end

re.on_frame(function()
    if not initialized and d2d ~= nil then
        d2d.register(inventory_overlay_d2d_initialize, inventory_overlay_d2d_draw)
    end
end)
