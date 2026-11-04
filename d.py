class Fighter:
    def __init__(self,name,hp,attack,defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def super_saiyan(self):
        self.attack = self.attack * 2

    def punch(self,opponent):
        damage = self.attack - opponent.defense

        if damage < 0:
            damage = 0

        opponent.hp -= damage
        if opponent.hp < 0:
            opponent.hp = 0

        print(f"{self.name}の攻撃！ {opponent.name}に{damage}のダメージ！ ({opponent.name}のHP： {opponent.hp})")

gokuu = Fighter("悟空",1000,100,50)
vegita = Fighter("ベジータ",1000,80,100)

gokuu.super_saiyan()
print(f"悟空はスーパーサイヤ人に変身した！ 攻撃力: {gokuu.attack}")

for turn in range(1,11):
    print(f"--- ターン{turn} ---")

    gokuu.punch(vegita)
    if vegita.hp <= 0:
        print(f"{vegita.name}は倒れた！{gokuu.name}の勝利！")
        break

    vegita.punch(gokuu)
    if gokuu.hp <= 0:
        print(f"{gokuu.name}は倒れた！ {vegita.name}の勝利！")
        break
