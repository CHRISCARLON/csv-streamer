import logging

from src import stream_csv

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)

FILE = "TEST_URL"
MAX_BYTES = 10 * 1024 * 1024  # 10MB


def main():
    total_rows = 0
    total_bytes = 0
    batch_count = 0

    for table in stream_csv(FILE, batch_size=10000):
        batch_count += 1
        total_rows += table.num_rows
        total_bytes += table.nbytes

        if total_bytes >= MAX_BYTES:
            break


if __name__ == "__main__":
    main()
