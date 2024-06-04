# Dictionary comprehension = creates dictionaries using a expression
# can replace for loop and certain lambda functions

def main():
    cities_in_F = {'New York': 31, 'Atlanta': 71, 'San Diego': 73, 'San Jose;': 45}
    # dictionary: = {key: expression for (key, value) in iterables}
    cities_in_C = {key: round((values - 32) * (5 / 9)) for (key, values) in cities_in_F.items()}
    print(cities_in_C)

    weather = {'New York': "Snowing", 'Atlanta': "Sunny", 'San Diego': "Sunny", 'San Jose': "Cloudy"}
    # dictionary = {key: expression for (key, value) in iterable if conditional}
    sunny_weather = {key: values for (key, values) in weather.items() if values == "Sunny"}
    print(sunny_weather)

    cities = {'New York': 31, 'Atlanta': 71, 'San Diego': 80, 'San Jose': 45}
    # dictionary = {key: (if/else) for (key, value) in iterables}
    descent_weather = {key: ("Warm" if values >= 70 else "Cold") for (key, values) in cities.items()}
    print(descent_weather)


if __name__ == '__main__':
    main()
