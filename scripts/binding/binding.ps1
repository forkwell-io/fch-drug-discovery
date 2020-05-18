$path = "./output"
If(!(test-path $path))
{
    New-Item -ItemType Directory -Force -Path $path
    echo "Created new folder"
}

Get-ChildItem -File "*.pdbqt" | Foreach {
    echo "Processing for file $($_.name)"
    ./vina.exe --config "./importantStuff/conf.txt" --ligand $_.name --out "./output/$($_.name)_out"
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