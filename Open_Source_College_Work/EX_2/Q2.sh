read -p "Enter a number: " a
read -p "Enter a number: " b

read -p "Enter 1 for addition, Enter 2 for subtraction, Enter 3 for multiplication and Enter 4 for division: " choice

sum=$((a+b))
diff=$((a-b))
div=$((a/b))
multi=$((a*b))


if [ "$choice" -eq 1 ]
then
	echo "The value is $sum"

elif [ "$choice" -eq 2 ]
then
	echo "The difference is $diff"

elif [ "$choice" -eq 3 ]
then
	echo "The product is $multi"

elif [ "$choice" -eq 4 ]
then 
	echo "The product is $div"

else
	echo "Invalid Input"

fi
