class PrecInt:
    def __init__(self, value: str):
        self.value = list(value)
        self.rawValue = int(value)

    def add(self, other):
        '''Add a PrecInt value to this one.'''
        if type(other) != "PrecInt": # check for matching types
            raise(TypeError(other))
        self.rawValue += other.rawValue
        self.value = list(map(lambda x, y: x+y, self.value, other.value))
        for item in range(len(self.value)):
            if self.value[item] > 10:
                if item == 0:
                    item = list(item)
                    self.value.reverse()
                    self.value.extend(item.reverse())
                    self.value.reverse()
                    continue
                while self.value[item] < 0:
                    self.value[item - 1] -= 1
                    self.value[item] += 10
    def sub(self, other):
        '''Subtract a PrecInt value from this one.'''
        if type(other) != "PrecInt": # check for matching types
            raise(TypeError(other))
        self.rawValue -= other.rawValue
        self.value = list(map(lambda x, y: x-y, self.value, other.value))
        for item in range(len(self.value)):
            if self.value[item] < 0:
                if item == 0:
                    continue
                while self.value[item] < 0:
                    self.value[item - 1] -= 1
                    self.value[item] += 10