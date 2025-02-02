filenameKey = 'filename'
iconKey = 'icon'
nameKey = 'name'
dependencyIdKey = 'dependencyId'
increaseRateKey = 'increaseRate'

collectionNotificationKey = 'collectionNotification'

typeKey = 'type'
itemQuestTypeConst = 'itemQuestType'
observationQuestTypeConst = 'observationQuestType'

questGroupsKey = 'questGroups'
tasksKey = 'tasks'
observeKey = 'observe'
additionalRewardsKey = 'additionalRewards'
questStartAtCenterKey = 'questStartAtCenter'

questlineGroupId = '6A7C23160DA2BBC4'

itemSeedStrs = {
}

questlines = [
  { # Cooking collection
    filenameKey: 'cooking_collection',
    nameKey: 'Cooking Collection',
    iconKey: 'farmersdelight:cooking_pot',
    collectionNotificationKey: 'New dish cooked!',
    increaseRateKey: 0.04,
    typeKey: itemQuestTypeConst,
    questStartAtCenterKey: False,
    questGroupsKey: [
      {
        nameKey: 'Sweets (Farmers Delight) Completion',
        iconKey: 'farmersdelight:apple_pie',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:apple_pie',
            'farmersdelight:sweet_berry_cheesecake',
            'farmersdelight:chocolate_pie',
            'farmersdelight:sweet_berry_cookie',
            'farmersdelight:honey_cookie',
            'farmersdelight:melon_popsicle',
            'farmersdelight:glow_berry_custard'
        ]
      },
      {
        nameKey: 'Salads (Farmers Delight) Completion',
        iconKey: 'farmersdelight:fruit_salad',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:fruit_salad',
            'farmersdelight:mixed_salad',
            'farmersdelight:nether_salad'
        ]
      },
      {
        nameKey: 'Sandwiches (Farmers Delight) Completion',
        iconKey: 'farmersdelight:egg_sandwich',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:egg_sandwich',
            'farmersdelight:chicken_sandwich',
            'farmersdelight:hamburger',
            'farmersdelight:bacon_sandwich'
        ]
      },
      {
        nameKey: 'Soups (Farmers Delight) Completion',
        iconKey: 'farmersdelight:beef_stew',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:beef_stew',
            'farmersdelight:bone_broth',
            'farmersdelight:chicken_soup',
            'farmersdelight:vegetable_soup',
            'farmersdelight:fish_stew',
            'farmersdelight:pumpkin_soup',
            'farmersdelight:baked_cod_stew'
        ]
      },
      {
        nameKey: 'Asian Foods (Farmers Delight) Completion',
        iconKey: 'farmersdelight:dumplings',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:dumplings',
            'farmersdelight:fried_rice',
            'farmersdelight:cabbage_rolls'
        ]
      },
      {
        nameKey: 'Dinners (Farmers Delight) Completion',
        iconKey: 'farmersdelight:steak_and_potatoes',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:steak_and_potatoes',
            'farmersdelight:mutton_wrap',
            'farmersdelight:bacon_and_eggs',
            'farmersdelight:stuffed_potato',
            'farmersdelight:mushroom_rice',
            'farmersdelight:ratatouille'
        ]
      },
      {
        nameKey: 'Noodles (Farmers Delight) Completion',
        iconKey: 'farmersdelight:pasta_with_mutton_chop',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:pasta_with_meatballs',
            'farmersdelight:pasta_with_mutton_chop',
            'farmersdelight:vegetable_noodles',
            'farmersdelight:squid_ink_pasta',
            'farmersdelight:noodle_soup'
        ]
      },
      {
        nameKey: 'BBQ (Farmers Delight) Completion',
        iconKey: 'farmersdelight:barbecue_stick',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:barbecue_stick',
            'farmersdelight:grilled_salmon',
            'farmersdelight:roasted_mutton_chops'
        ]
      },
      { # Large Meals
        nameKey: 'Large Meals (Farmers Delight) Completion',
        iconKey: 'farmersdelight:roast_chicken_block',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
            'farmersdelight:roast_chicken_block',
            'farmersdelight:stuffed_pumpkin_block',
            'farmersdelight:honey_glazed_ham_block',
            'farmersdelight:shepherds_pie_block',
            'farmersdelight:rice_roll_medley_block'
        ]
      },
      { # MrCrayfish
        nameKey: 'MrCrayfish Meals Completion',
        iconKey: 'refurbished_furniture:light_stove',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          'refurbished_furniture:cheese_toastie',
          'refurbished_furniture:sweet_berry_jam_toast',
          'refurbished_furniture:glow_berry_jam_toast',
          'refurbished_furniture:cooked_vegetable_pizza',
          'refurbished_furniture:cooked_meatlovers_pizza'
        ]
      },
      { # Pork Dumplings
        nameKey: 'Pork Dumplings Completion',
        iconKey: 'minecraft:porkchop',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "dumplings_delight:pork_cabbage_boiled_dumpling",
          "dumplings_delight:pork_kelp_boiled_dumpling",
          "dumplings_delight:pork_potato_boiled_dumpling",
          "dumplings_delight:pork_fennel_boiled_dumpling"
        ]
      },
      { # Seafood Dumplings
        nameKey: 'Seafood Dumplings Completion',
        iconKey: 'minecraft:cod',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "dumplings_delight:cod_boiled_dumpling",
          "dumplings_delight:salmon_boiled_dumpling",
          "dumplings_delight:calamari_boiled_dumpling",
          "dumplings_delight:pufferfish_boiled_dumpling"
        ]
      },
      { # Vegetarian Dumplings
        nameKey: 'Vegetarian Dumplings Completion',
        iconKey: 'minecraft:kelp',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "dumplings_delight:tomato_egg_boiled_dumpling",
          "dumplings_delight:eggplant_egg_boiled_dumpling",
          "dumplings_delight:mushroom_boiled_dumpling",
          "dumplings_delight:fungus_boiled_dumpling",
          "dumplings_delight:garlic_chive_egg_boiled_dumpling",
          "dumplings_delight:dandelion_leaf_boiled_dumpling"
        ]
      },
      { # Misc Meat Dumplings
        nameKey: 'Misc Meat Dumplings Completion',
        iconKey: 'minecraft:cooked_mutton',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "dumplings_delight:dumpling_medley",
          "dumplings_delight:beef_tomato_boiled_dumpling",
          "dumplings_delight:mutton_boiled_dumpling",
          "dumplings_delight:chicken_mushroom_boiled_dumpling",
          "dumplings_delight:rabbit_meat_boiled_dumpling"
        ]
      },
      { # Wontons
        nameKey: 'Wontons Completion',
        iconKey: 'dumplings_delight:pork_cabbage_wonton',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "dumplings_delight:pork_carrot_wonton",
          "dumplings_delight:pork_mushroom_wonton",
          "dumplings_delight:pork_cabbage_wonton"
        ]
      },
      { # Jello
        nameKey: 'Jello Completion',
        iconKey: 'fruitsdelight:durian_jello',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "fruitsdelight:apple_jello",
          "fruitsdelight:blueberry_jello",
          "fruitsdelight:glowberry_jello",
          "fruitsdelight:hamimelon_jello",
          "fruitsdelight:melon_jello",
          "fruitsdelight:hawberry_jello",
          "fruitsdelight:lychee_jello",
          "fruitsdelight:mango_jello",
          "fruitsdelight:orange_jello",
          "fruitsdelight:peach_jello",
          "fruitsdelight:pear_jello",
          "fruitsdelight:persimmon_jello",
          "fruitsdelight:pineapple_jello",
          "fruitsdelight:lemon_jello",
          "fruitsdelight:cranberry_jello",
          "fruitsdelight:mangosteen_jello",
          "fruitsdelight:sweetberry_jello",
          "fruitsdelight:chorus_jello",
          "fruitsdelight:bayberry_jello",
          "fruitsdelight:kiwi_jello",
          "fruitsdelight:fig_jello",
          "fruitsdelight:durian_jello"
        ]
      },
      { # Fruit Sweets
        nameKey: 'Fruit Sweets Completion',
        iconKey: 'fruitsdelight:hamimelon_shaved_ice',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "fruitsdelight:hamimelon_juice",
          "fruitsdelight:hawberry_tea",
          "fruitsdelight:orange_juice",
          "fruitsdelight:lemon_juice",
          "fruitsdelight:pear_juice",
          "fruitsdelight:mango_tea",
          "fruitsdelight:peach_tea",
          "fruitsdelight:lychee_cherry_tea",
          "fruitsdelight:mangosteen_tea",
          "fruitsdelight:bayberry_soup",
          "fruitsdelight:kiwi_juice",
          "fruitsdelight:bellini_cocktail",
          "fruitsdelight:blueberry_custard",
          "fruitsdelight:hamimelon_shaved_ice"
        ]
      },
      { # Baked Fruits
        nameKey: 'Baked Fruits Completion',
        iconKey: 'fruitsdelight:cranberry_muffin',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "fruitsdelight:blueberry_muffin",
          "fruitsdelight:cranberry_muffin",
          "fruitsdelight:lemon_tart",
          "fruitsdelight:fig_tart",
          "fruitsdelight:persimmon_cookie",
          "fruitsdelight:lemon_cookie",
          "fruitsdelight:cranberry_cookie",
          "fruitsdelight:bayberry_cookie",
          "fruitsdelight:fig_pudding"
        ]
      },
      { # Misc Fruits
        nameKey: 'Misc Fruits Completion',
        iconKey: 'fruitsdelight:pineapple_fried_rice',
        dependencyIdKey: '17C8F49C46E40B53', # Chef's Beginning
        tasksKey: [
          "fruitsdelight:hamimelon_popsicle",
          "fruitsdelight:kiwi_popsicle",
          "fruitsdelight:hawberry_roll",
          "fruitsdelight:hawberry_stick",
          "fruitsdelight:mango_milkshake",
          "fruitsdelight:mango_salad",
          "fruitsdelight:pineapple_fried_rice"
        ]
      }
    ]
  },
  { # Aquarium
    filenameKey: 'aquarium',
    nameKey: 'Aquarium',
    iconKey: 'aquaculture:atlantic_herring',
    collectionNotificationKey: 'New fish caught!',
    increaseRateKey: 0.03,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla
        nameKey: 'Vanilla Completion',
        iconKey: 'minecraft:grass_block',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "minecraft:cod",
          "minecraft:salmon",
          "minecraft:tropical_fish",
          "minecraft:pufferfish"
        ]
      },
      { # Freshwater
        nameKey: 'Freshwater Completion',
        iconKey: 'minecraft:water_bucket',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:smallmouth_bass",
          "aquaculture:bluegill",
          "aquaculture:brown_trout",
          "aquaculture:carp",
          "aquaculture:catfish",
          "aquaculture:gar",
          "aquaculture:minnow",
          "aquaculture:muskellunge",
          "aquaculture:perch"
        ]
      },
      { # Arid
        nameKey: 'Arid Completion',
        iconKey: 'minecraft:dead_bush',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:bayad",
          "aquaculture:boulti",
          "aquaculture:capitaine",
          "aquaculture:synodontis"
        ]
      },
      { # Artic
        nameKey: 'Artic Completion',
        iconKey: 'minecraft:packed_ice',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:atlantic_cod",
          "aquaculture:blackfish",
          "aquaculture:pacific_halibut",
          "aquaculture:atlantic_halibut",
          "aquaculture:atlantic_herring",
          "aquaculture:pink_salmon",
          "aquaculture:pollock",
          "aquaculture:rainbow_trout"
        ]
      },
      { # Saltwater
        nameKey: 'Saltwater Completion',
        iconKey: 'minecraft:blue_ice',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:jellyfish",
          "aquaculture:red_grouper",
          "aquaculture:tuna"
        ]
      },
      { # Swamp
        nameKey: 'Swamp Completion',
        iconKey: 'minecraft:mangrove_propagule',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:box_turtle",
          "aquaculture:leech",
          "aquaculture:goldfish"
        ]
      },
      { # Mushroom
        nameKey: 'Mushroom Completion',
        iconKey: 'minecraft:red_mushroom',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:brown_shrooma",
          "aquaculture:red_shrooma"
        ]
      },
      { # Jungle
        nameKey: 'Jungle Completion',
        iconKey: 'minecraft:jungle_sapling',
        dependencyIdKey: '6089F50C4E683D57', # Catching Fishes
        tasksKey: [
          "aquaculture:arapaima",
          "aquaculture:piranha",
          "aquaculture:tambaqui",
          "aquaculture:arrau_turtle"
        ]
      }
    ]
  },
  { # Animals
    filenameKey: 'animal_watching',
    nameKey: 'Animal Watching',
    iconKey: 'minecraft:spyglass',
    collectionNotificationKey: 'New animal observed!',
    increaseRateKey: 0.02,
    typeKey: observationQuestTypeConst,
    questGroupsKey: [
      { # General Water
        nameKey: 'General Water Completion',
        iconKey: 'minecraft:water_bucket',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "livingthings:seahorse_spawn_egg",
            nameKey: "Spot a seahorse",
            observeKey: "livingthings:seahorse"
          },
          {
            iconKey: "livingthings:mantaray_spawn_egg",
            nameKey: "Spot a mantaray",
            observeKey: "livingthings:mantaray"
          },
          {
            iconKey: "livingthings:shark_spawn_egg",
            nameKey: "Spot a shark",
            observeKey: "livingthings:shark"
          },
          {
            iconKey: "minecraft:squid_spawn_egg",
            nameKey: "Spot a squid",
            observeKey: "minecraft:squid"
          },
          {
            iconKey: "minecraft:dolphin_spawn_egg",
            nameKey: "Spot a dolphin",
            observeKey: "minecraft:dolphin"
          }
        ]
      },
      { # Beaches
        nameKey: 'Beaches Completion',
        iconKey: 'artifacts:umbrella',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "livingthings:crab_spawn_egg",
            nameKey: "Spot a crab",
            observeKey: "livingthings:crab"
          },
          {
            iconKey: "minecraft:turtle_spawn_egg",
            nameKey: "Spot a turtle",
            observeKey: "minecraft:turtle"
          }
        ]
      },
      { # Desert
        nameKey: 'Desert Completion',
        iconKey: 'minecraft:dead_bush',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:camel_spawn_egg",
            nameKey: "Spot a camel",
            observeKey: "minecraft:camel"
          },
          {
            iconKey: "minecraft:sniffer_spawn_egg",
            nameKey: "Spot a sniffer",
            observeKey: "minecraft:sniffer"
          }
        ]
      },
      { # Forest
        nameKey: 'Forest Completion',
        iconKey: 'minecraft:oak_sapling',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "livingthings:owl_spawn_egg",
            nameKey: "Spot an owl",
            observeKey: "livingthings:owl"
          },
          {
            iconKey: "livingthings:raccoon_spawn_egg",
            nameKey: "Spot a raccoon",
            observeKey: "livingthings:raccoon"
          },
          {
            iconKey: "minecraft:wolf_spawn_egg",
            nameKey: "Spot a wolf",
            observeKey: "minecraft:wolf"
          }
        ]
      },
      { # Jungle
        nameKey: 'Jungle Completion',
        iconKey: 'minecraft:jungle_sapling',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "livingthings:monkey_spawn_egg",
            nameKey: "Spot a monkey",
            observeKey: "livingthings:monkey"
          },
          {
            iconKey: "livingthings:koala_spawn_egg",
            nameKey: "Spot a koala",
            observeKey: "livingthings:koala"
          },
          {
            iconKey: "minecraft:panda_spawn_egg",
            nameKey: "Spot a panda",
            observeKey: "minecraft:panda"
          },
          {
            iconKey: "minecraft:parrot_spawn_egg",
            nameKey: "Spot a parrot",
            observeKey: "minecraft:parrot"
          }
        ]
      },
      { # Mountain
        nameKey: 'Mountain Completion',
        iconKey: 'minecraft:goat_horn',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:goat_spawn_egg",
            nameKey: "Spot a Goat",
            observeKey: "minecraft:goat"
          }
        ]
      },
      { # Special
        nameKey: 'Special Completion',
        iconKey: 'minecraft:nether_star',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:bee_spawn_egg",
            nameKey: "Spot a bee",
            observeKey: "minecraft:bee"
          },
          {
            iconKey: "minecraft:allay_spawn_egg",
            nameKey: "Spot an allay",
            observeKey: "minecraft:allay"
          },
          {
            iconKey: "minecraft:cat_spawn_egg",
            nameKey: "Spot a cat",
            observeKey: "minecraft:cat"
          }
        ]
      },
      { # Savanna
        nameKey: 'Savanna Completion',
        iconKey: 'minecraft:acacia_sapling',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "livingthings:peacock_spawn_egg",
            nameKey: "Spot a peacock",
            observeKey: "livingthings:peacock"
          },
          {
            iconKey: "livingthings:ostrich_spawn_egg",
            nameKey: "Spot an ostrich",
            observeKey: "livingthings:ostrich"
          },
          {
            iconKey: "livingthings:lion_spawn_egg",
            nameKey: "Spot a lion",
            observeKey: "livingthings:lion"
          },
          {
            iconKey: "livingthings:giraffe_spawn_egg",
            nameKey: "Spot a giraffe",
            observeKey: "livingthings:giraffe"
          },
          {
            iconKey: "livingthings:elephant_spawn_egg",
            nameKey: "Spot an elephant",
            observeKey: "livingthings:elephant"
          },
          {
            iconKey: "minecraft:llama_spawn_egg",
            nameKey: "Spot a llama",
            observeKey: "minecraft:llama"
          },
          {
            iconKey: "minecraft:armadillo_spawn_egg",
            nameKey: "Spot a armadillo",
            observeKey: "minecraft:armadillo"
          }
        ]
      },
      { # Plains
        nameKey: 'Plains Completion',
        iconKey: 'minecraft:poppy',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:horse_spawn_egg",
            nameKey: "Spot a horse",
            observeKey: "minecraft:horse"
          },
          {
            iconKey: "minecraft:donkey_spawn_egg",
            nameKey: "Spot a donkey",
            observeKey: "minecraft:donkey"
          }
        ]
      },
      { # Grass
        nameKey: 'Grass Completion',
        iconKey: 'minecraft:grass_block',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:pig_spawn_egg",
            nameKey: "Spot a pig",
            observeKey: "minecraft:pig"
          },
          {
            iconKey: "minecraft:chicken_spawn_egg",
            nameKey: "Spot a chicken",
            observeKey: "minecraft:chicken"
          },
          {
            iconKey: "minecraft:rabbit_spawn_egg",
            nameKey: "Spot a rabbit",
            observeKey: "minecraft:rabbit"
          },
          {
            iconKey: "minecraft:sheep_spawn_egg",
            nameKey: "Spot a sheep",
            observeKey: "minecraft:sheep"
          },
          {
            iconKey: "minecraft:cow_spawn_egg",
            nameKey: "Spot a cow",
            observeKey: "minecraft:cow"
          }
        ]
      },
      { # Caves
        nameKey: 'Caves Completion',
        iconKey: 'minecraft:stone',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:bat_spawn_egg",
            nameKey: "Spot a bat",
            observeKey: "minecraft:bat"
          },
          {
            iconKey: "minecraft:glow_squid_spawn_egg",
            nameKey: "Spot a glow squid",
            observeKey: "minecraft:glow_squid"
          },
          {
            iconKey: "minecraft:axolotl_spawn_egg",
            nameKey: "Spot an axolotl",
            observeKey: "minecraft:axolotl"
          }
        ]
      },
      { # Snowy
        nameKey: 'Snowy Completion',
        iconKey: 'minecraft:snowball',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "livingthings:penguin_spawn_egg",
            nameKey: "Spot a penguin",
            observeKey: "livingthings:penguin"
          },
          {
            iconKey: "minecraft:polar_bear_spawn_egg",
            nameKey: "Spot a polar bear",
            observeKey: "minecraft:polar_bear"
          },
          {
            iconKey: "minecraft:fox_spawn_egg",
            nameKey: "Spot a fox",
            observeKey: "minecraft:fox"
          }
        ]
      },
      { # Swamp
        nameKey: 'Swamp Completion',
        iconKey: 'minecraft:mangrove_propagule',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "livingthings:snail_spawn_egg",
            nameKey: "Spot a snail",
            observeKey: "livingthings:snail"
          },
          {
            iconKey: "livingthings:flamingo_spawn_egg",
            nameKey: "Spot a flamingo",
            observeKey: "livingthings:flamingo"
          },
          {
            iconKey: "minecraft:frog_spawn_egg",
            nameKey: "Spot a frog",
            observeKey: "minecraft:frog"
          },
          {
            iconKey: "minecraft:tadpole_spawn_egg",
            nameKey: "Spot a tadpole",
            observeKey: "minecraft:tadpole"
          }
        ]
      },
      { # Mushroom
        nameKey: 'Mushroom Completion',
        iconKey: 'minecraft:red_mushroom',
        dependencyIdKey: '5BB57D9BEC8038FB', # Spotting animals
        tasksKey: [
          {
            iconKey: "livingthings:shroomie_spawn_egg",
            nameKey: "Spot a shroomie",
            observeKey: "livingthings:shroomie"
          },
          {
            iconKey: "minecraft:mooshroom_spawn_egg",
            nameKey: "Spot a mooshroom",
            observeKey: "minecraft:mooshroom"
          }
        ]
      }
    ]
  },
  { # Flora collection
    filenameKey: 'flora_compendium',
    nameKey: 'Flora Compendium',
    iconKey: "minecraft:red_tulip",
    collectionNotificationKey: 'New flora collected!',
    increaseRateKey: 0.02,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla Foods
        nameKey: 'Vanilla Foods Completion',
        iconKey: 'minecraft:apple',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:bamboo",
          "minecraft:beetroot_seeds",
          "minecraft:brown_mushroom",
          "minecraft:cactus",
          "minecraft:carrot",
          "minecraft:cocoa_beans",
          "minecraft:glow_berries",
          "minecraft:kelp",
          "minecraft:potato",
          "minecraft:red_mushroom",
          "minecraft:sugar_cane",
          "minecraft:sweet_berries",
          "minecraft:wheat_seeds"
        ]
      },
      { # Fruits
        nameKey: 'Fruits Completion',
        iconKey: 'minecraft:apple',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:melon_slice",
          "minecraft:pumpkin",
          "minecraft:apple",
          "fruitsdelight:pear",
          "fruitsdelight:hawberry",
          "fruitsdelight:lychee",
          "fruitsdelight:mango",
          "fruitsdelight:persimmon",
          "fruitsdelight:peach",
          "fruitsdelight:orange",
          "fruitsdelight:mangosteen",
          "fruitsdelight:bayberry",
          "fruitsdelight:kiwi",
          "fruitsdelight:fig",
          "fruitsdelight:durian",
          "fruitsdelight:blueberry",
          "fruitsdelight:lemon",
          "fruitsdelight:cranberry",
          "fruitsdelight:hamimelon_slice",
          "fruitsdelight:pineapple"
        ]
      },
      { # Modded Foods
        nameKey: 'Modded Foods Completion',
        iconKey: 'farmersdelight:onion',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "farmersdelight:cabbage_seeds",
          "farmersdelight:onion",
          "farmersdelight:rice",
          "farmersdelight:tomato_seeds",
          "dumplings_delight:chinese_cabbage_seeds",
          "dumplings_delight:garlic",
          "dumplings_delight:greenonion",
          "dumplings_delight:eggplant_seeds",
          "dumplings_delight:garlic_chive_seeds",
          "dumplings_delight:fennel_seeds"
        ]
      },
      { # Vanilla Flower
        nameKey: 'Vanilla Flower Completion',
        iconKey: 'minecraft:red_tulip',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:allium",
          "minecraft:azure_bluet",
          "minecraft:blue_orchid",
          "minecraft:cornflower",
          "minecraft:dandelion",
          "minecraft:lilac",
          "minecraft:lily_of_the_valley",
          "minecraft:orange_tulip",
          "minecraft:oxeye_daisy",
          "minecraft:peony",
          "minecraft:pink_tulip",
          "minecraft:poppy",
          "minecraft:red_tulip",
          "minecraft:rose_bush",
          "minecraft:sunflower",
          "minecraft:white_tulip",
          "minecraft:wither_rose",
          "minecraft:torchflower_seeds"
        ]
      },
      { # Vanilla Sapling
        nameKey: 'Vanilla Sapling Completion',
        iconKey: 'minecraft:oak_sapling',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:acacia_sapling",
          "minecraft:azalea",
          "minecraft:birch_sapling",
          "minecraft:cherry_sapling",
          "minecraft:dark_oak_sapling",
          "minecraft:jungle_sapling",
          "minecraft:oak_sapling",
          "minecraft:spruce_sapling",
          "minecraft:mangrove_propagule"
        ]
      },
      { # Vanilla Flora
        nameKey: 'Vanilla Flora Completion',
        iconKey: 'minecraft:pink_petals',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:flowering_azalea",
          "minecraft:moss_block",
          "minecraft:moss_carpet",
          "minecraft:pink_petals",
          "minecraft:spore_blossom",
          "minecraft:big_dripleaf",
          "minecraft:sea_pickle",
          "minecraft:lily_pad"
        ]
      },
      { # Maple Saplings
        nameKey: 'Maple Saplings',
        iconKey: 'biomeswevegone:maple_sapling',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "biomeswevegone:maple_sapling",
          "biomeswevegone:red_maple_sapling",
          "biomeswevegone:silver_maple_sapling"
        ]
      },
      { # Vanilla Varient
        nameKey: 'Vanilla Varient Saplings',
        iconKey: 'biomeswevegone:brown_oak_sapling',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "biomeswevegone:brown_oak_sapling",
          "biomeswevegone:orange_oak_sapling",
          "biomeswevegone:red_oak_sapling",
          "biomeswevegone:brown_birch_sapling",
          "biomeswevegone:orange_birch_sapling",
          "biomeswevegone:red_birch_sapling",
          "biomeswevegone:yellow_birch_sapling",
          "biomeswevegone:blue_spruce_sapling",
          "biomeswevegone:orange_spruce_sapling",
          "biomeswevegone:red_spruce_sapling",
          "biomeswevegone:yellow_spruce_sapling"
        ]
      },
      { # Special Saplings
        nameKey: 'Special Saplings',
        iconKey: 'biomeswevegone:witch_hazel_sapling',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "biomeswevegone:witch_hazel_sapling",
          "biomeswevegone:rainbow_eucalyptus_sapling",
          "biomeswevegone:blue_enchanted_sapling",
          "biomeswevegone:green_enchanted_sapling",
        ]
      },
      { # Other Modded Saplings
        nameKey: 'Other Modded Saplings',
        iconKey: 'biomeswevegone:araucaria_sapling',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "biomeswevegone:araucaria_sapling",
          "biomeswevegone:aspen_sapling",
          "biomeswevegone:baobab_sapling",
          "biomeswevegone:brown_zelkova_sapling",
          "biomeswevegone:cika_sapling",
          "biomeswevegone:cypress_sapling",
          "biomeswevegone:ebony_sapling",
          "biomeswevegone:fir_sapling",
          "biomeswevegone:holly_sapling",
          "biomeswevegone:indigo_jacaranda_sapling",
          "biomeswevegone:ironwood_sapling",
          "biomeswevegone:jacaranda_sapling",
          "biomeswevegone:mahogany_sapling",
          "biomeswevegone:orchard_sapling",
          "biomeswevegone:palm_sapling",
          "biomeswevegone:palo_verde_sapling",
          "biomeswevegone:pine_sapling",
          "biomeswevegone:redwood_sapling",
          "biomeswevegone:skyris_sapling",
          "biomeswevegone:spirit_sapling",
          "biomeswevegone:white_mangrove_sapling",
          "biomeswevegone:white_sakura_sapling",
          "biomeswevegone:willow_sapling",
          "biomeswevegone:yellow_sakura_sapling",
          "biomeswevegone:yucca_sapling",
          "biomeswevegone:zelkova_sapling"
        ]
      },
      { # Alliums
        nameKey: 'Alliums',
        iconKey: 'biomeswevegone:pink_allium',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
					"biomeswevegone:allium_flower_bush",
					"biomeswevegone:pink_allium_flower_bush",
					"biomeswevegone:pink_allium",
					"biomeswevegone:tall_allium",
					"biomeswevegone:tall_pink_allium",
					"biomeswevegone:tall_white_allium",
					"biomeswevegone:white_allium_flower_bush",
					"biomeswevegone:white_allium"
        ]
      },
      { # Amaranths
        nameKey: 'Amaranths',
        iconKey: 'biomeswevegone:amaranth',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
					"biomeswevegone:amaranth",
					"biomeswevegone:cyan_amaranth",
					"biomeswevegone:magenta_amaranth",
					"biomeswevegone:orange_amaranth",
					"biomeswevegone:purple_amaranth"
        ]
      },
      { # Roses
        nameKey: 'Roses',
        iconKey: 'biomeswevegone:rose',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
					"biomeswevegone:black_rose",
					"biomeswevegone:blue_rose_bush",
					"biomeswevegone:cyan_rose",
					"biomeswevegone:osiria_rose",
					"biomeswevegone:rose",
					"biomeswevegone:winter_rose"
        ]
      },
      { # Tulips
        nameKey: 'Tulips',
        iconKey: 'biomeswevegone:cyan_tulip',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
					"biomeswevegone:cyan_tulip",
					"biomeswevegone:green_tulip",
					"biomeswevegone:magenta_tulip",
					"biomeswevegone:purple_tulip",
					"biomeswevegone:yellow_tulip"
        ]
      },
      { # Daffodils
        nameKey: 'Daffodils',
        iconKey: 'biomeswevegone:daffodil',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
					"biomeswevegone:daffodil",
					"biomeswevegone:pink_daffodil",
					"biomeswevegone:yellow_daffodil"
        ]
      },
      { # Sages
        nameKey: 'Sages',
        iconKey: 'biomeswevegone:blue_sage',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
					"biomeswevegone:blue_sage",
					"biomeswevegone:purple_sage",
					"biomeswevegone:white_sage"
        ]
      },
      { # Flowering Flora
        nameKey: 'Flowering Flora',
        iconKey: 'biomeswevegone:flower_patch',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
					"biomeswevegone:flower_patch",
					"biomeswevegone:flowering_barrel_cactus",
					"biomeswevegone:flowering_indigo_jacaranda_bush",
					"biomeswevegone:flowering_jacaranda_bush",
					"biomeswevegone:flowering_tiny_lily_pads"
        ]
      },
      { # Other Misc Flowers
        nameKey: 'Other Misc Flowers',
        iconKey: 'biomeswevegone:alpine_bellflower',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
					"biomeswevegone:alpine_bellflower",
					"biomeswevegone:angelica",
					"biomeswevegone:begonia",
					"biomeswevegone:bistort",
					"biomeswevegone:california_poppy",
					"biomeswevegone:crocus",
					"biomeswevegone:cyan_pitcher_plant",
					"biomeswevegone:delphinium",
					"biomeswevegone:fairy_slipper",
					"biomeswevegone:foxglove",
					"biomeswevegone:guzmania",
					"biomeswevegone:incan_lily",
					"biomeswevegone:iris",
					"biomeswevegone:japanese_orchid",
					"biomeswevegone:kovan_flower",
					"biomeswevegone:lazarus_bellflower",
					"biomeswevegone:lollipop_flower",
					"biomeswevegone:magenta_pitcher_plant",
					"biomeswevegone:orange_daisy",
					"biomeswevegone:peach_leather_flower",
					"biomeswevegone:pink_anemone",
					"biomeswevegone:protea_flower",
					"biomeswevegone:richea",
					"biomeswevegone:silver_vase_flower",
					"biomeswevegone:snowdrops",
					"biomeswevegone:violet_leather_flower",
					"biomeswevegone:white_anemone",
					"biomeswevegone:white_sakura_petals",
					"biomeswevegone:winter_cyclamen",
					"biomeswevegone:winter_scilla",
					"biomeswevegone:yellow_sakura_petals"
        ]
      }
    ]
  },
  { # Mineral Museum
    filenameKey: 'mineral_museum',
    nameKey: 'Mineral Museum',
    iconKey: 'minecraft:raw_gold',
    collectionNotificationKey: 'New mineral mined!',
    increaseRateKey: 0.03,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla Blocks
        nameKey: 'Vanilla Blocks Completion',
        iconKey: 'minecraft:andesite',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.01,
        tasksKey: [
          "minecraft:cobblestone",
          "minecraft:mossy_cobblestone",
          "minecraft:cobbled_deepslate",
          "minecraft:diorite",
          "minecraft:granite",
          "minecraft:andesite",
          "minecraft:sandstone",
          "minecraft:red_sandstone",
          "minecraft:calcite",
          "minecraft:dripstone_block",
          "minecraft:pointed_dripstone",
          "minecraft:smooth_basalt",
          "minecraft:tuff",
          "minecraft:obsidian"
        ]
      },
      { # Ore
        nameKey: 'Ore Completion',
        iconKey: 'minecraft:raw_iron',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.03,
        tasksKey: [
          "minecraft:coal",
          "minecraft:raw_copper",
          "minecraft:raw_iron",
          "minecraft:amethyst_shard",
          "minecraft:raw_gold",
          "minecraft:redstone",
          "minecraft:lapis_lazuli",
          "minecraft:diamond"
        ]
      }
    ]
  }
]