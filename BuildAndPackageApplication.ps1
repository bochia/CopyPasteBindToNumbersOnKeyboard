$currentDirectory = Get-Location

$cssString = "css"
$htmlString = "html"
$settingsString = "settings"

$distFolderPath = Join-Path -Path $currentDirectory -ChildPath "dist"
$cssFolderPath = Join-Path -Path $currentDirectory -ChildPath $cssString
$htmlFolderPath = Join-Path -Path $currentDirectory -ChildPath $htmlString
$settingsFolderPath = Join-Path -Path $currentDirectory -ChildPath $settingsString

# Delete old folders from previous build.
$cssDistFolderPath = Join-Path -Path $distFolderPath -ChildPath $cssString
$htmlDistFolderPath = Join-Path -Path $distFolderPath -ChildPath $htmlString
$settingsDistFolderPath = Join-Path -Path $distFolderPath -ChildPath $settingsString
if (Test-Path -Path $cssDistFolderPath) {
    Remove-Item $cssDistFolderPath -Recurse
}

if (Test-Path -Path $htmlDistFolderPath) {
    Remove-Item $htmlDistFolderPath -Recurse
}

if (Test-Path -Path $settingsDistFolderPath) {
    Remove-Item $settingsDistFolderPath -Recurse
}

# Copy new files into dist folder.
Copy-Item -Path $cssFolderPath -Destination $distFolderPath -Recurse
Copy-Item -Path $htmlFolderPath -Destination $distFolderPath -Recurse
Copy-Item -Path $settingsFolderPath -Destination $distFolderPath -Recurse

pyinstaller --onefile --noconsole CopyPasteBind.py --add-data="html\MainWindow.html;." --add-data="css\style.css;."
