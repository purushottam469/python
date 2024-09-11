#class and object

class electronic:
        os="window"
        ram="none"
        hard_disk="none"

        def __init__(self,ram,hard_disk): # dunden method  # yo constructior jaba object initilize garxam taba call hunxa. 
            print("hi i am called")
            self.ram = ram
            self.hard_disk = hard_disk

            
        def get_ram(self):
            return self.ram

laptop=electronic(4,500)    

    # laptop.get_ram()



print(laptop.os)
print(laptop.hard_disk)
print(laptop.ram)


            