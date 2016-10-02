#!/bin/bash
x=0
until [ "$x" -ge 10 ]; do
    echo "Current value of x: $x"
    x=$(expr $x + 1)
    sleep 1
    # sleep 1 은 프로그램이 잠깐 쉬도록 한다. 이 문장은 없어도 상관없다.  
done
