class Item:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
        self.item_type = "item"

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "type": self.item_type,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
    
    @staticmethod
    def from_dict(data):
        item_type = data.get("type")

        if item_type == "task":
            return Task(
                title=data["title"],
                description=data["description"],
                priority=data.get("priority", "Medium"),
                completed=data.get("completed", False),
            )
        
        elif item_type == "habit":
            return Habit(
                title=data["title"],
                description=data["description"],
                due_date=data.get("due_date", ""),
                completed=data.get("completed", False),
            )
        elif item_type == "deadline":
            return DeadlineTask(
                title=data["title"],
                description=data["description"],
                due_date=data.get("due_date", ""),
                completed=data.get("completed", False),
            )
        
        return Item(
            title=data["title"],
            description=data["description"],
            completed=data.get("completed", False),
        )

class Task(Item):
    def __init__(self, title, description, priority="Medium", completed=False):
        super().__init__(title, description, completed)
        self.priority = priority
        self.item_type = "task"
    
    def to_dict(self):
        data = super().to_dict()
        data["priority"] = self.priority
        return data
    
class Habit(Item):
    def __init__(self,title,description,due_date="",streak=0, completed=False):
        super().__init__(title, description, completed)
        self.streak = streak
        self.due_date = due_date
        self.item_type = "habit"

    def mark_complete(self):
        if not self.completed:
            self.completed = True
            self.streak += 1

    def to_dict(self):
        data = super().to_dict()
        data["streak"] = self.streak
        return data
    
class DeadlineTask(Item):
    def __init__(self, title, description, due_date="", completed=False):
        super().__init__(title, description, completed)
        self.due_date = due_date
        self.item_type = "deadline"

    def to_dict(self):
        data = super().to_dict()
        data["due_date"] = self.due_date
        return data