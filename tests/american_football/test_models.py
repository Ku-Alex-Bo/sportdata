import pytest

from sportdata.american_football.models import Team, Player, Clock
from pydantic_core import ValidationError
from datetime import time, datetime


def test_team():
    #test valid data
    team = Team(id="1",title="Tigers")

    assert team.id == "1"
    assert team.title == "Tigers"

    #test invalid data
    with pytest.raises(ValidationError):
        Team(id="Tigers", title=123)


def test_player():
    #test valid data
    team = Team(id="1",title="Tigers")

    player = Player(
        id="1",
        name="Alex",
        jersey="99",
        position="Quarteback",
        team=team,
    )

    assert player.id == "1"
    assert player.name == "Alex"
    assert player.jersey == "99"
    assert player.position == "Quarteback"
    assert player.team == team

    #test invalid data
    with pytest.raises(ValidationError):
        Player(
            id="1",
            name="Alex",
            jersey="1001",
            position="Quarteback",
            team=team,
        )

def test_clock():
    #test valid data
    clock = Clock(
        gameclock="5:30", 
        wallclock=datetime(2023, 1, 1, 12, 0, 0),
        period=2,
    )

    assert clock.gameclock == time(minute=5, second=30)
    assert clock.period == 2

    #test invalid data
    with pytest.raises(ValidationError):
        Clock(
            gameclock="61:00", 
            wallclock=datetime(2023, 1, 1, 12, 0, 0),
            period=2,
        )


