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
      # TODO animal = GoldDustDayGecko()
        pass

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

    # TODO some form of option counter / track environment (river, swamp, etc.) with that specific index
    # gather all viable environments
    options = []

    # can refactor this to make it DRY - args (rivers, mountains) - max num?
    for river in arboretum.rivers:
        if len(river.animals) < 12:
            options.append(river)
    for swamp in arboretum.swamps:
        if len(river.animals) < 8:
            options.append(swamp)
    for grassland in arboretum.grasslands:
        if len(river.animals) < 22:
            options.append(grassland)
    for mountain in arboretum.mountains:
        if len(river.animals) < 6:
            options.append(mountain)
    for forest in arboretum.forests:
        if len(river.animals) < 20:
            options.append(forest)
    for coastline in arboretum.coastlines:
        if len(river.animals) < 15:
            options.append(coastline)

    for index, option in enumerate(options):
        print(f'{index + 1}. {option} ({len(option.animals)} animals)')

    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river} ({len(river.animals)} animals)')

    # for index, swamp in enumerate(arboretum.swamps):
    #     print(f'{index + 1}. Swamp {swamp} ({len(swamp.animals)} animals)')

    print("Release the animal into which biome?")
    choice = input("> ")

    options[int(choice) - 1].add_animal(animal)
    # arboretum.rivers[int(choice) - 1].add_animal(animal)
