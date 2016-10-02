#!/bin/bash
if [ -d /etc/magic ]; then
 # 대괄호가 test 역할을 한다.세미콜론 ";"은 명령의 끝이라고 쉘에게 알려준다. 세미콜론 뒤에 오는 모든 것은 분리된 라인에 있는 것처럼 실행된다. 세미콜론을 사용함으로써 보다 읽기 쉬워진다.
 cp /etc/magic .
 echo "Done."
else
 echo "Honey, Magic is not what you're looking for."
 exit
fi
