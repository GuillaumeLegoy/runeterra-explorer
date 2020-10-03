<script>
  import Search from "./Search.svelte";
  import Output from "./Output.svelte";
  import DeckEncoder from "runeterra";
</script>

<body>
  <div class="container">
    <div id="searchWrapper">
      <Search />
    </div>
    <ul id="CardsList" />
  </div>
  <div id="myData" />
  <script>
    const CardsList = document.getElementById("CardsList");
    const searchBar = document.getElementById("searchBar");

    let hpCards = [];

    searchBar.addEventListener("input", (e) => {
      const searchString = e.target.value.toLowerCase();

      const filteredCards = hpCards.filter((card) => {
        return card.name.toLowerCase().includes(searchString);
      });
      displayCards(filteredCards);
    });

    const loadCards = async () => {
      try {
        const res = await fetch("/build/data.json");
        hpCards = await res.json();
        displayCards(hpCards);
      } catch (err) {
        console.error(err);
      }
    };

    const displayCards = (Cards) => {
      const htmlString = Cards.map((card) => {
        return `
            <div> Name: ${card.name}  Region: ${card.region} </div>
            `;
      }).join("");
      CardsList.innerHTML = htmlString;
    };

    loadCards();
  </script>
</body>
