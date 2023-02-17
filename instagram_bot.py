import Common
from pheed import pheed
from highlight import highlight

def instagram_bot(target_list:list, ID, PW, mode=1, view='off'):
    '''
    Args:
        target_list (list): 인스타그램 계정
        
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
    if not mode in [1, 2, 3]:
        return
    driver = Common.web(view)
    driver.get('https://www.instagram.com')

    Common.login(driver, ID, PW)
    Common.check_login(driver)

    for target in target_list:
        if mode in [1, 2]:
            pheed(driver, target)
        if mode in [1, 3]:
            highlight(driver, target)
        print(target, '완료')
    driver.quit()

