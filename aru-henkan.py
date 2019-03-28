# coding:utf-8
import sys
import MeCab
from Converter import RomaKanaConverter as RKC

def tokenize_wakati(string):
    # 分かち書き
    tagger = MeCab.Tagger("-Owakati")

    # 空白で分割 リストの末尾に\nが入るので削除        
    token_list = tagger.parse(text).split(" ")[:-1]
    return token_list

def parse_chasen(string):
    tagger = MeCab.Tagger("-Ochasen")
    result = tagger.parse(string).split("\t")[:-2]
    # 形態素解析の結果は
    # 君      キミ    君      名詞-代名詞-一般
    # カナと品詞だけ抜き出して返す
    kana_lex_list = [result[1], result[3]]
    return kana_lex_list

def aru_henkan(string):
    # 形態素解析を分かち書きごとに行う
    token_list = tokenize_wakati(string)
    kana_lex_list = [parse_chasen(token) for token in token_list]
    return kana_lex_list

if __name__ == '__main__':
    # TODO:ここを標準入力にする
    text = 'オタクはモリモリと飯を食え'
    result = aru_henkan(text)
    [print(item) for item in result]