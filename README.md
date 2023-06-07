### 라이브러리 설치
```c
$ pip install -r requirements.txt
```

### 실행
```c
python main.py
```
### GUI (2023.03.05_구현)
(2023.06.05_GUI업데이트)  
![image](https://github.com/HHYUNHH/instagram/assets/112064615/af4e1b55-7939-4086-b875-d818f8d4578d)

Target : 인스타그램 계정 (구분자 \n)  
Login : 로그인 할 계정  
Mode : 탐색 범위 설정  
View : 시각화 설정  
**입력예시**  
![image](https://github.com/HHYUNHH/instagram/assets/112064615/bc8f5c54-bea6-45fa-a4dd-82a261c1a089)

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
1: Feed + Highlight  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
2: Feed  
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

+ 테스트 확인(2023.02.18_Window10)
+ ~~view = 'off' 는 mode = 2 만 호환가능~~
+ 버전 체크 안함
+ 호출 제한 횟수 도달 시 에러 (제한횟수 미지)
+ ~~쓸모없는 에러메세지 다수 출력 확인~~ *(2023.03.29)
+ ~~저장하지 못하는 유형 존재 (상황 직면 시 쿼리스트링 출력)~~ *GUI 구현 후 출력 시각화 미설계
+ 로그인 상태 유지 기능 추가 (View 옵션 On 경우에만 가능), 브라우저 내 계정정보 존재 시 로그인 입력값 불필요(2023.03.29)
+ 변경된 일부 태그명 수정(2023.03.29)
+ 하이라이트 탐색 후 진입 대기시간 연장(5초 → 10초)(2023.05.20)
+ 포스트 순서 정렬 함수 추가(2023.05.20)
+ GUI 토글버튼으로 작업 조기 종료시 재귀하는 현상 수정(2023.05.20)
+ 로그인 확인 에러 수정(2023.06.05)
+ 피트 탐색 최대 대기시간 수정(1초 → 2초)(2023.06.05)
+ 일부 이미지 확장자 통일(JPG, HEIC, HEIF → PNG)(2023.06.05)

### GUI개선사항
2023.03.29
+ 프로세스방식 스레드화
+ 프로그래스바 추가
+ 실행버튼 토글식으로 변경

2023.06.05
+ 문자 수정
