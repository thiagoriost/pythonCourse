class Counter:
    count = 0
    
    @classmethod
    def incrementar(cls):
        cls.count += 1
        
Counter.incrementar()
Counter.incrementar()
print(Counter.count)