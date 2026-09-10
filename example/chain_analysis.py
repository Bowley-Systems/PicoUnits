from picounits import LENGTH, MASS, CURRENT, TIME, VOLTAGE, RESISTANCE

length = 1.25 * LENGTH
mass = 200 * MASS
current = 1.5 * CURRENT
time = 4.2 * TIME
voltage = 48 * VOLTAGE
resistance = 3.2 * RESISTANCE

area = length * length
volume = area * length

force = mass * length / (time ** 2)
power = voltage * current
energy = power * time

resistance_drop = current * resistance
remaining_voltage = voltage - resistance_drop

acceleration = force / mass
velocity = length / time
momentum = mass * velocity

work = force * length
mechanical_power = work / time

efficiency = mechanical_power / power

result_1 = momentum * acceleration
result_2 = energy / volume
result_3 = force / area
result_4 = voltage / current
result_5 = result_1 / (result_2 * result_3)

result_1.info()
