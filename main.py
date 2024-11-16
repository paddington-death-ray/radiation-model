import numpy as np
import matplotlib.pyplot as plt


SEMIMAJOR_AXIS_EARTH = 	149598023000 #m
ECCENTRICITY_EARTH = 0.0167086
RADIUS_EARTH = 6371000 #m
RADIUS_SUN = 6.957 * 10**8
SOLAR_LUMINOSITY = 3.828 * 10**26 #W/m2s

EARTH_DENSITY = 5513 #kg/m3

STEFANS_CONSTANT = 5.670374419 * 10**-8
SOLAR_TEMP = 15700000


def calculate_temp(r_a, r_e, E):
    alpha = r_a + ((1-r_a)**2)*(r_e)/(1-(r_e)*(r_a))
    d = (SEMIMAJOR_AXIS_EARTH) * (1 - ECCENTRICITY_EARTH**2) / (1 - ECCENTRICITY_EARTH*np.cos(0))
    solar_constant = ((SOLAR_LUMINOSITY/(4*np.pi*d**2)))
    print(solar_constant)
    return np.sqrt(np.sqrt(((1-alpha)*solar_constant)/(2*STEFANS_CONSTANT*(2-E))))

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

    plt.plot(E_space, calculate_temp(0.255, 0.102, E_space))
    plt.show()


if __name__ == "__main__":
    main()