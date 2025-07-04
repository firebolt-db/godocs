from pathlib import Path
import pytest

import scripts.check_redirect_loops as crl


@pytest.mark.parametrize(["root_dir"], [(x,) for x in
    (Path(__file__).parent / "test_data" / "check_redirect_loops").glob("*/")
])
def test_check_redirect_loops(root_dir):
    with pytest.raises(crl.RedirectLoopsError):
        crl.main(root_dir)
