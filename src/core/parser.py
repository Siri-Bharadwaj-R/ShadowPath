import json

from ..core.models import Relationship


def load_relationships(file_path: str):
    """
    Load relationships from a JSON file.
    """

    with open(file_path, "r") as file:
        data = json.load(file)

    relationships = []

    for relationship in data["relationships"]:
        relationships.append(
            Relationship(
                source=relationship["from"],
                target=relationship["to"]
            )
        )

    return relationships