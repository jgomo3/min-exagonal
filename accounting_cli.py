import argparse

import accounting

parser = argparse.ArgumentParser(description='Tool for using the accounting system')
parser.add_argument('command', type=str, help='The command to perform')
parser.add_argument('args', type=int, nargs='+', help='The arguments for the command')

dispatcher = {
    'discount': accounting.Discounter().discount
}

args = parser.parse_args()

print(
    dispatcher[args.command](args.args[0])
)
