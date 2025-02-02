import json
import sys
from typing import Dict

LIB_DIRS = ["."]

if __name__ == "__main__":
    files = sys.argv[1:]  # changed files

    dirs_to_run: Dict[str, set] = {
        "lint": set(),
        "test": set(),
    }

    # Always check all files until there are multiple projects in this repository.
    dirs_to_run["test"].update(LIB_DIRS)
    dirs_to_run["lint"].update(LIB_DIRS)

    """
    if len(files) == 300:
        # max diff length is 300 files - there are likely files missing
        raise ValueError("Max diff reached. Please manually run CI on changed libs.")

    for file in files:
        if any(
            file.startswith(dir_)
            for dir_ in (
                "pyproject.toml",
                "poetry.lock",
                ".github/workflows",
                ".github/tools",
                ".github/actions",
                ".github/scripts/check_diff.py",
            )
        ):
            # add all LIB_DIRS for infra changes
            dirs_to_run["test"].update(LIB_DIRS)
            dirs_to_run["lint"].update(LIB_DIRS)

        if any(file.startswith(dir_) for dir_ in LIB_DIRS):
            for dir_ in LIB_DIRS:
                if file.startswith(dir_):
                    dirs_to_run["test"].add(dir_)
                    dirs_to_run["lint"].add(dir_)
        elif file.startswith("libs/"):
            raise ValueError(
                f"Unknown lib: {file}. check_diff.py likely needs "
                "an update for this new library!"
            )
    """

    outputs = {
        "dirs-to-lint": list(dirs_to_run["lint"]),
        "dirs-to-test": list(dirs_to_run["test"]),
    }
    for key, value in outputs.items():
        json_output = json.dumps(value)
        print(f"{key}={json_output}")  # noqa: T201
