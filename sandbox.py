class Org(object):
    
    def __init__(self, val):
        self.val = val

    
    @property
    def value (self):
        return self.val 

    @value.setter
    def value(self,value):
        self.val = value 


class hoge(Org):
    pass



t = hoge(1)
t.value = 'hoge'

print(t.value)