# calculating minimum and maximum costs of solutions
# according to following formula's:
# fuel_weight = (Mass + Payload-mass) x FtW / (1-FtW) = F
# fuel_costs = Base cost + math.ceil( fuel_weight x 1000 ) x 5

import math

# features Cygnus (1)
cygnus_payload_mass = 2000
cygnus_payload_volume = 18.9
cygnus_mass = 7400
cygnus_base_cost = 390000000
cygnus_ftw = 0.73
cygnus_fuel_weight_max = (cygnus_mass + cygnus_payload_mass) * cygnus_ftw / (1 - cygnus_ftw)
cygnus_fuel_costs_max = cygnus_base_cost + math.ceil(cygnus_fuel_weight_max * 1000) * 5
cygnus_fuel_weight_min = (cygnus_mass) * cygnus_ftw / (1 - cygnus_ftw)
cygnus_fuel_costs_min = cygnus_base_cost + math.ceil(cygnus_fuel_weight_min * 1000) * 5
print(cygnus_fuel_weight_max)
print(cygnus_fuel_costs_max)
print(cygnus_fuel_weight_min)
print(cygnus_fuel_costs_min)


# features Progress (2)
progress_payload_mass = 2400
progress_payload_volume = 7.6
progress_mass = 7020
progress_base_cost = 175000000
progress_ftw = 0.74
progress_fuel_weight_max = (progress_mass + progress_payload_mass) * progress_ftw / (1 - progress_ftw)
progress_fuel_costs_max = progress_base_cost + math.ceil(progress_fuel_weight_max * 1000) * 5
progress_fuel_weight_min = (progress_mass) * progress_ftw / (1 - progress_ftw)
progress_fuel_costs_min = progress_base_cost + math.ceil(progress_fuel_weight_min * 1000) * 5
print(progress_fuel_weight_max)
print(progress_fuel_costs_max)
print(progress_fuel_weight_min)
print(progress_fuel_costs_min)

# features Kounotori (3)
kounotori_payload_mass = 5200
kounotori_payload_volume = 14
kounotori_mass = 10500
kounotori_base_cost = 420000000
kounotori_ftw = 0.71
kounotori_fuel_weight_max = (kounotori_mass + kounotori_payload_mass) * kounotori_ftw / (1 - kounotori_ftw)
kounotori_fuel_costs_max = kounotori_base_cost + math.ceil(kounotori_fuel_weight_max * 1000) * 5
kounotori_fuel_weight_min = (kounotori_mass) * kounotori_ftw / (1 - kounotori_ftw)
kounotori_fuel_costs_min = kounotori_base_cost + math.ceil(kounotori_fuel_weight_min * 1000) * 5
print(kounotori_fuel_weight_max)
print(kounotori_fuel_costs_max)
print(kounotori_fuel_weight_min)
print(kounotori_fuel_costs_min)

# features Dragon (4)
dragon_payload_mass = 6000
dragon_payload_volume = 10
dragon_mass = 12200
dragon_base_cost = 347000000
dragon_ftw = 0.72
dragon_fuel_weight_max = (dragon_mass + dragon_payload_mass) * dragon_ftw / (1 - dragon_ftw)
dragon_fuel_costs_max = dragon_base_cost + math.ceil(dragon_fuel_weight_max * 1000) * 5
dragon_fuel_weight_min = (dragon_mass) * dragon_ftw / (1 - dragon_ftw)
dragon_fuel_costs_min = dragon_base_cost + math.ceil(dragon_fuel_weight_min * 1000) * 5
print(dragon_fuel_weight_max)
print(dragon_fuel_costs_max)
print(dragon_fuel_weight_min)
print(dragon_fuel_costs_min)

# sum of four ships
maximum_totaal = cygnus_fuel_costs_max + progress_fuel_costs_max + kounotori_fuel_costs_max + dragon_fuel_costs_max
print("maximum totaalkosten:")
print(maximum_totaal)
minimum_totaal = cygnus_fuel_costs_min + progress_fuel_costs_min + kounotori_fuel_costs_min + dragon_fuel_costs_min
print("minimun totaalkosten:")
print(minimum_totaal)

# output:
# maximum totaalkosten:
# 2019317585
# minimun totaalkosten:
# 1817328670
