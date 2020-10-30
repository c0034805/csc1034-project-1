from . import panda
import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--reverse", help="Move Camera In Reverse",
                        action = "store_true")
    parser.add_argument("--no-walk", help="Suppress Walking",
                        action="store_true")
    parser.add_argument("--scale", type=int, help="Scale Panda Size")
    parser.add_argument("--location", type=int, nargs='+', help="Set Panda's Location")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
