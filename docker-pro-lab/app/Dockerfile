# 1. 기반 이미지 설정
FROM python:3.9-slim

# 2. 컨테이너 내부의 작업 디렉터리 지정
WORKDIR /app

# 3. 필요한 라이브러리 목록 파일 복사
COPY requirements.txt .

# 4. 라이브러리 설치(캐시 효율을 위해 라이브러리 먼저 설치)
RUN pip install --no-cache-dir -r requirements.txt

# 5. 앱 코드 복사
COPY app.py .

# 6. 컨테이너가 시작될 때 실행할 명령
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=5000", "--debug"]