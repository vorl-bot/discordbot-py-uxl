import random

fishes = ['고등어?','다리 달린 물고기','다리 달린 물고기','실패']

text1 =''
text2 =''


def fishresult():
    fish_result = random.choice(fishes)
    fsize = random.randrange(1,101)
    text1 =''
    text2 =''

    if fish_result == '실패':
        text1 = '이런!'
        text2 = '물고기가 도망갔다. 아무것도 낚지 못했다...'

    elif fish_result == '인면어':
        humanfishes = ['\"살려주세요. 살려주세요...\"','\"죽...여...줘....\"']
        humanfish = random.choice(humanfishes)
        fsize = fsize + 100
        text1 = '...이게 뭐지? 인면어를 낚았다.'
        text2 = humanfish + ' ...그것은 그렇게 말하곤 더 이상 움직이지 않았다.'

    elif fish_result == '다리 달린 물고기':
        legs = str(random.randrange(2,25))
        text1 = '다리가 ' + legs +'개 달린 물고기...?'
        text2 = '그것은 저벅저벅 걸어 도망쳤다.'
    
    elif fish_result == '폴리 1개':
        text1 = ':coin:' + fish_result+'을(를) 낚았다.'
        text2 = '짤랑짤랑'

    elif fish_result == '쓰레기' or fish_result =='돌멩이' or fish_result =='유리병':
        text1 = fish_result+'을(를) 낚았다.'
        text2 = '물고기가 아니잖아?'

    elif fish_result == '고래상어' or fish_result =='철갑상어' or fish_result =='실러캔스' or fish_result =='피라루쿠' or fish_result =='청상아리' or fish_result =='청새치' or fish_result =='킹크랩' or fish_result =='거대오징어' or fish_result =='크라켄'or fish_result == '대왕참치':
        fsize = fsize + 100
        text1 = fish_result+'을(를) 낚았다.'
        text2 = '성과 기록: '+str(fsize)+'cm?!'
    
    else:
        text1 = fish_result+'을(를) 낚았다.'
        text2 = '성과 기록: '+str(fsize)+'cm'

    return text1, text2
