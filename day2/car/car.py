class Car(object):
  def __init__(self, car_type = None , car_model = None, car_name =None ):
    self.car_type = car_type
    self.speed = 0
    if car_model is None:
      self.car_model = "GM"
    else:
      self.car_model = car_model
    if car_name is None:
      self.car_name = "General"
    else:
      self.car_name = car_name

  def car_doors(self):
   if self.car_type != "porshe" or "Koenigsegg":
     return 4
   return 2

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

  def is_saloon(self, number):
      if self.car_type == "saloon":
          return True
      return False
