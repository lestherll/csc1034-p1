from . import panda

import argparse


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")

    # argument for suppressing rotation
    parser.add_argument("--no-rotate",
                        help="Suppress Rotation",
                        action="store_true")

    # argument for setting the size of the panda
    parser.add_argument("--scale",
                        type=float,
                        action="store",
                        default=0.005,
                        help="Set scale of the panda")


    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()

