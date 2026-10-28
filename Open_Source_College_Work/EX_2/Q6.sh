read -p "Enter a number: " num1
read -p "Enter a number: " num2

read -p "Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division: " ch

a=$((num1+num2))
s=$((num1-num2))
d=$((num1/num2))
m=$((num1*num2))

case $ch in
	1) echo "$a";;
	2) echo "$s";;
	3) echo "$m";;
	4) echo "$d";;
	*) echo "Invalid Input";;
esac
