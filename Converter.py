# coding:utf-8

class RomaKanaConverter:
    # mode: "kana" or "roma"
    def __init__(self, text, mode):
        # set kana or roma mode
        if mode == "kana":
            self.kana_text = text
        elif mode == "roma":
            self.roma_text = text
        else:
            print("set mode correctly")

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
        kana_token_list = []
        [kana_token_list.append(item) for item in self.kana_text]
        return kana_token_list

    def tokenize_roma(self):
        pass

    def roma2kana(self):
        pass

    def kana2roma(self):
        self.roma_text = ""
        kana_token_list = self.tokenize_kana()
        for token in kana_token_list:
            self.roma_text += self.kana_roma_dict[token]
        print(self.roma_text)

if __name__ == "__main__":
    text = "コンニチハ"
    print(text)
    print("↓")
    RKC = RomaKanaConverter(text, mode="kana")
    RKC.kana2roma()
