#!/usr/bin/env python

addresses = [
    {"type": "DE", "name": "DeepL SE", "street": "Maarweg 165",
     "city": "Cologne", "ZIP": 50825},
    {"type": "US", "name": "Linux Foundation", "street": "548 Market St",
     "city": "San Francisco", "state": "CA", "ZIP": "94104"},
    {"something": "something else"},
]

def print_address(address):
    match address:
        case {
            "type": ("DE" | "Deutschland" | "Germany"),
            "name": str(name),
            "street": str(street),
            "city": str(city),
            "ZIP": (str() | int()) as zip_code
        }:
            print(name)
            print(street)
            print(f"{zip_code} {city}")
            print("Germany")
        case {
            "type": ("US" | "USA" | "United States"),
            "name": str(name), "street": str(street),
            "city": str(city),
            "state": str(state),
            "ZIP": (str() | int()) as zip_code
        }:
            print(name)
            print(street)
            print(f"{city} {state} {zip_code}")
            print("US")
        case x:
           print(f"Unknown data format: {x}")


if __name__ == "__main__":
    for address in addresses:
        print_address(address)
        print("---")

