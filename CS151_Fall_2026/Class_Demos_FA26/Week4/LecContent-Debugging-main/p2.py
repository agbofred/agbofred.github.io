import astrolib
from rich import print
from rich.traceback import install
install(show_locals=True)

# ENVIRONMENT DATA
outside_temp = 40
inside_temp = 2000
shield_level = 8

# ENGINE DATA
pressure_sensor = 400
flow_sensor = 20
density_sensor = 1.5

print("System Check Initializing...")

# --- MISSION LOGIC ---
is_engine_ready = False
is_thermal_ready = False

final_status = astrolib.validate_mission_parameters(
    pressure_sensor, 
    flow_sensor, 
    density_sensor, 
    inside_temp, 
    outside_temp, 
    shield_level,
    0
)

if final_status:
    print("[bold green]ALL SYSTEMS GO: Proceed to launch.")
else:
    print("[bold red]LAUNCH ABORTED: Systems do not meet safety threshold.")
    print("[red]Check sensor calibration and variable assignments.")
