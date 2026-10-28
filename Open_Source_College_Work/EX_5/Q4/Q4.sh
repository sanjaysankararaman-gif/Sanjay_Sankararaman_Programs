path=$(pwd)
newpath=$path/downloads
p1=$path/text
p2=$path/scripts
p3=$path/pdf


for ((i=0;i<4;i++))
do
	touch $path/downloads/file_$i.pdf
	touch $path/downloads/file_$i.txt
	touch $path/downloads/file_$i.sh
done



mkdir -p scripts
mkdir -p text
mkdir -p pdf

for f in $newpath/*
do

	if [[ $f == *.txt ]]
	then
		mv $f $path/text
		echo "Moved $f to $p1" >> organiser.log
		
	elif [[ $f == *.sh ]]
	then
		mv $f $path/scripts 
		echo "Moved $f to $p2" >> organiser.log
		
	elif [[ $f == *.pdf ]]
	then
		mv $f $path/pdf
		echo "Moved $f to $p3" >> organiser.log
	fi

	
done
