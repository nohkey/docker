import os
import mysql.connector
from flask import Flask
import time

# Flask 앱 초기화
app = Flask(__name__)

# DB 연결 시도 함수
def get_db_connection():
    conn = None
    retries = 10
    print("데이터베이스 연결 시도 중...")
    while retries > 0:
        try:
            # 환경 변수에서 접속 정보를 읽어옴
            conn = mysql.connector.connect(
                host=os.environ.get('DB_HOST'),      # '-e DB_HOST=???'
                user=os.environ.get('DB_USER'),      # '-e DB_USER=???'
                password=os.environ.get('DB_PASSWORD'),# '-e DB_PASSWORD=???'
                database=os.environ.get('DB_NAME'),   # '-e DB_NAME=???'
                charset='utf8mb4'
            )
            print("데이터베이스 연결 성공")
            return conn
        except mysql.connector.Error as e:
            # DB가 아직 준비 중일 수 있으므로 3초 대기 후 재시도
            print(f"DB 연결 실패. 3초 후 {retries-1}회 재시도... (오류: {e})")
            retries -= 1
            time.sleep(3) 
    print("데이터베이스 연결 실패")
    return None

# Flask 웹 서버 로직
@app.route('/')
def index():
    # DB 연결
    conn = get_db_connection()
    if conn is None:
        # 연결 실패 시 에러 메시지 반환
        return "<h1>DB 연결 실패.</h1><p>DB 컨테이너 로그와 네트워크 설정을 확인하세요.</p>", 500
    
    try:
        # DB에서 데이터 조회
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users")
        users = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        
        # HTML 페이지 생성
        user_list_html = "".join([f"<li>{user}</li>" for user in users])
        return f"""
        <h1>🐳 도커와 MySQL 연동 성공 (v2.0)</h1>
        <p>데이터베이스의 'users' 테이블에서 가져온 목록입니다:</p>
        <ul>
            {user_list_html}
        </ul>
        """
    except Exception as e:
        # 쿼리 실행 중 에러 발생 시
        return f"<h1>데이터 조회 중 오류 발생:</h1><p>{e}</p>"

# 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)