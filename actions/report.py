def build_facility_report(arboretum):

    def printEnvironment(env_type, environment):
        print(f'{env_type} - {environment} [{str(environment.id)[:8]}]')
        for animal in environment.animals:
            print(f'     {animal}')

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
