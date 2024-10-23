"""Ensures that the files in `dist/` are prefixed with ${{ github.ref_name }}

Tag must adhere to naming convention of distributed files. For example, the tag
`dagster_modal-0.1.2` must match the prefix of the files in the `dist/` folder:

    -rw-r--r--@ 2.0K Oct 23 14:06 dagster_modal-0.1.2-py3-none-any.whl
    -rw-r--r--@ 1.6K Oct 23 14:06 dagster_modal-0.1.2.tar.gz

USAGE

    $ python ../../.github/validate-release-version.py dagster_modal-v0.1.3

"""

import sys
import os

RELEASE_DIRECTORY = "dist"

if len(sys.argv) != 2:
    print("Requires positional argument: <github.ref_name>")
    sys.exit(1)

github_ref_name = sys.argv[1]

if not os.path.exists(RELEASE_DIRECTORY):
    print("Release directory `dist/` must exist in cwd")
    sys.exit(1)

for filename in os.listdir(RELEASE_DIRECTORY):
    if not filename.startswith(github_ref_name):
        print(f"{filename} does not start with prefix {github_ref_name}")
        sys.exit(1)


print(f"Success: all files in `dist/` are prefixed with {github_ref_name}")