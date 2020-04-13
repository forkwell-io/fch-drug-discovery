Get-ChildItem -File "*.pdbqt_out" | Foreach {
    node .\convert.js $_.name
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