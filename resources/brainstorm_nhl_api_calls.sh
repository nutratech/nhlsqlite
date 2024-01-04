#!/bin/bash -e

set -x

cd "$(dirname "$0")"

# Get games by day (365 calls/year)
curl https://api-web.nhle.com/v1/schedule/2023-09-23 | jq | tee nhl_api_schedule_daily_league.json | wc
# output:    3891    6943  115479

# Get games by team by month (32 x 12 = 384 calls/year)
curl -X GET "https://api-web.nhle.com/v1/club-schedule/DET/month/2023-12" | jq | tee nhl_api_schedule_monthly_team.json | wc
# output:   1080    1924   28420

# Notice the output
# "preSeasonStartDate": "2022-09-24",
# "regularSeasonStartDate": "2022-10-07",
# "regularSeasonEndDate": "2023-04-14",
# "playoffEndDate": "2023-06-13",
# "numberOfGames": 11

# Get some playoff games
curl https://api-web.nhle.com/v1/schedule/2023-04-16 | jq | tee nhl_api_schedule_playoff_games-1st_round.json
curl https://api-web.nhle.com/v1/schedule/2023-04-30 | jq | tee nhl_api_schedule_playoff_games-2nd_round.json
curl https://api-web.nhle.com/v1/schedule/2023-05-16 | jq | tee nhl_api_schedule_playoff_games-stanley_cup_final.json
curl https://api-web.nhle.com/v1/schedule/2023-05-30 | jq | tee nhl_api_schedule_playoff_games-conference_finals.json
