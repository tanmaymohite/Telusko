class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def machine(self):
        print('config is ',self.cpu,self.ram)


comp1 = computer('ryzen 5','16gb')
comp2 = computer('i5','8gb')

comp1.machine()
comp2.machine()



