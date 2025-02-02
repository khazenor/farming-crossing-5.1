ItemEvents.modifyTooltips(event => {
  event.add(
    [
      'mob_catcher:diamond_mob_catcher', 
      'compostbag:compost_bag', 
      'hangglider:hang_glider', 
      'packingtape:tape', 
      'waystones:warp_plate', 
      'waystones:waystone', 
      'mob_catcher:netherite_mob_catcher', 
      'minecraft:minecart', 
      'minecraft:rail', 
      'minecraft:powered_rail', 
      'sophisticatedbackpacks:gold_backpack', 
      'sophisticatedbackpacks:diamond_backpack', 
      'expandedstorage:wood_to_diamond_conversion_kit', 
      'sophisticatedstorage:basic_to_diamond_tier_upgrade'
    ],
    [
      Text.translate('fcCustomVillagers.youCanBuyThisItemFromJess')
    ])

})