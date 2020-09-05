import pandas as pd
import math

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result


def fill_tourney_per_area(df):
    temp_list = []
    for i in range(len(df.index)):
        temp_list.append(df.iloc[i, 2] / df.iloc[i, 0])
    df["Tourney / Area"] = temp_list


def calc_ping_score(df):
    temp_list = []
    for i in range(len(df.index)):
        temp_list.append(1- df.iloc[i, 5])
    df["Ping Score(ms)"] = temp_list

def calc_total_score(df):
    temp_list = []
    for i in range(len(df.index)):
        # tourney/area, med entrants, PGR Players, PGR Tournaments, Ping
        temp_list.append(21.25 * df.iloc(axis=0)[i, 6] +
        21.25 * df.iloc(axis=0)[i, 5] +
        21.25 * df.iloc(axis=0)[i, 3] +
        21.25 * df.iloc(axis=0)[i, 4] +
        15 * df.iloc(axis=0)[i, 7])
    print(temp_list)
    new_index = df.index.get_level_values(level=0)
    return pd.Series(index=new_index, data=temp_list, name="Score")



def main():
    df = pd.read_excel("/Users/dentsui14/Downloads/Global Data Regions.xlsx")
    fill_tourney_per_area(df)
    new_df = normalize(df)
    calc_ping_score(new_df)
    final_list = calc_total_score(new_df)
    print(final_list.sort_values(ascending=False))
    final_list.sort_values(ascending=False).to_excel("/Users/dentsui14/Downloads/Global Region Rank.xlsx")

if __name__ == "__main__":
    main()