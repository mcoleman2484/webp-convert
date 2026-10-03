![WebP Convert](assets/hero.png)

# WebP Convert

*WebP in, a format your editor likes out.*

## Overview

**WebP Convert** runs on your own PC. Convert WebP images to PNG or JPEG, or the other way around.

A saved meme or a site asset arrives as WebP. Paint will not open it.

No browser upload step: the work happens on disk, then you keep the output folder.

## What's included

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Features

- WebP to PNG or JPEG
- JPEG to WebP
- Quality setting
- Folder batch

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/mcoleman2484/webp-convert

MIT license. See `LICENSE`.
