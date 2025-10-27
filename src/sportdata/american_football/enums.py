from enum import Enum


class DriveResult(str, Enum):
    PUNT = "punt"


class PlayType(str, Enum):
    KICKOFF = "kickoff"
    RUSH = "rush"
    PASS_RECEPTION = "pass-reception"
    PASS_INCOMPLETION = "pass-incompletion"
    PUNT = "punt"