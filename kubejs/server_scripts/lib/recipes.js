// priority: 1

const simpleCutting = (event, input, output, number) => {
  cuttingRecipe(event, input, [itemObj(output, number)])
}

const cuttingRecipe = (event, input, resultArr) => {
  event.custom({
    "type": "farmersdelight:cutting",
    "ingredients": [{ "item": input }],
    "result": resultArr,
    "tool": {
      "tag": "c:tools/knife"
    }
  })
}

const strippingRecipe = (event, log, strippedLog) => {
  event.custom({
    "type": "farmersdelight:cutting",
    "ingredients": [
      {
        "item": log
      }
    ],
    "result": [
      {
        "item": {
          "count": 1,
          "id": strippedLog
        }
      },
      {
        "item": {
          "count": 1,
          "id": "farmersdelight:tree_bark"
        }
      }
    ],
    "sound": {
      "sound_id": "minecraft:item.axe.strip"
    },
    "tool": {
      "type": "farmersdelight:item_ability",
      "action": "axe_strip"
    }
  })
}

const refurbishedFrying = (event, input, output) => {
  event.custom({
    "type": "refurbished_furniture:frying_pan_cooking",
    "category": "food",
    "ingredient": {
      "item": input
    },
    "result": {
      "id": output
    },
    "time": 400
  })
}

const farmersCooking = (event, ingredients, result, resultNum) => {
  let recipe = {
    "type": "farmersdelight:cooking",
    "experience": 1.0,
    "cookingtime": 100,
    "ingredients": arrayToItemObjArr(ingredients),
    "recipe_book_tab": "misc",
    "result": {
      "count": resultNum,
      "id": result
    }
  }
  event.custom(recipe)
}

const arrayToItemObjArr = (items) => {
  let itemObjArr = []
  for (let item of items) {
    if (item.includes("#")) {
      let tag = item.replace("#", '')
      itemObjArr.push({'tag': tag})
    } else {
      itemObjArr.push({'item': item})
    }
  }
  return itemObjArr
}

const itemObj = (id, count) => {
  return {
    "item": {
      "id": id,
      "count": count
    }
  }
}