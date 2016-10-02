#!/bin/bash
if test -f/etc/magic
then
 # 파일이 존재하면, 복사하고 메시지를 출력한다.
 cp /etc/magic .
 echo "Done."
else
 # 파일이 존재하지 않으면, 메시지를 출력하고 프로그램을 종료한다.
 echo "This file does not exist."
 exit
fi
