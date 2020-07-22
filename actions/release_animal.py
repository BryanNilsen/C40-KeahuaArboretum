from animals import RiverDolphin
from animals import Kikakapu
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
      # TODO animal = Gecko()
        pass

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
      # TODO animal = Goose()
        pass

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        # TODO animal = Pueo()
        pass

    if choice == "6":
        # TODO animal = Ulae()
        pass

    if choice == "7":
        # TODO animal = Ulae()
        pass

    if choice == "8":
        # TODO animal = Ulae()
        pass

    # TODO some form of option counter / track environment (river, swamp, etc.) with that specific index
    # optioncount = 0

    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river} ({len(river.animals)} animals)')

    # for index, swamp in enumerate(arboretum.swamps):
    #     print(f'{index + 1}. Swamp {swamp} ({len(swamp.animals)} animals)')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].add_animal(animal)
