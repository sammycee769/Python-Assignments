from datetime import datetime

class Entry:
    def __init__(self, entry_id, title, content):
        self.id = entry_id
        self.title = title
        self.content = content
        self.date_created = datetime.now()

    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.content = content

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_date_created(self):
        return self.date_created.strftime("%d/%m/%Y %I:%M:%S %p")

    def __str__(self):
        return f"Entry ID: {self.id}\nTitle: {self.title}\nContent: {self.content}\nDate Created: {self.get_date_created()}"