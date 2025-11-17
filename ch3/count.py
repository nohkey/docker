import sys
import time

print("컨테이너가 실행됩니다. 1초마다 카운터가 증가합니다.")
sys.stdout.flush()

counter = 0

# 1초마다 카운터를 출력하며 실행을 계속
while True:
    print(f"카운터: {counter}")
    sys.stdout.flush()
    counter += 1
    time.sleep(1)
