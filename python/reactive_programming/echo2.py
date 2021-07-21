import sys
from rx import from_
from rx.operators import map


def main():
    argv = from_(sys.argv[1:]).pipe(map(lambda i: i.capitalize()))

    argv.subscribe(on_next=lambda i: print(f"on_next:{i}"),
                   on_error=lambda e: print(f"on_error{e}"),
                   on_completed=lambda: print("on_completed"))

    print("Done")


if __name__ == "__main__":
    main()
