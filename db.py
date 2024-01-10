from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://test:test@54.180.112.156', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.db_jungle_firstPro                        # 'jungle'라는 이름의 db를 만듭니다.

# MongoDB에서 데이터 모두 보기
all_users = list(db.china.find({}))

print(all_users)