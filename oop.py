class peguet405(object):
    count=0

    def __init__(self,  type,color='white', ring='mamuli',airbag='false'):
        self.type=type
        self.color=color
        self.ring=ring
        self.airbag=airbag
    def print_color(self):
        print(self.color)
    
p1=peguet405('taksuz')
p1.print_color()

    
