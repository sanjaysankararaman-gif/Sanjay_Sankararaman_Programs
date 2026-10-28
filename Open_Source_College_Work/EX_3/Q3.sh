read -p "Enter a natural number: " n
m=$((n+1))
p=1

for ((i=1;i<m;i++))
do
	p=$((p*i))
done

echo "The factorial of the number $n is $p"

	
