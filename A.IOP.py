import discord
import openpyxl
import asyncio




client = discord.Client()

@client.event
async def on_ready():
    print('*DB Online*')
    print("Client Name= " + "'" + client.user.name + "'")
    print("Client ID= " + "'" + client.user.id + "'")
    print('---LOG---')
    await client.change_presence(game=discord.Game(name='사용법 : /인형도감?', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('/오류'):
        clear = message.content.split(" ")
        print(clear)

    if message.content.startswith("/인형도감사용법") or message.content.startswith("/인형도감?"):
        channel = message.channel
        embed = discord.Embed(
            title = '명령어목록',
            description = '"전 도움말을 다 읽는 파인데"',
            colour = discord.Colour.red()
        )

        embed.set_footer(text = '대소문자 무시와 띄어쓰기는 안된다구욧!')
        embed.add_field(name='/[인형이름]', value='해당 인형의 프로필를 알려줍니다' + '\n' + '/No.[숫자].  또는 /[인형별명]으로도 검색가능합니다.', inline=False)
        embed.add_field(name='/[인형이름] 드랍', value='해당 인형의 드랍 지역을 알려줍니다.', inline=False)
        embed.add_field(name='/[제조시간]', value='해당 제조시간에서 획득할 수 있는 인형 또는 장비, 요정 등을 알려줍니다. ' + '\n' + '00:00 또는 0000의 양식으로 검색해주세요.', inline=False)
        embed.add_field(name='/자원소비량', value='인형별 자원 소비량을 알려줍니다.', inline=False)
        embed.add_field(name='/장비최소식', value='장비 제조의 필요한 최소 조건을 알려줍니다.', inline=False)
        embed.add_field(name='/요정등장조건', value='요정별 등장 조건을 알려줍니다.', inline=False)
        embed.add_field(name='팁', value='[괄호]는 예시일 뿐, 명령어에 포함되어있지않습니다. 괄호를 뺴야 정상작동합니다.', inline=False)
        embed.add_field(name='현재 구현 인형', value='No.1~94', inline=False)

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/DB Online?"):
         await client.send_message(message.channel, embed=discord.Embed(title = 'DB Online', descrption = ''))

    if message.content.startswith("/자원소비량"):
        channel = message.channel
        embed = discord.Embed(
            title = '자원소비량',
            description = '"그치만.. 이렇게라도 하지않으면 지휘관의 자원은 넘쳐나는걸?"',
            colour = discord.Colour.red()
        )

        embed.set_footer(text = '(숫자) = 증가폭')
        embed.add_field(name='HG', value='(편제 인원당)' + '\n' +'탄약' + '\n' + 'ㄴ 10 / 15 / 20 / 25 / 30 / (+5)' + '\n' + '식량' + '\n' + 'ㄴ 10 / 15 / 20 / 25 / 30 / (+5)', inline=True)
        embed.add_field(name='SMG', value='(편제 인원당)' + '\n' +'탄약' + '\n' + 'ㄴ 25 / 40 / 55 / 70 / 85 / (+15)' + '\n' + '식량' + '\n' + 'ㄴ 20 / 30 / 40 / 50 / 60 / (+10)', inline=True)
        embed.add_field(name='AR', value='(편제 인원당)' + '\n' +'탄약' + '\n' + 'ㄴ 20 / 30 / 40 / 50 / 60 / (+10)' + '\n' + '식량' + '\n' + 'ㄴ 20 / 30 / 40 / 50 / 60 / (+10)', inline=True)
        embed.add_field(name='RF', value='(편제 인원당)' + '\n' +'탄약' + '\n' + 'ㄴ 15 / 25 / 35 / 45 / 55 / (+10)' + '\n' + '식량' + '\n' + 'ㄴ 30 / 45 / 60 / 75 / 90 / (+15)', inline=True)
        embed.add_field(name='MG', value='(편제 인원당)' + '\n' +'탄약' + '\n' + 'ㄴ 40 / 65 / 80 / 115 / 140 / (+25)' + '\n' + '식량' + '\n' + 'ㄴ 30 / 45 / 60 / 75 / 90 / (+15)', inline=True)
        embed.add_field(name='SG', value='(편제 인원당)' + '\n' +'탄약' + '\n' + 'ㄴ 30 / 45 / 60 / 75 / 90 / (+15)' + '\n' + '식량' + '\n' + 'ㄴ 40 / 65 / 80 / 115 / 140 / (+25)', inline=True)
        embed.add_field(name='헬리포트 인력', value='(총기 종류에 무관하게 편제 수 합산 × 2)' + '\n' +'ex) 3/4/5/1/2 링크면 (3 + 4 + 5 + 1 + 2) × 2 = 30 소모', inline=True)

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/장비최소식"):
        channel = message.channel
        embed = discord.Embed(
            title = '장비최소식',
            description = '"우중 센세 제발.."',
            colour = discord.Colour.red()
        )

        embed.add_field(name='사이트류', value='탄약' + '\n' + 'ㄴ 150 이하' + '\n' + '부품' + '\n' + 'ㄴ 150 이하', inline=True)
        embed.add_field(name='야시장비', value='조건없음', inline=True)
        embed.add_field(name='소음기', value='조건없음', inline=True)
        embed.add_field(name='탄약류', value='탄약' + '\n' + 'ㄴ 탄약 100 이상', inline=True)
        embed.add_field(name='외골격', value='조건없음', inline=True)
        embed.add_field(name='방탄판', value='조건없음', inline=True)
        embed.add_field(name='탄약통', value='부품' + '\n' + 'ㄴ 부품 150 이상', inline=True)
        embed.add_field(name='슈트', value='조건없음', inline=True)

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/요정등장조건"):
        channel = message.channel
        embed = discord.Embed(
            title = '요정 등장 조건',
            description = '"공수레 공수거 공수좀"',
            colour = discord.Colour.red()
        )

        embed.set_footer(text = '(숫자) = 증가폭')
        embed.add_field(name='인력 탄약 식량 부품', value='------', inline=True)
        embed.add_field(name='500 500 500 500', value='용사 요정, 격노 요정, 방패 요정, 수호 요정, 도발 요정, 저격 요정, 포격 요정, 공습 요정, 지휘 요정, 수색 요정, 조명 요정 (최소식요정들)', inline=True)
        embed.add_field(name='2000 500 2000 1000', value='최소식 요정, 방어 요정, 증원 요정, 공수 요정', inline=True)
        embed.add_field(name='500 2000 2000 1000', value='최소식 요정, 매설 요정, 로켓 요정, 공사 요정', inline=True)
        embed.add_field(name='2000 2000 2000 1000', value='이벤트 요정을 제외한 모든 요정이 등장할 수 있는 범용식', inline=True)

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/SkillPoint") or message.content.startswith("/스포") or message.content.startswith("/제작자"):
        await client.send_file(message.channel, 'ACCESS DENIED.jpg')
        channel = message.channel
        embed = discord.Embed(
            title = '스킬포인트 | 제작자',
            description = '카리나, 안젤리아, 페르시카, 꼬마 봇의 제작자',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='♥', inline=True)
        embed.add_field(name='종류', value='NoYe', inline=True)
        embed.add_field(name='제조시간', value='Unknow', inline=True) 
        embed.add_field(name='별명', value='스포', inline=True)
        print('SkillPoint')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/콜트리볼버") or message.content.startswith("/콜라") or message.content.startswith("/No.1."):
        await client.send_file(message.channel, 'No.1_콜트_리볼버.png')
        channel = message.channel
        embed = discord.Embed(
            title = '콜트 리볼버 | No.1.',
            description = '"지휘관, 날…불렀어? 콜라 있어? 저기, 콜라 있는거야?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:50', inline=True) 
        embed.add_field(name='스킬', value='일제사격' + '\n' + '지속시간 동안 아군 전원 화력 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '화력 상승치 : 22%' + '\n' + '지속시간 : 8초', inline=True) 
        embed.add_field(name='버프', value='1편제-화력 12%, 명중 25% 상승' + '\n' + '□■□ 2편제-화력 15%, 명중 31% 상승' + '\n' + '■◎■ 3편제-화력 18%, 명중 37% 상승' + '\n' + '□■□ 4편제-화력 21%, 명중 43% 상승' + '\n' + '5편제-화력 24%, 명중 50% 상승', inline=True)
        embed.add_field(name='별명', value='콜라', inline=True)
        print('콜트 리볼버')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M1911") or message.content.startswith("/운명이") or message.content.startswith("/No.2."):
        await client.send_file(message.channel, 'No.2_M1911.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M1911 | No.2',
            description = '"운명적인 만남이네요~! 또 이렇게 지휘관님이랑 만나게 되다니~"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:20', inline=True) 
        embed.add_field(name='스킬', value='연막탄' + '\n' + '폭발한 위치의 2.5 반경에 적의 사속/이속을 감소시키는 연막이 발생' + '\n' + '초반 쿨타임 : 1초' + '\n' + '쿨타임 : 12초' + '\n' + '사속/이속 감속치 : 36/45%' + '\n' + '지속시간 : 4초', inline=True) 
        embed.add_field(name='버프', value='1편제 - 사속 10%, 명중 25% 상승' + '\n' + '□■□ 2편제 - 사속 12%, 명중 31% 상승' + '\n' + '■◎■ 3편제 - 사속 15%, 명중 37% 상승' + '\n' + '□■□ 4편제 - 사속 17%, 명중 43% 상승' + '\n' + '5편제 - 사속 20%, 명중 50% 상승', inline=True)
        embed.add_field(name='별명', value='운명이', inline=True)
        print('M1911')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M9") or message.content.startswith("/엠구나노") or message.content.startswith("/No.3."):
        await client.send_file(message.channel, 'No.3_M9.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M9 | No.3',
            description = '"베레타 M9인거야! 인기인인거야!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:40', inline=True) 
        embed.add_field(name='스킬', value='섬광탄' + '\n' + '폭발한 위치의 2.5 반경에 적에게 기절을 건다.' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 3.2초', inline=True) 
        embed.add_field(name='버프', value='1편제 - 화력 10%, 회피 10% 상승' + '\n' + '□■■ 2편제 - 화력 12%, 회피 12% 상승' + '\n' + '□◎□ 3편제 - 화력 15%, 회피 15% 상승' + '\n' + '□■■ 4편제 - 화력 17%, 회피 17% 상승' + '\n' + '5편제 - 화력 20%, 회피 20% 상승', inline=True)
        embed.add_field(name='별명', value='엠구나노', inline=True)
        print('M19')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/콜트파이슨") or message.content.startswith("/No.4."):
        await client.send_file(message.channel, 'No.4_콜트_파이슨.png')
        channel = message.channel
        embed = discord.Embed(
            title = '콜트파이슨 | No.4',
            description = '"당신이 새로운 "사냥감"인가, 지휘관? 후훗, 걱정 마, 불경한 뜻은 전혀 없으니까."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='제조불가', inline=True) 
        embed.add_field(name='스킬', value='겁없는 녀석들' + '\n' + '패시브: 자신이 화력 / 사속 / 회피 / 명중 / 치명타율 버프를 받을 때(요정특성 포함).' + '\n' + '버프 진형의 아군에게 해당 스탯 버프 부여(3초 지속, 최대 3중첩)' + '\n' + '액티브: 발동 후 6회의 공격은 일정 확률로 지속시간 동안 자신의 화력 상승(최대 중첩 6회)' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 15초' + '\n' + '패시브 상승치(%) :  6 / 6 / 30 / 30 / 12' + '\n' + '화력 상승치 : 30%' + '\n' + '액티브 화력 상승 지속시간 : 3.2초', inline=True) 
        embed.add_field(name='버프', value='1편제 - 화력 15%, 치명타율 10% 상승' + '\n' + '□■■ 2편제 - 화력 18%, 치명타율 12% 상승' + '\n' + '■◎□ 3편제 - 화력 22%, 치명타율 15% 상승' + '\n' + '■■□ 4편제 - 화력 26%, 치명타율 17% 상승' + '\n' + '5편제 - 화력 30%, 치명타율 20% 상승', inline=True)
        print('콜트파이슨')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/나강할매") or message.content.startswith("/나강리볼버") or message.content.startswith("/No.5."):
        await client.send_file(message.channel, 'No.5_나강_리볼버.png')
        channel = message.channel
        embed = discord.Embed(
            title = '나강리볼버 | No.5 ',
            description = '"이런 늙은이가 취향이라니, 자네도 참 별나구먼."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:20', inline=True) 
        embed.add_field(name='스킬', value='기선제압N' + '\n' + '지속시간 동안 적 전체 화력 감소/뒤쪽의 수치는 주간작전에 사용시' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8/5초' + '\n' + '화력감소치 : 35/20%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 화력 16%, 치명률 8% 상승' + '\n' + '□■□ 2편제 - 화력 20%, 치명률 10% 상승' + '\n' + '■◎□ 3편제 - 화력 24%, 치명률 12% 상승' + '\n' + '□■□ 4편제 - 화력 28%, 치명률 14% 상승' + '\n' + '5편제 - 화력 32%, 치명률 16% 상승', inline=True)
        embed.add_field(name='별명', value='나강할매', inline=True)
        print('나강리볼버')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/토카레프") or message.content.startswith("/No.6."):
        await client.send_file(message.channel, 'No.6_토카레프.png')
        channel = message.channel
        embed = discord.Embed(
            title = '토카레프 | No.6',
            description = '"아, 지휘관, 잘 부탁드립니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:45', inline=True) 
        embed.add_field(name='스킬', value='엄호개시' + '\n' + '지속시간 동안 아군 전체 회피 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '회피 증가치 : 55%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 사속 10%, 명중 25% 상승' + '\n' + '□■■ 2편제 - 사속 12%, 명중 31% 상승' + '\n' + '□◎□ 3편제 - 사속 15%, 명중 37% 상승' + '\n' + '□■■ 4편제 - 사속 17%, 명중 43% 상승' + '\n' + '5편제 - 사속 20%, 명중 50% 상승', inline=True)
        print('토카레프')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/스테츠킨") or message.content.startswith("/스테") or message.content.startswith("/No.7."):
        await client.send_file(message.channel, 'No.7_스테츠킨.png')
        channel = message.channel
        embed = discord.Embed(
            title = '스테츠킨 | No.7',
            description = '"자동 권총, 스테츠킨 APS! 등장!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:55', inline=True) 
        embed.add_field(name='스킬', value='진압신호' + '\n' + '지속시간 동안 아군 전원 사속 상승' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '사속 상승치 : 22%', inline=True)
        embed.add_field(name='버프', value='1편제 - 화력 6%, 사속 12% 상승' + '\n' + '□■■ 2편제 - 화력 7%, 사속 15% 상승' + '\n' + '□◎□ 3편제 - 화력 9%, 사속 18% 상승' + '\n' + '□■■ 4편제 - 화력 10%, 사속 21% 상승' + '\n' + '5편제 - 화력 12%, 사속 24% 상승', inline=True)
        embed.add_field(name='별명', value='스테, 번개머리, 수타치킨', inline=True)
        print('스테츠킨')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/마카로프") or message.content.startswith("/No.8."):
        await client.send_file(message.channel, 'No.8_마카로프.png')
        channel = message.channel
        embed = discord.Embed(
            title = '마카로프 | No.8',
            description = '"나는 있지, 지휘관님이 명령하기보다는 서로 맞춰나가는 쪽이 더 좋아."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:40', inline=True) 
        embed.add_field(name='스킬', value='시야봉쇄' + '\n' + '지속시간 동안 적 전체 명중 감소' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '명중 감소치 : 36%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 화력 10%, 사속 6% 상승' + '\n' + '■□□ 2편제 - 화력 12%, 사속 7% 상승' + '\n' + '■◎■ 3편제 - 화력 15%, 사속 9% 상승' + '\n' + '■□□ 4편제 - 화력 17%, 사속 10% 상승' + '\n' + '5편제 - 화력 20%, 사속 12% 상승', inline=True)
        print('마카로프')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/P38") or message.content.startswith("/상하이조") or message.content.startswith("/No.9."):
        await client.send_file(message.channel, 'No.9_P38.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'P38 | No.9',
            description = '"이것은 운명의 만남이에요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:20', inline=True) 
        embed.add_field(name='스킬', value='조명탄' + '\n' + '지속시간 동안 아군 전체 명중 상승(야간작전 전용)' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 15초' + '\n' + '명중 감소치 : 90%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 사속 7%, 명중 28% 상승' + '\n' + '□■■ 2편제 - 사속 8%, 명중 35% 상승' + '\n' + '□◎□ 3편제 - 사속 10%, 명중 42% 상승' + '\n' + '□■■ 4편제 - 사속 12%, 명중 49% 상승' + '\n' + '5편제 - 사속 14%, 명중 56% 상승', inline=True)
        embed.add_field(name='별명', value='상하이조', inline=True)
        print('P38')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/PPK") or message.content.startswith("/발터") or message.content.startswith("/No.10."):
        await client.send_file(message.channel, 'No.10_PPK.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'PPK | No.10',
            description = '"우후훗, 발터 PPK야. 지휘관, 만나게 돼서...기쁘네요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:22', inline=True) 
        embed.add_field(name='스킬', value='사냥신호' + '\n' + '지속시간 동안 아군 전원 화력, 치명률 증가' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 15초' + '\n' + '화력, 치명률 증가치 : 10%, 35%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 사속 16%, 치명률 8% 상승' + '\n' + '■□□ 2편제 - 사속 20%, 치명률 10% 상승' + '\n' + '■◎□ 3편제 - 사속 24%, 치명률 12% 상승' + '\n' + '■□□ 4편제 - 사속 28%, 치명률 14% 상승' + '\n' + '5편제 - 사속 32%, 치명률 16% 상승', inline=True)
        embed.add_field(name='별명', value='신살자, 유신, 발터, 피피케이', inline=True)
        print('PPK')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/P08") or message.content.startswith("/No.11."):
        await client.send_file(message.channel, 'No.11_P08.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'P08 | No.11',
            description = '"루거 P08식 자동권총입니다. 모자라지만 잘 부탁드립니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:30', inline=True) 
        embed.add_field(name='스킬', value='엄호개시N' + '\n' + '지속시간 동안 아군 전체 회피 증가/ 뒤쪽의 수치는 주간작전에 사용시' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 8 / 5초' + '\n' + '회피 증가치 : 85 / 35%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 화력 7%, 명중 35% 상승' + '\n' + '□■□ 2편제 - 화력 8%, 명중 43% 상승' + '\n' + '□◎■ 3편제 - 화력 10%, 명중 52% 상승' + '\n' + '□■□ 4편제 - 화력 12%, 명중 61% 상승' + '\n' + '5편제 - 화력 14%, 명중 70% 상승', inline=True)
        print('P08')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/C96") or message.content.startswith("/No.12."):
        await client.send_file(message.channel, 'No.12_C96.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'C96 | No.12',
            description = '"당신이 제 지휘관인 것이군요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:30', inline=True) 
        embed.add_field(name='스킬', value='조명탄' + '\n' + '지속시간 동안 아군 전체 명중 증가(야간작전 전용)' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 15초' + '\n' + '명중 증가치 : 100%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 명중 32%, 회피 15% 상승' + '\n' + '■□□ 2편제 - 명중 40%, 회피 18% 상승' + '\n' + '□◎■ 3편제 - 명중 48%, 회피 22% 상승' + '\n' + '■□□ 4편제 - 명중 56%, 회피 26% 상승' + '\n' + '5편제 - 명중 64%, 회피 30% 상승', inline=True)
        print('C96')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/92식") or message.content.startswith("/No.13."):
        await client.send_file(message.channel, 'No.13_92식.png')
        channel = message.channel
        embed = discord.Embed(
            title = '92식 | No.13',
            description = '"바로 저, 92식 권총이 착임했습니다. 배속되는 소대는 어디인가요?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:35', inline=True) 
        embed.add_field(name='스킬', value='돌격개시' + '\n' + '지속시간 동안 아군 전원 화력, 사속 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '화력, 사속 증가치 : 10%, 10%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 명중 25%, 회피 20% 상승' + '\n' + '■■■ 2편제 - 명중 31%, 회피 25% 상승' + '\n' + '■◎■ 3편제 - 명중 37%, 회피 30% 상승' + '\n' + '■■■ 4편제 - 명중 43%, 회피 35% 상승' + '\n' + '5편제 - 명중 50%, 회피 40% 상승', inline=True)
        print('92식')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/아스트라리볼버") or message.content.startswith("/No.14."):
        await client.send_file(message.channel, 'No.14_아스트라_리볼버.png')
        channel = message.channel
        embed = discord.Embed(
            title = '아스트라 리볼버 | No.14',
            description = '"잘 부탁드릴게요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:40', inline=True) 
        embed.add_field(name='스킬', value='진압신호' + '\n' + '지속시간 동안 아군 전원 사속 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '사속 증가치 : 20%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 사속 10%, 회피 10% 상승' + '\n' + '■□■ 2편제 - 사속 12%, 회피 12% 상승' + '\n' + '□◎□ 3편제 - 사속 15%, 회피 15% 상승' + '\n' + '■□■ 4편제 - 사속 17%, 회피 17% 상승' + '\n' + '5편제 - 사속 20%, 회피 20% 상승', inline=True)
        print('아스트라 리볼버')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/글록17") or message.content.startswith("/No.15."):
        await client.send_file(message.channel, 'No.15_글록_17.png')
        channel = message.channel
        embed = discord.Embed(
            title = '글록17 | No.15',
            description = '"글록 17, 도착! 지금, 웃고계신건가요?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='기선제압' + '\n' + '지속시간 동안 적 전체 화력 감소' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '화력 감소치 : 25%', inline=True) 
        embed.add_field(name='버프', value='1편제 - 명중 32%, 회피 15% 상승' + '\n' + '■□■ 2편제 - 명중 40%, 회피 18% 상승' + '\n' + '□◎■ 3편제 - 명중 48%, 회피 22% 상승' + '\n' + '■□■ 4편제 - 명중 56%, 회피 26% 상승' + '\n' + '5편제 - 명중 64%, 회피 30% 상승', inline=True)
        print('글록17')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/톰슨") or message.content.startswith("/님총톰") or message.content.startswith("/시카고타자기") or message.content.startswith("/No.15."):
        await client.send_file(message.channel, 'No.16_톰슨.png')
        channel = message.channel
        embed = discord.Embed(
            title = '톰슨 | No.16',
            description = '"당신이 새로운 보스인가... 시카고 타자기야. 잘 부탁해."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='02:39', inline=True) 
        embed.add_field(name='스킬', value='포스실드' + '\n' + '자신의 피해를 막는 왜곡방벽을 9999점 생성한다' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 4초', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 12%, 회피 15% 상승' + '\n' + '■□□' + '\n' + '□◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='님통촘, 시카고타자기', inline=True)
        print('톰슨')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M3") or message.content.startswith("/No.17."):
        await client.send_file(message.channel, 'No.17_M3.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M3 | No.17',
            description = '"아, 안녕하세요! M3라고 합니다. 자, 잘부탁드립니다!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:30', inline=True) 
        embed.add_field(name='스킬', value='수류탄' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 5.5배', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='명중 40%, 회피 30% 상승' + '\n' + '□□□' + '\n' + '■◎□' + '\n' + '□□□', inline=True)
        print('M3')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MAC10") or message.content.startswith("/MAC-10") or message.content.startswith("/No.18."):
        await client.send_file(message.channel, 'No.18_MAC-10.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MAC-10 | No.18',
            description = '"지휘관의 지시라면…잉그램 M10은…기쁘게 받아들이죠."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='02:00', inline=True) 
        embed.add_field(name='스킬', value='연막탄' + '\n' + '폭발 위치의 2.5 반경에 적의 사속/이속을 감소시키는 연막이 발생' + '\n' + '초반 쿨타임 : 1초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 4초' + '\n' + '사속 / 이속 감소치 : 36 / 50%', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 12% 상승' + '\n' + '■□□' + '\n' + '■◎□' + '\n' + '■□□', inline=True)
        print('MAC-10')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/FMG9") or message.content.startswith("/FMG-9") or message.content.startswith("/No.19."):
        await client.send_file(message.channel, 'No.19_FMG-9.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'FMG-9 | No.19',
            description = '"FMG-9이 보스의 지휘 하에 들어왔습니다. 아, 걱정 마세요. 지금은 변장하지 않았으니까요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='연막탄' + '\n' + '지속시간 동안 자신의 회피 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '회피 증가치 : 120%', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 10%, 회피 12% 상승' + '\n' + '■□□' + '\n' + '□◎□' + '\n' + '■□□', inline=True)
        print('FMG-9')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/Vector") or message.content.startswith("/벡터") or message.content.startswith("/No.20."):
        await client.send_file(message.channel, 'No.20_Vector.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'Vector | No.20',
            description = '"응? 새로운 지휘관? 그래, 사이좋게 지내자."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='02:35', inline=True) 
        embed.add_field(name='스킬', value='소이탄' + '\n' + '소이탄을 던져 1.5 반경에 피해를 주고 매 0.33초마다 화상 대미지를 입히는 구간을 생성' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '폭발/지속 피해량 : 7 / 1배' + '\n' + '지속 시간 : 5초', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='사속 25% 상승승' + '\n' + '□□□' + '\n' + '■◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='벡터, 벡린탄', inline=True)
        print('Vector')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/PPSh-41") or message.content.startswith("/PPSh41") or message.content.startswith("/파파샤") or message.content.startswith("/No.21."):
        await client.send_file(message.channel, 'No.21_PPSh-41.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'PPSh-41 | No.21',
            description = '"처음 뵙겠습니다. 지휘관, 저…전혀 무겁지 않아요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:50', inline=True) 
        embed.add_field(name='스킬', value='수류탄' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 5.5배', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 10%, 사속 5% 상승' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        embed.add_field(name='별명', value='파파샤', inline=True)
        print('PPSh-41')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/PPS-43") or message.content.startswith("/PPS43") or message.content.startswith("/핑파샤") or message.content.startswith("/No.22."):
        await client.send_file(message.channel, 'No.22_PPS-43.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'PPS-43 | No.22',
            description = '"동지여, 만나서 영광입니다. 저는 가벼운 게 장점입니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='02:10', inline=True) 
        embed.add_field(name='스킬', value='수류탄' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 6배', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 12% 상승' + '\n' + '■□□' + '\n' + '■◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='핑파샤', inline=True)
        print('PPS-43')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/PP-90") or message.content.startswith("/PP90") or message.content.startswith("/란코") or message.content.startswith("/No.23."):
        await client.send_file(message.channel, 'No.23_PP-90.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'PP-90 | No.23',
            description = '"PP-90이야, 잘 부탁해. 지휘관의 첫 지시, 기쁜 마음으로 기다리고 있을게!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='02:20', inline=True) 
        embed.add_field(name='스킬', value='회피기동T' + '\n' + '지속시간 동안 자신의 회피 증가' + '\n' + '초반 쿨타임 : 4초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 15초' + '\n' + '회피 증가치 : 45%', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 8%, 회피 20% 상승' + '\n' + '■□□' + '\n' + '□◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='란코', inline=True)
        print('PP-90')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/PP-2000") or message.content.startswith("/PP2000") or message.content.startswith("/PPAP") or message.content.startswith("/피피이천") or message.content.startswith("/No.24."):
        await client.send_file(message.channel, 'No.24_PP-2000.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'PP-2000 | No.24',
            description = '"PP-2000입니다. 계속 당신의 곁에 있을 수 있겠네요. 후훗."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:10', inline=True) 
        embed.add_field(name='스킬', value='수류탄' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 5.5배', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 10%, 명중 25% 상승' + '\n' + '■□□' + '\n' + '□◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='PPAP, 피피이천', inline=True)
        print('PP-2000')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MP40") or message.content.startswith("/승만이") or message.content.startswith("/엠피") or message.content.startswith("/No.25."):
        await client.send_file(message.channel, 'No.25_MP40.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MP40 | No.25',
            description = '"지휘관님. 저, 있는 힘껏 노력할게요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:30', inline=True) 
        embed.add_field(name='스킬', value='소이탄' + '\n' + '소이탄을 던져 1.5 반경에 피해를 주고 매 0.33초마다 화상 데미지를 입히는 구간을 생성' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '폭발/지속 피해량 : 5.5 / 1배' + '\n' + '지속시간 : 5초', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='명중 25%, 회피 20% 상승' + '\n' + '■□□' + '\n' + '□◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='엠피, 승만이', inline=True)
        print('MP40')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MP5") or message.content.startswith("/우유") or message.content.startswith("/No.26."):
        await client.send_file(message.channel, 'No.26_MP5.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MP5 | No.26',
            description = '"MP5, 지금 막 도착했습니다! 키, 키가 작다고 해서 얕잡아 보지 말아주셔요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='02:20', inline=True) 
        embed.add_field(name='스킬', value='포스실드' + '\n' + '자신의 피해를 막는 왜곡방벽을 9999점 생성한다' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 3초', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='명중 40%, 치명률 20% 상승' + '\n' + '■□□' + '\n' + '□◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='우유', inline=True)
        print('MP5')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/스콜피온") or message.content.startswith("/사소리") or message.content.startswith("/No.27."):
        await client.send_file(message.channel, 'No.27_스콜피온.png')
        channel = message.channel
        embed = discord.Embed(
            title = '스콜피온 | No.27',
            description = '"Vz.61 스콜피온이야. 잘 부탁해~ 전갈이긴 하지만 독은 없다구~"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='02:00', inline=True) 
        embed.add_field(name='스킬', value='소이탄' + '\n' + '소이탄을 던져 1.5 반경에 피해를 주고 매 0.33초마다 화상 데미지를 입히는 구간을 생성' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' + '폭발/지속 피해량 : 6 / 1배' + '\n' + '지속시간 : 5초', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='사속 15%, 명중 50% 상승' + '\n' + '□□□' + '\n' + '■◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='사소리', inline=True)
        print('스콜피온')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MP7") or message.content.startswith("/엠삐칠") or message.content.startswith("/No.28."):
        await client.send_file(message.channel, 'No.28_MP7.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MP7 | No.28',
            description = '""사육사 씨", 드디어 마중 나온 거야? 수고했어."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='02:18(중형제조)', inline=True) 
        embed.add_field(name='스킬', value='현월무희' + '\n' + '지속시간 동안 자신의 사속, 명중이 감소하는 대신 기동력과 회피 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 8초' + '\n' + '사속, 명중 감소량 : 20%' + '\n' + '기동력, 회피 증가량 : 50% / 180%' + '\n' + '지속시간 : 5초', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='사속 15%, 명중 25% 상승' + '\n' + '■□□' + '\n' + '■◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='엠삐칠', inline=True)
        print('MP7')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/스텐MkII") or message.content.startswith("/스댕") or message.content.startswith("/비빗쟈") or message.content.startswith("/No.29."):
        await client.send_file(message.channel, 'No.29_스텐_Mkll.png')
        channel = message.channel
        embed = discord.Embed(
            title = '스텐 MkII | No.29',
            description = '"소문의 지휘관님이신가요? 처음 뵙겠습니다! 가자구요~"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:40', inline=True) 
        embed.add_field(name='스킬', value='수류탄' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' +'피해량 : 6배', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='명중 10%, 회피 30% 상승' + '\n' + '■□□' + '\n' + '■◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='스댕, 비빗쟈', inline=True)
        print('스텐 MkII')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/No.30."):
        await client.send_file(message.channel, 'ACCESS DENIED.jpg')
        channel = message.channel
        embed = discord.Embed(
            title = 'ACCESS DENIED | No.30',
            description = '해당 번호는 결번입니다.',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='ACCESS DENIED', inline=True)
        embed.add_field(name='종류', value='ACCESS DENIED', inline=True)
        embed.add_field(name='제조시간', value='ACCESS DENIED', inline=True) 
        embed.add_field(name='스킬', value='ACCESS DENIED' + '\n' + 'ACCESS DENIED' + '\n' + '초반 쿨타임 : ACCESS DENIED초' + '\n' + '쿨타임 : ACCESS DENIED초' + '\n' + '지속시간 : ACCESS DENIED초' + '\n' + 'ACCESS DENIED : 0', inline=True) 
        embed.add_field(name='버프', value='ACCESS DENIED' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='ACCESS DENIED', inline=True)
        print('ACCESS DENIED 30')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/베레타38형") or message.content.startswith("/No.31."):
        await client.send_file(message.channel, 'No.31_베레타_38형.png')
        channel = message.channel
        embed = discord.Embed(
            title = '베레타 38형 | No.31',
            description = '"베레타 M38입니다. 잘부탁드립니다!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:30', inline=True) 
        embed.add_field(name='스킬', value='섬광탄' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 기절을 건다.' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 16초' + '\n' +'기절 지속시간 : 3.2초', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 5%, 사속 10% 상승' + '\n' + '■□□' + '\n' + '□◎□' + '\n' + '■□□', inline=True)
        print('베레타 38형')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/마이크로우지") or message.content.startswith("/우지") or message.content.startswith("/No.32."):
        await client.send_file(message.channel, 'No.32_마이크로_우지.png')
        channel = message.channel
        embed = discord.Embed(
            title = '마이크로 우지 | No.32',
            description = '"뭘 그렇게 보고 있는 거야? 부, 부끄러우니까 그만두라고..."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:40', inline=True) 
        embed.add_field(name='스킬', value='소이탄' + '\n' + '소이탄을 던져 1.5 반경에 피해를 주고 매 0.33초마다 화상 데미지를 입히는 구간을 생성' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 16초' + '\n' +'폭발/지속 피해량 : 6 / 1배' + '\n' +'지속시간 : 5초', inline=True)
        embed.add_field(name='버프(AR 한정)', value='화력 18% 상승' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        embed.add_field(name='별명', value='우지', inline=True)
        print('마이크로 우지')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M45") or message.content.startswith("/시나몬롤") or message.content.startswith("/No.33."):
        await client.send_file(message.channel, 'No.33_M45.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M45 | No.33',
            description = '"지휘관! 맡아주셔서 감사드려요! 맛있는 빵을 구울수 있도록 힘낼게요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:20', inline=True) 
        embed.add_field(name='스킬', value='연막탄' + '\n' + '폭발 위치의 2.5 반경에 적의 사속/이속을 감소시키는 연막이 발생' + '\n' + '초반 쿨타임 : 1초' + '\n' + '쿨타임 : 12초' + '\n' +'사속/이속 감소치 : 36 / 45%' + '\n' +'지속시간 : 4초', inline=True)
        embed.add_field(name='버프(AR 한정)', value='사속 10%, 회피 10% 상승' + '\n' + '■□□' + '\n' + '□◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='시나몬롤', inline=True)
        print('M45')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M1개런드") or message.content.startswith("/가란드") or message.content.startswith("/No.34."):
        await client.send_file(message.channel, 'No.34_M1_개런드.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M1 개런드 | No.34',
            description = '"M1개런드 입니다. 앞으로 쭉 지휘관과 함께 싸우겠습니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='04:00', inline=True) 
        embed.add_field(name='스킬', value='정밀저격' + '\n' + '1.5초간 조준한 후에 공격하던 적에게 피해를 준다' + '\n' + '초반 쿨타임 : 10초' + '\n' + '쿨타임 : 16초' + '\n' +'피해량 : 5.5배' , inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 12% 감소' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='가란드', inline=True)
        print('M1개런드')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M1A1") or message.content.startswith("/책가방") or message.content.startswith("/No.35."):
        await client.send_file(message.channel, 'No.35_M1A1.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M1A1 | No.35',
            description = '"M1A1 들어가겠습니다. 함께 전쟁을 극복해나가요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='고속사격T' + '\n' + '지속시간 동안 자신의 사속 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 16초' + '\n' + '사속 증가치 : 40%' + '\n' +'지속시간 : 15초' , inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 12% 감소' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        embed.add_field(name='별명', value='책가방', inline=True)
        print('M1A1')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/스프링필드") or message.content.startswith("/춘전이") or message.content.startswith("/No.36."):
        await client.send_file(message.channel, 'No.36_스프링필드_J.png')
        channel = message.channel
        embed = discord.Embed(
            title = '스프링필드 | No.36',
            description = '"지휘관, 제가 할 수 있는 일이 있다면, 부디 명령을…"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='04:25', inline=True) 
        embed.add_field(name='스킬', value='저격개시' + '\n' + '1.5초간 조준한 후에 가장 멀리있는 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 10초' + '\n' + '피해량 : 6배', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 15% 감소' + '\n' + '□□■' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='춘전이', inline=True)
        print('스프링필드')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M14") or message.content.startswith("/엠씹새") or message.content.startswith("/씹새") or message.content.startswith("/No.37."):
        await client.send_file(message.channel, 'No.37_M14.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M14 | No.37',
            description = '"지휘관! 당신의 기대에 반드시 보답할게요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='03:40', inline=True) 
        embed.add_field(name='스킬', value='화력전개' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '화력 증가치 : 60%', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 12% 감소' + '\n' + '□□■' + '\n' + '□◎□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='엠씹새, 씹새', inline=True)
        print('M14')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M21") or message.content.startswith("/No.38."):
        await client.send_file(message.channel, 'No.38_M21.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M21 | No.38',
            description = '"헬로~ M21이야. 저격무기라고 해서 모두 어둡지만은 않다구~"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='목표제거' + '\n' + '1.5초간 조준한 후에 특정 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 10초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 5.5배', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 12% 감소' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        print('M21')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/모신나강") or message.content.startswith("/하라쇼") or message.content.startswith("/No.39.") :
        await client.send_file(message.channel, 'No.39_모신나강.png')
        channel = message.channel
        embed = discord.Embed(
            title = '모신나강 | No.39',
            description = '"동지, 훌륭해~"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='04:10', inline=True) 
        embed.add_field(name='스킬', value='저격개시' + '\n' + '1.5초간 조준한 후에 가장 멀리 있는 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 10초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 6배', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 15% 감소' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        print('모신나강')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/SVT-38") or message.content.startswith("/SVT38") or message.content.startswith("/No.40.") :
        await client.send_file(message.channel, 'No.40_SVT-38.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'SVT-38 | No.40',
            description = '"토카레프 M1940 등장. 지휘관, 지시를"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='03:30', inline=True) 
        embed.add_field(name='스킬', value='목표제거' + '\n' + '1.5초간 조준한 후에 특정 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 10초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 5배', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 10% 감소' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        print('SVT-38')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/시모노프") or message.content.startswith("/SKS") or message.content.startswith("/No.41.") :
        await client.send_file(message.channel, 'No.41_시모노프.png')
        channel = message.channel
        embed = discord.Embed(
            title = '시모노프 | No.41',
            description = '"안녕하세요, 지휘관. 에이스인 내가 있으면 일당백이라고. 잘 부탁해."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='03:30', inline=True) 
        embed.add_field(name='스킬', value='고속사격' + '\n' + '지속시간 동안 자신의 사속 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '사속 증가치 : 55%' + '지속시간 : 5초', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 10% 감소' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        print('시모노프')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/PTRD") or message.content.startswith("/No.42."):
        await client.send_file(message.channel, 'No.42_PTRD.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'PTRD | No.42',
            description = '"괜찮아, 지휘관. 누구라 해도 나의 탄환에서는 도망칠 수 없어."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='04:30', inline=True) 
        embed.add_field(name='스킬', value='확인사살' + '\n' + '2초간 조준한 후에 최전방의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 15초' + '\n' + '쿨타임 : 16.9초' + '\n' + '피해량 : 7배', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 15% 감소' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        print('PTRD')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/SVD") or message.content.startswith("/스브드") or message.content.startswith("/No.43."):
        await client.send_file(message.channel, 'No.43_SVD.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'SVD | No.43',
            description = '"스나이퍼 SVD야. 어디보자, 어느 행운아가 나를 맞이한 거야?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='04:15', inline=True) 
        embed.add_field(name='스킬', value='고속사격' + '\n' + '지속시간 동안 자신의 사속 증가.' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '사속증가치 : 65%' + '지속시간 : 5초', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 15% 감소' + '\n' + '□□■' + '\n' + '□◎□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='스브드', inline=True)
        print('SVD')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/SV-98") or message.content.startswith("/SV98") or message.content.startswith("/큐하치") or message.content.startswith("/스브") or message.content.startswith("/No.44."):
        await client.send_file(message.channel, 'No.44_SV-98.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'SV-98 | No.44',
            description = '"SV-98 보고합니다. 명령을 내려주십시오."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='03:40', inline=True) 
        embed.add_field(name='스킬', value='확인사살' + '\n' + '1.5초간 조준한 후에 최전방의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 10초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 5.5배', inline=True)
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 12% 감소' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='큐하치, 스브', inline=True)
        print('SV-98')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/No.45."):
        await client.send_file(message.channel, 'ACCESS DENIED.jpg')
        channel = message.channel
        embed = discord.Embed(
            title = 'ACCESS DENIED | No.45',
            description = '해당 번호는 결번입니다.',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='ACCESS DENIED', inline=True)
        embed.add_field(name='종류', value='ACCESS DENIED', inline=True)
        embed.add_field(name='제조시간', value='ACCESS DENIED', inline=True) 
        embed.add_field(name='스킬', value='ACCESS DENIED' + '\n' + 'ACCESS DENIED' + '\n' + '초반 쿨타임 : ACCESS DENIED초' + '\n' + '쿨타임 : ACCESS DENIED초' + '\n' + '지속시간 : ACCESS DENIED초' + '\n' + 'ACCESS DENIED : 0', inline=True) 
        embed.add_field(name='버프', value='ACCESS DENIED' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='ACCESS DENIED', inline=True)
        print('ACCESS DENIED 45')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/Kar.98k") or message.content.startswith("/부츠") or message.content.startswith("/카구팔") or message.content.startswith("/No.46."):
        await client.send_file(message.channel, 'No.46_Kar98k.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'Kar98k | No.46',
            description = '"지휘관, 마우저 카라비너 98 Kurz가 당신을 위해 있는 힘을 다하겠습니다. 당신에게 방해되는 것은 한 번에 처리해버릴게요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='04:40', inline=True) 
        embed.add_field(name='스킬', value='이중저격' + '\n' + '1초씩 두번 조준 사격하며 각각 현재 타깃에게 대미지를 입힌다.' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 3.5배', inline=True) 
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 18% 감소' + '\n' + '□□■' + '\n' + '□◎□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='카구팔, 부츠', inline=True)
        print('Kar98k')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/G43") or message.content.startswith("/구텐탁") or message.content.startswith("/No.47."):
        await client.send_file(message.channel, 'No.47_G43.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'G43 | No.47',
            description = '"Guten Tag! 저는 발터 게베어 43, 오늘도 우아한 싸움을 보여드리겠어요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='03:10', inline=True) 
        embed.add_field(name='스킬', value='고속사격N' + '\n' + '지속시간 동안 자신의 사속 증가 / 뒤쪽의 수치는 주간작전에 사용시' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '사속 증가치 : 85 / 28%', inline=True) 
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 10% 감소' + '\n' + '□□■' + '\n' + '□◎□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='구텐탁', inline=True)
        print('G43')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/WA2000") or message.content.startswith("/와짱")  or message.content.startswith("/와짱") or message.content.startswith("/No.48."):
        await client.send_file(message.channel, 'No.48_WA2000.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'WA2000 | No.48',
            description = '"나의 이름은 발터 WA2000. 지휘관, 나의 발목을 잡는다면 가만두지 않을 거야!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='04:50', inline=True) 
        embed.add_field(name='스킬', value='고속사격' + '\n' + '지속시간 동안 자신의 사속 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '사속 증가치 : 75%', inline=True) 
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 18% 감소' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='와짱(쨩)', inline=True)
        print('WA2000')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/56식반") or message.content.startswith("/No.49."):
        await client.send_file(message.channel, 'No.49_56식_반.png')
        channel = message.channel
        embed = discord.Embed(
            title = '56식 반 | No.49',
            description = '"56식 반, 정식으로 배치를 명 받았습니다. 지휘관, 그리고 전우여러분! 잘부탁드려요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='화력전개' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '화력 증가치 : 60', inline=True) 
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 12% 감소' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        print('56식 반')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/리엔필드") or message.content.startswith("/리줌마") or message.content.startswith("/No.50."):
        await client.send_file(message.channel, 'No.50_리엔필드.png')
        channel = message.channel
        embed = discord.Embed(
            title = '리엔필드 | No.50',
            description = '"오늘부로 배속된 리-엔필드 No.4 Mk I입니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='05:00', inline=True) 
        embed.add_field(name='스킬', value='화력전개' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '화력 증가치 : 75%', inline=True) 
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 18% 감소' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        embed.add_field(name='별명', value='리줌마', inline=True)
        print('리엔필드')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/FN-49") or message.content.startswith("/FN49") or message.content.startswith("/요요요") or message.content.startswith("/No.51."):
        await client.send_file(message.channel, 'No.51_FN-49.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'FN-49 | No.51',
            description = '"자, 자자자자, 잘 부탁 드립니다!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='03:10', inline=True) 
        embed.add_field(name='스킬', value='화력전개' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '화력 증가치 : 55%', inline=True) 
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 10% 감소' + '\n' + '□□■' + '\n' + '□◎□' + '\n' + '□□■', inline=True)
        print('FN-49')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/BM59") or message.content.startswith("/No.52."):
        await client.send_file(message.channel, 'No.52_BM59.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'BM59 | No.52',
            description = '"베레타 BM59입니다. 갖가지 개조를 거친 저라면, 지휘관을 실망시킬 일은 없겠죠."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='03:20', inline=True) 
        embed.add_field(name='스킬', value='고속사격  ' + '\n' + '지속시간 동안 자신의 사속 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '사속 증가치 : 55%', inline=True) 
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 10% 감소' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        print('BM59')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/NTW-20") or message.content.startswith("/NTW20") or message.content.startswith("/노태우") or message.content.startswith("/No.53."):
        await client.send_file(message.channel, 'No.53_NTW-20.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'NTW-20 | No.53',
            description = '"지휘관, 대물 저격총인 Denel NTW-20다. 강철의 벽이라 해도, 내가 뚫을 수 있다는 걸 보여주지."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='04:45', inline=True) 
        embed.add_field(name='스킬', value='확인사살' + '\n' + '2초간 조준한 후에 최전방의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 15초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 8배', inline=True) 
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 18% 감소' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='노태우', inline=True)
        print('NTW-20')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M16") or message.content.startswith("/M16A1") or message.content.startswith("/우리형") or message.content.startswith("/No.54."):
        await client.send_file(message.channel, 'No.54_M16A1.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M16A1 | No.54',
            description = '"여어! M16이다. 임무라면 나한테 맡겨두도록."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='섬광탄' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 기절을 건다.' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 16초' + '\n' + '기절 지속시간 : 4초', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='화력 10%, 회피 12% 상승' + '\n' + '□■■' + '\n' + '□◎□' + '\n' + '□■■', inline=True)
        embed.add_field(name='별명', value='우리형', inline=True)
        print('M16A1')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/느그형") or message.content.startswith("/철혈M16"):
        await client.send_file(message.channel, 'No.54_M16A1S.E.jpg')
        channel = message.channel
        embed = discord.Embed(
            title = 'M16A1 | No.54',
            description = '"여어! M16이다. 임무라면 나한테 맡겨두도록."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='섬광탄' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 기절을 건다.' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 16초' + '\n' + '기절 지속시간 : 4초', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='화력 10%, 회피 12% 상승' + '\n' + '□■■' + '\n' + '□◎□' + '\n' + '□■■', inline=True)
        embed.add_field(name='별명', value='느그형', inline=True)
        print('M16A1')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M4") or message.content.startswith("/M4A1") or message.content.startswith("/혐포") or message.content.startswith("/엠포") or message.content.startswith("/No.55."):
        await client.send_file(message.channel, 'No.55_M4A1.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M4A1 | No.55',
            description = '"지휘관, 잘… 부탁드리겠습니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='화력전개T' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 4초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 10초' + '\n' + '화력 증가치 : 70%', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 18%, 치명률 30% 상승' + '\n' + '□■■' + '\n' + '□◎■' + '\n' + '□■■', inline=True)
        embed.add_field(name='별명', value='엠포, 혐포', inline=True)
        print('M4A1')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M4SOPMODII") or message.content.startswith("/솦모챠") or message.content.startswith("/솦모") or message.content.startswith("/비누") or message.content.startswith("/No.56."):
        await client.send_file(message.channel, 'No.56_M4_SOPMOD_II.jpg')
        channel = message.channel
        embed = discord.Embed(
            title = 'M4 SOP MODII | No.56',
            description = '"지휘관, 잘… 부탁드리겠습니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='살상류탄' + '\n' + '폭발한 위치의 1.5반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 12배', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='명중 50%, 회피 12% 상승' + '\n' + '□□■' + '\n' + '□◎■' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='솦모챠, 비누', inline=True)
        print('M4 SOP MODII')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/STAR-15") or message.content.startswith("/AR15") or message.content.startswith("/스타") or message.content.startswith("/No.57."):
        await client.send_file(message.channel, 'No.57_ST_AR-15.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'ST AR-15 | No.57',
            description = '"콜트 AR-15야. 정식으로 귀하의 부대에 합류하겠습니다. 제 활약을 확실히 눈에 새겨주세요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='고속사격T' + '\n' + '지속시간 동안 자신의 사속 증가' + '\n' + '초반 쿨타임 : 4초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 15초' + '\n' + '사속증가치 : 45%', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='사속 10%, 회피 12% 상승' + '\n' + '□□■' + '\n' + '□◎■' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='스타', inline=True)
        print('ST AR-15')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/AK-47") or message.content.startswith("/AK47") or message.content.startswith("/에케") or message.content.startswith("/No.58."):
        await client.send_file(message.channel, 'No.58_AK-47.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'AK-47 | No.58',
            description = '"아하핫, 드디어 나의 차례구나, 지구를 뒤흔들 성능을 보여줄게!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='03:20', inline=True) 
        embed.add_field(name='스킬', value='기습공격' + '\n' + '지속시간 동안 자신의 화력, 명중 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '화력, 명중 증가치 : 35, 100%', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='회피 18% 상승' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□■□', inline=True)
        embed.add_field(name='별명', value='에케', inline=True)
        print('AK-47')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/AK-74U") or message.content.startswith("/AK74U") or message.content.startswith("/No.59."):
        await client.send_file(message.channel, 'No.59_AK-74U.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'AK-74U | No.59',
            description = '"아, 네가 보스야? AK-74U, 이게 내 이름이니까, 장사하고 싶으면, 날 어떻게 모실지 잘 생각해 봐."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='거부반응' + '\n' + '지속시간 동안 자신이 공격한 적은 일정 시간 동안 화력, 명중 감소 (엘리트 적은 효과 반감)' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 5초' + '\n' + '디버프 지속시간 : 5초' + '\n' + '화력, 명중 감소치 : 50%', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 15%, 명중 25% 상승' + '\n' + '■□□' + '\n' + '■◎□' + '\n' + '■□□', inline=True)
        print('AK-74U')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/ASVAL") or message.content.startswith("/아스발") or message.content.startswith("/No.60."):
        await client.send_file(message.channel, 'No.60_AS_Val.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'AS VAL | No.60',
            description = '"안녕하세요오...저...아앗...아무것도 아니에요..."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='03:30', inline=True) 
        embed.add_field(name='스킬', value='화력전개N' + '\n' + '지속시간 동안 자신의 화력 증가 / 뒤쪽의 수치는 주간작전에 사용시' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 6초' + '\n' + '화력 증가치 : 180 / 60%', inline=True) 
        embed.add_field(name='버프(AR 한정)', value='화력 25%, 사속 10% 상승' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='아스발', inline=True)
        print('AS VAL')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/StG44") or message.content.startswith("/서태지") or message.content.startswith("/No.61."):
        await client.send_file(message.channel, 'No.61_StG44.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'StG44 | No.61',
            description = '"안녕하세요, 아, 악수는 거절하겠어요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='03:00', inline=True) 
        embed.add_field(name='스킬', value='파열류탄' + '\n' + '유탄을 발사하여 폭발한 위치의 1/2.5/4 반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 4.5/1.8/1배', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='회피 20%, 명중 60% 상승' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='서태지', inline=True)
        print('StG44')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/G3") or message.content.startswith("/No.63."):
        await client.send_file(message.channel, 'No.63_G3.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'G3 | No.62',
            description = '"안녕하세요, 지휘관씨, G3라고 불러주세요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='02:50', inline=True) 
        embed.add_field(name='스킬', value='살상류탄' + '\n' + '폭발한 위치의 1.5반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 10배', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='회피 20%, 명중 60% 상승' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        print('G3')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/G36") or message.content.startswith("/지상렬") or message.content.startswith("/상렬이") or message.content.startswith("/No.64."):
        await client.send_file(message.channel, 'No.64_G36.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'G36 | No.65',
            description = '"구텐 탁. 오늘부터 주인님의 전속 메이드가 되어 봉사하겠습니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='03:40', inline=True) 
        embed.add_field(name='스킬', value='화력전개T' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 4초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 10초' + '\n' + '화력 증가치 : 70%', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='화력 30%, 사속 10% 상' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='지상렬, 상렬이', inline=True)
        print('G36')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/HK416") or message.content.startswith("/흥국이") or message.content.startswith("/No.65."):
        await client.send_file(message.channel, 'No.65_HK416.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'HK416 | No.65',
            description = '"HK416. 지휘관, 제대로 기억해주세요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='03:55', inline=True) 
        embed.add_field(name='스킬', value='살상류탄' + '\n' + '폭발한 위치의 1.5반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 15배', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='화력 40% 상승' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='흥국이', inline=True)
        print('HK416')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/56-1식") or message.content.startswith("/No.66."):
        await client.send_file(message.channel, 'No.66_56-1식.png')
        channel = message.channel
        embed = discord.Embed(
            title = '56-1식 | No.66',
            description = '"니 하오, 지휘관. 56식 자동보총 1형이야. 모든 적을 섬멸해줄께."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='03:25', inline=True) 
        embed.add_field(name='스킬', value='파열류탄 체인 블라스트(일)' + '\n' + '폭발한 위치의 1/2.5/4반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 5/2/1배', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='회피 15%, 치명률 10% 상승' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        print('56-1식')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/No.67."):
        await client.send_file(message.channel, 'ACCESS DENIED.jpg')
        channel = message.channel
        embed = discord.Embed(
            title = 'ACCESS DENIED | No.67',
            description = '해당 번호는 결번입니다.',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='ACCESS DENIED', inline=True)
        embed.add_field(name='종류', value='ACCESS DENIED', inline=True)
        embed.add_field(name='제조시간', value='ACCESS DENIED', inline=True) 
        embed.add_field(name='스킬', value='ACCESS DENIED' + '\n' + 'ACCESS DENIED' + '\n' + '초반 쿨타임 : ACCESS DENIED초' + '\n' + '쿨타임 : ACCESS DENIED초' + '\n' + '지속시간 : ACCESS DENIED초' + '\n' + 'ACCESS DENIED : 0', inline=True) 
        embed.add_field(name='버프', value='ACCESS DENIED' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='ACCESS DENIED', inline=True)
        print('ACCESS DENIED 67')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/L85A1") or message.content.startswith("/장미") or message.content.startswith("/하지메마시떼") or message.content.startswith("/No.68."):
        await client.send_file(message.channel, 'No.68_L85A1.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'L85A1 | No.68',
            description = '"M4 SOPMOD-II, 지휘관, 드디어 만났네요!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='02:50', inline=True) 
        embed.add_field(name='스킬', value='강행돌파' + '\n' + '지속시간 동안 자신의 화력, 사속 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '화력, 사속 증가치 : 35, 15%', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='화력 20%, 명중 50% 상승' + '\n' + '□■□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='장미', inline=True)
        print('L85A1')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/FAMAS") or message.content.startswith("/파마스") or message.content.startswith("/No.69."):
        await client.send_file(message.channel, 'No.69_FAMAS.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'FAMAS | No.69',
            description = '"지휘관님, 제가 당신의 제대에 가세한다면 일당백이나 다름없습니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='03:30', inline=True) 
        embed.add_field(name='스킬', value='파열류탄' + '\n' + '폭발한 위치의 1/2.5/4반경 내의 적에게 피해를 준다.' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 16초' + '\n' + '피해량 : 5/2/1배', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='화력 25%, 명중 60% 증가' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='파마스', inline=True)
        print('FAMAS')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/FNC") or message.content.startswith("/초코") or message.content.startswith("/No.70."):
        await client.send_file(message.channel, 'No.70_FNC.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'FNC | No.70',
            description = '"처음 뵙겠습니다, 지휘관님. 초콜렛 드실래요?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='03:20', inline=True) 
        embed.add_field(name='스킬', value='화력전개' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '화력 증가치 : 60%', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='명중 50%, 회피 12% 상승' + '\n' + '□□■' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='초코', inline=True)
        print('FNC')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/갈릴") or message.content.startswith("/No.71."):
        await client.send_file(message.channel, 'No.71_갈릴.png')
        channel = message.channel
        embed = discord.Embed(
            title = '갈릴 | No.71',
            description = '"여어, 잘 부탁해, My 지휘관!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='02:40', inline=True) 
        embed.add_field(name='스킬', value='호흡조절' + '\n' + '지속시간 동안 자신의 명중 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 15초' + '\n' + '명중 증가치 : 500%', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='명중 50%, 회피 10% 상승' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        print('갈릴')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/TAR-21") or message.content.startswith("/TAR21") or message.content.startswith("/타보르") or message.content.startswith("/타줌마") or message.content.startswith("/No.72."):
        await client.send_file(message.channel, 'No.72_TAR-21.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'TAR-21 | No.72',
            description = '"TAR-21, 지금부터 따르겠습니다, 부디 저에 대해 많이 신경써 주세요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='03:30', inline=True) 
        embed.add_field(name='스킬', value='강행돌파' + '\n' + '지속시간 동안 자신의 명중 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 5초' + '\n' + '화력, 사속 증가치 : 75, 25%', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='명중 50%, 회피 10% 상승' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='타보르, 타줌마', inline=True)
        print('TAR-21')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/AUG") or message.content.startswith("/어그") or message.content.startswith("/No.73."):
        await client.send_file(message.channel, 'No.73_AUG.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'AUG | No.73',
            description = '"지휘관님, 만약 적에게 장례식 화환을 보내고 싶으시다면······ 제가 당신의 "최고의 선택" 일 거에요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='장례식의 비' + '\n' + '지속시간 동안 자신의 명중이 감소하지만 사속이 150이 되고 난사한다.' + '\n' + '초반 쿨타임 : 4초' + '\n' + '쿨타임 : 16초' + '\n' + '지속시간 : 7초' + '\n' + '명중 감소치 : 0%', inline=True) 
        embed.add_field(name='버프', value='화력 12%, 명중 20% 상승' + '\n' + '□■■' + '\n' + '□◎■' + '\n' + '□■■', inline=True)
        embed.add_field(name='별명', value='어그', inline=True)
        print('AUG')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/SIG-510") or message.content.startswith("/SIG510") or message.content.startswith("/시그") or message.content.startswith("/No.74."):
        await client.send_file(message.channel, 'No.74_SIG-510.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'SIG-510 | No.74',
            description = '"SIG-510, 지금부터 따르겠습니다, 부디 저에 대해 많이 신경써 주세요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='AR', inline=True)
        embed.add_field(name='제조시간', value='02:40', inline=True) 
        embed.add_field(name='스킬', value='화력전개' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '화력 증가치 : 55%', inline=True) 
        embed.add_field(name='버프(SMG 한정)', value='화력 20%, 사속 10% 상승' + '\n' + '□□■' + '\n' + '□◎□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='시그', inline=True)
        print('SIG-510')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M1918") or message.content.startswith("/바쨩") or message.content.startswith("/바짱") or message.content.startswith("/No.75."):
        await client.send_file(message.channel, 'No.75_M1918.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M1918 | No.75',
            description = '"브라우닝 M1918이야. 왓! 지휘관! 여기에 계셨던거예요? 놀래키지 마셔요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='06:25', inline=True) 
        embed.add_field(name='스킬', value='화력전개MG' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 6초' + '\n' + '화력 증가치 : 70%', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='화력 15%, 장갑 10% 상승' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='바짱(쨩)', inline=True)
        print('M1918')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/No.76."):
        await client.send_file(message.channel, 'ACCESS DENIED.jpg')
        channel = message.channel
        embed = discord.Embed(
            title = 'ACCESS DENIED | No.76',
            description = '해당 번호는 결번입니다.',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='ACCESS DENIED', inline=True)
        embed.add_field(name='종류', value='ACCESS DENIED', inline=True)
        embed.add_field(name='제조시간', value='ACCESS DENIED', inline=True) 
        embed.add_field(name='스킬', value='ACCESS DENIED' + '\n' + 'ACCESS DENIED' + '\n' + '초반 쿨타임 : ACCESS DENIED초' + '\n' + '쿨타임 : ACCESS DENIED초' + '\n' + '지속시간 : ACCESS DENIED초' + '\n' + 'ACCESS DENIED : 0', inline=True) 
        embed.add_field(name='버프', value='ACCESS DENIED' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='ACCESS DENIED', inline=True)
        print('ACCESS DENIED 76')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M2HB") or message.content.startswith("/쵸로이") or message.content.startswith("/연필") or message.content.startswith("/HB연필") or message.content.startswith("/No.77."):
        await client.send_file(message.channel, 'No.77_M2HB.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M2HB | No.77',
            description = '"저기~ 지휘관! 어서 적에게 총탄의 비를 퍼붓고 싶어! 더는 기다릴 수 없어!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='06:10', inline=True) 
        embed.add_field(name='스킬', value='사중극점' + '\n' + '3회 일반 공격 후 4회째 공격을 강화' + '\n' + 'Passive Skill' + '\n' + '공격력 배율 : 2.4배', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='화력 22% 상승' + '\n' + '□□□' + '\n' + '◎□■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='쵸로이, HB, HB연필', inline=True)
        print('M2HB')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M60") or message.content.startswith("/No.78"):
        await client.send_file(message.channel, 'No.78_M60.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M60 | No.78',
            description = '"M60이야! 자, 지시를 내려줘!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='06:10', inline=True) 
        embed.add_field(name='스킬', value='화력전개N-MG' + '\n' + '지속시간 동안 자신의 화력 증가 / 뒤쪽의 수치는 주간작전에 사용시' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 6초' + '\n' + '화력 증가치 : 105 / 35%', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='화력 10%, 사속 8% 상승' + '\n' + '◎□■' + '\n' + '□□□' + '\n' + '□□■', inline=True)
        print('M60')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M249") or message.content.startswith("/풍선껌") or message.content.startswith("/No.79."):
        await client.send_file(message.channel, 'No.79_M249_SAW.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M249 | No.79',
            description = '"지휘관, 너무 기대하지는 마."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='준비만전N' + '\n' + '야간작전에서 지속시간 동안 자신의 화력 증가, 발사중인 탄띠에 탄 추가 괄호 안의 수치는 주간작전에 사용시' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 8초' + '\n' + '화력, 발사수 증가치 : 45%(10%), 4발', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='사속 12%, 명중 10% 상승' + '\n' + '□□□' + '\n' + '◎□■' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='풍선껌', inline=True)
        print('M249')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M1919A4") or message.content.startswith("/이치큐") or message.content.startswith("/No.80."):
        await client.send_file(message.channel, 'No.80_M1919A4.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M249 | No.80',
            description = '"저는 브라우닝 M1919! 적을 분쇄하기 위해 찾아왔습니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='05:40', inline=True) 
        embed.add_field(name='스킬', value='사냥충동' + '\n' + '지속시간 동안 자신의 명중 상승, 모든 공격이 치명타가 된다.' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 6초' + '\n' + '명중 증가치 : 65%', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='명중 25%, 장갑 10% 상승' + '\n' + '□□■' + '\n' + '□□□' + '\n' + '◎□□', inline=True)
        embed.add_field(name='별명', value='이치큐', inline=True)
        print('M1919A4')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/LWMMG") or message.content.startswith("/람지") or message.content.startswith("/No.81."):
        await client.send_file(message.channel, 'No.81_LWMMG.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'LWMMG | No.81',
            description = '"처음 뵙겠습니다. 지휘관. 아니...다른 녀석들을 소개할 필요는 없어. 나 혼자서도 충분하니까."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='05:10', inline=True) 
        embed.add_field(name='스킬', value='사냥충동' + '\n' + '지속시간 동안 자신의 명중 상승, 모든 공격이 치명타가 된다.' + '\n' + '초반 쿨타임 : 3초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 6초' + '\n' + '명중 증가치 : 60%', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='화력 10%, 사속 10% 상승' + '\n' + '□□□' + '\n' + '◎□■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='람지', inline=True)
        print('LWMMG')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/DP-28") or message.content.startswith("/DP28") or message.content.startswith("/디피") or message.content.startswith("/No.82."):
        await client.send_file(message.channel, 'No.82_DP-28.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'DP-28 | No.82',
            description = '"꼬마야, 잘부탁해. 뭔가 곤란한 거라도 있니?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='05:00', inline=True) 
        embed.add_field(name='스킬', value='준비만전' + '\n' + '지속시간 동안 자신의 화력 증가 발사중인 탄띠에 탄 추가' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 8초' + '\n' + '화력, 발사수 증가치 : 28%, 3발', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='사속 15% 상승' + '\n' + '□□■' + '\n' + '□□□' + '\n' + '◎□■', inline=True)
        embed.add_field(name='별명', value='디피', inline=True)
        print('DP-28')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/No.83."):
        await client.send_file(message.channel, 'ACCESS DENIED.jpg')
        channel = message.channel
        embed = discord.Embed(
            title = 'ACCESS DENIED | No.83',
            description = '해당 번호는 결번입니다.',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='ACCESS DENIED', inline=True)
        embed.add_field(name='종류', value='ACCESS DENIED', inline=True)
        embed.add_field(name='제조시간', value='ACCESS DENIED', inline=True) 
        embed.add_field(name='스킬', value='ACCESS DENIED' + '\n' + 'ACCESS DENIED' + '\n' + '초반 쿨타임 : ACCESS DENIED초' + '\n' + '쿨타임 : ACCESS DENIED초' + '\n' + '지속시간 : ACCESS DENIED초' + '\n' + 'ACCESS DENIED : 0', inline=True) 
        embed.add_field(name='버프', value='ACCESS DENIED' + '\n' + '□□□' + '\n' + '□◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='ACCESS DENIED', inline=True)
        print('ACCESS DENIED 83')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/RPD") or message.content.startswith("/No.84."):
        await client.send_file(message.channel, 'No.84_RPD.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'RPD | No.84',
            description = '"지휘관, RPD가 왔습니다. 함께 싸울 수 있어서 영광입니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='불가능', inline=True) 
        embed.add_field(name='스킬', value='화력전개MG' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 8초' + '\n' + '화력 증가치 : 65%', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='사속 16% 상승' + '\n' + '□□■' + '\n' + '◎□□' + '\n' + '□□■', inline=True)
        print('RPD')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/PK") or message.content.startswith("/피카") or message.content.startswith("/No.85."):
        await client.send_file(message.channel, 'No.85_PK.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'PK | No.85',
            description = '"지휘관, 적은 제대로 섬멸할 테니까, 가까이 오지 말아줄래?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='06:30', inline=True) 
        embed.add_field(name='스킬', value='사중극점' + '\n' + '3회 일반 공격 후 4회째 공격을 강화' + '\n' + '쿨타임 : Passive Skill' + '\n' + '공격력 배율 : 2.6배', inline=True) 
        embed.add_field(name='버프(SG 한정)', value='화력 18% 상승' + '\n' + '□□■' + '\n' + '◎□■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='피카', inline=True)
        print('PK')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MG42") or message.content.startswith("/망가42") or message.content.startswith("/No.86."):
        await client.send_file(message.channel, 'No.86_MG42.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MG42 | No.86',
            description = '"처음뵙겠습니다, 지휘관님. 옷을 찢는 것 같은 소리를 들어보지 않겠어요?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='05:50', inline=True) 
        embed.add_field(name='스킬', value='화력전개MG' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 6초' + '\n' + '화력 증가치 : 65%', inline=True)  
        embed.add_field(name='버프(SG 한정)', value='화력 22% 상승' + '\n' + '◎□■' + '\n' + '□□□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='망가42', inline=True)
        print('MG42')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MG34") or message.content.startswith("/망가34") or message.content.startswith("/No.87."):
        await client.send_file(message.channel, 'No.87_MG34.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MG34 | No.87',
            description = '"당신이 지휘관이네요, MG42의 언니, MG34에요! 앞으로 잘 지내보도록 해요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='05:00', inline=True) 
        embed.add_field(name='스킬', value='화력전개MG' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 4초' + '\n' + '화력 증가치 : 60%', inline=True)  
        embed.add_field(name='버프(SG 한정)', value='화력 20% 상승' + '\n' + '□□■' + '\n' + '□□□' + '\n' + '◎□□', inline=True)
        embed.add_field(name='별명', value='망가34', inline=True)
        print('MG34')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MG34") or message.content.startswith("/망가34") or message.content.startswith("/No.87."):
        await client.send_file(message.channel, 'No.87_MG34.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MG34 | No.87',
            description = '"당신이 지휘관이네요, MG42의 언니, MG34에요! 앞으로 잘 지내보도록 해요."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='05:00', inline=True) 
        embed.add_field(name='스킬', value='화력전개MG' + '\n' + '지속시간 동안 자신의 화력 증가' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 4초' + '\n' + '화력 증가치 : 60%', inline=True)  
        embed.add_field(name='버프(SG 한정)', value='화력 20% 상승' + '\n' + '□□■' + '\n' + '□□□' + '\n' + '◎□□', inline=True)
        embed.add_field(name='별명', value='망가34', inline=True)
        print('MG34')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MG3") or message.content.startswith("/망가3") or message.content.startswith("/No.88."):
        await client.send_file(message.channel, 'No.88_MG3.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MG3 | No.88',
            description = '"나는 새로 들어온 MG3야! 폭풍과도 같은 화력을 맛보게 해줄게!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='06:30', inline=True) 
        embed.add_field(name='스킬', value='준비만전' + '\n' + '지속시간 동안 자신의 화력 증가 발사중인 탄띠에 탄 추가' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 8초' + '\n' + '화력, 발사수 증가치 : 30%, 4발', inline=True)  
        embed.add_field(name='버프(SG 한정)', value='화력 10%, 명중 15% 상승' + '\n' + '□□■' + '\n' + '◎□□' + '\n' + '□□■', inline=True)
        embed.add_field(name='별명', value='망가3', inline=True)
        print('MG3')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/브렌") or message.content.startswith("/No.89."):
        await client.send_file(message.channel, 'No.89_브렌.png')
        channel = message.channel
        embed = discord.Embed(
            title = '브렌 | No.89',
            description = '"나는 브렌 경기관총이다. 가혹한 임무라면 나에게 맡겨라."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='MG', inline=True)
        embed.add_field(name='제조시간', value='05:20', inline=True) 
        embed.add_field(name='스킬', value='준비만전' + '\n' + '지속시간 동안 자신의 화력 증가 발사중인 탄띠에 탄 추가' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 18초' + '\n' + '지속시간 : 8초' + '\n' + '화력, 발사수 증가치 : 30%, 3발', inline=True)  
        embed.add_field(name='버프(SG 한정)', value='사속 10%, 명중 12% 상승' + '\n' + '◎□■' + '\n' + '□□□' + '\n' + '□□■', inline=True)
        print('브렌')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/FNP-9") or message.content.startswith("/FNP9") or message.content.startswith("/No.90."):
        await client.send_file(message.channel, 'No.90_FNP-9.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'FNP-9 | No.90',
            description = '"FNP-9 화려하게 등장! 지휘관, 너의 제대에 넣어줘!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:25', inline=True) 
        embed.add_field(name='스킬', value='퇴로차단' + '\n' + '지속시간 동안 적 전체 회피 감소' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '회피 감소치 : 40%', inline=True)  
        embed.add_field(name='버프', value='1편제 - 사속 10%, 명중 20% 상승' + '\n' + '□■■ 2편제 - 사속 12%, 명중 25% 상승' + '\n' + '□◎■ 3편제 - 사속 15%, 명중 30% 상승' + '\n' + '□■■ 4편제 - 사속 17%, 명중 35% 상승' + '\n' + '5편제 - 사속 20%, 명중 40% 상승', inline=True)
        print('FNP-9')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MP-446") or message.content.startswith("/MP446") or message.content.startswith("/바이킹") or message.content.startswith("/No.91."):
        await client.send_file(message.channel, 'No.91_MP-446.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MP-446 | No.91',
            description = '"겨우 찾아내 줬네, 지휘관! MP446이야, 바이킹이라고 불러줘!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:25', inline=True) 
        embed.add_field(name='스킬', value='격발차단' + '\n' + '지속시간 동안 적 전체 사속 감소' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '사속 감소치 : 22%', inline=True)  
        embed.add_field(name='버프', value='1편제 - 화력 14% 상승' + '\n' + '■■□ 2편제 - 2편제 - 화력 17% 상승' + '\n' + '■◎□ 3편제 - 화력 21% 상승' + '\n' + '■■□ 4편제 - 화력 24% 상승' + '\n' + '5편제 - 화력 28% 상승', inline=True)
        embed.add_field(name='별명', value='바이킹', inline=True)
        print('MP-446')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/MP-446") or message.content.startswith("/MP446") or message.content.startswith("/바이킹") or message.content.startswith("/No.91."):
        await client.send_file(message.channel, 'No.91_MP-446.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'MP-446 | No.91',
            description = '"겨우 찾아내 줬네, 지휘관! MP446이야, 바이킹이라고 불러줘!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='00:25', inline=True) 
        embed.add_field(name='스킬', value='격발차단' + '\n' + '지속시간 동안 적 전체 사속 감소' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '사속 감소치 : 22%', inline=True)  
        embed.add_field(name='버프', value='1편제 - 화력 14% 상승' + '\n' + '■■□ 2편제 - 2편제 - 화력 17% 상승' + '\n' + '■◎□ 3편제 - 화력 21% 상승' + '\n' + '■■□ 4편제 - 화력 24% 상승' + '\n' + '5편제 - 화력 28% 상승', inline=True)
        print('MP-446')

        await client.send_message(channel,embed=embed)\

    if message.content.startswith("/SpectreM4") or message.content.startswith("/스펙트라") or message.content.startswith("/No.92."):
        await client.send_file(message.channel, 'No.92_Spectre_M4.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'Spectre M4 | No.92',
            description = '"스펙터 M4! 정식으로 입대합니다. 지휘관? 환영회 같은 건 없는 거야?"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:20', inline=True) 
        embed.add_field(name='스킬', value='회피기동' + '\n' + '지속시간 동안 자신의 회피 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '회피 증가치 : 110%', inline=True)  
        embed.add_field(name='버프(AR 한정)', value='화력 20% 상승' + '\n' + '□□□' + '\n' + '■◎□' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='스펙트라', inline=True)
        print('Spectre M4')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/IDW") or message.content.startswith("/고양이") or message.content.startswith("/아디따") or message.content.startswith("/No.93."):
        await client.send_file(message.channel, 'No.93_IDW.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'IDW | No.93',
            description = '"IDW다냥! 거둬주는 거냥? 지휘관...와앗! 다행이다냥~!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:10', inline=True) 
        embed.add_field(name='스킬', value='회피기동' + '\n' + '지속시간 동안 자신의 회피 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 5초' + '\n' + '회피 증가치 : 110%', inline=True)  
        embed.add_field(name='버프(AR 한정)', value='회피 20% 상승' + '\n' + '■□□' + '\n' + '■◎□' + '\n' + '■□□', inline=True)
        embed.add_field(name='별명', value='고양이, 아디따', inline=True)
        print('IDW')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/64식") or message.content.startswith("/No.94."):
        await client.send_file(message.channel, 'No.94_64식.png')
        channel = message.channel
        embed = discord.Embed(
            title = '64식 | No.94',
            description = '"저는 64식 소음 기관단총입니다. 지휘관의 곁에서 공부할 수 있어서, 영광입니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★', inline=True)
        embed.add_field(name='종류', value='SMG', inline=True)
        embed.add_field(name='제조시간', value='01:25', inline=True) 
        embed.add_field(name='스킬', value='회피기동' + '\n' + '폭발한 위치의 2.5반경 내의 적에게 기절을 건다.' + '\n' + '초반 쿨타임 : 5초' + '\n' + '쿨타임 : 16초' + '\n' + '기절 지속시간 : 3.2초', inline=True)  
        embed.add_field(name='버프(AR 한정)', value='사속 20% 상승' + '\n' + '□□□' + '\n' + '■◎□' + '\n' + '□□□', inline=True)
        print('64식')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/한양조88식") or message.content.startswith("/한조") or message.content.startswith("/No.95."):
        await client.send_file(message.channel, 'No.95_한양조_88식.png')
        channel = message.channel
        embed = discord.Embed(
            title = '한양조 88식 | No.95',
            description = '"어서 오세요! 저는 한양조 88식이에요. 주인님을 위해 봉사하겠습니다!"',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★', inline=True)
        embed.add_field(name='종류', value='RF', inline=True)
        embed.add_field(name='제조시간', value='03:50', inline=True) 
        embed.add_field(name='스킬', value='화력전개N' + '\n' + '지속시간 동안 자신의 화력 증가 / 뒤쪽의 수치는 주간작전에 사용 시' + '\n' + '초반 쿨타임 : 8초' + '\n' + '쿨타임 : 8초' + '\n' + '지속시간 : 6초' + '\n' + '화력 증가치 : 90 / 30%', inline=True)  
        embed.add_field(name='버프(HG 한정)', value='스킬 쿨타임 12% 감소' + '\n' + '□□□' + '\n' + '□◎■' + '\n' + '□□□', inline=True)
        embed.add_field(name='별명', value='한조', inline=True)
        print('한양조 88식')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/그리즐리MkV") or message.content.startswith("/그리즐리") or message.content.startswith("/곰누나") or message.content.startswith("/웅녀") or message.content.startswith("/No.96."):
        await client.send_file(message.channel, 'No.96_그릴즐리_MkV.png')
        channel = message.channel
        embed = discord.Embed(
            title = '그릴즐리 MkV | No.96   ',
            description = '"어머, 지휘관님. 그리즐리 매그넘, 오늘부터 당신을 따라가겠습니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='01:10', inline=True) 
        embed.add_field(name='스킬', value='일제사격' + '\n' + '지속시간 동안 아군 전원 화력 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '화력 증가치 : 25%', inline=True)  
        embed.add_field(name='버프', value='1편제 - 화력 15%, 회피 10% 상승' + '\n' + '■■□ 2편제 - 화력 18%, 회피 12% 상승' + '\n' + '□◎■ 3편제 - 화력 22%, 회피 15% 상승' + '\n' + '■■□ 4편제 - 화력 26%, 회피 17% 상승' + '\n' + '5편제 - 화력 30%, 회피 20% 상승', inline=True)
        embed.add_field(name='별명', value='곰누나, 웅녀, 그리즐리', inline=True)
        print('그릴즐리 MkV')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/M950A") or message.content.startswith("/미역") or message.content.startswith("/켈리코") or message.content.startswith("/No.97."):
        await client.send_file(message.channel, 'No.97_M950A.png')
        channel = message.channel
        embed = discord.Embed(
            title = 'M950A | No.97   ',
            description = '"M950A. 지휘관, 오늘부터 당신을 따르겠습니다."',
            colour = discord.Colour.blue()
        )

        embed.add_field(name='등급', value='★★★★★', inline=True)
        embed.add_field(name='종류', value='HG', inline=True)
        embed.add_field(name='제조시간', value='01:05', inline=True) 
        embed.add_field(name='스킬', value='진압신호' + '\n' + '지속시간 동안 아군 전원 화력 증가' + '\n' + '초반 쿨타임 : 6초' + '\n' + '쿨타임 : 12초' + '\n' + '지속시간 : 8초' + '\n' + '화력 증가치 : 25%', inline=True)  
        embed.add_field(name='버프', value='1편제 - 사속 15%, 명중 25% 증가' + '\n' + '■□■ 2편제 - 사속 18%, 명중 31% 증가' + '\n' + '□◎□ 3편제 - 사속 22%, 명중 37% 증가' + '\n' + '■□■ 4편제 - 사속 26%, 명중 43% 증가' + '\n' + '5편제 - 사속 30%, 명중 50% 증가', inline=True)
        embed.add_field(name='별명', value='켈리코, 미역', inline=True)
        print('M950A')

        await client.send_message(channel,embed=embed)

    if message.content.startswith("/00:20") or message.content.startswith("/0020"):
        channel = message.channel
        embed = discord.Embed(
            title = '00:20',
            description = '검색결과',
            colour = discord.Colour.blue()
        )

        embed.set_footer(text = '/[인형이름]을 통해 바로 해당 인형의 정보를 검색 가능합니다.')
        embed.add_field(name='인형', value='M1911' + '\n' + '나강 리볼버' + '\n' + 'P38', inline=True)
        embed.add_field(name='장비', value='X', inline=True)
        embed.add_field(name='요정', value='X', inline=True) 
        print('00:20')

        await client.send_message(channel,embed=embed)

client.run('NTQ4NzIzNTAxNzkyNjI0NjQ5.D1Jesg.qG6cx2bOVrc4S_gXpB8WhauLyPU')
