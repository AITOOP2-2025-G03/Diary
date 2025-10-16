from diaries.DiarySample import DiarySample
from diaries.HaruDiary import HaruDiary
from diaries.TakumiDiary import TakumiDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    HaruDiary(),
    TakumiDiary(), 
    ]

for d in diaries:
    print("--------------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
