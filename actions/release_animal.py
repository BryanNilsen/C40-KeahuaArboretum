from animals import RiverDolphin
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import GoldDustDayGecko
from animals import Opeapea
from animals import NeneGoose
from animals import HawaiianHappyFaceSpider
# from animals import RainbowTrout


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
    # print("9. Rainbow Trout")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = GoldDustDayGecko()

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
        animal = NeneGoose()

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal = Opeapea()

    if choice == "8":
        animal = HawaiianHappyFaceSpider()

    # if choice == "9":
    #     animal = RainbowTrout()

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

    # Handle if user has no options
    if len(options) > 0:
        # prompt user to place animal
        print("Release the animal into which biome?")
        choice = input("> ")
        # TODO check input is a valid option
        if int(choice) > 0 and int(choice) <= len(options) + 1:
            # place animal in selected biome list
            options[int(choice) - 1].add_animal(animal)
        else:
            print("Invalid Entry")
            input("\n\nPress any key to continue...")
    else:
        print("No biomes available for this animal.")
        print("Select a different animal or annex a new biome.")
        input("\n\nPress any key to continue...")
