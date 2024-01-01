from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    A class for holding an data path
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


