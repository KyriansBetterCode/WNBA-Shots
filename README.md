# WNBA Spatial Mechanics Efficiency Analysis

## 1. Research Question
How much do shot action mechanics (Movement vs Set) reduce shooting efficiency across  WNBA field-goal attempts from the same location?

## 2. Dataset Overview
- **Source:** Direct API extraction from `stats.nba.com` using `nba_api` (WNBA League ID `'10'`).
- **Scope:** WNBA Regular Season field goal attempts, sorted by `PLAYER_ID`.
- **Key Features:** `LOC_X`, `LOC_Y`, `SHOT_DISTANCE`, `ACTION_TYPE`, `SHOT_MADE_FLAG`.

## 3. AI Note
AI (Gemini) was used to assist in writing code and troubleshooting python scripts to pull data from NBA api, specifically in sorting by League ID number and the WNBA league code. It was also used to help categorize movement shots.