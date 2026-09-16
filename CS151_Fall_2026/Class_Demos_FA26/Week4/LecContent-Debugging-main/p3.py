import astrolib
from rich import print
from rich.traceback import install
install(show_locals=True)

# --- ENVIRONMENT DATA ---
p_val = 200
f_val = 10
d_val = 1.1
c_temp = 3000
a_temp = 100
sweep = 5

# --- CALCULATION LOGIC ---
heat_intensity = 450
shield_factor = 0

print("Calculating shield requirements for intensity:", heat_intensity)

if heat_intensity > 400:
    shield_factor = 10
elif heat_intensity > 100:
    shield_factor = 5
elif heat_intensity > 0:
    shield_factor = 1
else:
    shield_factor = 0

is_mission_go = astrolib.validate_mission_parameters(
    p_val, 
    f_val, 
    d_val, 
    c_temp, 
    a_temp, 
    shield_factor, 
    sweep
)

if is_mission_go:
    print("[bold green]Mission is a go!")
else:
    print("[bold red]Abort! Abort! Abort!")
