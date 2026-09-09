#!/usr/bin/env python3

import json
from pathlib import Path

NOTES_FILE = Path("notes.json")


def load_notes():
    if not NOTES_FILE.exists():
        return []

    try:
        return json.loads(NOTES_FILE.read_text())
    except (json.JSONDecodeError, OSError):
        return []


def save_notes(notes):
    NOTES_FILE.write_text(json.dumps(notes, indent=2))


def create_note(notes):
    text = input("Note: ").strip()

    if not text:
        print("Empty note.")
        return

    notes.append(text)
    save_notes(notes)
    print("Note saved.")


def list_notes(notes):
    if not notes:
        print("No notes yet.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")


def search_notes(notes):
    query = input("Search: ").strip().lower()

    for index, note in enumerate(notes, start=1):
        if query in note.lower():
            print(f"{index}. {note}")


def delete_note(notes):
    list_notes(notes)

    if not notes:
        return

    try:
        number = int(input("Delete note #: "))
        removed = notes.pop(number - 1)
        save_notes(notes)
        print(f"Deleted: {removed}")
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    notes = load_notes()

    while True:
        print("\nTerminal Notes")
        print("--------------")
        print("1. Create note")
        print("2. List notes")
        print("3. Search")
        print("4. Delete")
        print("5. Exit")

        choice = input("> ").strip()

        if choice == "1":
            create_note(notes)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            break
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()
