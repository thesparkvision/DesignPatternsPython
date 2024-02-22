class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
    
    def delete_entry(self, pos):
        self.count -= 1
        self.entries.pop(pos)

    def __str__(self):
        return "\n".join(self.entries)

class PersistenceManager:
    def save_file(self, data, filename):
        f = open(filename, "w")
        f.write(data)
        f.close()

    def load_file(self, filename):
        f = open(filename, "r")
        return f.read()

    def load_from_web_uri(self, uri):
        pass

journal = Journal()
journal.add_entry("Today was a good day")
journal.add_entry("I ate some chocolate")
journal.add_entry("I went to office today")
journal.delete_entry(2)
print(journal)

persistence_manager = PersistenceManager()
persistence_manager.save_file(str(journal), "journal.txt")
print(persistence_manager.load_file("journal.txt"))