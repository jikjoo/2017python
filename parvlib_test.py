from ParvisLib import MainID, MainWord

sub_television = ['텔레비전','티브이','티이브이','티-브이','티부이','티비','텔레비젼','테레비전','테레비젼','태레비젼','태레비전','텔레비','테레비',
 '텔리비죤','텔레비죤','영상표기장치','방송수신기','방송수신장치','영상수신장치','영상수신기']
eng_television = ['tv','tv set','television','catv','broadcast','broadcast','televi']

sub_surround = ['이웃','테두리','근처','가장자리','주위','인접','외부','환경','저면','후면','에지','이면','배면','양면']
eng_surround =[
    'context','edge','surround','outline','circumstance','background','peripheral region','outdoor','inside',
    'natural','outskirt','end','periph','periphery','boundar','perimeter','circumst','ends','boundary',
    'interpos','around','peripheral','border','circumference','neighboring','rear side','periphera','last','external']

sub_device = [	'머신','수단','설치','설비','노드','장비','디바이스','기계','유닛','로봇','회로','방법','도구','구조','이큅먼트','인스톨리제이션',
 '기','시스템','인스톨래이션','모듈','단말','보조장치','기구','엘러먼트','기기']
eng_device = ['setup','device','instrument','part','accessory','apparatus','system','arrangement','attachment','supplementary device',
    'assembly','contrivance','equipment','component','element','unit','plant','installation','auxiliary device','package','accessories',
    'auxiliaries','instrum','machin','facility']
sub_remocon = ['리모트컨트롤','리모트 컨트롤러','리모컨','리모트','원격제어기','원격제어기','리모트 콘트롤러','컨트롤러','콘트롤러']
eng_remocon = ['controler','remo','remote controller','remotecontrol','remote controler','remote','remotcontrol','remocon']
sub_speaker = ['스피카','음향변환','음성','스피이카','메거폰','음향 변환기','확성기','고성기','스삐카','매가폰','라우드스피커','스피이커','사운드',
    '전기 음향 변환기','앰프','트랜스듀서','스피크']
eng_speaker = ['spica','megaphone','loud-speaker','speak','speaker','loudspeaker']
television = MainID(15)
surround = MainID(16)
device = MainID(17)
remcon = MainID(18)
speaker = MainID(19)


speaker.insert_sub(['스피커'])
surround.insert_sub(['주변'])
device.insert_sub(['장치'])
remcon.insert_sub(['리모콘'])
