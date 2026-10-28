read -p "Enter a number: " a
read -p "Enter another number: " b
read -p "Enter another number: " c

if [ $a -gt $b ] 
then
	if [ $a -gt $c ]
	then 
		echo "$a is the greatest number"
	else
		echo "$c is the greatest number"
	fi

elif [ $b -gt $a ]
then
	if [ $b -gt $c ]
	then
		echo "$b is the greatest number"
	else
		echo "$c is the greatest number"
	fi
fi

