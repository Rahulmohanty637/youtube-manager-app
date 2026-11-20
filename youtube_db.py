import sqlite3

con = sqlite3.connect("youtube.db")
cursor = con.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )
            """)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()

    if not rows:
        print("The table is empty")
        return

    for row in rows:
        print(row)


def add_video():
    name = input("Enter the name of the video: ")
    time = input("Enter the duration of the video: ")

    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()


def update_video():
    video_id = int(input("Enter the id: "))
    new_name = input("Enter your new name: ")
    new_time = input("Enter your new time: ")

    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    con.commit()


def delete_video():
    video_id = int(input("Enter the id: "))
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("\n Youtube Manager APP | Choose an option")
        print("1. List all youtube videos ")
        print("2. Add a new youtube video ")
        print("3. Update the youtube video details ")
        print("4. Delete the youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match (choice):
            case "1":
                list_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                break
            case _:
                print("Invalid Choice")

    con.close()


if __name__ == "__main__":
    main()
