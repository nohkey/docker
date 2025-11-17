import os
import sys
import time

# fork()를 사용하여 자식 프로세스를 생성
pid = os.fork()

if pid > 0:
    # 부모 프로세스: 좀비 프로세스를 정리하고 계속 실행됩니다.
    print(f"부모 프로세스 (PID: {os.getpid()})가 자식 프로세스 (PID: {pid})를 생성했습니다.")
    sys.stdout.flush()

    # 5초간 대기하여 좀비가 되는 것을 잠시 기다립니다.
    time.sleep(5)
    print("5초 후 부모가 좀비를 정리합니다.")

    # os.wait()를 호출하여 자식 프로세스를 수집합니다.
    # 이 시점에서 좀비가 정리되어 사라집니다.
    os.wait()
    sys.stdout.flush()

    print("좀비 프로세스가 정리되었습니다. 컨테이너는 계속 실행됩니다.")
    while True:
        time.sleep(1)
else:
    # 자식 프로세스: 즉시 종료되어 좀비가 됩니다.
    print(f"자식 프로세스 (PID: {os.getpid()})가 즉시 종료됩니다.")
    sys.exit(0)
