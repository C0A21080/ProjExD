import random
import datetime

NUM_OF_TRIALS = 5 #最大繰り返し回数
NUM_OF_ALL_CHARS = 10 #対象文字数
NUM_OF_ABS_CHARS = 2 #欠損文字数


def main():
    st = datetime.datetime.now() #時間計測開始
    for _ in range(NUM_OF_TRIALS):
        seikai = shutudai()
        f = kaitou(seikai)
        if f == 1: #完全正解なのでbreakする
            break
    ed = datetime.datetime.now() #時間計測終了
    print(f"{(ed-st).seconds}秒かかりました")



def shutudai():
     #全アルファベット文字のリスト
    alphabets = [chr(c+65) for c in range(26)] #chr(コード)->文字
     #26文字からランダムにNUM_OF_ALL_CHARS個の文字を選ぶ
    all_char_lst = random.sample(alphabets, NUM_OF_ALL_CHARS)
    print(f"対象文字：{all_char_lst}")

    #対象文字からNUM_OF_ABS_CHARS個の欠損文字をランダムに選ぶ
    abs_char_lst = random.sample(all_char_lst, NUM_OF_ABS_CHARS)
    print(f"欠損文字：{abs_char_lst}")#欠損文字の正解なので後で非表示にする

    #対象文字から欠損文字を除いた表示文字を表示する
    pre_char_lst = [c for c in all_char_lst if c not in abs_char_lst]
    print(f"表示文字：{pre_char_lst}")

    return abs_char_lst #正解欠損文字をmain関数に返す


def kaitou(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？"))
    if num != NUM_OF_ABS_CHARS:
        print("不正解です。またチャレンジしてください")
        return 0 #文字数回答で不正解の場合
    else:
        print("正解です。それでは具体的に欠損文字を1つずつ入力してください")
        for i in range(NUM_OF_ABS_CHARS):
            c = input(f"{i+1}つ目の文字を入力して下さい：")
            if c not in seikai:
                print("不正解です。またチャレンジしてください")
                return 0 #文字回答で不正解の場合
            seikai.remove(c)
        print("正解です。ゲームを終了します")
        return 1 #完全正解の場合


if __name__ == "__main__":
    main()