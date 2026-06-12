import os

print(os.getcwd())

from core.parser import load_relationships


def main():
    relationships = load_relationships(
        "../data/sample_domain.json"
    )

    print("Loaded Relationships:\n")

    for relationship in relationships:
        print(
            f"{relationship.source} -> {relationship.target}"
        )


if __name__ == "__main__":
    main()