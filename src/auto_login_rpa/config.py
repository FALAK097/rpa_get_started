from dataclasses import dataclass
import json

@dataclass
class LoginConfig:
    url: str
    username: str
    password: str

    @classmethod
    def from_json(cls, file_path: str):
        """Load configuration from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return cls(
                    url=data["LOGIN_URL"],
                    username=data["USERNAME"],
                    password=data["PASSWORD"]
                )
        except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
            print(f"Error loading configuration: {e}")
            raise
