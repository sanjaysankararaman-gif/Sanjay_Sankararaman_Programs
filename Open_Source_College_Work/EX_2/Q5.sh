read -p "Enter marks in Subject 1: " sub1
read -p "Enter marks in Subject 2: " sub2
read -p "Enter marks in Subject 3: " sub3
read -p "Enter marks in Subject 4: " sub4
read -p "Enter marks in Subject 5: " sub5

total=$((sub1+sub2+sub3+sub4+sub5))

if [ $total -gt 250 ]
then
	echo "Pass"
else
	echo "Fail"

fi

