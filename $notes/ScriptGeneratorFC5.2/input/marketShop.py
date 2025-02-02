from src import questCollectionReader

fcCategoryKey = 'fc'
floraCategoryKey = 'flora'
farmCategoryKey = 'farm'
miningCategoryKey = 'mining'

nameKey = 'name'
iconKey = 'icon'
entryGroupsKey = 'entryGroups'
itemsKey = 'items'
priceKey = 'price'
priceItemKey = 'priceItem'
productNumKey = 'productNum'
componentsKey = 'components'

categories = {
  fcCategoryKey: {
    nameKey: "Farming Crossing Shop",
    iconKey: "minecraft:mangrove_propagule",
    entryGroupsKey: [
      {
        itemsKey: [
          'kubejs:check_food_cravings',
          'kubejs:check_collection_progress'
        ]
      },
      {
        priceKey: 4,
        itemsKey: ["minecraft:quartz"]
      },
      {
        priceKey: 6,
        itemsKey: ["minecraft:glowstone_dust"]
      },
      {
        priceKey: 8,
        itemsKey: [
          "minecraft:bundle",
          "minecraft:beehive",
          "minecraft:bee_spawn_egg"
        ]
      },
      {
        priceKey: 4,
        itemsKey: [
          "minecraft:saddle",
          "minecraft:lead",
          "horseexpert:monocle"
        ]
      },
      {
        productNumKey: 4,
        itemsKey: [
          "minecraft:emerald"
        ]
      }
    ]
  },
  'crops': {
    nameKey: 'Crops',
    iconKey: 'minecraft:carrot',
    entryGroupsKey: [
      {
        priceKey: 8,
        productNumKey: 4,
        itemsKey: [
          "minecraft:wheat_seeds",
          "minecraft:carrot",
          "minecraft:cocoa_beans",
          "minecraft:glow_berries",
          "minecraft:potato",
          "minecraft:sugar_cane",
          "minecraft:sweet_berries",
          "minecraft:brown_mushroom",
          "minecraft:red_mushroom",
          "minecraft:beetroot_seeds",
          "minecraft:melon_seeds",
          "minecraft:pumpkin_seeds",
          "farmersdelight:cabbage_seeds",
          "farmersdelight:tomato_seeds",
          "farmersdelight:rice",
          "farmersdelight:onion",
          "dumplings_delight:chinese_cabbage_seeds",
          "dumplings_delight:eggplant_seeds",
          "dumplings_delight:fennel_seeds",
          "dumplings_delight:garlic_chive_seeds",
          "dumplings_delight:garlic",
          "dumplings_delight:greenonion",
          "fruitsdelight:hamimelon_seeds",
          "fruitsdelight:lemon_seeds",
          "fruitsdelight:blueberry"
        ]
      }
    ]
  },
  'fruit_saplings': {
    nameKey: 'Fruit Saplings',
    iconKey: 'fruitsdelight:apple_sapling',
    entryGroupsKey: [
      {
        priceKey: 8,
        productNumKey: 4,
        itemsKey: [
          "fruitsdelight:apple_sapling",
          "fruitsdelight:bayberry_sapling",
          "fruitsdelight:durian_sapling",
          "fruitsdelight:fig_sapling",
          "fruitsdelight:hawberry_sapling",
          "fruitsdelight:kiwi_sapling",
          "fruitsdelight:lychee_sapling",
          "fruitsdelight:mango_sapling",
          "fruitsdelight:mangosteen_sapling",
          "fruitsdelight:orange_sapling",
          "fruitsdelight:peach_sapling",
          "fruitsdelight:pear_sapling",
          "fruitsdelight:persimmon_sapling",
          "fruitsdelight:pineapple_sapling"
        ]
      }
    ]
  },
  'blocks': {
    nameKey: 'Blocks',
    iconKey: '',
    entryGroupsKey: [
      { # blocks
        priceKey: 32,
        itemsKey: [
          "minecraft:ice",
          "minecraft:blackstone",
          "minecraft:end_stone",
          'minecraft:sea_lantern',
          'minecraft:shroomlight',
          'minecraft:ochre_froglight',
          'minecraft:pearlescent_froglight',
          'minecraft:verdant_froglight'
        ]
      }
    ]
  },
  'handcrafted': {
    nameKey: "Handcrafted Furniture Sheets and Cushions",
    iconKey: "handcrafted:brown_cushion",
    entryGroupsKey: [
      { # handcrafted
        productNumKey: 2,
        itemsKey: [
          "handcrafted:black_sheet",
          "handcrafted:blue_sheet",
          "handcrafted:brown_sheet",
          "handcrafted:cyan_sheet",
          "handcrafted:gray_sheet",
          "handcrafted:green_sheet",
          "handcrafted:light_blue_sheet",
          "handcrafted:light_gray_sheet",
          "handcrafted:lime_sheet",
          "handcrafted:magenta_sheet",
          "handcrafted:orange_sheet",
          "handcrafted:pink_sheet",
          "handcrafted:purple_sheet",
          "handcrafted:red_sheet",
          "handcrafted:white_sheet",
          "handcrafted:yellow_sheet",
          "handcrafted:black_cushion",
          "handcrafted:blue_cushion",
          "handcrafted:brown_cushion",
          "handcrafted:cyan_cushion",
          "handcrafted:gray_cushion",
          "handcrafted:green_cushion",
          "handcrafted:light_blue_cushion",
          "handcrafted:light_gray_cushion",
          "handcrafted:lime_cushion",
          "handcrafted:magenta_cushion",
          "handcrafted:orange_cushion",
          "handcrafted:pink_cushion",
          "handcrafted:purple_cushion",
          "handcrafted:red_cushion",
          "handcrafted:white_cushion",
          "handcrafted:yellow_cushion" 
        ]
      }
    ]
  },
  'dyes': {
    nameKey: "Dyes",
    iconKey: "minecraft:lime_dye",
    entryGroupsKey: [
      { # dyes
        priceKey: 4,
        productNumKey: 8,
        itemsKey: [
          "minecraft:black_dye",
          "minecraft:blue_dye",
          "minecraft:brown_dye",
          "minecraft:cyan_dye",
          "minecraft:gray_dye",
          "minecraft:green_dye",
          "minecraft:light_blue_dye",
          "minecraft:light_gray_dye",
          "minecraft:lime_dye",
          "minecraft:magenta_dye",
          "minecraft:orange_dye",
          "minecraft:pink_dye",
          "minecraft:purple_dye",
          "minecraft:red_dye",
          "minecraft:white_dye",
          "minecraft:yellow_dye"
        ]
      },
    ]
  },
  floraCategoryKey: {
    nameKey: "Plants",
    iconKey: "minecraft:poppy",
    entryGroupsKey: [
      {
        productNumKey: 4,
        itemsKey: [
          "minecraft:crimson_fungus",
          "minecraft:warped_fungus"
        ]
      },
      {
        priceKey: 8,
        itemsKey: [
          "minecraft:chorus_fruit"
        ]
      },
      { # not in collection
        priceKey: 32,
        productNumKey: 4,
        itemsKey: [
          'minecraft:vine',
          'minecraft:weeping_vines',
          'minecraft:twisting_vines'
        ]
      }
    ]
  },
  farmCategoryKey: {
    nameKey: "Animal Range",
    iconKey: "minecraft:leather",
    entryGroupsKey: [
      { # meats
        priceKey: 2,
        productNumKey: 8,
        itemsKey: [
          "minecraft:beef",
          "minecraft:chicken",
          "minecraft:mutton",
          "minecraft:porkchop",
          "minecraft:rabbit",
          "aquaculture:fish_fillet_raw",
          "farmersdelight:ham",
          "minecraft:rabbit_foot",
          "minecraft:feather",
          "dumplings_delight:calamari"
        ]
      },
      { # 2
        priceKey: 2,
        itemsKey: [
          "minecraft:leather",
          "minecraft:rabbit_hide",
          "minecraft:ink_sac"
        ]
      }
    ]
  },
  'mob_drops': {
    nameKey: "Mob Drops",
    iconKey: "minecraft:rotten_flesh",
    entryGroupsKey: [
      { # minecraft:arrow
        productNumKey: 4,
        itemsKey: ["minecraft:arrow"]
      },
      { # mob 2
        priceKey: 2,
        itemsKey: [
          "minecraft:string",
          "minecraft:slime_ball"
        ]
      },
      { # mob 4
        priceKey: 4,
        itemsKey: [
          "minecraft:rotten_flesh",
          "minecraft:bone",
          "minecraft:bow"
        ]
      },
      {
        priceKey: 8,
        itemsKey: [
          "minecraft:spider_eye",
          "minecraft:gunpowder",
          "minecraft:prismarine_shard",
          "minecraft:prismarine_crystals",
          "minecraft:glow_ink_sac"
        ]
      },
      {
        priceKey: 24,
        itemsKey: [
          "minecraft:ender_pearl",
          "minecraft:blaze_rod",
          "minecraft:ghast_tear",
          "minecraft:phantom_membrane"
        ]
      }
    ]
  },
  'spawneggs': {
    nameKey: "Non Quest Related Spawn Eggs",
    iconKey: "minecraft:blaze_spawn_egg",
    entryGroupsKey: [
      { # spawn eggs
        priceKey: 64,
        productNumKey: 1,
        itemsKey: questCollectionReader.nonQuestSpawnEggs([
          "aquaculture:arrau_turtle_spawn_egg",
          "aquaculture:box_turtle_spawn_egg",
          "aquaculture:starshell_turtle_spawn_egg",
          "artifacts:mimic_spawn_egg",
          "minecraft:allay_spawn_egg",
          "minecraft:axolotl_spawn_egg",
          "minecraft:bat_spawn_egg",
          "minecraft:bee_spawn_egg",
          "minecraft:blaze_spawn_egg",
          "minecraft:camel_spawn_egg",
          "minecraft:cat_spawn_egg",
          "minecraft:cave_spider_spawn_egg",
          "minecraft:chicken_spawn_egg",
          "minecraft:cod_spawn_egg",
          "minecraft:cow_spawn_egg",
          "minecraft:creeper_spawn_egg",
          "minecraft:dolphin_spawn_egg",
          "minecraft:donkey_spawn_egg",
          "minecraft:drowned_spawn_egg",
          "minecraft:enderman_spawn_egg",
          "minecraft:endermite_spawn_egg",
          "minecraft:evoker_spawn_egg",
          "minecraft:fox_spawn_egg",
          "minecraft:frog_spawn_egg",
          "minecraft:ghast_spawn_egg",
          "minecraft:glow_squid_spawn_egg",
          "minecraft:goat_spawn_egg",
          "minecraft:guardian_spawn_egg",
          "minecraft:hoglin_spawn_egg",
          "minecraft:horse_spawn_egg",
          "minecraft:husk_spawn_egg",
          "minecraft:iron_golem_spawn_egg",
          "minecraft:magma_cube_spawn_egg",
          "minecraft:phantom_spawn_egg",
          "minecraft:piglin_brute_spawn_egg",
          "minecraft:piglin_spawn_egg",
          "minecraft:pillager_spawn_egg",
          "minecraft:ravager_spawn_egg",
          "minecraft:shulker_spawn_egg",
          "minecraft:silverfish_spawn_egg",
          "minecraft:skeleton_horse_spawn_egg",
          "minecraft:skeleton_spawn_egg",
          "minecraft:slime_spawn_egg",
          "minecraft:sniffer_spawn_egg",
          "minecraft:snow_golem_spawn_egg",
          "minecraft:spider_spawn_egg",
          "minecraft:stray_spawn_egg",
          "minecraft:strider_spawn_egg",
          "minecraft:trader_llama_spawn_egg",
          "minecraft:vex_spawn_egg",
          "minecraft:vindicator_spawn_egg",
          "minecraft:witch_spawn_egg",
          "minecraft:wither_skeleton_spawn_egg",
          "minecraft:zoglin_spawn_egg",
          "minecraft:zombie_horse_spawn_egg",
          "minecraft:zombie_spawn_egg",
          "minecraft:zombie_villager_spawn_egg",
          "minecraft:zombified_piglin_spawn_egg",
        ])
      }
    ]
  },
  'collectables': {
    nameKey: "Collection Task Items",
    iconKey: "minecraft:writable_book",
    entryGroupsKey: [
      {
        priceKey: 64,
        itemsKey: questCollectionReader.collectionQuestItems()
      }
    ]
  }
}

enchantments = {
  "farmersdelight:backstabbing": 3,
  "minecraft:aqua_affinity": 1,
  "minecraft:bane_of_arthropods": 5,
  "minecraft:binding_curse": 1,
  "minecraft:blast_protection": 4,
  "minecraft:breach": 4,
  "minecraft:channeling": 1,
  "minecraft:density": 5,
  "minecraft:depth_strider": 3,
  "minecraft:efficiency": 5,
  "minecraft:feather_falling": 4,
  "minecraft:fire_aspect": 2,
  "minecraft:fire_protection": 4,
  "minecraft:flame": 1,
  "minecraft:fortune": 3,
  "minecraft:frost_walker": 2,
  "minecraft:impaling": 5,
  "minecraft:infinity": 1,
  "minecraft:knockback": 2,
  "minecraft:looting": 3,
  "minecraft:loyalty": 3,
  "minecraft:luck_of_the_sea": 2,
  "minecraft:lure": 3,
  "minecraft:mending": 1,
  "minecraft:multishot": 1,
  "minecraft:piercing": 4,
  "minecraft:power": 5,
  "minecraft:projectile_protection": 4,
  "minecraft:protection": 4,
  "minecraft:punch": 2,
  "minecraft:quick_charge": 3,
  "minecraft:respiration": 3,
  "minecraft:riptide": 3,
  "minecraft:sharpness": 5,
  "minecraft:silk_touch": 1,
  "minecraft:smite": 5,
  "minecraft:soul_speed": 3,
  "minecraft:sweeping_edge": 3,
  "minecraft:swift_sneak": 3,
  "minecraft:thorns": 3,
  "minecraft:unbreaking": 3,
  "minecraft:vanishing_curse": 1,
  "minecraft:wind_burst": 3
}
