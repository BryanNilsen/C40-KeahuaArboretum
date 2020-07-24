from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Mountain
from environments import Forest
from helpers import print_banner


def annex_habitat(arboretum):
    print_banner()
    # MENU OPTIONS
    print("HABITAT OPTIONS:")
    print("")
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")
    print("")
    choice = input("Choose habitat to annex >> ")
    print("")

    if choice == "1":
        name = input("Enter a name for your River >> ")
        river = River(name)
        arboretum.rivers.append(river)
    if choice == "2":
        name = input("Enter a name for your Swamp >> ")
        swamp = Swamp(name)
        arboretum.swamps.append(swamp)
    if choice == "3":
        name = input("Enter a name for your Coastline >> ")
        coastline = Coastline(name)
        arboretum.coastlines.append(coastline)
    if choice == "4":
        name = input("Enter a name for your Grassland >> ")
        grassland = Grassland(name)
        arboretum.grasslands.append(grassland)
    if choice == "5":
        name = input("Enter a name for your Mountain >> ")
        mountain = Mountain(name)
        arboretum.mountains.append(mountain)
    if choice == "6":
        name = input("Enter a name for your Forest >> ")
        forest = Forest(name)
        arboretum.forests.append(forest)
