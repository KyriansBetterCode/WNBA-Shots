# Data card: WNBA 2025 shots with player bios

**One row = one field-goal attempt.** 38,535 rows × 25 columns: 22 shot columns plus three player-bio columns (`height_in`, `weight_lb`, `position`).

**Question.** Do a player's position and height help predict whether a WNBA shot is made? The outcome is `made_flag` (1 = made, 0 = missed). The overall make rate is 0.4392 (16,926 made, 21,609 missed).

## 1. Where did it come from?

- **Shots.** The 2025 WNBA regular-season shot chart from stats.nba.com, pulled with the `nba_api` Python package. Pulled on: August 31, 2026. Download it with `shotdata.py`.
- **Player bios.** Height, weight and position from the `nba_api` team roster endpoint (`CommonTeamRoster`, league_id "10", season "2025"), one roster per team. Pulled on October 31, 2026.
- **The join.** Bios are matched to shots on `player_id`, many shots to one player. The result is `shots_with_bios.csv`.
- **Rebuild.** Run `shotdata.py`, then the bios script, then `freeze_notebook.ipynb`. The clean file is written to `data/clean.csv`. It stays on my laptop and is gitignored. The repo holds the freeze notebook, the freeze receipt and a 10,000-row sample (seed 651).
- **Terms.** The data come from NBA.com and are used here for coursework under NBA.com's Terms of Use. The raw and clean files are not committed.

## 2. How was it collected?

- Each attempt is logged by the league's stats system with the player, game, period, clock, shot type and court location (`loc_x`, `loc_y`). I did not collect it myself.
- Bios are the height, weight and position listed on each team's roster at the time of the pull. I did not check them against another source.
- Height is in inches and weight is in pounds. Position is a roster label: G, F, C, or a blend (G-F, F-C, C-F, F-G). I group by the first letter into G, F and C.
- The data cover 286 games, 13 teams and 179 players, from 2025-05-16 to 2025-09-11.

## 3. Missing or mixed in?

**Bios are missing for some players.**

| Column | Players missing | Shots missing |
|---|---|---|
| `height_in` | 19 | 332 (0.9%) |
| `position` | 19 | 332 (0.9%) |
| `weight_lb` | 52 | 6,566 (17%) |

- The same 19 players have no bios at all. Some were probably off the roster on the pull date.
- 33 more players have height and position but no weight. Many are 2025 rookies, so the roster source seems to leave weight blank for them. The make rate is 0.4422 where weight is present and 0.4249 where it is missing, so the gaps are not random.

**Position groups (players).** G: 81, F: 59, C: 20, no position: 19.

**Other things to know.**
- Backcourt shots (92) and overtime shots (96) are flagged with `is_backcourt` and `is_overtime` and kept in the data.
- Columns dropped: `grid_type` and `shot_attempted_flag` (constant) and `event_type` (redundant with the outcome). Minutes and seconds became `seconds_left`.
- Only the regular season is included. No playoffs and no other seasons.
- Shots per player range from 1 to 691, with a median of 180. 36 players have fewer than 50 shots.
- **Rows are not independent.** One player takes many shots, and height and position are the same on every one of a player's shots. Resampling must be by `player_id`, not by shot.

## Who is missing from the data

- The 332 shots by the 19 players with no bios cannot be used for the question. That is 0.9% of the shots, but those players have shots in the data and no bios.
- Players with no weight (52) are mostly rookies, so any weight analysis describes established players better.
- Only the WNBA's 2025 regular season is covered. Findings do not speak for the playoffs, other seasons, college or other leagues.

## Decisions

- **Predictors.** Height and position are the main predictors. Weight is not used as a main predictor, and missing weights are not filled in with an average. Any weight analysis uses the 127 players who have it, and says so.
- **Complete cases.** Models of height and position use the shots with bios present. This drops 332 shots.
- **Seed.** 651 everywhere.
- **Unit.** `player_id` is the unit for bootstrapping and for cross-validation.