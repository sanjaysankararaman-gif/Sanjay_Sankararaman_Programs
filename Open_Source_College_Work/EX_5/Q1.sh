d=$(date +%H)

if [[ d -gt 5 && d -le 11 ]]
then
	echo "Good Morning"
elif [[ d -gt 12 && d -le 16 ]]
then
	echo "Good Afternoon"

else
	echo "Good Evening"


fi
