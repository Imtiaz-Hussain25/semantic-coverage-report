# Semantic Coverage Report

Calculate per-class pixel coverage from segmentation label maps.

## What this project does

This is an original command-line utility for analyzing or presenting computer vision outputs. It does not include pretrained weights, training code, or copied research implementations.

## Input and output

Input example: `{"0":"background","1":"road"}`

Run: `python main.py labels.png classes.json report.csv`

See `python main.py --help` for positional arguments. Output is written to the requested file, except the neighbor search, which prints ranked results.

## Related tools

MMSegmentation or any model exporting integer-label PNG masks. This project is independent of those implementations and consumes their exported results where applicable.

## Requirements

Python 3.10 or newer. Install Pillow with `pip install -r requirements.txt`.

## Limitations

Requires Pillow. The PNG must store class IDs, not a colorized preview. Model inference is not locally tested. The utility has been checked for syntax only; Pillow-dependent execution is not locally tested.


## Why it is useful

Semantic segmentation produces a class ID at each pixel. This tool turns that label map into a table of class counts and percentages, useful for comparing scene composition.

## Data contract

Input is a single-channel integer PNG mask and a JSON object mapping class IDs to names. Output CSV includes class ID, class name, pixel count, and percent of image area.

## Reproduce the example

```bash
python main.py examples/labels.png examples/classes.json examples/report.csv
```

The command reads the included sample input. Generated reports in `examples/` can be removed when finished.

## Interpretation

A colorized preview is not a valid input. Unknown IDs are reported as `unknown`. Coverage is not an accuracy metric.

## License

MIT. See `LICENSE`.


