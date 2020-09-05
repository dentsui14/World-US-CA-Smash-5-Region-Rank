from countryinfo import CountryInfo
import pandas as pd
from test import SmashDataInfo
import math
import xlrd
import xlwt
import openpyxl


def get_pgr_player_points(country, player_rank, pgr_player_points_df):
    if country == "United States":
        if player_rank == 0:
            return pgr_player_points_df.loc[5, "United States"]
        elif player_rank <= 5:
            return pgr_player_points_df.loc[0, "United States"]
        elif player_rank <= 10:
            return pgr_player_points_df.loc[1, "United States"]
        elif player_rank <= 20:
            return pgr_player_points_df.loc[2, "United States"]
        elif player_rank <= 30:
            return pgr_player_points_df.loc[3, "United States"]
        else:
            return pgr_player_points_df.loc[4, "United States"]
    elif country == "Japan":
        if player_rank == 0:
            return pgr_player_points_df.loc[5, "Japan"]
        elif player_rank <= 5:
            return pgr_player_points_df.loc[0, "Japan"]
        elif player_rank <= 10:
            return pgr_player_points_df.loc[1, "Japan"]
        elif player_rank <= 20:
            return pgr_player_points_df.loc[2, "Japan"]
        elif player_rank <= 30:
            return pgr_player_points_df.loc[3, "Japan"]
        else:
            return pgr_player_points_df.loc[4, "Japan"]
    else:
        if player_rank == 0:
            return pgr_player_points_df.loc[5, "Int'l"]
        elif player_rank <= 5:
            return pgr_player_points_df.loc[0, "Int'l"]
        elif player_rank <= 10:
            return pgr_player_points_df.loc[1, "Int'l"]
        elif player_rank <= 20:
            return pgr_player_points_df.loc[2, "Int'l"]
        elif player_rank <= 30:
            return pgr_player_points_df.loc[3, "Int'l"]
        else:
            return pgr_player_points_df.loc[4, "Int'l"]


class Regions:
    c_length = 181
    def __init__(self):
        self.ref = SmashDataInfo()
        self.region_df = pd.DataFrame(data={ # " Region": [None for x in range(self.c_length)],
                                            # "Iso Code": [None for x in range(self.c_length)],
                                            "Area(km^2)": [None for x in range(self.c_length)],
                                            "Ping(ms)": [None for x in range(self.c_length)],
                                            "PGR Tournament Points": [0 for x in range(self.c_length)],
                                            "PGR Player Points": [0 for x in range(self.c_length)],
                                            "Number of Locals": [0 for x in range(self.c_length)],
                                            "Median Local Entrants": [0 for x in range(self.c_length)]})
        self.region_df.index = [[None for x in range(self.c_length)], [None for x in range(self.c_length)]]
        self.region_df.index.set_names = ["Region", "Abbreviation"]




    def fill_index(self):
        str = "United States,Canada,Turkey,Sweden,Denmark,France,\
Germany,China,Singapore,Japan,Mexico,Australia,Norway,\
Brazil,South Korea,United Kingdom,Netherlands,Philippines,\
Guam,Israel,Peru,Spain,Switzerland,Costa Rica,\
Italy,Ireland,Iraq,New Zealand,Belgium,Croatia,\
United States Virgin Islands,Dominican Republic,\
Austria,Georgia,French Guiana,Christmas Island,El Salvador,\
Finland,Andorra,Gibraltar,\
Aruba,Chile,United Arab Emirates,Guyana,Thailand,Puerto Rico,\
Zimbabwe,Argentina,Venezuela,Ghana,Guatemala,Greece,\
Colombia,Hungary,Malta,Taiwan,Zambia,Portugal,Kuwait,\
Cape Verde,Honduras,Serbia,San Marino,Luxembourg,Bermuda,\
American Samoa,Comoros,Ukraine,Romania,\
French Southern and Antarctic Lands,Bangladesh,Saudi Arabia,Syria,\
Poland,Iceland,India,Armenia,British Virgin Islands,Panama,\
Hong Kong,Niger,Suriname,South Africa,\
Cayman Islands,Ecuador,Czech Republic,\
Heard Island and McDonald Islands,Uzbekistan,Vietnam,Russia,\
Afghanistan,Central African Republic,Paraguay,Nicaragua,Morocco,\
North Korea,British Indian Ocean Territory,Cuba,Uruguay,\
Belize,Jamaica,Bahamas,Senegal,Qatar,Jersey,\
Bolivia,Sudan,Belarus,Algeria,Trinidad and Tobago,Cyprus,\
Bosnia and Herzegovina,Western Sahara,Iran,Albania,Bahrain,\
Réunion,Burundi,Malaysia,Isle of Man,Cambodia,Barbados,\
Slovakia,Liechtenstein,South Georgia,\
Nigeria,Angola,Vatican City,Mongolia,South Sudan,\
Haiti,Indonesia,Oman,Lithuania,Mauritius,\
Guinea,Pakistan,Jordan,Libya,Palestine,Brunei,Grenada,\
Papua New Guinea,Lebanon,Azerbaijan,Cocos (Keeling) Islands,\
Anguilla,Sri Lanka,Somalia,Kenya,Latvia,Guadeloupe,\
Uganda,Pitcairn Islands,Bulgaria,Chad,Benin,Namibia,\
Northern Mariana Islands,Tunisia,New Caledonia,Egypt,Estonia,\
Madagascar,DR Congo,Slovenia,Montenegro,Guernsey,\
Faroe Islands,Botswana,Saint Lucia,Norfolk Island,Greenland,\
Kazakhstan,Djibouti,French Polynesia,Montserrat,\
Nepal,Myanmar,Ethiopia,Falkland Islands"  # Removed US, CA, blank and none, England, Wales, Scotland.
                                        # Need to deal with US and CA.
                                        # Territories with more significant overseas areas will be separate (contigious america, china france)

        region_list = list(str.split(","))

        iso_list = []
        for i in range(self.c_length):
            try:
                iso_list.append(CountryInfo(region_list[i]).iso(alpha=2))  # for each country try to search for iso code
            except KeyError:
                iso_list.append(None)
        self.region_df.index = [region_list, iso_list]


    def fill_area(self): # in km^2
        area_list = []
        for country in self.region_df.index.get_level_values(0):
            try:
                area_list.append(CountryInfo(country).area()) # for each country try to get the area
            except KeyError:
                area_list.append(None)

        self.region_df["Area(km^2)"] = area_list
        self.region_df.loc["United States", "Area(km^2)"] = 7663941.7  # United States
        self.region_df.loc["France", "Area(km^2)"] = 551695.0  # France
        self.region_df.loc["China", "Area(km^2)"] = 9596960.0  # China
        self.region_df.loc["US Virgin Islands", "Area(km^2)"] = 346.4  # US Virgin Islands
        self.region_df.loc["Andorra", "Area(km^2)"] = 468.0  # Andorra
        self.region_df.loc["British Virgin Islands", "Area(km^2)"] = 346.4  # British Virgin Islands
        self.region_df.loc["Bahamas", "Area(km^2)"] = 10008.8  # Bahamas
        self.region_df.loc["Vatican City", "Area(km^2)"] = .44  # Vatican City
        self.region_df.loc["Palestine", "Area(km^2)"] = 6020  # Palestine
        self.region_df.loc["Montenegro", "Area(km^2)"] = 13812  # Montenegro
        self.region_df.loc["Myanmar", "Area(km^2)"] = 676578  # Myanmar

    def fill_internet(self):
        internet_df = pd.read_excel("/Users/dentsui14/Downloads/PingSpeeds.xlsx")
        internet_df.index = internet_df["Country"]
        for country in internet_df["Country"]:
            try:
                num = internet_df.loc[country, "Ping(ms)"]  # Get the ping for each country
                self.region_df.loc[country, "Ping(ms)"] = num
            except KeyError:
                pass


    def fill_pgr_tournament(self):
        tournament_df = pd.read_excel("/Users/dentsui14/Downloads/Ultimate PGR Spring 2020 TTS.xlsx").head(69)
        for i in range(len(tournament_df.index)):
            classification = tournament_df.loc[i, "Cause"] #determine whether more points is entrants or PGR
            if classification == "Entrants":
                point_value = tournament_df.loc[i, "Pts."]
            else:
                point_value = tournament_df.loc[i, "Total"]
            print(point_value)
            if tournament_df.loc[i, "Region"] == "Int'l": # Updates score based on whichever region located within
                self.region_df.loc[(tournament_df.loc[i, "Sub-Region"], slice(None)), "PGR Tournament Points"] += point_value
            else:
                self.region_df.loc[(tournament_df.loc[i, "Region"], slice(None)), "PGR Tournament Points"] += point_value

    def fill_pgr_players(self):
        pgr_players_df = pd.read_excel("/Users/dentsui14/Downloads/PGRU v2 list.xlsx")
        pgr_player_points_df = pd.read_excel("/Users/dentsui14/Downloads/PGRU Player Points.xlsx")

        for i in range(len(pgr_players_df.index)):
            player = pgr_players_df.loc[i, "Player"]
            filt = self.ref.players_df["tag"] == player
            player_df = self.ref.players_df[filt]
            country = None
            if len(player_df.index) == 1: #if there is only one player with the name.
                country = self.ref.players_df.loc[player_df.index[0], "country"]
            else:
                print(player)
            if country is None:
                pass
            else:
                player_rank = pgr_players_df.loc[i, "Rank"]
                points = get_pgr_player_points(country, player_rank, pgr_player_points_df)
                try:
                    self.region_df.loc[(country, slice(None)), "PGR Player Points"] += points
                except KeyError:
                    if country == "US":
                        self.region_df.loc[("United States", slice(None)), "PGR Player Points"] += points
                    elif country == "CA":
                        self.region_df.loc[("Canada", slice(None)), "PGR Player Points"] += points
                    elif country == "":
                        pass
                    else:
                        raise KeyError
        # DIO, Frozen, Mr. E, Prodigy, Rivers, Ryuga, Sinji, Light, Kola
        self.region_df.loc[(("United States", slice(None)), "PGR Player Points")] += \
            7 * get_pgr_player_points("United States", 0, pgr_player_points_df) + \
            get_pgr_player_points("United States", 10, pgr_player_points_df) + \
            get_pgr_player_points("United States", 46, pgr_player_points_df)
        # Ron, Kuro, Sigma
        self.region_df.loc[(("Japan", slice(None)), "PGR Player Points")] += \
            get_pgr_player_points("Japan", 0, pgr_player_points_df) + \
            get_pgr_player_points("Japan", 18, pgr_player_points_df) + \
            get_pgr_player_points("Japan", 50, pgr_player_points_df)
        # Joker
        self.region_df.loc[(("Mexico", slice(None)), "PGR Player Points")] += \
            get_pgr_player_points("Mexico", 0, pgr_player_points_df)


    def fill_tournament_info(self):
        filt = (self.ref.all_tournament_info_df["online"] == 0) & (self.ref.all_tournament_info_df["rank"] == "")
        tournament_info_df = self.ref.all_tournament_info_df[filt]

        for country in self.region_df.index.get_level_values(1):
            if isinstance(country, str) or (country is not None and not math.isnan(country)):
                filt = tournament_info_df["country"] == country
                temp_tournament_df = tournament_info_df[filt]
                self.region_df.loc[(slice(None), country), "Number of Locals"] = len(temp_tournament_df.index)
                self.region_df.loc[(slice(None), country), "Median Local Entrants"] = temp_tournament_df["entrants"].median()
        print(self.region_df)


    def __str__(self):
        print(self.region_df)

def main():
    # h = Regions()
    # print(h.region_df.index)
    a = Regions()
    a.fill_index()
    a.fill_area()
    a.fill_internet()
    a.fill_pgr_tournament()
    a.fill_pgr_players()
    pd.set_option("display.max_rows", 181)
    a.fill_tournament_info()
    a.region_df.dropna(axis="index", inplace=True)
    a.region_df.drop(labels=["Andorra", "Bahamas", "Palestine", "Montenegro", "Myanmar"], level=0, inplace=True, )
    print(a.region_df)
    a.region_df.to_excel("/Users/dentsui14/Downloads/Global Data Regions.xlsx")

if __name__ == "__main__":
    main()
