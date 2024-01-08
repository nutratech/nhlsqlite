#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:10:22 2024

@author: shane
"""

import requests
import json


class ApiClient:
    """Base class for API client to NHL API"""
    def __init__(self):
        self.url = "https://api-web.nhle.com/v1"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
        }

    def get(self, endpoint: str, params: dict = None) -> dict:
        """GET request to NHL API"""
        response = requests.get(
            f"{self.url}/{endpoint}", headers=self.headers, params=params
        )
        return dict(json.loads(response.text))

    def get_seasons(self) -> dict:
        """Get all seasons"""
        return self.get("seasons")

    def get_teams(self) -> dict:
        """Get all teams"""
        return self.get("teams")

    def get_team(self, team_id: int) -> dict:
        """Get team by ID"""
        return self.get(f"teams/{team_id}")

    def get_team_roster(self, team_id: int) -> dict:
        """Get team roster by ID"""
        return self.get(f"teams/{team_id}/roster")

    def get_team_stats(self, team_id: int) -> dict:
        """Get team stats by ID"""
        return self.get(f"teams/{team_id}/stats")

    def get_team_schedule(self, team_id: int) -> dict:
        """Get team schedule by ID"""
        return self.get(f"teams/{team_id}/schedule")

    def get_team_schedule_next(self, team_id: int) -> dict:
        """Get team next game by ID"""
        return self.get(f"teams/{team_id}/schedule?expand=schedule.next")

    def get_team_schedule_previous(self, team_id: int) -> dict:
        """Get team previous game by ID"""
        return self.get(f"teams/{team_id}/schedule?expand=schedule.previous")

    def get_team_schedule_today(self, team_id: int) -> dict:
        """Get team today game by ID"""
        return self.get(f"teams/{team_id}/schedule?expand=schedule.today")

    def get_team_schedule_season(self, team_id: int, season: str) -> dict:
        """Get team schedule by ID and season"""
        return self.get(f"teams/{team_id}/schedule?season={season}")

    def get_team_schedule_season_next(self, team_id: int, season: str) -> dict:
        """Get team next game by ID and season"""
        return self.get(
            f"teams/{team_id}/schedule?season={season}&expand=schedule.next"
        )

    def get_team_schedule_season_previous(self, team_id: int, season: str) -> dict:
        """Get team previous game by ID and season"""
        return self.get(
            f"teams/{team_id}/schedule?season={season}&expand=schedule.previous"
        )

    def get_team_schedule_season_today(self, team_id: int, season: str) -> dict:
        """Get team today game by ID and season"""
        return self.get(
            f"teams/{team_id}/schedule?season={season}&expand=schedule.today"
        )

    def get_team_stats_season(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}")

    def get_team_stats_season_playoffs(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.playoffs"
        )

    def get_team_stats_season_regular(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regular"
        )

    def get_team_stats_season_regular_home(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.home"
        )

    def get_team_stats_season_regular_away(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.away"
        )

    def get_team_stats_season_regular_shootout(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.shootout"
        )

    def get_team_stats_season_regular_goalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation"
        )

    def get_team_stats_season_regular_goalsByGameSituation_home(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.home"
        )

    def get_team_stats_season_regular_goalsByGameSituation_away(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.away"
        )

    def get_team_stats_season_regular_goalsByGameSituation_shootout(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.shootout"
        )

    def get_team_stats_season_regular_goalsByGameSituation_firstPeriodGoalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.firstPeriodGoalsByGameSituation")

    def get_team_stats_season_regular_goalsByGameSituation_secondPeriodGoalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.secondPeriodGoalsByGameSituation")

    def get_team_stats_season_regular_goalsByGameSituation_thirdPeriodGoalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.thirdPeriodGoalsByGameSituation")

    def get_team_stats_season_regular_goalsByGameSituation_overtimeGoalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.overtimeGoalsByGameSituation")

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.shootoutGoalsByGameSituation")

    def get_team_stats_season_regular_goalsByGameSituation_emptyNetGoalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.emptyNetGoalsByGameSituation")

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_gameWinningGoalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.gameWinningGoalsByGameSituation")

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_gameTyingGoalsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.gameTyingGoalsByGameSituation")

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_shootoutAttemptsByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.shootoutAttemptsByGameSituation"
        )

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutMissesByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.shootoutGoalsByGameSituation.shootoutMissesByGameSituation"
        )

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutSavesByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.shootoutGoalsByGameSituation.shootoutGoalsByGameSituation.shootoutSavesByGameSituation"
        )

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutSavesByGameSituation_shootoutSavePercentageByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.shootoutGoalsByGameSituation.shootoutGoalsByGameSituation.shootoutSavesByGameSituation.shootoutSavePercentageByGameSituation"
        )

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutSavesByGameSituation_shootoutSavePercentageByGameSituation_shootoutGoalsAgainstAverageByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
            f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.shootoutGoalsByGameSituation.shootoutGoalsByGameSituation.shootoutSavesByGameSituation.shootoutSavePercentageByGameSituation.shootoutGoalsAgainstAverageByGameSituation"
        )

    def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutSavesByGameSituation_shootoutSavePercentageByGameSituation_shootoutGoalsAgainstAverageByGameSituation_shootoutShotsAgainstByGameSituation(self, team_id: int, season: str) -> dict:
        """Get team stats by ID and season"""
        return self.get(
                f"teams/{team_id}/stats?season={season}&expand=team.stats.regularSeasonStat.goalsByGameSituation.shootoutGoalsByGameSituation.shootoutGoalsByGameSituation.shootoutSavesByGameSituation.shootoutSavePercentageByGameSituation.shootoutGoalsAgainstAverageByGameSituation.shootoutShotsAgainstByGameSituation"
        )

    # def get_team_stats_season_regular_goalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutGoalsByGameSituation_shootoutSavesByGameSituation_shootoutSavePercentageByGameSituation_shootoutGoalsAgainstAve