import sqlite3
import pandas as pd
import json
from countryinfo import CountryInfo

class SmashDataInfo:
    def __init__(self):
        # create new database
        conn = sqlite3.connect("/Users/dentsui14/Downloads/pgru_s1.db")
        conn2 = sqlite3.connect("/Users/dentsui14/Downloads/ultimate_player_database.db")

        # create Cursor to execute queries
        cur = conn.cursor()
        cur2 = conn2.cursor()

        self.players_df = pd.read_sql_query("SELECT * FROM players", conn)

        self.ranking_df = pd.read_sql_query("SELECT * FROM ranking", conn)

        self.ranking_seasons_df = pd.read_sql_query("SELECT * FROM ranking_seasons", conn)

        self.sets_df = pd.read_sql_query("SELECT * FROM sets", conn)

        self.tournament_info_df = pd.read_sql_query("SELECT * FROM tournament_info", conn)

        self.all_tournament_info_df = pd.read_sql_query("SELECT * FROM tournament_info", conn2)

def main():
    a = SmashDataInfo()
    filt = a.all_tournament_info_df["country"] == "NZ"
    print(a.all_tournament_info_df[filt])

        # hi = 0
        # for i in sets_df.index:
        #     if sets_df.loc[i, "game_data"] != "[]":
        #         print(sets_df.loc[i, "game_data"])
        #         hi += 1
        # print(hi)

        # print(players_df.iloc[22165, 9])
        # list = json.loads((players_df.iloc[22165, 9]))
        # print(type(list[0]))

        # mu_chart_df = pd.DataFrame(columns=["ultimate/bayonetta"])


if __name__ == "__main__":
    main()



