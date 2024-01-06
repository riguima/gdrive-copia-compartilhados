import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tinydb import TinyDB

db = TinyDB("db.json")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)


def create_folder(metadata):
    file_metadata = {
        "title": metadata["title"],
        "parents": [{"id": parent} for parent in get_parents(metadata)],
        "mimeType": "application/vnd.google-apps.folder",
    }
    folder = drive.CreateFile(file_metadata)
    folder.Upload()
    return folder


def get_parents(metadata):
    parents = []
    for parent in db.all():
        if parent.keys()[0] in metadata["parents"]:
            parents.append(parent.values()[0])
    return parents


def create_files(query):
    for metadata in drive.ListFile({"q": query}).GetList():
        if metadata["shared"]:
            if metadata["mimeType"] == "application/vnd.google-apps.folder":
                if metadata["parents"]:
                    folder = create_folder(metadata)
                else:
                    folder = create_folder(metadata)
                db.insert({metadata["id"]: folder["id"]})
                create_files(f"'{metadata["id"]}' in parents and trashed=false")
            else:
                file = drive.CreateFile({"id": metadata["id"]})
                file.GetContentFile(file["title"])
                file_metadata = {
                    "title": metadata["title"],
                    "parents": [{"id": parent} for parent in get_parents(metadata)],
                }
                new_file = drive.CreateFile(file_metadata)
                new_file.SetContentFile(file["title"])
                new_file.Upload()
                os.remove(file["title"])


if __name__ == "__main__":
    create_files("")
