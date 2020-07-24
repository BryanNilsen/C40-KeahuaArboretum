from helpers import print_banner
from plants import RainbowEucalyptus


def cultivate_plant(arboretum):
    # initial plant variable
    plant = None

    print_banner()
    print("PLANT CULTIVATING OPTIONS:")
    print("")
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    print("")
    choice = input("Choose plant to cultivate >> ")

    if choice == "1":
        # plant = MountainApple()
        pass

    if choice == "2":
        # plant = Silversword()
        pass

    if choice == "3":
        plant = RainbowEucalyptus()
        print(plant)
        input("\n\nPress enter to continue...")

    if choice == "4":
        # plant = BlueJadeVine()
        pass

    # Get all biome lists
    biomes = [arboretum.rivers, arboretum.coastlines, arboretum.swamps,
              arboretum.grasslands, arboretum.mountains, arboretum.forests]

    # Create empty options list of available biome environments
    options = []

    # iterate biome lists and add available environments to options list
    for biome in biomes:
        for environment in biome:
            if len(environment.plants) < environment.plant_max:
                options.append(environment)

    # iterate options list to create menu options
    for index, option in enumerate(options):
        print(f'{index + 1}. {option} ({len(option.plants)} plants)')

    # Handle if user has no options
    if len(options) > 0:
        # prompt user to place plant
        print("Cultivate the plant in which biome?")
        choice = input("> ")
        # TODO check input is a valid option
        if int(choice) > 0 and int(choice) <= len(options) + 1:
            # place plant in selected biome list
            options[int(choice) - 1].add_plant(plant)
        else:
            print("Invalid Entry")
            input("\n\nPress enter to continue...")
    else:
        print("No biomes available for this plant.")
        print("Select a different plant or annex a new biome.")
        input("\n\nPress enter to continue...")
