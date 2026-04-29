import os
from datetime import datetime

class JournalManager:
    """
    Encapsulates all journal file operations using OOP principles.
    """
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        """Appends a new entry with a timestamp to the file."""
        entry_text = input("\nEnter your journal entry: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            # Using 'a' mode to append. It creates the file if it doesn't exist.
            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}] {entry_text}\n")
            print("Entry saved successfully!")
        except PermissionError:
            print("Error: You do not have permission to write to this file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_all_entries(self):
        """Reads and displays all entries from the file."""
        try:
            # Using 'r' mode to read.
            with open(self.filename, "r") as file:
                content = file.read()
                if not content:
                    print("\nThe journal is currently empty.")
                else:
                    print("\n--- Your Journal Entries ---")
                    print(content)
        except FileNotFoundError:
            print("\nError: No journal file found. Try adding an entry first.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def search_entry(self):
        """Searches for a specific keyword or date in the file."""
        keyword = input("\nEnter keyword or date (YYYY-MM-DD) to search for: ").lower()
        found = False
        
        try:
            with open(self.filename, "r") as file:
                print("\n--- Search Results ---")
                for line in file:
                    if keyword in line.lower():
                        print(line.strip())
                        found = True
                
                if not found:
                    print(f"No entries found containing '{keyword}'.")
        except FileNotFoundError:
            print("\nError: Journal file does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_journal(self):
        """Prompts for confirmation and deletes the journal file."""
        if not os.path.exists(self.filename):
            print("\nError: No journal file exists to delete.")
            return

        confirm = input("\nAre you sure you want to delete ALL entries? (yes/no): ").lower()
        if confirm == 'yes':
            try:
                os.remove(self.filename)
                print("Journal file deleted successfully.")
            except Exception as e:
                print(f"An error occurred while deleting: {e}")
        else:
            print("Deletion cancelled.")

def main():
    manager = JournalManager()
    
    while True:
        print("\n--- Personal Journal: File Operator ---")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            manager.add_entry()
        elif choice == '2':
            manager.view_all_entries()
        elif choice == '3':
            manager.search_entry()
        elif choice == '4':
            manager.delete_journal()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()