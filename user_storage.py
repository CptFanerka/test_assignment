import os
from fnmatch import fnmatch
import json
import quest_storage


class FileStorage():
    path = 'saves/'


    @classmethod
    def findByEmail(self, email):
        for path, _, files in os.walk(self.path):
            for filename in files:
                full_name = os.path.join(path, filename)
                if fnmatch(full_name, self.path+email+'.json'):
                    return True
        return False

    @classmethod
    def checkMove(self, CurrentStage, FormStageCode):
        return FormStageCode in CurrentStage.cases

    @classmethod
    def saveUserProgress(self, email, QuestStageCode):
        file = open(self.path + email + '.json', 'w')
        jsonStr = json.dumps(QuestStageCode, ensure_ascii=False)
        file.write(jsonStr)
        file.close()

    @classmethod
    def loadUserProgress(self, email):
        stages = quest_storage.FileStorage.load()
        with open(self.path + email + '.json', 'r', encoding='cp1251', errors='ignore') as file:
            questCode = json.load(file)
        for i in range(len(stages)):
            temp = stages[i]['_code']
            if temp == questCode:
                quest = quest_storage.QuestStage()
                quest.code = stages[i]['_code']
                quest.name = stages[i]['_name']
                quest.body = stages[i]['_body']
                quest.cases = stages[i]['_cases']
                return quest
        raise Exception('UserProgress is not found')


    @classmethod
    def listNextStagesCode(self, email):
        currentStage = FileStorage.loadUserProgress(email)
        return currentStage.cases


    @classmethod
    def listNextStagesName(self, casesList):
        stages = quest_storage.FileStorage.load()
        namesList = []
        for i in range(len(casesList)):
            for j in range(len(stages)):
                if casesList[i] == stages[j]['_code']:
                    namesList.append(stages[j]['_name'])
        return namesList
