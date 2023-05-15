#!/bin/bash

"""module that translates english to french and french to english"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = 'qyK7qn7zcpSwOSfb6krCG-VfAXcuikGc8XKGBkSaySUr'
URL = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/1dbb886a-3c93-45bc-80d6-2da152a343d6'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version= '2018-05-01', authenticator=authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    """function that translates english to french"""
    etext = english_text
    french_text = language_translator.translate(text = etext, source='English', target='French').get_result()
    frenchtextlst = french_text['translations']
    for key in frenchtextlst:
        keydic = key['translation']
    return keydic

def french_to_english(french_text):
    """function that translates english to french"""
    etext = french_text
    english_text = language_translator.translate(text = etext, source='French', target='English').get_result()
    englishtextlst = english_text['translations']
    for key in englishtextlst:
        keydic2 = key['translation']
    return keydic2
