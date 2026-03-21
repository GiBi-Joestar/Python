import pandas as pd

df = pd.read_csv("pokemon.csv",index_col="Name")

#selection by column

# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name","Height","Weight"]].to_string())


#selection by rows
# print(df.iloc[0:11:2])


# pokemon = input("Enter a Pokemon name: ")
# tall_pokemon = df[df["Height"] >= 2]
# heavy_pokemon = df[df["Weight"] > 100]

# ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
# print(ff_pokemon)

# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))

# group = df.groupby("Type1")

# print(group["Height"].mean())

poki = df.drop(columns=["Legendary"])

#Handle missing data
df = df.fillna({"Type2":"None"})
print(df.to_string)