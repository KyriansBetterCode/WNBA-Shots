import pandas as pd
from nba_api.stats.endpoints import shotchartdetail

# Fetch all shot attempts for the regular season
shot_chart = shotchartdetail.ShotChartDetail(
    league_id="10",
    team_id=0,                  # 0 queries all 30 teams
    player_id=0,                # 0 queries all active players
    season_nullable="2025",   # Change to any recent season
    season_type_all_star="Regular Season",
    context_measure_simple="FGA" # Field Goal Attempts
)

# Extract main DataFrame
df_shots = shot_chart.get_data_frames()[0]

# --- ORGANIZE DATASET BY PLAYER ID ---
# Sorts primarily by PLAYER_ID, then chronologically by GAME_ID and game event
df_shots = df_shots.sort_values(
    by=['PLAYER_ID', 'GAME_ID', 'GAME_EVENT_ID']
).reset_index(drop=True)

# Display shape and primary columns grouped by player
print("Data Shape:", df_shots.shape)
print(df_shots[['PLAYER_ID', 'PLAYER_NAME', 'TEAM_NAME', 'PERIOD', 
                'MINUTES_REMAINING', 'SECONDS_REMAINING', 'ACTION_TYPE', 
                'SHOT_TYPE', 'SHOT_DISTANCE', 'LOC_X', 'LOC_Y', 'SHOT_MADE_FLAG']].head(10))

# Save to CSV for your repository
df_shots.to_csv('wnba_shots_2025.csv', index=False)

