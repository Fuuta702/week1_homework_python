name = input("名前を入力してください") 
if " " in name:
    words = name.split()
    num = len(words[0]) + len(words[1])
elif "・"in name:
    words = name.split("・")
    num = len(words[0]) + len(words[1]) + len(words[2])
else:
    len(name)
    num = len(name)

age = input("西暦/月/日を入力してください")
day = age.split("/")
year = int(day[0]) + int(day[1]) + int(day[2])

unnsei = num + year
if unnsei % 6 == 0:
    print(f"{name}さんの運勢：大吉")
elif unnsei % 3 == 0:
    print(f"{name}さんの運勢：中吉")
elif unnsei % 2 == 0:
    print(f"{name}さんの運勢：吉")
else:
    print(f"{name}さんの運勢：凶")




