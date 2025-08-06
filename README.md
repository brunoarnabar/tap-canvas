# tap-canvas

`tap-canvas` is a Singer tap for canvas.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

- [ ] `Developer TODO:` Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

```bash
pipx install tap-canvas
```

## Configuration

### Accepted Config Options

- [ ] `Developer TODO:` Provide a list of config options accepted by the tap.

- `record_limit`: Optional. Maximum number of records to return per stream when syncing.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-canvas --about
```

### Source Authentication and Authorization

- [ ] `Developer TODO:` If your tap requires special access on the source system, or any special authentication requirements, provide those here.

## Usage

You can easily run `tap-canvas` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-canvas --version
tap-canvas --help
tap-canvas --config CONFIG --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_canvas/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-canvas` CLI interface directly using `poetry run`:

```bash
poetry run tap-canvas --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-canvas
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-canvas --version
# OR run a test `elt` pipeline:
meltano elt tap-canvas target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.


----

In a python enviorment
- run 
  - poetry install
  - poetry lock
  - poetry version patch

to create the dist
- run
  - twine upload dist/*

For the package:
- run
  - rm -rf dist
    - or Remove-Item -Recurse -Force dist
  - poetry version patch
  - poetry build
  - poetry run twine upload dist/*

you should also run
  - poetry install
to install the package in the current environment.

Then run 
- pip install -e .
to install the package in editable mode.
---

to push up to gitlab and github:
- using source control in vscode
  - add the files
  - commit the files
  - push the files
- in the terminal
  - git push github HEAD:main

