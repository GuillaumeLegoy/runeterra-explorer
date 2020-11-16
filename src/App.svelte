<script>
  let me;
  let hpCards = [];
  let options = [
		'Champions',
		'Items',
		'Traits'
  ]
  let type = "Champions";
  

  const loadCards = async (type) => {
    console.log(type)

    try {

        const res = await fetch("/build/${type}.json");

      console.log(type)
      console.log(res)
      hpCards = await res.json();
      displayCards(hpCards);
    } catch (err) {
      console.error(err);
    }
  };

  const displayCards = (Cards) => {
    let htmlString = JSON.stringify(Cards, undefined, 2);
    console.log(htmlString)
    me.innerHTML = htmlString ;
  };

  loadCards()
 
</script>


{#each options as value}
	<label><input type="radio" {value} bind:group={type}> {value}</label>
{/each}



{#if type.value == "Champions"}
	<p>Please select at least one flavour</p>
{:else if flavours.length > scoops}



<pre bind:this={me}></pre>