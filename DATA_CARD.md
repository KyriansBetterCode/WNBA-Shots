# Data Card: WNBA Spatial Shot Dataset

### 1. Where the Data Came From
Extracted directly from `stats.nba.com` endpoints using the official `nba_api` Python client wrapper for WNBA League ID `'10'`

### 2. How It Was Collected
Automated optical tracking cameras installed in WNBA arenas record 3D coordinates for players and the ball at 25 frames per second. The API converts these raw tracking frames into categorical and spatial metrics (`LOC_X`, `LOC_Y`, `ACTION_TYPE`) at the precise moment a shot attempt is released.

### 3. Who Is Missing From It 
- **Non-WNBA Athletes**
- **Off-Court Context**
- **Defensive Proximity Details** 
- **Season Timeframes** 