import re

words = ["orange", "october", "octpus", "order", "banana", "baby", "busy"]

#正規表現のパターン一致するものを画面表示
pattern = r"oc.*"
print ("ocから始まるパターン", pattern)
for word in words:
    if re.match(pattern, word):
        print("-", word)

pattern = r"b.*y"
print("bから始まるパターン", pattern)
for word in words:
    if re.search(pattern, word):
        print("-", word)
