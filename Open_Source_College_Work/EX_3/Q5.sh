read -p "Enter file name =" file

if [ -f "$file" ]
then
	if [ -r "$file" ]
	then
		echo "$file is readable"
	else
		echo "$file is not readable"
	fi
	if [ -w "$file" ]
	then
		echo "$file is writeable"
	else
		echo "$file is not writeable"
	fi
	
	if [ -x "$file" ]
	then 
		echo "$file is executeable"
	else
		echo "$file is not executeable"
	fi
else
	echo "$file does not exit"

fi

		
