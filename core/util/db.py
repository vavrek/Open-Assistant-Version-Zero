import sqlite3
import json

#from importlib import reload


class DB:
    def __init__(self, path=None):
        self.path = ":memory:" if path is None else path
        self.db = sqlite3.connect(self.path)
        
    def create_schema(self):
        self.db.execute("CREATE TABLE IF NOT EXISTS Prompt (Prompt TEXT)")
        self.db.execute("CREATE TABLE IF NOT EXISTS Command (Command TEXT)")
        self.db.execute("CREATE TABLE IF NOT EXISTS PromptCommand (PromptID INT, CommandID INT)")
        self.db.commit()
        
    def add_action(self, prompt, command):
        p = self.db.execute("SELECT rowid FROM Prompt WHERE Prompt = ?", (prompt,)).fetchone()
        if p is None:
            prompt_id = self.db.execute("INSERT INTO Prompt (Prompt) VALUES (?)", (prompt,)).lastrowid
        else:
            prompt_id = p[0]

        c = self.db.execute("SELECT Command FROM Command WHERE Command = ?", (command,)).fetchone()
        if c is None:
            command_id = self.db.execute("INSERT INTO Command (Command) VALUES (?)", (command,)).lastrowid
        else:
            command_id = c[0]
            
        action_id = self.db.execute("SELECT PromptID, CommandID FROM PromptCommand WHERE PromptID=? AND CommandID=?", (prompt_id, command_id)).fetchone()
        if action_id is None:
            self.db.execute("INSERT INTO PromptCommand (PromptID, CommandID) VALUES (?, ?)", (prompt_id, command_id))
            
        self.db.commit()
        
    def get_action(self, prompt):
        action = self.db.execute("SELECT Command FROM Command INNER JOIN PromptCommand ON PromptCommand.CommandID = Command.rowid INNER JOIN Prompt ON Prompt.rowid = PromptCommand.rowid WHERE Prompt = ?", (prompt,)).fetchone()
        if action is not None:
            return action[0]
            
    def get_prompts(self):
        for prompt in self.db.execute("SELECT Prompt FROM Prompt"):
            yield prompt[0]
        
    def load_commands(self, path):
        pass