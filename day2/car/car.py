class Car(object):
  def __init__(self, car_type = None , model = None, name =None ):
    self.car_type = car_type
    self.speed = 0
    self.num_of_doors = 2
    if model is None:
      self.model = "GM"
    else:
      self.model = model
    if name is None:
      self.name = "General"
    else:
      self.name = name

  def car_doors(self):
   if self.car_type != "porshe" or "Koenigsegg":
     self.num_of_doors = 4
     return self
   return self.num_of_doors

  def num_of_wheels(self):
    if self.car_type != "trailer":
      return 4
    else:
      return 8

  def drive(self, number):
    if self.car_type == "trailer":
      if number == 7:
        self.speed = 77
        return self
      if number <= 1 and number <= 7:
        self.speed = 30
        return self
      if number > 7:
        self.speed = 0
        return self
      else:
        if number >= 1:
          self.speed = 1000
          return self
    else:
      return self

  def is_saloon(self, number, car_type):
    if self.car_type == "saloon":
      return True
    return False
