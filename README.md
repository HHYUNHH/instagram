### 라이브러리 설치
```c
$ pip install -r requirements.txt
```

### 실행
```c
python main.py
```
### GUI (2023.03.05_구현)
Target : 인스타그램 계정 (구분자 \n)  
Login : 로그인 할 계정  
Mode : 탐색 범위 설정  
View : 시각화 설정  
#### 입력예시  
![image](https://user-images.githubusercontent.com/112064615/222964064-bb66f661-16db-4bef-add8-4fb4e774d1b6.png)

---
### ~~파라미터 설정~~  
Args:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
target_list (list): 인스타그램 계정  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
ID, PW (str): 로그인 할 인스타그램 계정  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
mode (int): 원하는 모드 설정  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
1: Pheed + Highlight  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
2: Pheed  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
3: Highlight  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Default: 1  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
view (str): 시각화 설정 (대소문자 구별X)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
'On': On  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
'Off': Off  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Default: 'Off'  
```c
# 예시
target_list = ['bts.bighitofficial', 'blackpinkofficial']
ID = 'kimchiman123'
PW = 'qwer1234'
mode = 1
view = 'on'
```
+ ~~view = 'off' 는 mode = 2 만 호환가능~~
+ ~~라이브러리화 후 테스트 안함~~ *확인 완료 이상 없음(2023.02.18_Window10)
+ 버전 체크 안함
+ 호출 제한 횟수 도달 시 에러 (제한횟수 미지)
+ 에러 유발의 원인으로 인터넷 속도의 영향이 큼
+ 쓸모없는 에러메세지 다수 출력 확인
+ ~~저장하지 못하는 유형 존재 (상황 직면 시 쿼리스트링 출력)~~ *GUI 구현 후 출력 시각화 미설계
+ 조기중단 후 재시작 시 데이터 소실가능성 존재 (소실을 원치 않을 경우 로그파일 삭제 권장)
