read -p "Enter an integer =" n


for ((i=2;i<n;i++))
do
	if [ $((n%i)) -eq 0 ]
	then 
		echo "Not a prime number"
		break
	else
		continue
		
	fi
	echo "Prime Number"	
done

