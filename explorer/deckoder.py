from lor_deckcodes import LoRDeck
from postgres import Postgres
import pandas as pd
import sys
from scipy.stats import hypergeom

# Decoding
deck = LoRDeck.from_deckcode(sys.argv[1])

# list all cards with card format 3:01SI001
print(list(deck))


def sql_output_as_dataframe(output) -> list:
    return [
        pd.DataFrame(result[0], columns=[x[0] for x in result[1]]) for result in output
    ]


with Postgres("dev/guillaumelegoy") as conn:
    deck_info = []
    card_codes = []
    card_count = {}

    for card in list(deck):
        card_codes.append(card[-7:])
        card_count[card[-7:]] = card[:1]

    card_count = pd.DataFrame.from_dict(card_count, orient="index").reset_index()

    card_info = conn.execute_query(
        f"SELECT code, card_name, region, cost, attack, health, rarity, main_type, subtype, supertype, keywords "
        f"FROM legendofruneterra_explorer.cards WHERE code IN %(card_codes)s",
        parameters={"card_codes": tuple(card_codes)},
    )

    deck_info = pd.DataFrame(
        card_info,
        columns=[
            "card_code",
            "card_name",
            "region",
            "cost",
            "attack",
            "health",
            "rarity",
            "main_type",
            "subtype",
            "supertype",
            "keywords",
        ],
    )

    deck_info = (
        pd.merge(
            deck_info, card_count, how="left", left_on="card_code", right_on="index",
        )
        .drop("index", axis=1)
        .rename(columns={0: "card_count"})
    )

    deck_info["mulligan_probability"] = hypergeom(
        40, deck_info["card_count"].astype(int), 10
    ).pmf(1)

    print(deck_info)
