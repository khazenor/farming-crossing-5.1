from src import const
from lib import fcTrans
from lib import questTrans
from lib import translationApi
from src import updateTransCache
from input import supportedLanugages
import json

engTextsUsedByModpack = []

def translateTexts():
	# print("updating language caches...")
	# updateTransCache.main()
	print('Translating modpack texts...')

	for transCode in supportedLanugages.languages:
		print(f'Translating {transCode}...')
		transModpackFeatureTexts(transCode)
		transQuests(transCode)

	print('Removing unused translations from cache ...')
	updateTransCache.removeUnusedTranslationFromCache(engTextsUsedByModpack)

def transModpackFeatureTexts(transCode):
	en_us = json.load(open(const.fcTransFileDir(const.engLangCode), 'r'))
	fcTrans.langCode = transCode
	for transKey in en_us:
		engText = en_us[transKey]
		engTextsUsedByModpack.append(engText)
		transText = translationApi.translate(engText, transCode)
		fcTrans.addTranslationsToJson(transKey, transText, transCode)

def transQuests(transCode):
	en_us = questTrans.loadSnbt(const.engLangCode)
	for transKey in en_us:
		engComponent = en_us[transKey]
		if type(engComponent) == list:
			transList = []
			for engText in engComponent:
				transList.append(translationApi.translate(engText, transCode))
				engTextsUsedByModpack.append(engText)
			questTrans.addTrans(transKey, transList, transCode)
		else:
			engTextsUsedByModpack.append(engComponent)
			transText = translationApi.translate(engComponent, transCode)
			questTrans.addTrans(transKey, transText, transCode)
