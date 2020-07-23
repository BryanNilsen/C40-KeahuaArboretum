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

    choice = input("Choose the animal type you want to feed >> ")

    # get all the animals based on the class selected
    animals_by_selected_class = []

    biomes = [arboretum.rivers, arboretum.swamps, arboretum.grasslands,
              arboretum.mountains, arboretum.coastlines, arboretum.forests]

    def find_all_animals_by_class(animalclass):
        for biome in biomes:
            for environment in biome:
                for animal in environment.animals:
                    if isinstance(animal, animalclass):
                        animals_by_selected_class.append(animal)

    if choice == "1":
        find_all_animals_by_class(GoldDustDayGecko)

    if choice == "2":
        find_all_animals_by_class(RiverDolphin)

    if choice == "3":
        find_all_animals_by_class(NeneGoose)

    if choice == "4":
        find_all_animals_by_class(Kikakapu)

    if choice == "5":
        find_all_animals_by_class(Pueo)

    if choice == "6":
        find_all_animals_by_class(Ulae)

    if choice == "7":
        find_all_animals_by_class(Opeapea)

    if choice == "8":
        find_all_animals_by_class(HawaiianHappyFaceSpider)

    if choice == "9":
        find_all_animals_by_class(RainbowTrout)

    # GENERATE NUMBERED LIST OF AVAILABLE ANIMALS TO FEED
    for index, animal in enumerate(animals_by_selected_class):
        print(f'{index + 1}. {animal}')

    # PROMPT USER TO SELECT ANIMAL
    print(f"Select an animal to feed >> ")
    choice = input(">> ")

    # STORE SELECTED ANIMAL
    selected_animal = animals_by_selected_class[int(choice) - 1]

    # convert animal prey set to list
    options = list(selected_animal.prey)

    # GENERATE NUMBERED LIST OF FEED OPTIONS
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
