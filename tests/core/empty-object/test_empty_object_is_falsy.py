from web3._utils.empty import (
    empty,
)


def test_empty_object_is_falsy():
    assert not bool(empty)
    assert not empty
