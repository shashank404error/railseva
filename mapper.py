def get_bot_to_tweet_hindi(msg):
 return bot_msg_hindi[msg]

def get_bot_to_tweet_english(msg):
  return bot_msg_english[msg]

bot_msg_hindi = {
	  "लेट चल रही ट्रेन की समस्या": "यह ट्रेन अपने तय समय से बहुत देरी से चल रही है | कृपया समाधान निकालें |",
    "वातानुकूलित कोच के ए.सी. में समस्या": "इस गाड़ी के वातानुकूलित कोच का ए.सी  काम नहीं कर रहा है | कृपया सहायता करें |"
    # "ट्रेन के कोच की लाइट में समस्या":
    # "ट्रेन में सामान की चोरी":
    # "सामान पीछे छूट गया":
    # "सामान का दावा नहीं":
    # "संदिग्ध वस्तुएं":
    # "भिखारी द्वारा उपद्रव":
    # "हिजड़ा द्वारा उपद्रव":
    # "यात्री द्वारा उपद्रव":
    # "कोच शौचालय की सफाई समस्या":
    # "कोच की आंतरिक सफाई की समस्या":
    # "ट्रेन के कोच में पानी की समस्या":
    # "भोजन और खानपान सेवा में समस्या":
  }

bot_msg_english = {
    "Train running late":"The train is running a lot late, please help!",
    "A.C not working":"The A.C of my coach is not working, concerned authorities please look into it!"
    # "Lights not working":
    # "Theft of passengers belongings/snatching":
    # "Luggage left behind":
    # "Unclaimed luggage found":
    # "Suspected articles found":
    # "Nuisance by beggar":
    # "Nuisance by eunuch":
    # "Nuisance by passenger":
    # "Toilets not clean":
    # "Coach interior not clean":
    # "No water in coach":
    # "Issues in catering & vending services":
}