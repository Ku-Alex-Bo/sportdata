from pydantic import BaseModel, Field
from sportdata.american_football.enums import DriveResult, PlayType
from typing import List


class Boxscore(BaseModel):
    pass


class Player(BaseModel):
    pass


class Clock(BaseModel)
    displayValue: str


class Play(BaseModel):
    """
    Play parsing
    """
    number: int
    drive_number: int
    period: int
    description: str
    play_type: PlayType
    yards: int


class Drive(BaseModel):
    """
    Drive parsing
    """
    number: int
    plays: List[Play]
    period: int
    result: DriveResult

    def add_play(self, play: Play) -> None:
        plays.append(play)


class Game(BaseModel):
    players: Dict[str, List[Player]]
    boxscore: Boxscore
    pbp: List[Drive]

    def add_drive(self, drive: Drive) -> None:
        self.pbp.append(drive)
