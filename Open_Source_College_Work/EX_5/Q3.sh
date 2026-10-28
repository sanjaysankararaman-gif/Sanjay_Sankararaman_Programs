path=$(pwd)

d=$(find $path -type f -size +2c|wc -l)


if [ $d -gt 5 ]
then
	echo "Many large files"
else
	 echo "Few large files"
	 
fi


