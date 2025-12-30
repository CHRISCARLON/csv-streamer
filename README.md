# CSV Streamer

I find myself doing a lot of the same thing recently... and that thing is streaming large csv files over the network in batches. 

So I made a small python library using a few techniques that I know to stream csv files and yield them as batches of arrow tables for further processing/wrangling etc.

There's 4 paths and one entry point:

- stream_csv()

You can stream:

- Local CSVs
- Local CSVs in a zip file
- Remote CSVs
- Remote CSVs in a zip file

## Example

```python
import logging
from csv_streamer import stream_csv

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)

FILE = "https://assets.publishing.service.gov.uk/media/68c2e11b7596dbfa052bfecc/north_east.zip"
MAX_BYTES = 10 * 1024 * 1024  # 10MB


def main():
    total_rows = 0
    total_bytes = 0
    batch_count = 0

    for table in stream_csv(FILE, batch_size=10000):
        batch_count += 1
        total_rows += table.num_rows
        total_bytes += table.nbytes
        print(table)

        if total_bytes >= MAX_BYTES:
            break


if __name__ == "__main__":
    main()
```
