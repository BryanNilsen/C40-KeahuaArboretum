from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.report import build_facility_report
from helpers import print_banner

# ANIMAL ACTIONS
from actions.release_animal import release_animal
from actions.feed_animal import feed_animal

# PLANT ACTIONS
from actions.cultivate_plant import cultivate_plant


keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")


def build_menu():
    '''
    Title Menu with options list
    '''
    print_banner()
    print("MAIN MENU:")
    print("")
    # MAIN MENU
    print("1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Exit")
    print("")


def main_menu():
    """
    Show Keahua title with main menu options
    Handle user-selected menu option
    Arguments: None
    """
    build_menu()
    print("Choose a KILLER option.")
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        cultivate_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    # NOT NEEDED - if user types 6, the code will just end
    # if choice == "6":
    #     exit()

    if choice != "6":
        main_menu()


main_menu()
