param (
    [string]$Version
)

if (-Not (Test-Path ./venv))
{
    python -m venv venv
}
& ./venv/Scripts/activate.ps1

python ./split.py

if (Test-Path ./output) {
    Remove-Item ./output -Recurse -Force
}
New-Item -Path "./output/reframework" -Name "fonts" -ItemType "Directory"
New-Item -Path "./output/reframework" -Name "images" -ItemType "Directory"
New-Item -Path "./output/reframework" -Name "autorun" -ItemType "Directory"

if (Test-Path "./RE2InventoryOverlay.zip") {
    Remove-Item "./RE2InventoryOverlay.zip"
}

$modinfo=@"
name=RE2 Inventory Overlay
version=v$version
description=Inventory overlay for Resident Evil 2 (RT and non-RT). Requires REFRamework and reframework-d2d
author=NonBinarySearch
screenshot=screenshot.png
"@

Out-File -FilePath "./output/modinfo.ini" -InputObject $modinfo
Copy-Item "./screenshot.png" -Destination "./output/"

& luacheck .\RE2InventoryOverlayNonBinarySearch.lua --config .\.luacheckrc
if ($LastExitCode -ne 0) {
    Write-Error "luacheck failed"
    exit
}

Copy-Item "./RE2InventoryOverlayNonBinarySearch.lua" -Destination "./output/reframework/autorun"

Copy-Item "./assets/NotoSansMono-SemiBold.ttf" -Destination "./output/reframework/fonts"
Copy-Item "./assets/items" -Filter "*.png" -Destination "./output/reframework/images/NonBinarySearchInventoryOverlay/items/" -Recurse
Copy-Item "./assets/weapons" -Filter "*.png" -Destination "./output/reframework/images/NonBinarySearchInventoryOverlay/weapons/" -Recurse

Compress-Archive -Path "./output/*" -DestinationPath "RE2InventoryOverlay.zip"