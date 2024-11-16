import numpy as np
import matplotlib.pyplot as plt


SEMIMAJOR_AXIS_EARTH = 149598023000 #m
ECCENTRICITY_EARTH = 0.0167086
RADIUS_EARTH = 6371000 #m
SOLAR_LUMINOSITY = 3.828 * 10**26

def emission_from_point(I, albedo):
    pass


def solar_intensity(theta, phi, t):
    d = (SEMIMAJOR_AXIS_EARTH) * (1 - ECCENTRICITY_EARTH**2) / (1 - ECCENTRICITY_EARTH*np.cos(0))
    intensity = (SOLAR_LUMINOSITY * (np.sin(theta)**2 * np.cos(phi))) / (4 * np.pi * d**2)

    new_array = []
    for a in intensity:
        new_array.append(max(0, a)) #if intensity is negative, it is in the dark zone. Return 0
    return new_array


def main():
    phi_space = np.linspace(-(np.pi), np.pi, 100)

    plt.plot(phi_space, solar_intensity(np.pi/2, phi_space, 0))
    plt.show()


if __name__ == "__main__":
    main()