from lor_deckcodes import LoRDeck
from postgres import Postgres
import pandas as pd
import sys

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

    for card in list(deck):
        card_codes.append(card[-7:])

    card_info = conn.execute_query(
        f"SELECT card_name, region, cost, attack, health, rarity, main_type, subtype, supertype, keywords "
        f"FROM legendofruneterra_explorer.cards WHERE code IN %(card_codes)s",
        parameters={"card_codes": tuple(card_codes)},
    )

    print(
        pd.DataFrame(
            card_info,
            columns=[
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
    )
