# coding:utf-8

class RomaKanaConverter:
    # mode: "kana" or "roma"
    def __init__(self):
        self.create_dict()
        
    def create_dict(self):
        kana_roma_dict = {}
        roma_kana_dict = {}
        # set dict for conversion
        with open("kana_roma.csv", "r", encoding="utf-8") as f:
            l_strip = [s.strip() for s in f.readlines()]
        for line in l_strip:
            (roma, _, kana) = line.split(",")
            kana_roma_dict[kana] = roma
            roma_kana_dict[roma] = kana
        self.roma_kana_dict = roma_kana_dict
        self.kana_roma_dict = kana_roma_dict

    def tokenize_kana(self):
        # 一文字ずつリスト化してるだけ
        kana_token_list = []
        [kana_token_list.append(item) for item in self.kana_text]
        return kana_token_list

    def tokenize_roma(self):
        roma_token_list = []
        token_idx = [0]
        vowel = ['a', 'i', 'u', 'e', 'o']
        # 分割の仕方 ko nn ni ti ha
        # 母音　or　連続n2個　の後で区切る -> idxはトークンの最初の子音
        for i in range(len(self.roma_text)):
            # 現在地が母音 次の文字から違うトークン
            if (self.roma_text[i] in vowel) and (i+1 < len(self.roma_text)):
                token_idx.append(i+1)
            # 現在地からnが2個連続 2個後の文字から違うトークン 
            elif (self.roma_text[i-1] in vowel and self.roma_text[i] == 'n' and self.roma_text[i+1] == 'n') and (i+2 < len(self.roma_text)):
                token_idx.append(i+2)
        token_idx = list(set(token_idx))

        # わざわざループ2回でやらなくていいのでは
        for i in range(len(token_idx)):
            if i == len(token_idx) - 1:
                roma_token_list.append(self.roma_text[ token_idx[i] : ])
            else:
                roma_token_list.append(self.roma_text[ token_idx[i] : token_idx[i+1] ])
        return roma_token_list

    def roma2kana(self, text, _print=False):
        self.set_text("roma", text)
        self.kana_text = ""
        roma_token_list = self.tokenize_roma()
        for token in roma_token_list:
            self.kana_text += self.roma_kana_dict[token]
        if _print:
            print(self.kana_text)
        return self.kana_text

    def kana2roma(self, text, _print=False):
        self.set_text("kana", text)
        self.roma_text = ""
        kana_token_list = self.tokenize_kana()
        for token in kana_token_list:
            self.roma_text += self.kana_roma_dict[token]
        if _print:
            print(self.roma_text)
        return self.roma_text

    def set_text(self, mode, text):
        if mode == "roma":
            self.roma_text = text
        elif mode == "kana":
            self.kana_text = text

if __name__ == "__main__":
    RKC = RomaKanaConverter()
    print("モライモライ")
    print("↓")
    RKC.kana2roma("モライモライ",_print=True)

    RKC = RomaKanaConverter()
    print("konnnitiha")
    print("↓")
    RKC.roma2kana("konnnitiha", _print=True)

