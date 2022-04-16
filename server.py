import strike
import flask
import requests
import db
import twitter
import mapper
import config
from flask import jsonify
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# The public API link of the hosted server has to be added here.
# Use ngrok to easily make your api public
baseAPI=config.baseAPI

@app.route('/', methods=['POST'])
def home():
    
    data = request.get_json()
    name=data["bybrisk_session_variables"]["username"]
    ## Create a strike object
    strikeObj = strike.Create("getting_started",baseAPI+"/tweet")


    # First Question: Whats your name?
    quesObj1 = strikeObj.Question("issue").\
                QuestionText().\
                SetTextToQuestion("नमस्कार "+name+"! कृपया अपनी समस्या बताएं?")

    quesObj1.Answer(False).AnswerCardArray(strike.VERTICAL_ORIENTATION).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"लेट चल रही ट्रेन की समस्या\nTrain running late","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"वातानुकूलित कोच के ए.सी. में समस्या\nA.C not working","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"ट्रेन के कोच की लाइट में समस्या\nLights not working","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"ट्रेन में सामान की चोरी\nTheft of passengers belongings/snatching","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"सामान पीछे छूट गया\nLuggage left behind","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"सामान का दावा नहीं\nUnclaimed luggage found","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"संदिग्ध वस्तुएं\nSuspected articles found","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"भिखारी द्वारा उपद्रव\nNuisance by beggar","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"हिजड़ा द्वारा उपद्रव\nNuisance by eunuch","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"यात्री द्वारा उपद्रव\nNuisance by passenger","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"कोच शौचालय की सफाई समस्या\nToilets not clean","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"कोच की आंतरिक सफाई की समस्या\nCoach interior not clean","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"ट्रेन के कोच में पानी की समस्या\nNo water in coach","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"भोजन और खानपान सेवा में समस्या\nIssues in catering & vending services","#4a5566",True)

    questionObj2 = strikeObj.Question("train_no").\
                QuestionText().\
                SetTextToQuestion("कृपया अपना ट्रेन नंबर प्रदान करें")

    questionObj2.Answer(False).NumberInput()

    questionObj3 = strikeObj.Question("pnr").\
                QuestionText().\
                SetTextToQuestion("आपका पीएनआर (PNR) क्या है?")

    questionObj3.Answer(False).NumberInput()              
    return jsonify(strikeObj.Data())



@app.route('/tweet', methods=['POST'])
def tweet():

    data = request.get_json()
    name = data["bybrisk_session_variables"]["username"]
    userID = data["bybrisk_session_variables"]["userId"]
    issue = data["user_session_variables"]["issue"][0]
    train_no = data["user_session_variables"]["train_no"]
    pnr = data["user_session_variables"]["pnr"]
    phone = data["bybrisk_session_variables"]["phone"]

    ## Get settings from db
    res = db.get_data_from_db(userID)

    issues = issue.split("\n")
    issues_in_hindi = mapper.get_bot_to_tweet_hindi(issues[0])
    issues_in_english = mapper.get_bot_to_tweet_english(issues[1])

    tweetmsg = "Hi I'm "+name+" travelling on "+train_no+". "+issues_in_english+" My PNR - "+pnr

    if res[2] == "Hindi":
        tweetmsg = "मेरा नाम "+name+" है और में रेल गाड़ी संख्या - "+train_no+" में हूँ | "+issues_in_hindi+" मेरा पीएनआर (PNR) - "+pnr
        if res[1] == "True":
            tweetmsg = tweetmsg + "\nमेरा फ़ोन नंबर - "+phone
    else:
       if res[1] == "True":
            tweetmsg = tweetmsg + "\nMy contact number - "+phone            
    
    ## Tweet the data
    # twitter.tweet(tweetmsg)
    ##id = twitter.tweet("Testing a railway bot3")
    id = "12324"

    tweetmsg = tweetmsg +"\n\n"+config.baseTwitterLink+id

    strikeObj = strike.Create("getting_started", baseAPI)

    question_text = strikeObj.Question("sub_topic").\
                QuestionCard().\
                SetHeaderToQuestion(1,strike.HALF_WIDTH).\
                AddTextRowToQuestion(strike.H4,tweetmsg,"#4a5566",False)



    return jsonify(strikeObj.Data())

@app.route('/get-setting', methods=['POST'])
def getSetting():
    data = request.get_json()
    name = data["bybrisk_session_variables"]["username"]
    
    strikeObj = strike.Create("getting_started", baseAPI+"/save-setting")

    question_text = strikeObj.Question("settings").\
                QuestionText().\
                SetTextToQuestion("नमस्कार "+name+"! आपका ट्वीट भेजते समय हमें किन बातों का ध्यान रखना चाहिए?\n(Multiple select)")

    question_text.Answer(True).AnswerCardArray(strike.VERTICAL_ORIENTATION).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"मोबाइल नंबर प्रदर्शित करें\nDisplay mobile number","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"हिंदी में ट्वीट करें\nTweet in Hindi","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"मोबाइल नंबर प्रदर्शित नहीं करें\nDon't display mobile number","#4a5566",True).\
    AnswerCard().SetHeaderToAnswer(1,strike.HALF_WIDTH).AddTextRowToAnswer(strike.H4,"अंग्रेजी में ट्वीट करें\nTweet in English","#4a5566",True)


    return jsonify(strikeObj.Data())

@app.route('/save-setting', methods=['POST'])
def saveSetting():

    ## save data to RDS
    data = request.get_json()
    userID = data["bybrisk_session_variables"]["userId"]
    settings = data["user_session_variables"]["settings"]
    showNumber = "False"
    language = "English"
    
    for setting in settings:
        if setting == "मोबाइल नंबर प्रदर्शित करें\nDisplay mobile number":
            showNumber = "True"
        if setting == "हिंदी में ट्वीट करें\nTweet in Hindi":
            language = "Hindi"
        if setting == "मोबाइल नंबर प्रदर्शित नहीं करें\nDon't display mobile number":
            showNumber = "False"
        if setting == "अंग्रेजी में ट्वीट करें\nTweet in English":
            language = "English"      

    db.save_setting_to_db(userID,showNumber,language)
    
    strikeObj = strike.Create("getting_started", "")

    question_text = strikeObj.Question("").\
                QuestionText().\
                SetTextToQuestion("सेटिंग अपडेट कर दी गई है\nThe setting has been updated")

    return jsonify(strikeObj.Data())    

app.run(host='0.0.0.0', port=5001)