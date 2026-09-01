# Data Card: WNBA Spatial Shot Dataset

## What Qualifies my Data For the Project?
### **At least 2,000 rows:** The data has 38,535 rows
### **Clear outcome:** `SHOT_MADE_FLAG` (0 or 1)
### **At least 8 useful input columns:** 23 columns (`LOC_X`, `LOC_Y`, `ACTION_TYPE`, `SHOT_DISTANCE`, `SHOT_ZONE_RANGE`, etc...)
### **A subgroup column:** `TEAM_NAME`, `SHOT_ZONE_BASIC`, `PLAYER_NAME`
### **Cause and effect question:** *Does 4th quarter fatigue cause drops in efficiency independent of shot selection?*
### **Origin:** Extracted from official `stats.nba.com` tracking via `nba_api`

## Data Card Questions
### 1. Where the Data Came From?
Extracted directly from `stats.nba.com` endpoints using the official `nba_api` Python client wrapper for WNBA League ID `'10'`

### 2. How It Was Collected?
Automated optical tracking cameras installed in WNBA arenas record 3D coordinates for players and the ball at 25 frames per second. The API converts these raw tracking frames into categorical and spatial metrics (`LOC_X`, `LOC_Y`, `ACTION_TYPE`) at the precise moment a shot attempt is released.

### 3. Who Is Missing From It?
- **Non-WNBA Athletes:** This data does not include NBA, GLeague, NCAA, high school, or international leagues
- **Off-Ball Context:** The data doesn't account for off ball actions such as playcalls, screens, passes, turnovers, fouls, off-ball player motion.)
- **Defensive Proximity Details:** This data does not include defender distance or a defenders name per shot.
- **Season Timeframes:** The data is limited to the 2025 WNBA regular season, so Preseason and Postseason statistics are *not* included
- **Filtered / Atyipical Shots:** *Excludes* full court heaves or attempts where action-type traction failed