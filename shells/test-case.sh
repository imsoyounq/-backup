#!/bin/bash
for x in 0 1 2 3 4 5 6 7 8 9 10; do
case $x in
    0) echo "Value of x is 0."
      ;;
    5) echo "Value of x is 5."
      ;;
    9) echo "Value of x is 9."
      ;;
    *) echo "Unrecognized value."
    sleep 0.5
esac
done
