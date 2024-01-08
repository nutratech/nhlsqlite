-- Copyright 2023 Shane Jaroch
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--     http://www.apache.org/licenses/LICENSE-2.0
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
--
CREATE TABLE license (
  license text
);

CREATE TABLE `version` (
  id integer PRIMARY KEY AUTOINCREMENT,
  `version` text NOT NULL UNIQUE,
  created date NOT NULL,
  type text,
  notes text
);

--
--------------------------------
-- Tables: season, team
--------------------------------
-- TODO: partial_season bool
CREATE TABLE season (
  season int PRIMARY KEY, -- both years, i.e. 20172018
  year_start int,
  year_end int
);

CREATE TABLE team (
  abbrev text PRIMARY KEY, -- tri_code
  name text NOT NULL UNIQUE
);

--
--------------------------------
-- Tables: game_type, game
--------------------------------
CREATE TABLE game_type (
  type text PRIMARY KEY, -- R=Regular season, P=Playoff
  description text NOT NULL UNIQUE
);

CREATE TABLE game_outcome (
  outcome text PRIMARY KEY -- Regulation
);

CREATE TABLE game (
  game_id integer PRIMARY KEY, -- the NHL's ID (e.g. 2015020663)
  season int NOT NULL, -- NHL's season ID (e.g. 20232024)
  date_time datetime NOT NULL,
  game_type text NOT NULL, -- R=Regular season, P=Playoff
  team_abbrev_away text NOT NULL,
  team_abbrev_home text NOT NULL,
  goals_away int,
  goals_home int,
  outcome text,
  venue text NOT NULL,
  FOREIGN KEY (season) REFERENCES season (season) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (game_type) REFERENCES game_type (type) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (team_abbrev_away) REFERENCES team (abbrev) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (team_abbrev_home) REFERENCES team (abbrev) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (outcome) REFERENCES game_outcome (outcome) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Create indexes on abbreviation and outcome columns
BEGIN TRANSACTION;
CREATE INDEX game_index_team_away ON game (team_abbrev_away);
CREATE INDEX game_index_team_home ON game (team_abbrev_home);
CREATE INDEX game_index_outcome ON game (outcome);
COMMIT;
