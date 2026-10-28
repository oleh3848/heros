import random

classes={
    "Warior":{"hp":(110,140),"attack":(10,16)},
    "Pudg":{"hp":(200,300),"attack":(5,8)},
    "Mag":{"hp":(100,120),"attack":(15,19)},
    "Cherier":{"hp":(150,170),"attack":(12,15)}
}
def create_hero(name,hero_class):
    stats = classes[hero_class]
    return{
        "name":name,
        "class": hero_class,
        "hp":random.randint(*stats["hp"]),
        "attack":random.randint(*stats["attack"])
    }
def show_hero(hero):
    print("="*30)
    print(f"Hero:{hero["name"]}-{hero["class"]}")
    print(f"Hp:{hero["hp"]}")
    print(f"Attack:{hero["attack"]}")
    print("="*30)


hero = create_hero("gurack","Warior")
show_hero(hero)

hero = {
    "name":"Mazer",
    "attack": 50,
    "class":"vendy",
    "hp":100
}
print(hero["name"])
if hero["hp"] <30:
    print("залишилось мало хп")
else:
    print("герой повний сил")




if hero["class"] =="vendy":
    print("ти вогняний маг")
else:
    print("ти льодянийц маг ")






locations=["засніжені гори","палаючі рівнини","спустошені поля"]

for l in locations:
    print("locatioin:"+l)



def greetings():
    print("привіт")


greetings()
greetings()
greetings()