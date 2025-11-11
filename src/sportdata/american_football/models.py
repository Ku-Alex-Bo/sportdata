from pydantic import BaseModel, Field, validator
from sportdata.american_football.enums import PlayResult, Dict
from typing import List
from datetime import datetime, time


class Stats(BaseModel):
    passing: None | Dict[str, "PassingStats"] = None
    rushing: None | Dict[str, "RushingStats"] = None
    receiving: None | Dict[str, "ReceivingStats"] = None


class PlayerStats(BaseModel):
    """
    Base class for player stats
    """
  
    yards: int = 0


class PassingStats(PlayerStats):
    """
    Quarterback stats
    """    
    
    attempts: int
    complete: int
    touchdowns: int


class RushingStats(PlayerStats):
    """
    Rusher stats
    """

    attempts: int
    touchdowns: int

class ReceivingStats(PlayerStats):
    """
    Receiver stats
    """

    attempts: int
    complete: int


class Team(BaseModel):
    """
    Base Team Model
    """
    id: str
    title: str


class Player(BaseModel):
    id: str
    name: str
    jersey: str
    position: str
    team: None | Team
    stats: None | PlayerStats


class Participants(BaseModel):
    passer: None | str
    rusher: None | str
    fumbler: None | str
    receiver: None | str
    tackler: None | str


class Clock(BaseModel):
    gameclock: time | None = Field(None, description="Game time in format MM:SS")
    wallclock: datetime | None = Field(None, description="Real UTC timestamp")
    period: int | None = Field(None, description="Period number (1–5)")

    @validator("gameclock", pre=True)
    def validate_gameclock(cls, v):
        """Parses 'MM:SS' or datetime.time to time instance with validation."""
        if v is None:
            return None

        if isinstance(v, time):
            minutes = v.minute
            seconds = v.second

        elif isinstance(v, str):
            try:
                minutes, seconds = map(int, v.split(":"))
            except ValueError:
                raise ValueError("Game clock must be in 'MM:SS' format, e.g. '14:23'")
        else:
            raise TypeError("Game clock must be str ('MM:SS') or datetime.time")

        # Time quarter validate — 15:00 maximum, 0:00 minimum
        if not (0 <= minutes <= 15):
            raise ValueError(f"Invalid game clock minutes: {minutes} (expected 0–15)")
        if not (0 <= seconds < 60):
            raise ValueError(f"Invalid game clock seconds: {seconds} (expected 0–59)")

        return time(minute=minutes, second=seconds)

    @validator("wallclock", pre=True)
    def validate_wallclock(cls, v):
        """Parses ISO 8601 timestamp '2025-11-09T14:37:06Z'."""
        if isinstance(v, str):
            return datetime.fromisoformat(v.replace("Z", "+00:00"))
        return v


class Play(BaseModel):
    number: int
    drive_number: int
    period: int
    clock: Clock
    result: PlayResult
    text: str
    shortText: str
    yards: int
    participants: Participants


class Game(BaseModel):
    players: Dict[str, List[Player]]
    stats: Stats
    timeline: List[Play]

    def add_play(self, play: Play) -> None:
        self.pbp.append(play)
