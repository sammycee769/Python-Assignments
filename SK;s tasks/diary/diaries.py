from diary import Diary

class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def find_diary_by_username(self, username):
        username = username.strip()
        for diary in self.diaries:
            if diary.get_user_name() == username:
                return diary
        raise ValueError("Diary not found")

    def delete_diary(self, username, password):
        diary = self._find_diary(username, password)
        self.diaries.remove(diary)

    def _find_diary(self, username, password):
        diary = self.find_diary_by_username(username)
        diary.validate_password(password)
        return diary