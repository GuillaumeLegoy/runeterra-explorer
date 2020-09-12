<script>
  import Search from './search.svelte'

  let searchQuery = ''
  let searchTerm = null

  function handleSubmit() {
    searchTerm = searchQuery.trim()
    searchResults = []

    if (!searchTerm) return

    searchUnsplash()
  }

  function searchUnsplash() {
    return 'try again'
  }
</script>

<style>
  .App {
    width: 100%;
    max-width: 1500px;
    padding: 20px;
    margin: 0 auto 50px;
    text-align: center;
  }

  h1 {
    font-size: 50px;
    margin-top: 30px;
    margin-bottom: 30px;
  }
</style>

<main class="App">
  <h1>Deckoder</h1>

  <Search bind:query={searchQuery} {handleSubmit} />
</main>
