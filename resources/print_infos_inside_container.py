
import os
import sys


def print_infos_inside_container():
    print("Container informations :")
    print(f"  - python : version   = {sys.version}")
    print(f"             location  = {sys.executable}")
    print(f"  - system : os        = {os.name}")
    print(f"             user id   = {os.getuid()}")
    print(f"             group id  = {os.getgid()}")
    print("")
    print("Interesting paths :")
    print(f" - Curent directory: {os.getcwd()}")
    for f in os.listdir(os.getcwd()):
        print(f"     - {f}")
    print("  - Content of home directory:")
    for f in os.listdir("/home"):
        print(f"     - {f}")


if __name__ == "__main__":
    print_infos_inside_container()
