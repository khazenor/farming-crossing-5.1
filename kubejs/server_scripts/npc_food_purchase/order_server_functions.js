// priority: 1

const handleMenuInteraction = (event) => {
  let player = event.player
  let target = event.target
  let handItemId = player.mainHandItem.id
  if (playerHasActiveOrder(player)) {
    let activeOrder = player.persistentData.activeOrder
    tellPlayerAlreadyOrdered(player, activeOrder)
  } else {
    setPlayerOrder(player, target, handItemId)
    givePlayerOrderItem(player)
    tellPlayerVillagerOrder(
      player,
      target,
      Text.translate(global.menuInfo[handItemId].size)
    )
  }
  event.cancel()
}

const handleMealSubmission = (event) => {
  let player = event.player
  let target = event.target
  let handItemId = player.mainHandItem.id

  deliverDishForPlayer(player, handItemId)
  player.mainHandItem.count --
  tellPlayerVillagerThankYou(player, target, handItemId)
  rewardPlayerIfOrderIsComplete(player, target)

  event.cancel()
}

const tellPlayerAlreadyOrdered = (player, activeOrder) => {
  player.tell(Text.translate('npcFoodPurchase.alreadyHaveOrderFrom',
    global.genStrFromObj(
      activeOrder.customerName
    )
  ))
}

const setPlayerOrder = (player, target, menuId) => {
  let order = global.getOrderObject(
    target,
    menuId
  )
  player.persistentData.activeOrder = order
}

const givePlayerOrderItem = (player) => {
  let activeOrder = getPlayerActiveOrder(player)
  player.give(Item.of("kubejs:customer_order"))
}

const shouldSubmitMeal = (event) => {
  let player = event.player
  let target = event.target

  return playerHasActiveOrder(player) &&
    isPlayerHoldingRequestedDish(player) &&
    isEntityActiveCustomer(target, player)
}

const isPlayerHoldingRequestedDish = (player) => {
  let requestedDishes = getPlayerActiveOrder(player).requestedDishes
  return global.getObjArrIncludes(requestedDishes, player.mainHandItem.id)
}

const isEntityActiveCustomer = (entity, player) => {
  let entityUUID = entity.uuid.toString()
  let customerUUID = global.genStrFromObj(
    player.persistentData.activeOrder.customerUUID
  )
  return entityUUID === customerUUID
}

const getPlayerActiveOrder = (player) => {
  return player.persistentData.activeOrder
}

const deliverDishForPlayer = (player, dishId) => {
  let requestedDishes = (global.arrFromObj(
    player.persistentData.activeOrder.requestedDishes
  ))
  let removeIndex = requestedDishes.indexOf(dishId)
  requestedDishes.splice(removeIndex, 1)
  player.persistentData.activeOrder.requestedDishes = requestedDishes
  let completedDishes = (global.arrFromObj(
    player.persistentData.activeOrder.completedDishes
  ))
  completedDishes.push(dishId)
  player.persistentData.activeOrder.completedDishes = completedDishes
}

const deleteOrderBookFromPlayerInventory = (player) => {
  for (let itemStack of player.inventory.allItems) {
    if (itemStack.id === 'kubejs:customer_order') {
      itemStack.count = 0
    }
  }
}

const tellPlayerVillagerOrder = (player, villager, desc) => {
  let villagerName = villager.name.getString()
  player.tell(
    Text.translate(
      'npcFoodPurchase.hereIsMyOrder',
      villagerName,
      desc
    )
  )
}

const tellPlayerVillagerThankYou = (player, villager, itemId) => {
  let villagerName = villager.name.getString()
  let itemName = global.getTranItemName(itemId)
  player.tell(
    Text.translate(
      'npcFoodPurchase.thankYouForDish',
      villagerName,
      itemName
    )
  )
}

const rewardPlayerIfOrderIsComplete = (player, villager) => {
  if (playerHasActiveOrder(player)) {
    let requestedDishes = global.arrFromObj(
      player.persistentData.activeOrder.requestedDishes
    )
  
    if (requestedDishes.length === 0) {
      let villagerName = villager.name.getString()
      let numTickets = global.genNumFromObj(player.persistentData.activeOrder.reward)
      numTickets = Math.floor(numTickets)
      player.give(`${numTickets}x kubejs:miles_ticket`)
      
      player.tell(
        Text.translate(
          'npcFoodPurchase.hereAreTixs',
          villagerName,
          `${numTickets}`
        )
      )
      deleteOrderBookFromPlayerInventory(player)
      player.persistentData.activeOrder = 'cleared'
    }
  }
}

const playerHasActiveOrder = (player) => {
  if (!player.persistentData.activeOrder) {
    return false
  }

  let activeOrder = global.genStrFromObj(
    player.persistentData.activeOrder
  )
  return activeOrder !== 'cleared'
}