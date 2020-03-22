import json


class FileStorage():
    path = 'stages.json'
    
    def obj_dict(obj):
        return obj.__dict__
        
    @classmethod
    def save(self, quests: list):
        file = open(self.path, 'w')
        jsonStr = json.dumps(quests, ensure_ascii=False, default=self.obj_dict)
        file.write(jsonStr)
        file.close()

    @classmethod
    def load(self):
        with open(self.path, 'r', encoding='cp1251', errors='ignore') as file:
            data = json.load(file)
        return data


class QuestStage():
    _code: str
    _name: str
    _body: str
    _cases: list

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value: str):
        self._code = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value: str):
        self._body = value

    @property
    def cases(self):
        return self._cases

    @cases.setter
    def cases(self, value: list):
        self._cases = value
