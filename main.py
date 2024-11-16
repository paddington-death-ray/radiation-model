import numpy as np
import matplotlib.pyplot as plt


SEMIMAJOR_AXIS_EARTH = 227939366000 #m
ECCENTRICITY_EARTH = 0.0934
RADIUS_EARTH = 1737000 #m
SOLAR_LUMINOSITY = 3.828 * 10**26 #W/m2s

EARTH_DENSITY = 3344 #kg/m3
HEAT_CAPACITY_ROCK = 2000 #
STEFANS_CONSTANT = 5.670374419 * 10**-8 #

CRUST_DEPTH = 0.002 #m
ROTATIONAL_VELOCITY_EARTH = (2*np.pi) / (24*3600*30)

def emission_from_point(I, emissivity, T, dt):
    dT_dt = (I - emissivity*STEFANS_CONSTANT*T**4) / (EARTH_DENSITY * HEAT_CAPACITY_ROCK * CRUST_DEPTH)
    return dT_dt * dt


def solar_intensity(theta, phi):
    phi -= np.pi 
    d = (SEMIMAJOR_AXIS_EARTH) * (1 - ECCENTRICITY_EARTH**2) / (1 - ECCENTRICITY_EARTH*np.cos(0))
    intensity = (SOLAR_LUMINOSITY * (np.sin(theta)**2 * np.cos(phi))) / (4 * np.pi * d**2)
    return max(0, intensity)


def main():
    phi_space = np.linspace(-(np.pi), np.pi, 100)

    intensity_chart = []
    for val in phi_space:
        intensity_chart.append(solar_intensity(np.pi/2, val))

    temperature_history = [273+120]
    intensity_history = []
    time_history = np.linspace(0,24*365,10000)
    for minute in time_history:
        phi = ROTATIONAL_VELOCITY_EARTH * minute*3600
        intensity = solar_intensity(np.pi/2, phi)
        intensity_history.append(intensity)
        temperature = temperature_history[-1] + emission_from_point(intensity, 0.05, temperature_history[-1], 3600)
        temperature_history.append(temperature)
    temperature_history = temperature_history[:-1]
    
    plt.plot(time_history, temperature_history)
    plt.plot(time_history, intensity_history)
    plt.xticks()
    plt.xlabel("Time (hours)")
    plt.show()


if __name__ == "__main__":
    main()