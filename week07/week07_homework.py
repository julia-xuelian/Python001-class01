class Zoo:
    def __init__(self, name):
        self.name = name
        self.Cat =[]

    def add_animal(self, animal):
        if animal in self.Cat:
            return Exception("已在园中，请不要重复添加！")
        else:
            self.Cat.append(animal)

class Animal:
    def __init__(self, kind, bodytype, character):
        self.kind = kind
        self.bodytype = bodytype
        self.character = character

    @staticmethod
    def ferocity(kind, bodytype, character):
        if kind == '食草动物' or bodytype == '小型' or character == '温驯':
            return False
        else:
            return True


class Cat(Animal):
    def __init__(self, name, kind, bodytype, character):
        self.name = name
        super().__init__(kind, bodytype, character)

    @classmethod
    def cry(cls):
        sound = '喵喵喵'
        return f"{cls.__name__} 的叫声是 {sound}."

    def fit_for_pet(self):     
        if self.bodytype != '大型' and self.character == '温驯':
            return '适合作为宠物'
        else:
            return '不适合作为宠物'

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    print(f'{cat1.cry()}')
    print(f'{cat1.name} {cat1.fit_for_pet()}')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    
 
