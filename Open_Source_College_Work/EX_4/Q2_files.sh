#echo "$(mkdir -p student_files_1)"
#echo "$(mkdir -p backup)"

mkdir -p student_files_1
mkdir -p backup


for ((i=0;i<10;i++))
do
	touch /home/it26150975/Operating_Systems/EX_4/student_files_1/text_$i.txt

done

	
