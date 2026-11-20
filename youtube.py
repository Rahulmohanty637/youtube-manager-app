import json

file_name = "youtube.txt"


def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} duration: {video['time']}")
    print("*" * 70)


def add_video(videos):
    name = input("Enter the name of video: ")
    time = input("Enter the time of vide: ")

    videos.append({"name": name, "time": time})
    save_data(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))

    if 1 <= index <= 5:
        name = input("Enter new name: ")
        time = input("Enter new duration: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data(videos)
    else:
        print("Invalid index")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))

    if 1 <= index <= 5:
        del videos[index - 1]
        save_data(videos)
        print("Video deleted")
    else:
        print("Invalid index")


def main():
    videos = []
    while True:
        print("\n Youtube Manager APP | Choose an option")
        print("1. List all youtube videos ")
        print("2. Add a new youtube video ")
        print("3. Update the youtube video details ")
        print("4. Delete the youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match (choice):
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
