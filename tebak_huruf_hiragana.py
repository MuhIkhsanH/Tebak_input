import random
import sys
import os

jepang =[
    {
        "huruf": "あ",
        "arti": "a"
    },
    {
        "huruf": "い",
        "arti": "i"
    },
    {
        "huruf": "う",
        "arti": "u"
    },
    {
        "huruf": "え",
        "arti": "e"
    },
    {
        "huruf": "お",
        "arti": "o"
    },
    {
        "huruf": "は",
        "arti": "ha"
    },
    {
        "huruf": "ひ",
        "arti": "hi"
    },
    {
        "huruf": "ふ",
        "arti": "fu"
    },
    {
        "huruf": "へ",
        "arti": "he"
    },
    {
        "huruf": "ほ",
        "arti": "ho"
    },
    {
        "huruf": "か",
        "arti": "ka"
    },
    {
        "huruf": "き",
        "arti": "ki"
    },
    {
        "huruf": "く",
        "arti": "ku"
    },
    {
        "huruf": "け",
        "arti": "ke"
    },
    {
        "huruf": "こ",
        "arti": "ko"
    },
    {
        "huruf": "た",
        "arti": "ta"
    },
    {
        "huruf": "ち",
        "arti": "chi"
    },
    {
        "huruf": "つ",
        "arti": "tsu"
    },
    {
        "huruf": "て",
        "arti": "te"
    },
    {
        "huruf": "と",
        "arti": "to"
    },
    {
        "huruf": "さ",
        "arti": "sa"
    },
    {
        "huruf": "し",
        "arti": "shi"
    },
    {
        "huruf": "す",
        "arti": "su"
    },
    {
        "huruf": "せ",
        "arti": "se"
    },
    {
        "huruf": "そ",
        "arti": "so"
    },
    {
        "huruf": "な",
        "arti": "na"
    },
    {
        "huruf": "に",
        "arti": "ni"
    },
    {
        "huruf": "ぬ",
        "arti": "nu"
    },
    {
        "huruf": "ね",
        "arti": "ne"
    },
    {
        "huruf": "の",
        "arti": "no"
    },
    {
        "huruf": "ま",
        "arti": "ma"
    },
    {
        "huruf": "み",
        "arti": "mi"
    },
    {
        "huruf": "む",
        "arti": "mu"
    },
    {
        "huruf": "め",
        "arti": "me"
    },
    {
        "huruf": "も",
        "arti": "mo"
    },
    {
        "huruf": "や",
        "arti": "ya"
    },
    {
        "huruf": "ゆ",
        "arti": "yu"
    },
    {
        "huruf": "よ",
        "arti": "yo"
    },
    {
        "huruf": "ら",
        "arti": "ra"
    },
    {
        "huruf": "り",
        "arti": "ri"
    },
    {
        "huruf": "る",
        "arti": 'ru'
    },
    {
        "huruf": "わ",
        "arti": "wa"
    },
    {
        "huruf": "を",
        "arti": "wo"
    },
    {
        "huruf": "ん",
        "arti": "n"
    },
    {
        "huruf": "が", # 44
        "arti": "ga"
    },
    {
        "huruf": "ぎ",
        "arti": "gi"
    },
    {
        "huruf": "ぐ",
        "arti": "gu"
    },
    {
        "huruf": "げ",
        "arti": "ge"
    },
    {
        "huruf": "ご",
        "arti": "go"
    },
    {
        "huruf": "ざ", #49
        "arti": "za"
    },
    {
        "huruf": "じ",
        "arti": "ji"
    },
    {
        "huruf": "ず",
        "arti": "zu"
    },
    {
        "huruf": "ぜ",
        "arti": "ze"
    },
    {
        "huruf": "ぞ",
        "arti": "zo"
    },
    {
        "huruf": "だ", # 54
        "arti": "da"
    },
    {
        "huruf": "ぢ",
        "arti": "ji"
    },
    {
        "huruf": "づ",
        "arti": "zu"
    },
    {
        "huruf": "で",
        "arti": "de"
    },
    {
        "huruf": "ど",
        "arti": "do"
    },
    {
        "huruf": "ば", # 59
        "arti": "ba"
    },
    {
        "huruf": "び",
        "arti": "bi"
    },
    {
        "huruf": "ぶ",
        "arti": "bu"
    },
    {
        "huruf": "べ",
        "arti": "be"
    },
    {
        "huruf": "ぼ",
        "arti": "bo"
    },
    {
        "huruf": "ぱ", # 64
        "arti": "pa"
    },
    {
        "huruf": "ぴ",
        "arti": "pi"
    },
    {
        "huruf": "ぷ",
        "arti": "pu"
    },
    {
        "huruf": "ぺ",
        "arti": "pe"
    },
    {
        "huruf": "ぽ",
        "arti": "po"
    }
]

total = 68
skor = 0
print("Latihan Hiragana \n")
idx = jepang[total]
last = idx["huruf"]
print("last huruf:",last,"\n")
while 1:
    data = random.randint(0,total)
    ke = jepang[data]
    print("Huruf Apa Ini:",ke["huruf"])
    msk = input("Jawab: ").lower()
    if msk == "":
        print("Tidak Boleh Kosong\n")
        pass
    elif msk == ke["arti"]:
        print("Benar\n")
        skor += 1
    else:
        print("Salah, Jawabannya Adalah:",ke["arti"])
        print("Skor Anda: ",skor)
        input("Enter Untuk Mengulang>>")
        os.system("cls")
        os.system("python hiragana.py")
        #sys.exit()
