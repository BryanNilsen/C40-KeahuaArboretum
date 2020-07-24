from helpers import print_banner


def build_facility_report(arboretum):

    print_banner()
    print(f"KEAHUA ARBORETUM - FACILITY REPORT")
    print("----------------------------------")
    print("")

    def printEnvironment(env_type, environment):
        print(f'{env_type} - {environment} [{str(environment.id)[:8]}]')
        if len(environment.animals) > 0:
            print("  Animals:")
        for animal in environment.animals:
            print(f'     {animal}')

        if len(environment.plants) > 0:
            print("  Plants:")
        for plant in environment.plants:
            print(f'     {plant}')

    for river in arboretum.rivers:
        printEnvironment("River", river)

    for swamp in arboretum.swamps:
        printEnvironment("Swamp", swamp)

    for mountain in arboretum.mountains:
        printEnvironment("Mountain", mountain)

    for grassland in arboretum.grasslands:
        printEnvironment("Grassland", grassland)

    for coastline in arboretum.coastlines:
        printEnvironment("Coastline", coastline)

    for forest in arboretum.forests:
        printEnvironment("Forest", forest)

    input("\n\nPress any key to continue...")
