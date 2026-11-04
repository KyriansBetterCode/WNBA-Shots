# WNBA 2025 shots: does a shot-quality model need to know who took the shot?

CMAT 651-02, Clark Atlanta University. Capstone by Ty'Kuan Smith.

## Question

A shot-quality model predicts whether a shot goes in. If a model already knows the shot (distance, location, shot type, time left), do the shooter's **height and position** improve its predictions for players it has never seen?

- Outcome: `made_flag` (1 = made, 0 = missed). Overall make rate 0.4392 (16,926 of 38,535 shots).
- The questions rest on **160 players** (179 players, 19 with no listed height or position), not 38,535 shots. Cross-validation and resampling are by `player_id`.
- Side question: off-the-dribble (by label) versus not labeled as off-the-dribble. The `action_type` label does not say whether a shot came off the dribble, so this is reported with and without plain "Jump Shot" rows and is not a causal claim.

See `DATA_CARD.md` for the data, what is missing, and the decisions made.

## Data

- Every shot of the 2025 WNBA regular season: 38,535 shots, 286 games, 13 teams, 179 players. Pulled from stats.nba.com with `nba_api` (`shotdata.py`).
- Player bios (height, weight, position) from the `nba_api` team-roster endpoint, pulled October 31, 2026 and joined by `player_id` (`buildBiosWithShots.ipynb`). Weight is missing for 17% of shots, so height is used.
- The data come from NBA.com and are used for coursework under NBA.com's Terms of Use. **The raw and clean data files are not in this repository.** A 10,000-row sample (`wnba_sample_10k.csv`, seed 651) is included.

## Files

| File | What it is |
|---|---|
| `shotdata.py` | Pulls the raw shots (`wnba_shots_2025.csv`) |
| `freeze_notebook.ipynb`, `freeze_receipt.json` | Cleans the raw file to `wnba_clean.csv` and records a receipt. The clean file is frozen and not changed. |
| `buildBiosWithShots.ipynb` | Pulls the bios (`player_bios.csv`) and joins them to the shots (`shots_with_bios.csv`) |
| `DATA_CARD.md` | Where the data came from, how it was collected, who is missing |
| `topics/` | Presentation notebooks (CLT, multivariate normal). Read `../wnba_clean.csv`. |
| `labs/` | Lab notebooks |
| `notebooks/` | Capstone notebooks |
| `archive/` | Earlier work on the first question (moving versus set shots) |

## How to reproduce

1. Create the environment and install `requirements.txt`.
2. Run `shotdata.py` to pull the shots.
3. Run `freeze_notebook.ipynb` to write `wnba_clean.csv`.
4. Run `buildBiosWithShots.ipynb` to pull the bios and write `shots_with_bios.csv`.
5. Run the notebooks in `notebooks/` and `topics/` with Restart & Run All.

Seed 651 everywhere.

## AI disclosure

- **Gemini.** Helped with my code and with sorting movement shots from the `action_type` text. I chose the rule: labels with Driving, Pullup/Pull-Up or Step Back are "off-the-dribble (by label)"; everything else is "not labeled as off-the-dribble".
- **Claude (Anthropic).** Helped write the bios scripts, the data card and the proposal edits. I ran the scripts and checked the row count after the join. I found the 6,566 missing weights myself and chose to use height.
- The question, the decision it helps with, and the claims I make are my own.