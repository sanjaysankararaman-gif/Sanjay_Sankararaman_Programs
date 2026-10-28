echo Enter radius of circle
read radius

area=$(echo "3.14*$radius*$radius"|bc)

echo "$area"


