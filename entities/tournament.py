from dataclasses import dataclass
from enum import Enum
from typing import Union,Literal,Set

class TournamentStatus(Enum):
    UPCOMING: str = "upcoming"
    ONGOING: str = "ongoing"
    CLOSING: str = "closing"
    COMPLETED: str = "completed"

class MatchStatus(Enum):
    UPCOMING: str = "upcoming"
    FINISHED: str = "finished"
    CANCELED: str = "canceled"

@dataclass
class TournamentPlayer:
    player_username:str
    paid: bool

    team_id:str | None = None
    player_universal_id:str | None = None


@dataclass
class Team:
    team_id:str
    captain:TournamentPlayer
    players:Set[TournamentPlayer]

    win_count:int = 0
    lose_count:int = 0
    team_name: str | None

    def get_team_name(self) -> str:
        if self.team_name:
            return self.team_name
        else:
            return self.captain.player_username

    def get_win_rate(self) -> float:
        if self.win_count+self.lose_count == 0:
            return 0.0
        return self.win_count/(self.win_count+self.lose_count)

@dataclass
# Nested within Match
class MatchResult:
    team1:Team
    team2:Team
    match_date:str
    match_location:str
    team1_score: float
    team2_score: float

    def get_win_team(self) -> str:
        if self.team1_score > self.team2_score:
            return self.team1.get_team_name()
        elif self.team1_score < self.team2_score:
            return self.team2.get_team_name()
        else:
            return "tie"

    def get_lose_team(self) -> str:
        if self.team1_score < self.team2_score:
            return self.match.team1.get_team_name()
        elif self.team1_score > self.team2_score:
            return self.match.team2.get_team_name()
        else:
            return "tie"

@dataclass
class Match:
    match_id:str
    team1: Team
    team2: Team

    status: Literal[MatchStatus.UPCOMING, MatchStatus.FINISHED, MatchStatus.CANCELED] = "upcoming"
    match_result: MatchResult | None


@dataclass
class Tournament:
    tournament_id: str
    tournament_title:str
    tournament_description:str
    tournament_status: Literal[TournamentStatus.UPCOMING, TournamentStatus.ONGOING, TournamentStatus.CLOSING, TournamentStatus.COMPLETED] = "upcoming",
    root_admin: TournamentPlayer

    admins: Set[TournamentPlayer] = set()
    players: Set[TournamentPlayer] = set()
    teams: Set[Team] = set()
    matches: Set[Match] = set()

