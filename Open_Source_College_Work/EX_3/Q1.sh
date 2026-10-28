read -p "Enter a positive integer: " n
m=$((n+1))
sum=0

for ((i=1;i<m;i++))
do
	sum=$((sum+i))
done

echo "The sum of first $n natural numbers is $sum"


