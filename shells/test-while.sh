#!/bin/bash
# true는 실제 하나의 프로그램이다. 중단없이 루프가 계속 돌도록 하는 것.
# true 대신 ":" 명령을 사용할 수 있다. while :; do
# ":" 명령이 bash 안에 내포된 특성이기 때문에 훨씬 빠르다.
while true; do
 echo "Press CTRL-C to quit."
done
