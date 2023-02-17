from instagram_bot import instagram_bot

'''
Args:
    target_list (list):  인스타그램 계정
    
    ID, PW (str): 로그인 할 인스타그램 계정
    
    mode (int): 원하는 모드 설정
        1: Pheed + Highlight
        2: Pheed
        3: Highlight
        Default: 1
        
    view (str): 시각화 설정 (대소문자 구별X)
        'On': On
        'Off': Off
        Default: 'Off'
'''

target_list = None
ID = None
PW = None

instagram_bot(
    target_list=target_list,
    ID=ID,
    PW=PW,
    mode=1,
    view='on'
    )