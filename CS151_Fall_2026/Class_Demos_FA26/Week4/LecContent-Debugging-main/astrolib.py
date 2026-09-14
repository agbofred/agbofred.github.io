# astrolib.py

from rich.console import Console
from time import sleep

con = Console()

def calculate_stability_index(pressure, flow_rate, density):
    """
    Calculates the engine stability index.

    Inputs: 
        pressure (int/float), 
        flow_rate (int/float), 
        density (int/float)
    Returns: 
        float
    """
    return (pressure / flow_rate) * density

def run_sensor_sweep(duration):
    """
    Simulates a sensor scan over a set duration.

    Inputs: 
        duration (int) - A number of seconds.
    Returns: 
        bool - True if sweep completes without interference.
    """
    with con.status("[bold green]Sweeping..."):
        for _ in range(duration):
            sleep(1/10)

    return True

def validate_mission_parameters(press_val, flow_val, den_val, core_temp, amb_temp, shield_fact, sweep_time):
    """
    High-level check of physics and sensors.

    Inputs: 
        press_val, flow_val, den_val (numbers) - Physics parameters
        core_temp, amb_temp, shield_fact (numbers) - Thermal params.
        sweep_time (int) - Time to sweep for
    Returns: 
        bool - True if all systems are a go
    """
    stability = calculate_stability_index(press_val, flow_val, den_val)
    is_thermal_safe = check_thermal_threshold(core_temp, amb_temp, shield_fact)
    sweep_confirmed = run_sensor_sweep(sweep_time)
   
    if sweep_time > 0:
        run_sensor_sweep(sweep_time)
    if stability > 1.5 and is_thermal_safe:
        return True
    return False


def check_thermal_threshold(core_temp, ambient_temp, shield_factor):
    """
    Evaluates if the heat shield can handle the current core temperature.
    
    Inputs:
        core_temp (int/float): The internal temperature.
        ambient_temp (int/float): The outside temperature.
        shield_factor (int/float): Heat resistance (1 to 10).
    Returns:
        bool: True if safe, False if critical.
    """
    effective_heat = abs(core_temp - ambient_temp)
    # Logic error if shield_factor is 0
    safety_margin = effective_heat / shield_factor
    return safety_margin < 500
