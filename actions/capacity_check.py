import os


def capacity_check(environment, kind, maxnum):
    # if len(river.animals) < maxnum
    if environment.kind < maxnum:
        return True
    else:
        raise AttributeError()
        os.system('clear')
        print("**** That biome is not large enough ****")
        print("****   Please choose another one    ****")
        input("\n\nPress any key to continue...")
