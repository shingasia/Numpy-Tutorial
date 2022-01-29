import os  # from os import * 대신에 import os로 적어야 내장 open() 함수와 충돌이 없다.
import webbrowser


print(os.fspath("C:\\Users\\skdsk"))
print(os.getenv('JAVA_HOME', default='없음'))         # 환경변수 값을 돌려줌
print(os.O_RDONLY)
print(os.O_WRONLY)
print(os.O_RDWR)
print(os.O_APPEND)
print(os.O_CREAT)
print(os.O_EXCL)
print(os.O_TRUNC)


# os 모듈은 디렉터리 삭제, 이동, 복사 작업을 할 때 용이할 듯
