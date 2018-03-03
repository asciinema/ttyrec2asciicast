import sys
import asciinema.asciicast.v2 as v2

## ttyrec format parsing is implemented according to this spec:
## https://nethackwiki.com/wiki/Ttyrec


with open(sys.argv[1], mode='rb') as ttyrec:
    with v2.writer(sys.argv[2], width=80, height=24) as w:
        base_sec = None
        base_usec = None

        while True:
            header = ttyrec.read(12)

            if not header:
                break

            sec = int.from_bytes(header[0:4], byteorder='little')
            usec = int.from_bytes(header[4:8], byteorder='little')
            size = int.from_bytes(header[8:-1], byteorder='little')

            if not base_sec:
                base_sec = sec
                base_usec = usec

            sec = sec - base_sec
            usec = usec - base_usec
            ts = sec + (usec / 1000000)
            data = ttyrec.read(size)

            w.write_stdout(ts, data)
