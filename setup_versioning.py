import subprocess
import sys


def get_last_version():
    bash_command = "git describe --tags --abbrev=0 --match v[0-9]*"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    outputstr = str(output)
    outputstr = outputstr[3:-3]  # "b'vXX.XX.XX\\n'" becomes "XX.XX.XX"
    outputstr = outputstr.replace('-', '.')
    major, minor, patch, *_ = outputstr.split('.')
    version = f'{major}.{minor}.{patch}'
    return version


def bump_patch(version: str):
    major, minor, patch = version.split('.')
    bumped = str(int(patch) + 1)
    return f'{major}.{minor}.{bumped}'


def push_new_version_as_tag(version):
    bash_command = f"git tag v{version}"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bash_command = f"git push origin v{version}"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


if __name__ == '__main__':
    if sys.argv[1] == 'push':
        last_version = get_last_version()
        version = bump_patch(last_version)
        push_new_version_as_tag(version)
