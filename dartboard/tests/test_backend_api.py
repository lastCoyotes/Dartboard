import pytest
import os
from pathlib import Path
from backend.django_setup import setup as setup_api
from backend.models import *
from backend.dartboard_api import *
import django


def setup():
    setup_api()


def teardown():
    database_loc = str(Path(__file__).resolve().parent.parent) + "/db.sqlite3"

    if os.path.exists(database_loc):
        os.remove(database_loc)


def test_create_player():
    setup()

    player = create_player("unittest", "player")

    name_player = get_players_by_name("unittest", "player")
    assert name_player.first_name == "unittest"
    assert name_player.last_name == "player"

    id_player = get_players_by_id(player.id)
    assert id_player.first_name == "unittest"
    assert id_player.last_name == "player"

    teardown()
