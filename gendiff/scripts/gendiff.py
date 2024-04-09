import gendiff.console as console
from gendiff import generate_diff


def main():
    args = console.get_console_args()
    report = generate_diff(args.first_file, args.second_file, args.format)
    print(report)


if __name__ == "__main__":
    main()
