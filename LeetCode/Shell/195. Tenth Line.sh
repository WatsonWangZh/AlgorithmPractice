# Given a text file file.txt, print just the 10th line of the file.

# Example:
# Assume that file.txt has the following content:
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10

# Your script should output the tenth line, which is:
# Line 10

# Note:
# 1. If the file contains less than 10 lines, what should you output?
# 2. There's at least three different solutions. Try to explore all possibilities.

# Read from the file file.txt and output the tenth line to stdout.

sed -n '10p' file.txt

tail -n +10 file.txt | head -n 1

head -n 10 file.txt | tail -n +10

awk '{if(NR==10){print $0}}' file.txt

# https://mp.weixin.qq.com/s/EI63RZZcPzJT4c0zl8XQSA

row_num=$(cat file.txt | wc -l)
echo $row_num
if [ $row_num -lt 10 ];then
    echo "The number of row is less than 10"
else
    sed -n '10p' file.txt
fi