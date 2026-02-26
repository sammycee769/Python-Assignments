from entry import Entry

class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password.strip()
        self.is_locked = True
        self.entries = []

    def get_user_name(self):
        return self.username

    def get_number_of_entries(self):
        return len(self.entries)

    def check_lock_status(self):
        return self.is_locked

    def un_lock(self, password):
        self._validate_double_unlock()
        self.validate_password(password)
        self.is_locked = False

    def lock(self):
        self.is_locked = True

    def validate_password(self, password):
        if self.password != password.strip():
            raise ValueError("Invalid password")

    def create_entry(self, title, content):
        entry_id = len(self.entries) + 1
        entry = Entry(entry_id, title, content)
        self.entries.append(entry)

    def find_entry_by_id(self, entry_id):
        entry = self._find_entry(entry_id)
        return str(entry)

    def delete_entry(self, entry_id):
        self._validate_lock_status()
        entry = self._find_entry(entry_id)
        self.entries.remove(entry)

    def update_entry(self, entry_id, title, content):
        self._validate_lock_status()
        entry = self._find_entry(entry_id)
        self._resolve_update_to_entry(title, content, entry)

    def update_title(self, entry_id, title):
        self._validate_lock_status()
        entry = self._find_entry(entry_id)
        entry.set_title(title)

    def update_content(self, entry_id, content):
        self._validate_lock_status()
        entry = self._find_entry(entry_id)
        entry.set_content(content)

    def _find_entry(self, entry_id):
        for entry in self.entries:
            if entry.get_id() == entry_id:
                return entry
        raise ValueError("Entry not found")

    def _validate_double_unlock(self):
        if not self.is_locked:
            raise ValueError("Diary is already unlocked")

    def _validate_lock_status(self):
        if self.is_locked:
            raise ValueError("Diary is locked")

    def _resolve_update_to_entry(self, title, content, entry):
        self._validate_empty_update(title, content)
        updated_title = title if title.strip() != "" else entry.get_title()
        updated_content = content if content.strip() != "" else entry.get_content()
        entry.set_title(updated_title)
        entry.set_content(updated_content)

    def _validate_empty_update(self, title, content):
        if title.strip() == "" and content.strip() == "":
            raise ValueError("Title and Content cannot be empty")