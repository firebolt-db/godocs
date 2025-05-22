#!/usr/bin/env python
import sys
from pathlib import Path

from md_utils import split_into_blocks

if __name__ == "__main__":
    tgt = Path(sys.argv[1]).read_text()
    for b in split_into_blocks(tgt):
        print([(i, t.as_dict()) for i, t in b.tokens], repr(b.content))
