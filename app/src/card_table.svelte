<script>
  import SvelteTable from 'svelte-table'
  const rows = [
    {
      region: 'Piltover & Zaun',
      attack: 1,
      cost: 5,
      health: 5,
      name: 'Subpurrsible',
      cardCode: '02PZ001',
      rarity: 'EPIC',
      type: 'Unit',
    },
    {
      region: 'Bilgewater',
      attack: 2,
      cost: 1,
      health: 1,
      name: 'Shellshocker ',
      cardCode: '02BW040',
      rarity: 'COMMON',
      type: 'Unit',
    },
    {
      region: 'Freljord',
      attack: 4,
      cost: 4,
      health: 3,
      name: 'Wolfrider',
      cardCode: '02FR009',
      rarity: 'COMMON',
      type: 'Unit',
    },
  ]
  const columns = [
    {
      key: 'region',
      title: 'Region',
      value: (v) => v.region,
      sortable: true,
      headerClass: 'text-left',
    },
    {
      key: 'attack',
      title: 'Attack',
      value: (v) => v.attack,
      sortable: true,
      headerClass: 'text-left',
    },
    {
      key: 'cost',
      title: 'Cost',
      value: (v) => v.cost,
      sortable: true,
      headerClass: 'text-left',
    },
    {
      key: 'health',
      title: 'Health',
      value: (v) => v.health,
      sortable: true,
      headerClass: 'text-left',
    },
    {
      key: 'name',
      title: 'Name',
      value: (v) => v.name,
      sortable: true,
      headerClass: 'text-left',
    },
    {
      key: 'cardCode',
      title: 'Card Code',
      value: (v) => v.cardCode,
      sortable: true,
      headerClass: 'text-left',
    },
    {
      key: 'rarity',
      title: 'Rarity',
      value: (v) => v.rarity,
      sortable: true,
      headerClass: 'text-left',
    },
    {
      key: 'type',
      title: 'Type',
      value: (v) => v.type,
      sortable: true,
      headerClass: 'text-left',
    },
  ]
</script>
