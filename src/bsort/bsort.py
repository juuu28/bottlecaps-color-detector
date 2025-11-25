#!/usr/bin/env python3
import argparse
import sys
import yaml
from infer import infer_image
from typing import Dict


def load_config(config_path: str) -> Dict:
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    return cfg


def main():
    parser = argparse.ArgumentParser(
        description="bsort: Run inference for Bottle Cap Detection"
    )
    subparsers = parser.add_subparsers(dest="command")

    # --- infer subcommand ---
    infer_parser = subparsers.add_parser("infer", help="Run inference on an image")
    infer_parser.add_argument("--config", required=True, help="Path to YAML config")
    infer_parser.add_argument("--image", required=True, help="Path to input image")

    args = parser.parse_args()

    if args.command == "infer":
        cfg = load_config(args.config)
        infer_image(cfg, args.image)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
