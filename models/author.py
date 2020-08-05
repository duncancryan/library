class Author():
    def __init__(self, name, is_alive = True, id= None):
        self.name = name
        self.is_alive = is_alive
        self.id = id

    def mark_as_dead(self):
        self.is_alive = False
    
    


