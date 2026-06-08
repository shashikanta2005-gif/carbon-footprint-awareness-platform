import pytest
from app import calculate_emissions

def test_walking_and_zero_inputs():
    """Verifies that completely zeroed inputs produce a zero metric score."""
    metrics = calculate_emissions(
        transport_type="Walking/Bicycle",
        distance=0.0,
        energy_mode="Daily Estimate (kWh)",
        energy_input=0.0,
        diet_type="Vegan"
    )
    # Total equals just the base baseline diet calculation factor
    assert metrics['transport'] == 0.0
    assert metrics['energy'] == 0.0
    assert metrics['total'] == metrics['diet']

def test_monthly_energy_scaling():
    """Asserts that monthly energy options scale correctly down by a factor of 30."""
    daily_metrics = calculate_emissions(
        transport_type="Walking/Bicycle",
        distance=0.0,
        energy_mode="Daily Estimate (kWh)",
        energy_input=10.0,
        diet_type="Vegan"
    )
    
    monthly_metrics = calculate_emissions(
        transport_type="Walking/Bicycle",
        distance=0.0,
        energy_mode="Monthly Utility Bill (kWh)",
        energy_input=300.0, # 300 / 30 = 10 daily equivalent
        diet_type="Vegan"
    )
    
    assert daily_metrics['energy'] == monthly_metrics['energy']
    assert daily_metrics['total'] == monthly_metrics['total']

def test_high_emission_car_calculations():
    """Ensures logic handles calculation matrices accurately for high emission profiles."""
    metrics = calculate_emissions(
        transport_type="Petrol/Diesel Car",
        distance=50.0, # 50 * 0.20 = 10.0 kg
        energy_mode="Daily Estimate (kWh)",
        energy_input=5.0, # 5 * 0.82 = 4.10 kg
        diet_type="Heavy Meat Consumer" # 7.20 kg
    )
    
    assert metrics['transport'] == 10.0
    assert metrics['energy'] == 4.1
    assert metrics['diet'] == 7.2
    assert metrics['total'] == 21.3