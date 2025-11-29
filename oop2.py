class Vehicle:
    #methods
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand

    def start_engine(self):
        print(f"Engine started ")
        
    def display_info(self):
        print(f"model:{self.model}, brand :{self.brand}")
    
class electric_car():
    def start_engine(self):
        print("Electric car engine started silently.")
        
#object instantiation
car1=Vehicle("Model S","Tesla")
car2=Vehicle("Mustang","Ford")
elec_car3=electric_car()

car2.display_info()
car1.start_engine()
elec_car3.start_engine()
        
    