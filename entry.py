class Entry:
    def __init__(self, title, description, due_date, priority, complete=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.complete = complete
    
    def change_description(description):
        self.description = description

    def completed(self):
        self.complete = True

    def change_due_date(due_date):
        self.due_date = due_date

    def change_priority(priority):
        self.priority = priority

    def __str__(self):
        return f"{self.title}({self.description})"
        
