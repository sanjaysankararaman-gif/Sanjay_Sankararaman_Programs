path=$(pwd)
mkdir -p Q5_files
new_path=$path/Q5_files


for ((i=0;i<10;i++))
do
	touch $new_path/num_$i.txt
done

#Method_1
c=0
for f in $new_path/*
do
	if [ -f $f ]
	then
		c=$((c+1))
	fi
done

echo "Number of files $c"

#Method_2
c=$(find $new_path -type f|wc -l)

echo "Number of files $c"



