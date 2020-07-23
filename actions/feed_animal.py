from animals import RiverDolphin
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import GoldDustDayGecko
from animals import Opeapea
from animals import NeneGoose
from animals import HawaiianHappyFaceSpider
from animals import RainbowTrout


def feed_animal(arboretum):
    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    print("9. Rainbow Trout")

    choice = input("Choose animal to feed > ")

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

    if choice == "9":
        animal = RainbowTrout()

    # convert animal prey set to list
    options = list(animal.prey)

    # iterate animal prey set to create menu options
    for index, option in enumerate(options):
        print(f'{index + 1}. {option}')

    # Handle if user has no options
    if len(options) > 0:
        # prompt user to select food for animal
        print(f"What is on the menu for the {animal} today?")
        choice = input(">> ")
        # TODO check input is a valid option
        # feed animal
        animal.feed(options[int(choice) - 1])
        input("\n\nPress any key to continue...")
    else:
        print("No food available for this animal.")
        print("Select a different animal.")
        input("\n\nPress any key to continue...")
