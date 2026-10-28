path=$(pwd)
mkdir -p Q4_files
new_path=$path/Q4_files

for ((i=0;i<10;i++))
do
	touch "$new_path/file_$i.txt"

done

for f in $new_path/*
do
	if [ -f $f ]
	then
		rm $f
		echo "Removed $f on $(date)" >> $path/log4.txt
	fi
		
		
done

