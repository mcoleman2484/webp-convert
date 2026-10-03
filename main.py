"""WebP Convert — Convert WebP images to PNG or JPEG, or the other way around."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='webp_convert',
        description='Convert WebP images to PNG or JPEG, or the other way around.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('WebP Convert')
    print('WebP in, a format your editor likes out.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
