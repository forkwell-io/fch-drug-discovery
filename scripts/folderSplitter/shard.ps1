# Number of portions to group the files into
$groupCount = 8

$path = "./"
$files = Get-ChildItem "$($path)*.pdbqt" -File 

For($fileIndex = 0; $fileIndex -lt $files.Count; $fileIndex++){
    $targetIndex = $fileIndex % $groupCount
    $targetPath = Join-Path $path $targetIndex
    If(!(Test-Path $targetPath -PathType Container)){
        [void](new-item -Path $path -name $targetIndex -Type Directory)
    }
    $files[$fileIndex] | Move-Item -Destination $targetPath -Force
}

echo""
echo " _____                       _      _       _ "
echo "/  __ \                     | |    | |     | |"
echo "| /  \/ ___  _ __ ___  _ __ | | ___| |_ ___| |"
echo "| |    / _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \ |"
echo "| \__/\ (_) | | | | | | |_) | |  __/ ||  __/_|"
echo " \____/\___/|_| |_| |_| .__/|_|\___|\__\___(_)"
echo "                      | |                     "
echo "                      |_|                     "
echo ""