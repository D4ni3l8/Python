train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# converting from fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = f_temp - 32 * (5/9)
  return c_temp

f100_in_celsius = f_to_c(100)

# function that converts celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

# function the calculates force
def get_force(mass, acceleration):
  return mass*acceleration

# calculating the force of a train given the mass and energy
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies", train_force, "Newtons of force")

c = 3*10**8 # constant that is usually set to the speed of light, which is roughly

def get_energy(mass, c):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies", bomb_energy, "joules")

# function that calculates work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does", train_work, "joules of work over", train_distance, "meters.")
