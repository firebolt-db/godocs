from pathlib import Path
import pytest

import scripts.check_group_structure as cgs


@pytest.mark.parametrize(["root_dir"], [(x,) for x in
    (Path(__file__).parent / "test_data" / "check_group_structure").glob("*/")
])
def test_check_group_structure(root_dir):
    with pytest.raises(cgs.GroupStructureError):
        cgs.main(root_dir)
