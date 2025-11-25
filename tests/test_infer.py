import pytest
from bsort.infer import infer_image

def test_infer_function_exists():
    assert callable(infer_image)
