# ttyrec2asciicast

Simple script for converting ttyrec recordings into asciinema's [asciicast
format](https://github.com/asciinema/asciinema/blob/develop/doc/asciicast-v2.md).

It uses [asciicast v2
writer](https://github.com/asciinema/asciinema/blob/develop/asciinema/asciicast/v2.py)
for generating the asciicast file.

Until the supporting code from asciinema repo gets released to PyPI it has to be
pulled and added to `PYTHONPATH`:

    git clone https://github.com/asciinema/asciinema.git /path/to/asciinema
    export PYTHONPATH=/path/to/asciinema

Then download or clone this script:

    git clone https://github.com/asciinema/ttyrec2asciicast.git /path/to/ttyrec2asciicast

And run it like this:

    python3 /path/to/ttyrec2asciicast/ttyrec2asciicast.py input.ttyrec output.cast
