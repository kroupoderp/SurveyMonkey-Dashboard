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
    surveys = []
    for survey in resp["data"]:
        surveys.append(survey["title"])
    return surveys

if __name__ == "__main__":
    getSurveys()