import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")

# Column selection
print(df.index.to_list())  # Pokémon names
print(df["Height"].to_string())
print(df["Weight"].to_string())
print(df[["Height","Weight"]].to_string())

# Row selection
print(df.iloc[0:11:2])

# Filtering
tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]
ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff_pokemon) 

# Lookup
pokemon = input("Enter a Pokemon name: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")

# Aggregations
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))

# Grouping
group = df.groupby("Type1")
print(group["Height"].mean())

# Drop column
poki = df.drop(columns=["Legendary"])

# Handle missing data
df = df.fillna({"Type2":"None"})
print(df.head(10).to_string())