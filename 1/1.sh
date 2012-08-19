# File: 1.sh
# Description: http://projecteuler.net/problem=1

SUM=0
for i in `seq 3 999`; do
    if [ "$(($i % 3))" = "0" ] || [ "$(($i % 5))" = "0" ]; then
        SUM=$(($SUM+$i))
    fi
done
echo $SUM
