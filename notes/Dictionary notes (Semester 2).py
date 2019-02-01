states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}  # Lines up with start of variable name in all languages, like Java and Python.

print(states["CA"])
print(states["AK"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000  # 39,500,000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000  # 21,300,000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000  # 737,000
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000  # 10,500,000
    }
}

print(nested_dictionary["GA"]["POPULATION"])
print(nested_dictionary["FL"]["NAME"])

georgia = nested_dictionary["GA"]
print(georgia)

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,  # 39,500,000
        "CITIES": [
            "Fresno",
            "San Fransisco",
            "Los Angeles"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,  # 21,300,000
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,  # 737,000
        "CITIES": [
            "Anchorage",
            "Fairbanks",
            "Juneau",
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,  # 10,500,000
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }
}

print(complex_dictionary["AK"]["CITIES"][0])
print()
print(complex_dictionary["FL"]["NAME"])
print(complex_dictionary["GA"]["CITIES"][0])
print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())
print()


for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)


# This is what makes it look pretty
print()
for state, info in complex_dictionary.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 20)
    print("=" * 20)


# Other Notes
states['AR'] = "Arizona?"  # It isn't Arizona

states['AR'] = "Arkansas"  # Fixed it.
print(states['AR'])
