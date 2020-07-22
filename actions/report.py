def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River {river} - [{str(river.id)[:8]}]')

    input("\n\nPress any key to continue...")
