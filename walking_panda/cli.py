from . import panda

import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")

    # option for suppressing rotation
    parser.add_argument("--no-rotate",
                        action="store_true",
                        help="Suppress Rotation")

    # option for allowing the program to rotate in anti-clockwise manner
    parser.add_argument("--anti-clockwise",
                        action="store_true",
                        help="Set rotation to anti-clockwise")

    # option for top view orientation
    parser.add_argument("--top-view",
                        action="store_true",
                        help="Set camera orientation to top view")

    # option for scaling the panda
    parser.add_argument("--scale",
                        type=float,
                        action="store",
                        default=1,
                        help="Scale panda size by a factor of SCALE")

    # option for setting the default size of the panda
    parser.add_argument("--size",
                        type=float,
                        action="store",
                        default=0.005,
                        help="Set the default size(0.005) of panda to SIZE")

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()

