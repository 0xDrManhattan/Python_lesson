print("Hello,VisualCode!")
class Car:
    name=None
    age=None
    is_rnd=None

    def set_data(self,name,age,is_rdn):

        self.name=name
        self.age=age
        self.is_rdn=is_rdn

    def get_data(self):
        print('Name:', self.name,'Age', self.age,'Is Run and Drive;',self.is_rdn)
car1=Car()
car2=Car()
car1.set_data('BWM',2024,True)
car2.set_data('AUDI',2024,True)
car1.get_data()