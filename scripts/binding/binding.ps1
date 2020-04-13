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

