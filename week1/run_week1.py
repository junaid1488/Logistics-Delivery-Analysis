import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent / "src"
sys.path.insert(0, str(SRC))

from week1_strategy import main

if __name__ == "__main__":
    main()
