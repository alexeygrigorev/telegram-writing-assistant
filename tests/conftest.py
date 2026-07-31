"""Shared pytest fixtures and safety nets for the test suite."""

import os

import pytest


@pytest.fixture(autouse=True)
def guard_std_fds():
    """Fail the test that closes stdout or stderr, at the point it happens.

    `open()` accepts a file descriptor as well as a path, and it treats any
    object with `__index__` as a descriptor. `MagicMock.__index__` returns 1,
    which is stdout. So patching a path constant like `INBOX_RAW` with a bare
    `MagicMock` makes the code under test open fd 1 and close it on the way out
    of the `with` block.

    Nothing fails at that moment. The test passes, and pytest crashes much later
    with `OSError: Bad file descriptor` while writing its own summary, which
    points at pytest rather than at the test that caused it. This fixture turns
    that into a normal failure naming the guilty test.

    Patch path constants with a real directory, usually `tmp_path`, or patch
    `builtins.open`.
    """
    def identify(fd):
        """What fd currently points at, or None if it is closed."""
        try:
            st = os.fstat(fd)
        except OSError:
            return None
        return (st.st_dev, st.st_ino)

    before = {fd: identify(fd) for fd in (1, 2)}

    yield

    for fd, name in ((1, "stdout"), (2, "stderr")):
        after = identify(fd)
        if after == before[fd]:
            continue
        # Closing fd 1 does not leave it closed for long: the next open() gets
        # the lowest free descriptor, which is 1 again, now pointing elsewhere.
        # So compare identity rather than checking that the fd still exists.
        pytest.fail(
            f"This test replaced or closed {name} (fd {fd}). A MagicMock most "
            f"likely reached open() as a file descriptor. Patch the path with "
            f"tmp_path, or patch builtins.open."
        )
