read -p "Enter a number: " n

new_num=0
backup=$n
while [ $n -gt 0 ]
do
	a=$((n%10))
	n=$((n/10))
	new_num=$((new_num * 10 + a))

done

if [ $new_num=$backup ]
then
	echo "$backup is a palindrome"
else
	echo "$backup is not a palindrome"

fi
