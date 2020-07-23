from animals import RiverDolphin
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import GoldDustDayGecko
# TODO import the rest of the animals here


def release_animal(arboretum):
    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = GoldDustDayGecko()

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
      # TODO animal = NeneGoose()
        pass

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        # TODO animal = Opeapea()
        pass

    if choice == "8":
        # TODO animal = HappyFaceSpider()
        pass

    # Get all biome lists
    biomes = [arboretum.rivers, arboretum.coastlines, arboretum.swamps,
              arboretum.grasslands, arboretum.mountains, arboretum.forests]

    # Create empty options list of available biome environments
    options = []

    # iterate biome lists and add available environments to options list
    for biome in biomes:
        for environment in biome:
            if len(environment.animals) < environment.animal_max:
                options.append(environment)

    # iterate options list to create menu options
    for index, option in enumerate(options):
        print(f'{index + 1}. {option} ({len(option.animals)} animals)')

    # prompt user to place animal
    print("Release the animal into which biome?")
    choice = input("> ")

    # place animal in selected biome list
    options[int(choice) - 1].add_animal(animal)
