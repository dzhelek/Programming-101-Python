import json


class Jsonable:
    def to_json(self, indent=4):
        result = {"dict": self.__dict__, "type": type(self).__name__}
        return json.dumps(result, indent = indent)

    @classmethod
    def from_json(cls, json_string):
        return cls(json_string)
