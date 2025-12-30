"""
CSV Streamer - Stream CSV files as Arrow tables.
"""

from .streamer import (
    ColumnError,
    DecodeError,
    NotCSVError,
    ParseError,
    SchemaError,
    StreamerError,
    stream_csv,
)

__all__ = [
    "stream_csv",
    "StreamerError",
    "NotCSVError",
    "DecodeError",
    "ParseError",
    "SchemaError",
    "ColumnError",
]
