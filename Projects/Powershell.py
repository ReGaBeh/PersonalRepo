import argparse
from tqdm import tqdm
from time import sleep


def loadTest():
    for x in tqdm(range(500), desc="Iterable"):
        pass


def load2():
    string = []
    try:
        for x in tqdm(range(int(args.x), int(args.y)), desc="Range"):
            sleep(0.01)
            string.append(x)
    except Exception as e:
        print(e)
    print(string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--z", help="Calls specified function", choices=["load", "load2"])
    parser.add_argument("--x", help="First parameter for load2()")
    parser.add_argument("--y", help="Second parameter for load2()")

    args = parser.parse_args()

    if args.z == "load":
        loadTest()
    elif args.z == "load2":
        load2()
