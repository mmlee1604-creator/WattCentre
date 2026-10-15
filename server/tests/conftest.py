import pytest

from .support import EXAMPLE_APPLIANCES


@pytest.fixture(autouse=True)
def _example_household(monkeypatch):
    """Every server test runs against the example household.

    The repository root's appliances.toml is the list of whoever is running
    WattCentre, edited by hand, so a test that read it would pass or fail
    depending on what somebody owns. create_app() and settings() take the
    list from WATTCENTRE_APPLIANCES before that file, so pointing it here
    keeps the suite independent of it. A test about the default path
    removes this variable itself.
    """
    monkeypatch.setenv("WATTCENTRE_APPLIANCES", str(EXAMPLE_APPLIANCES))
    monkeypatch.delenv("WATTCENTRE_TRAINED_CLASSES", raising=False)


@pytest.fixture
def store(tmp_path):
    from wattcentre_server.store import Store

    s = Store()
    s.open(tmp_path / "test.db")
    yield s
    s.close()
