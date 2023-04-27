import pytchat
import pandas as pd
from datetime import date


today_specific = date.today() # datetime.date(2022, 7, 12) << 이런식으로 나옴
today = today_specific.isoformat() # 위의 데이터를 iso 형식의 문자열로 변경

video_id = '타겟 라이브 유튜브 영상의 video id' # 유튜브 라이브 영상의 주소를 보면 뒤쪽에 video_id가 있으므로 해당 값을 확인하여 변경해줘야 함.

chat = pytchat.create(video_id=video_id)

empty_frame = pd.DataFrame(columns=["댓글 작성 시간", "댓글 작성자", "내용"])
empty_frame.to_csv(f'{today} 채팅내역.csv', encoding='cp949')

while chat.is_alive():
    try :
        data = chat.get()
        items = data.items
        for item in items:
            print(f"{item.datetime} [{item.author.name}]- {item.message}")
            data.tick()
            data2 = {'댓글 작성 시간': [item.datetime], '댓글 작성자': [item.author.name], '내용': [item.message]}
            result = pd.DataFrame(data2)
            result.to_csv(f'{today} 채팅내역.csv', mode='a', header=False, encoding='cp949')
    except KeyboardInterrupt:
        chat.terminate()
        break




