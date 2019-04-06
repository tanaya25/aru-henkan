# coding:utf-8
import sys
import MeCab
from Converter import RomaKanaConverter

class AruHenkan():
    def __init__(self):
        pass

    def set_text(self, text):
        self.text = text

    def tokenize_wakati(self, text):
        # 分かち書き
        tagger = MeCab.Tagger("-Owakati")

        # 空白で分割 リストの末尾に\nが入るので削除        
        token_list = tagger.parse(text).split(" ")[:-1]
        return token_list

    def extract_chasen(self, text):
        tagger = MeCab.Tagger("-Ochasen")
        result = tagger.parse(text).split("\t")[:-2]
        # 形態素解析の結果は
        # 君      キミ    君      名詞-代名詞-一般
        # 元の文字, カナ, 品詞だけ抜き出して返す
        kana_lex_list = [result[0], result[1], result[3]]
        return kana_lex_list

    def conversion(self, text):
        converted_text = ""
        for i in range(len(text)):
            if text[i] == 'i':
                converted_text += 'ai'
            else:
                converted_text += text[i]
        return converted_text

    def aru_henkan(self, text):
        self.set_text(text)
        # 形態素解析を分かち書きごとに行う
        token_list = self.tokenize_wakati(self.text)
        kana_lex_list = [self.extract_chasen(token) for token in token_list]
        RKC = RomaKanaConverter()
        converted_text = ""
        for item in kana_lex_list:
            (orig_text, kana, word_type) = item
            # 名詞だけ"ある変換"を行う
            if word_type.find("名詞") != -1:
                RKC.set_text("kana", kana)
                converted_roma = self.conversion(RKC.kana2roma(_print=True))
                RKC.set_text("roma", converted_roma)
                orig_text = RKC.roma2kana(_print=True)
            converted_text+=orig_text
        return converted_text

if __name__ == '__main__':
    AH = AruHenkan()
    for i in range(10):
        text = input()
        print("↓ある変換")
        print(AH.aru_henkan(text))
        print()

# テスト用 オタクはモリモリと飯を食え
#         異端アピ
#         在りし日の響き
