from lib import kubejs
from lib import fcTrans
from src import const
from src import questCollectionReader
import os

craftOutputNumber = 8
paymentItem = "minecraft:bone_meal"
floraDenyList = [
	"minecraft:apple",
	"minecraft:bamboo",
	"minecraft:beetroot_seeds",
	"minecraft:brown_mushroom",
	"minecraft:cactus",
	"minecraft:carrot",
	"minecraft:cocoa_beans",
	"minecraft:glow_berries",
	"minecraft:kelp",
	"minecraft:melon_slice",
	"minecraft:potato",
	"minecraft:pumpkin_seeds",
	"minecraft:pumpkin",
	"minecraft:red_mushroom",
	"minecraft:sugar_cane",
	"minecraft:sweet_berries",
	"minecraft:wheat_seeds",
	"farmersdelight:cabbage_seeds",
	"farmersdelight:onion",
	"farmersdelight:rice",
	"farmersdelight:tomato_seeds",
	'dumplings_delight:chinese_cabbage_seeds',
	'dumplings_delight:garlic',
	'dumplings_delight:greenonion',
	'dumplings_delight:eggplant_seeds',
	'dumplings_delight:garlic_chive_seeds',
	'dumplings_delight:fennel_seeds',
	'fruitsdelight:pear',
	'fruitsdelight:hawberry',
	'fruitsdelight:lychee',
	'fruitsdelight:mango',
	'fruitsdelight:persimmon',
	'fruitsdelight:peach',
	'fruitsdelight:orange',
	'fruitsdelight:mangosteen',
	'fruitsdelight:bayberry',
	'fruitsdelight:kiwi', 
	'fruitsdelight:fig',
	'fruitsdelight:durian',
	'fruitsdelight:blueberry',
	'fruitsdelight:lemon',
	'fruitsdelight:cranberry',
	'fruitsdelight:hamimelon_slice',
	'fruitsdelight:pineapple',
]
transParent = 'floraDuplicationTooltips'

def generateDuplicationRecipes():
	shapelessRecipeContent = ""
	craftedFlora = []

	for flora in questCollectionReader.collectionQuestLineItems('flora_compendium'):
		if flora not in floraDenyList:
			craftedFlora.append(flora)
			shapelessRecipeContent += kubejs.shapeless(flora, [flora, paymentItem], craftOutputNumber)

	with open(os.path.join(const.serverScripts(), 'flora_duplication_crafting.js'), 'w') as f:
		f.write(kubejs.recipeFileContent(shapelessRecipeContent))

	fcTrans.setDefaultTranslationParent(transParent)
	with open(os.path.join(const.clientScripts(), 'flora_duplication_tooltips.js'), 'w') as tooltipFile:
		tooltipFile.write(kubejs.tooltipFileContent(kubejs.eventAddTranslatedTooltips(craftedFlora, [
			"You can craft more of this flora with bone meal"
		])))
	fcTrans.resetDefaultTranslationParent()
