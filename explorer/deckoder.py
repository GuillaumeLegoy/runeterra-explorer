from lor_deckcodes import LoRDeck, CardCodeAndCount


# Decoding
deck = LoRDeck.from_deckcode('CEBQCAQDA4AQCAY6AMAQCCIUCYCACAQBAEAQEAYBAQAQGCY5GAZAMAIBAQGRKIZNFYAQCAQDAY')

# list all cards with card format 3:01SI001
print(list(deck))
