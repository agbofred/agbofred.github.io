import astrolib
from rich import print
from rich.traceback import install
install(show_locals=True)

# --- MISSION CONTROL CONFIG ---
base_sensor_time = 100
reduction_factor = 10
p_val = 400
f_val = 25
d_val = 1.2

in_temp = 3600
out_temp = 20
shield = 9

print("[bold cyan]Initializing Deep Space Scan...[/bold cyan]")

sweep_limit = base_sensor_time / reduction_factor

print("Target sweep duration calculated at:", sweep_limit)

if sweep_limit > 5:
    print("Beginning validation...")
    
    # This call will trigger a TypeError deep in the library.
    success = astrolib.validate_mission_parameters(
        p_val, 
        f_val, 
        d_val, 
        in_temp,
        out_temp,
        shield,
        sweep_limit
    )
    
    if success:
        print("[green]Scan verified.")
    else:
        print("[red]Scan failed.")

