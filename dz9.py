from abc import ABC, abstractmethod
from typing import Dict, Any

class MediaFile(ABC):
    def __init__(self, name: str, size: int, creation_date: str, owner: str):
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner

    @abstractmethod
    def get_metadata(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def convert(self, target_format: str):
        pass

class AudioFile(MediaFile):
    def __init__(self, name: str, size: int, creation_date: str, owner: str, bitrate: int):
        super().__init__(name, size, creation_date, owner)
        self.bitrate = bitrate

    def get_metadata(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "size": self.size,
            "creation_date": self.creation_date,
            "owner": self.owner,
            "bitrate": self.bitrate
        }

    def save(self):
        pass

    def delete(self):
        pass

    def convert(self, target_format: str):
        pass

class VideoFile(MediaFile):
    def __init__(self, name: str, size: int, creation_date: str, owner: str, resolution: str):
        super().__init__(name, size, creation_date, owner)
        self.resolution = resolution

    def get_metadata(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "size": self.size,
            "creation_date": self.creation_date,
            "owner": self.owner,
            "resolution": self.resolution
        }

    def save(self):
        pass

    def delete(self):
        pass

    def convert(self, target_format: str):
        pass

class PhotoFile(MediaFile):
    def __init__(self, name: str, size: int, creation_date: str, owner: str, dimensions: str):
        super().__init__(name, size, creation_date, owner)
        self.dimensions = dimensions

    def get_metadata(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "size": self.size,
            "creation_date": self.creation_date,
            "owner": self.owner,
            "dimensions": self.dimensions
        }

    def save(self):
        pass

    def delete(self):
        pass

    def convert(self, target_format: str):
        pass

class LocalFileStorage:
    def save_file(self, file: MediaFile):
        print(f"Сохраняем файл {file.name} локально")

    def delete_file(self, file: MediaFile):
        print(f"Удаляем файл {file.name} локально")

class CloudFileStorage:
    def save_file(self, file: MediaFile):
        print(f"Сохраняем файл {file.name} в облаке")

    def delete_file(self, file: MediaFile):
        print(f"Удаляем файл {file.name} из облака")

class S3FileStorage:
    def save_file(self, file: MediaFile):
        print(f"Сохраняем файл {file.name} на S3")

    def delete_file(self, file: MediaFile):
        print(f"Удаляем файл {file.name} с S3")

if __name__ == "__main__":
    audio = AudioFile(name="song.mp3", size=5000, creation_date="2025-01-01", owner="User1", bitrate=320)
    video = VideoFile(name="movie.mp4", size=200000, creation_date="2025-01-02", owner="User2", resolution="1920x1080")
    photo = PhotoFile(name="image.jpg", size=1500, creation_date="2025-01-03", owner="User3", dimensions="1024x768")

    local_storage = LocalFileStorage()
    local_storage.save_file(audio)
    local_storage.delete_file(audio)

    cloud_storage = CloudFileStorage()
    cloud_storage.save_file(video)
    cloud_storage.delete_file(video)

    s3_storage = S3FileStorage()
    s3_storage.save_file(photo)
    s3_storage.delete_file(photo)