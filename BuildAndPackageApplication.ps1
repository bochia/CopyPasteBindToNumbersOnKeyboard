$currentDirectory = Get-Location

$cssFolderPath = Join-Path -Path $currentDirectory -ChildPath "css"
$htmlFolderPath = Join-Path -Path $currentDirectory -ChildPath "html"
$distFolderPath = Join-Path -Path $currentDirectory -ChildPath "dist"

# Delete old folders from previous build.
$cssDistFolderPath = Join-Path -Path $distFolderPath -ChildPath "css"
$htmlDistFolderPath = Join-Path -Path $distFolderPath -ChildPath "html"
if (Test-Path -Path $cssDistFolderPath) {
    Remove-Item $cssDistFolderPath -Recurse
}

if (Test-Path -Path $htmlDistFolderPath) {
    Remove-Item $htmlDistFolderPath -Recurse
}

# Copy new files into dist folder.
Copy-Item -Path $cssFolderPath -Destination $distFolderPath -Recurse
Copy-Item -Path $htmlFolderPath -Destination $distFolderPath -Recurse

pyinstaller --onefile --noconsole CopyPasteBind.py --add-data="html\MainWindow.html;." --add-data="css\style.css;."
