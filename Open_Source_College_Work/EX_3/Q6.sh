read -p "Enter name of the text file =" file

words= $(wc -w "$file")
lines= $(wc -l "$file")
char= $(wc -c "$file")

echo "Number of lines = $lines"
echo "Number of words = $words"
echo "Number of characters = $char"

