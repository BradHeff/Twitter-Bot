import twint
import os
import glob
import pandas as pd

if os.path.isfile("Data/tweets.csv"):
    os.unlink("Data/tweets.csv")
#Put your list of accounts in like the template
username = ["TheHackersNews", "elonmusk", "TheCyberSecHub"]


def ai(user):
    c = twint.Config()
    c.Username = user
    c.Custom["tweet"] = ["tweet"]
    c.Store_csv = True
    c.Output = f'Data/{user}.csv'
    print(user)
    twint.run.Search(c)

for users in username:
    ai(users)

extension = 'csv'
all_filenames = [i for i in glob.glob('Data/*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

combined_csv.to_csv( "Data/tweets.csv", index=True, encoding='utf-8-sig')