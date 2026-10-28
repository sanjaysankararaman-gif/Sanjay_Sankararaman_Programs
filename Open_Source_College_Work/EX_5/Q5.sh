path=$(pwd)
dat=$(date)

touch $path/application.log

d=$(wc -c < application.log)

if [ $d -gt 20 ]
then
	mv application.log $dat.log
	touch application.log

else
	echo "No change"

fi


	

