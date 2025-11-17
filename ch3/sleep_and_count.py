import time
import datetime
import sys

print("컨테이너가 실행됩니다.")
sys.stdout.flush()

# 10초마다 현재 시간을 출력하며 실행을 계속
while True:
    print(f"현재 시간: {datetime.datetime.now()}")
    sys.stdout.flush() # <--- 이 줄을 추가했습니다.
    time.sleep(10)
