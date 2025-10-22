from diaries.DiarySample import DiarySample
from diaries.KubotaDiary import KubotaDiary
from diaries.HaruDiary import HaruDiary
from diaries.TakumiDiary import TakumiDiary
from diaries.UedaDiary import UedaDiary
# ↓のリストには、メンバーの各日記が格納されます。

diaries = [
    DiarySample(), 
    KubotaDiary(), 
    HaruDiary(),
    TakumiDiary(), 
    UedaDiary(), 
    ]

for d in diaries:
    print("--------------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()