import random

def main():
    seikai = shutudai()
    kaitou(seikai)

def shutudai():
    qas = [{"q":"サザエの旦那の名前は？","a":["マスオ","ますお"]},
    {"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},
    {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]}]
    print("問題：")
    r = random.randint(0,2)
    print(qas[r]["q"])
    return qas[r]["a"]


def kaito(seikai):
    ans = input("答えるんだ:")
    if ans in seikai:
        print("正解！！！")
    else:
        print("出直してこい")

ed=datetime.datetime.now()
print(f"解答まで{(ed-st).seconds}秒かかりました")

if __name__ =="__main__":
    main()