from pandas.io.ga import read_ga

read_ga(["visits"], dimensions=["date"], start_date="2012-12-12", end_date="2012-12-12", secrets="client_secrets.json", token_file_name="analytics.dat")
