from diaries.DiarySample import DiarySample
from diaries.HaruDiary import HaruDiary
from diaries.TakumiDiary import TakumiDiary
from diaries.KubotaDiary import KubotaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    KubotaDiary(),     
    TakumiDiary(), ]

for d in diaries:
    print("--------------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
