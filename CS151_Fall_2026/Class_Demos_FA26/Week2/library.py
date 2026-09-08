import conversion


grams_val = conversion.pounds_to_grams(2000)
kilometer = conversion.feet_kilo(2000)
liter_val = conversion.cups_to_litter(1)
current_temp= conversion.f_to_c(83)
xtra_cost_of_gas = (current_temp - 20) * 0.5

gas_per_unit = liter_val + xtra_cost_of_gas
total_gas = (grams_val/5000) * (kilometer/0.5) * gas_per_unit



print("Total gass required:  ", total_gas)