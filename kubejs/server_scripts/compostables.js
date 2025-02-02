
const compostables = [
  // saplings
  "regions_unexplored:alpha_sapling",
  "regions_unexplored:apple_oak_sapling",
  "regions_unexplored:ashen_sapling",
  "regions_unexplored:bamboo_sapling",
  "regions_unexplored:baobab_sapling",
  "regions_unexplored:blackwood_sapling",
  "regions_unexplored:blue_magnolia_sapling",
  "regions_unexplored:brimwood_sapling",
  "regions_unexplored:cobalt_sapling",
  "regions_unexplored:cypress_sapling",
  "regions_unexplored:dead_pine_sapling",
  "regions_unexplored:dead_sapling",
  "regions_unexplored:enchanted_birch_sapling",
  "regions_unexplored:eucalyptus_sapling",
  "regions_unexplored:flowering_sapling",
  "regions_unexplored:golden_larch_sapling",
  "regions_unexplored:joshua_sapling",
  "regions_unexplored:kapok_sapling",
  "regions_unexplored:larch_sapling",
  "regions_unexplored:magnolia_sapling",
  "regions_unexplored:maple_sapling",
  "regions_unexplored:mauve_sapling",
  "regions_unexplored:orange_maple_sapling",
  "regions_unexplored:palm_sapling",
  "regions_unexplored:pine_sapling",
  "regions_unexplored:pink_magnolia_sapling",
  "regions_unexplored:red_maple_sapling",
  "regions_unexplored:redwood_sapling",
  "regions_unexplored:silver_birch_sapling",
  "regions_unexplored:small_oak_sapling",
  "regions_unexplored:socotra_sapling",
  "regions_unexplored:white_magnolia_sapling",
  "regions_unexplored:willow_sapling",

  // leaves
  "regions_unexplored:alpha_leaves",
  "regions_unexplored:apple_oak_leaves",
  "regions_unexplored:ashen_leaves",
  "regions_unexplored:bamboo_leaves",
  "regions_unexplored:baobab_leaves",
  "regions_unexplored:blackwood_leaves",
  "regions_unexplored:blue_magnolia_leaves",
  "regions_unexplored:brimwood_leaves",
  "regions_unexplored:cobalt_webbing",
  "regions_unexplored:cypress_leaves",
  "regions_unexplored:dead_leaves",
  "regions_unexplored:dead_pine_leaves",
  "regions_unexplored:enchanted_birch_leaves",
  "regions_unexplored:eucalyptus_leaves",
  "regions_unexplored:flowering_leaves",
  "regions_unexplored:golden_larch_leaves",
  "regions_unexplored:joshua_leaves",
  "regions_unexplored:kapok_leaves",
  "regions_unexplored:larch_leaves",
  "regions_unexplored:magnolia_leaves",
  "regions_unexplored:maple_leaves",
  "regions_unexplored:mauve_leaves",
  "regions_unexplored:orange_maple_leaves",
  "regions_unexplored:palm_leaves",
  "regions_unexplored:pine_leaves",
  "regions_unexplored:pink_magnolia_leaves",
  "regions_unexplored:red_maple_leaves",
  "regions_unexplored:redwood_leaves",
  "regions_unexplored:silver_birch_leaves",
  "regions_unexplored:small_oak_leaves",
  "regions_unexplored:socotra_leaves",
  "regions_unexplored:white_magnolia_leaves",
  "regions_unexplored:willow_leaves",

  // flowers
  "regions_unexplored:alpha_dandelion",
  "regions_unexplored:alpha_rose",
  "regions_unexplored:aster",
  "regions_unexplored:black_snowbelle",
  "regions_unexplored:bleeding_heart",
  "regions_unexplored:blue_lupine",
  "regions_unexplored:blue_magnolia_flowers",
  "regions_unexplored:blue_snowbelle",
  "regions_unexplored:brown_snowbelle",
  "regions_unexplored:cyan_snowbelle",
  "regions_unexplored:daisy",
  "regions_unexplored:day_lily",
  "regions_unexplored:dorcel",
  "regions_unexplored:felicia_daisy",
  "regions_unexplored:fireweed",
  "regions_unexplored:gray_snowbelle",
  "regions_unexplored:green_snowbelle",
  "regions_unexplored:hibiscus",
  "regions_unexplored:hyacinth_flowers",
  "regions_unexplored:hyssop",
  "regions_unexplored:light_blue_snowbelle",
  "regions_unexplored:light_gray_snowbelle",
  "regions_unexplored:lime_snowbelle",
  "regions_unexplored:magenta_snowbelle",
  "regions_unexplored:mallow",
  "regions_unexplored:orange_coneflower",
  "regions_unexplored:orange_snowbelle",
  "regions_unexplored:pink_lupine",
  "regions_unexplored:pink_magnolia_flowers",
  "regions_unexplored:pink_snowbelle",
  "regions_unexplored:poppy_bush",
  "regions_unexplored:purple_coneflower",
  "regions_unexplored:purple_lupine",
  "regions_unexplored:purple_snowbelle",
  "regions_unexplored:red_lupine",
  "regions_unexplored:red_snowbelle",
  "regions_unexplored:salmon_poppy_bush",
  "regions_unexplored:tassel",
  "regions_unexplored:tsubaki",
  "regions_unexplored:waratah",
  "regions_unexplored:white_magnolia_flowers",
  "regions_unexplored:white_snowbelle",
  "regions_unexplored:white_trillium",
  "regions_unexplored:wilting_trillium",
  "regions_unexplored:yellow_lupine",
  "regions_unexplored:yellow_snowbelle"
]

const compostableChance = .3

ServerEvents.compostableRecipes(event => {
  for (let compostable of compostables) {
    event.add(compostable, compostableChance)
  }
})

ServerEvents.generateData('before_mods', (event) => {
  let data_map = { values: {} };
  for (let compostable of compostables) {
    // Build up compostables data map for NeoForge
    data_map.values[compostable] = { chance: compostableChance };
  }

  event.json(`neoforge:data_maps/item/compostables.json`, data_map);
})