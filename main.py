import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


SEMIMAJOR_AXIS_EARTH = 	149598023000 #m
ECCENTRICITY_EARTH = 0.0167086
RADIUS_EARTH = 6371000 #m
RADIUS_SUN = 6.957 * 10**8
SOLAR_LUMINOSITY = 3.828 * 10**26 #W/m2s

EARTH_DENSITY = 5513 #kg/m3

STEFANS_CONSTANT = 5.670374419 * 10**-8
SOLAR_TEMP = 15700000

BASE_CO2 = 422
PREINDUSTRIAL_CO2 = 278

k_prop = 8.95656 * 10**-3


def calculate_temp(r_a, r_e, E, delta_f):
    alpha = r_a + ((1-r_a)**2)*(r_e)/(1-(r_e)*(r_a))
    d = (SEMIMAJOR_AXIS_EARTH) * (1 - ECCENTRICITY_EARTH**2) / (1 - ECCENTRICITY_EARTH*np.cos(0))
    solar_constant = ((SOLAR_LUMINOSITY/(4*np.pi*d**2)))
    return np.sqrt(np.sqrt(((1-alpha)*solar_constant + delta_f)/(2*STEFANS_CONSTANT*(2-E))))


def radioactive_forcing(ppm):
    #https://agupubs.onlinelibrary.wiley.com/doi/10.1029/98GL01908
    delta_f = 5.35 * np.log((ppm)/PREINDUSTRIAL_CO2)
    print(delta_f)
    return delta_f


def solar_intensity(theta, phi):
    phi -= np.pi 
    d = (SEMIMAJOR_AXIS_EARTH) * (1 - ECCENTRICITY_EARTH**2) / (1 - ECCENTRICITY_EARTH*np.cos(0))
    intensity = (SOLAR_LUMINOSITY * (np.sin(theta)**2 * np.cos(phi))) / (4 * np.pi * d**2)
    return max(0, intensity)


def main():
    """
    phi_space = np.linspace(-(np.pi), np.pi, 100)
    time_history = np.linspace(0,24,24*3600)

    intensity_chart = []
    for val in phi_space:
        intensity_chart.append(solar_intensity(np.pi/2, val))
    """

    E_space = np.linspace(0,1,100)


    current_e = 0.847
    past_e = 0.827
    print()
    future_e = past_e + (radioactive_forcing(550)) * k_prop

    print((radioactive_forcing(422)))

    fig, ax = plt.subplots()


    pre_industrial_climate = calculate_temp(0.255, 0.102, past_e, 0)
    temperature_baseline = calculate_temp(0.255, 0.102, current_e, 0)
    new_temperature = calculate_temp(0.255, 0.102, future_e, 0)


    ax.plot(E_space*100, calculate_temp(0.255, 0.102, E_space, 0)-273, zorder=1)


    #current climate
    scatter1 = ax.scatter(past_e*100, pre_industrial_climate-273, marker="x", color="yellow", lw=2, zorder=2, label=f"1750 Climate: {pre_industrial_climate-273:.2f}°C")

    #current climate
    scatter2 = ax.scatter(current_e*100, temperature_baseline-273, marker="x", color="green", lw=2, zorder=2, label=f"2024 Climate: {temperature_baseline-273:.2f}°C")

    #2050 climate
    scatter3 = ax.scatter(future_e*100, new_temperature-273, marker="x", color="red", lw=2, zorder=2, label=f"2050 Climate: {new_temperature-273:.2f}°C")

    ax.set_xticks(np.arange(0, 110, 10))
    ax.set_yticks(np.arange(-30, 50, 10))
    ax.grid()
    ax.set_xlabel("% Infrared absorbed by atmosphere")
    ax.set_ylabel("Surface Temperature (°C)")

    ax.legend()

    ax.set_ylim([0,30])
    ax.set_xlim([50,100])

    plt.hlines(0, 0, 100, color="gray")
    plt.show()


if __name__ == "__main__":
    main()