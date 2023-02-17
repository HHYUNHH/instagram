import Common
from pheed import pheed
from highlight import highlight

def instagram_bot(target_list:list, ID, PW, mode=1, view='off'):
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

