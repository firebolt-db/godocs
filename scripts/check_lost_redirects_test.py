from pathlib import Path
import pytest

import scripts.check_lost_redirects as clp


@pytest.mark.parametrize(["root_dir"], [(x,) for x in
    (Path(__file__).parent / "test_data" / "check_lost_redirects").glob("*/")
])
def test_check_lost_redirects(root_dir):
    with pytest.raises(clp.LostRedirectsError):
        clp.main(root_dir, False)
