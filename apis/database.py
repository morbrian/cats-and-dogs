import uuid

class Database:
    def __init__(self, seed_data):
        self.dictionary = seed_data

    def store(self, id, data):
        if (id is not None):
            data['id'] = id
            self.dictionary[id] = data
            return data
        elif (data.get('id') is not None):
            self.dictionary[data.get('id')] = data
            return data
        else:
            id = str(uuid.uuid4())
            data['id'] = id
            self.dictionary[id] = data
            return data
    
    def records(self):
        return list(self.dictionary.values())
    
    def fetch(self, id):
        return self.dictionary.get(id)
    
    def delete(self, id):
        return self.dictionary.pop(id, None)