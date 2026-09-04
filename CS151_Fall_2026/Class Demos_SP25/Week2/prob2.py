import prob1

grams_val = prob1.pounds_to_grams(2000)
litre_val = prob1.cups_to_litter(1)
kilometer_val = prob1.feet_kilo(2000)
current_temp = prob1.f_to_c(83)
xtra_cost_of_gas = (current_temp - 20) * 0.5 # Extra cost of gas needed above the baseline

gas_per_unit = litre_val + xtra_cost_of_gas

total_gass = (grams_val/5000) * (kilometer_val/0.5) * gas_per_unit

print(total_gass)
