from enum import Enum


class PlayResult(str, Enum):
    KICKOFF = "kickoff"
    RUSH = "rush"
    PASS_RECEPTION = "pass-reception"
    PASS_INCOMPLETION = "pass-incompletion"
    PASS_INTERCEPTION_RETURN = "pass-interception-return"
    PUNT = "punt"
    SACK = "sack"
    PENALTY = "penalty"
    FUMBLE_RECOVERY_OPPONENT = "fumble-recovery-opponent"
    FUMBLE_RECOVERY_OWN = "fumble-recovery-own"
    OFFICIAL_TIMEOUT = "official-timeout"
    TIMEOUT = "timeout"
    FIELD_GOAL_GOOD = "field-goal-good"
    FIELD_GOAL_MISSED = "field-goal-missed"
    END_PERIOD = "end-period"
    END_OF_HALF = "end-of-half"
    END_OF_GAME = "end-of-game"
    TWO_MINUTE_WARNING = "two-minute-warning"
    RUSHING_TOUCHDOWN = "rushing-touchdown"
    PASSING_TOUCHDOWN = "passing-touchdown"
    OTHER = "other"


class DriveResult(str, Enum):
    PUNT = "punt"
    FUMBLE = "fumble"
    FIELD_GOAL_GOOD = "field-goal-good"
    FIELD_GOAL_MISSED = "field-goal-missed"
    TOUCHDOWN = "touchdown"
    TOUCHDOWN_EXTRA_POINT = "touchdown-extra-point"
    TOUCHDOWN_TWO_POINT_CONVERSION = "touchdown-two-point-conversion"
    SAFETY = "safety"
    OTHER = "other"