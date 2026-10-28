path=$(pwd)
mkdir -p documents
new_path=$path/documents

for ((i=0;i<10;i++))
do
	touch $new_path/text_$i.txt
	
done

for f in $new_path/*
do
	echo "$f" >> file_list_log.txt
	
done


