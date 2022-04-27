# fastapi_study

해당 문서는 FAST API를 이용한 공부의 일환으로 사용하였음.

1. study.py
    - 기본적인 route 및 parameter / API 작성 파일

2. database directory
    - DB connect 학습을 위한 파일
    - 공식문서를 참조하여 작성하였음.

<h3> run source code
<hr>

1. git clone

```
git clone https://github.com/bobyeong2/fastapi_study.git
```

2. package install

```
pip install -r requirements.txt
```

3. run

```
uvicorn app.main:app --reload
```

<hr>

작동 시 DB session & DB infomation을 제공하는 파일을 작성한 뒤 실행할 것.

- reference
  - <https://fastapi.tiangolo.com/tutorial/sql-databases/#alternative-db-session-with-middleware>

- create template and test function
  - <https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864#69f2>
