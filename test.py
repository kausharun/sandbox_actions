## THIS IS A TEST ACTION WORKFLOW (JOB)
from datetime import date


def print_date():
    today = date.today()
    print(f"Today's date is {today}")


def main():
    print("\n\nHey Kaushik, good afternoon!\n\n")
    print_date()


if __name__ == "__main__":
    main()
