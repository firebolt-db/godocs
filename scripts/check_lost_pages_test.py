from pathlib import Path
import pytest

import scripts.check_lost_pages as clp


@pytest.mark.parametrize(["root_dir"], [(x,) for x in
    (Path(__file__).parent / "test_data" / "check_lost_pages").glob("*/")
])
def test_check_lost_pages(root_dir):
    with pytest.raises(clp.LostPagesError):
        clp.main(root_dir)
