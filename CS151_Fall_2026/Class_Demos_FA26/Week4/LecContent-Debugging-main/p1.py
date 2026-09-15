import astrolib

from rich import print
from rich.traceback import install
install(show_locals=True)

# --- CONFIGURATION ---
initial_pressure = 500
flow_rate = 10
fluid_density = 1.2
core_heat = 1200
ambient_heat = 50
shielding = 5

print("[green]Starting Stress Test Simulation...[/green]")

time_step = 0
while time_step < 10:
    current_flow = flow_rate - time_step
    # if current_flow > 0:
    status = astrolib.validate_mission_parameters(
        initial_pressure, 
        current_flow, 
        fluid_density, 
        core_heat,
        ambient_heat,
        shielding,
        0
    )
    
    if status:
        print("System Stable")
    else:
        print("Warning: Stability Low")
        
    time_step = time_step + 1

print("Simulation Complete.")
