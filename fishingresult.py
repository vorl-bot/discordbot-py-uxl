import random

fishes = ['고등어','갈치','가다랑어','꽁치','날치','노가리','명태',
          '은어','전어','개복치','정어리','멸치','청어','참치',
          '우럭','도미','무지개송어','숭어','연어','농어','장어',
          '넙치','문어','오징어','복어','해삼','말미잘','멍게',
          '피라미','바닷가재','게','미꾸라지','바다거북','자라','피라냐','금태',
          '개불','해파리','클리오네','도루묵','조기','대구','아귀',
          '가리비','바지락','산호','백산호','빙어','칠성장어',
          '일각고래','철갑상어','실러캔스','피라루쿠','청상아리','거대 조개',
          '청새치','킹크랩','거대오징어','크라켄','대왕참치','불가사리',
          '새우','미역','다시마','녹조류','갯강구','촉수','촉수',
          '인면어','인면어','폴리 1개','폴리 1개','해저지네',
          '다리 달린 물고기','다리 달린 물고기','실패']

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
        legsrun = random.choice(['저벅저벅 걸어','사사사삭 기어'])
        text1 = '다리가 ' + legs +'개 달린 물고기...?'
        text2 = '그것은 ' + legsrun + ' 도망쳤다.'
    
    elif fish_result == '촉수':
        fsize = fsize + 100
        text1 = '정체불명의 촉수를 낚았다...?'
        text2 = '성과 기록: '+str(fsize)+'cm. 조금 꿈틀거린 것 같다...'

    elif fish_result == '폴리 1개':
        text1 = ':coin:' + fish_result+'을(를) 낚았다.'
        text2 = '짤랑짤랑'

    elif fish_result == '일각고래' or fish_result =='철갑상어' or fish_result =='실러캔스' or fish_result == '거대 조개' or fish_result =='피라루쿠' or fish_result =='청상아리' or fish_result =='청새치' or fish_result =='킹크랩' or fish_result =='거대오징어' or fish_result =='크라켄'or fish_result == '대왕참치':
        fsize = fsize + 100
        text1 = fish_result+'? 비슷한 것을 낚았다.'
        text2 = '성과 기록: '+str(fsize)+'cm?!'

    elif fish_result == '갈치':
        fsize = fsize + 50
        text1 = fish_result+'? 비슷한 것을 낚았다.'
        text2 = '성과 기록: '+str(fsize)+'cm'
    
    else:
        text1 = fish_result+'? 비슷한 것을 낚았다.'
        text2 = '성과 기록: '+str(fsize)+'cm'

    return text1, text2
