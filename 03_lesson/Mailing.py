from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address      
        self.from_address = from_address  
        self.cost = cost                  
        self.track = track

    def get_to_address(self):
        return self.to_address
    
    def get_from_address(self):
        return self.from_address
    
    def get_cost(self):
        return self.cost
    
    def get_track(self):
        return self.track
      
    def get_mailing_info(self):
        return(f"Mailing: {self.to_address}, {self.from_address}, {self.cost}, {self.track}")

   