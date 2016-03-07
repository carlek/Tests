# version 2.0 - remove 1.0 and properly handle rollback with database snapshots
# ( gone ... version 1.0 - stack commands with commit/rollback operating on stack.)
import sys
import copy
class SimpleDB:

    # Database and a Snapshot (stack) make up the class
    def __init__(self):
        self.database = {}
        self.snapshots = []

    # all methods for transactions
    def set(self, name, value):
        self.database[name] = value

    def get(self, name):
        if name in self.database:
            print(self.database[name])
        else:
            print('NULL')

    def unset(self, name):
        del self.database[name]

    def begin_block(self):
        self.snapshots.append(copy.deepcopy(self.database))

    def rollback(self):
        if self.snapshots:
            self.database = self.snapshots.pop()
        else:
            print('NO TRANSACTION')

    def commit(self):
        if self.snapshots:
            self.snapshots = []
        else:
            print('NO TRANSACTION')

    def numequalto(self, value):
        n = 0
        for k in self.database:
            if self.database[k] == value:
                n += 1
        print(n)

    def dump(self):
        for k in self.database:
            print(k, self.database[k])


if __name__ == '__main__':

    # initialize database
    db = SimpleDB()

    # process commands from stdin
    #f = open('input007.txt', 'r')
    #for line in f:
    for line in sys.stdin:
        if line.startswith('SET'):
            (cmd, name, value) = line.split()
            db.set(name, value)
            continue

        if line.startswith('GET'):
            (cmd, name) = line.split()
            db.get(name)
            continue

        if line.startswith('UNSET'):
            (cmd, name) = line.split()
            db.unset(name)
            continue

        if line.startswith('NUMEQUALTO'):
            (cmd, value) = line.split()
            db.numequalto(value)
            continue

        if line.startswith('BEGIN'):
            db.begin_block()
            continue

        if line.startswith('COMMIT'):
            db.commit()
            continue

        if line.startswith('ROLLBACK'):
            db.rollback()
            continue

        if line.startswith('END'):
            exit()

        if line.startswith('DUMP'):
            db.dump()
            continue

    #db.set('A', 1
    #db.set('B', 2)
    #db.commit()
    #db.print()
    pass
