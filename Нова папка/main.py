class Hero:
    def __init__(self,name, hero_class,hp,attack):
        self.name = name
        self.hero_class = hero_class
        self.hp = hp
        self.attack = attack
        print("Галк вийшов на поле бою")
    def say_hello(self):
        print(f"Привіт! Я {self.name}")
    def hit(self, target):
        print(f"{self.name} наносить удар{target.name}і наносить {self.attack}шкоди")
        target.take_damage(self.attack)
    def take_dammage(self,damage) :
        self.hp -=damage
        if self.hp >0:
            print(f"{self.name}, залишилось {self.hp}")
        else:
            print("Героя переможено((((")





spider_man =Hero("Людина павук","Боєць",120,120)
venom =Hero("Веном","Інопланетне чудовисько",200,80)

spider_man.hit(venom)





# class Enemy:
#     def __init__(self, name, hp, attack):
#         self.name = name
#         self.hp = hp
#         self.attack = attack
      

HULK = Hero("Галк", "Силач", 400, 350)
HULK.say_hello()