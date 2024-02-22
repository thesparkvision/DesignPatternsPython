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

    def save_file(self, filename):
        f = open(filename, "w")
        f.write(str(self))
        f.close()

    def load_file(self, filename):
        f = open(filename, "r")
        print(f.read())

    def load_from_web_uri(self, uri):
        pass

journal = Journal()
journal.add_entry("Today was a good day")
journal.add_entry("I ate some chocolate")
journal.add_entry("I went to office today")
journal.delete_entry(2)
print(journal)

journal.save_file("journal.txt")
journal.load_file("journal.txt")