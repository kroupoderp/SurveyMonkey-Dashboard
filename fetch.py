import requests, json

access_token = 'xGXDyPakeNjQedIC4BTUQcgjknJ-MK-s.0x0Ap51iGOXnNHDjYPGDTkt6PSEycjqvlNEspmq0s2gbzkMXQnD.4n2AnQ9G2DsYjhaiFFYMCJcCM.87kITTBft8YHHCfOi'
url = "https://api.surveymonkey.com/v3/surveys"

request_headers = {
    'Content-Type': "application/json",
    'Authorization': f'bearer {access_token}'
}

def query():
    d = requests.get(url, headers=request_headers).text
    json_frmt = json.loads(d)
    return json_frmt

def getSurveys():
	    resp = query()
	    surveys = {}
	    for survey in resp["data"]:
	        surveys[survey["title"]] = survey["id"]
	    return surveys
	
def getQuestions(survey_id):
    questions = []
    d = requests.get(url + f'/{survey_id}/details', headers=request_headers).text
    json_frmt = json.loads(d)

    if len(json_frmt["pages"]) == 1:
        print("EXECUTED")
        for dataset in json_frmt["pages"][0]["questions"]:
            questions.append(dataset["headings"][0]["heading"])
        return questions
    else:
        for page in json_frmt["pages"]:
            for dataset in page["questions"]:
                questions.append(dataset["headings"][0]["heading"])
        return questions


if __name__ == "__main__":
    print(getQuestions("188231210"))