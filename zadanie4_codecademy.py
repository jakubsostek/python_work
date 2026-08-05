# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def f_to_c(temperature):
  c_temp = (temperature - 32) * 5/9
  return c_temp

celsius = f_to_c(100)
print(celsius)

def c_to_f(temperature):
  f_temp = temperature * 9/5 + 32
  return f_temp

fahrenheit = c_to_f(0)
print(fahrenheit)

def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(22680, 10)
print(train_force)

print(f"The GE train supplies {train_force} Newtons of force.")

def get_energy(mass, c=3*10**8):
    return mass * (c ** 2)

bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules")

def get_work(mass,acceleration,distance):
    return get_force(mass,acceleration) * distance

train_work =  get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")



