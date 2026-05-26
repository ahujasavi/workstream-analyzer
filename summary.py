import csv
from collections import defaultdict

STATUS_ORDER = ["Green", "Amber", "Red"]


def load_workstreams(filepath):
    # Reads the CSV file and returns a list of rows as dictionaries.
    with open(filepath, newline="") as f:
        return list(csv.DictReader(f))


def group_by_status(workstreams):
    # Organizes workstreams into a dict keyed by their status.
    groups = defaultdict(list)
    for ws in workstreams:
        groups[ws["status"]].append(ws)
    return groups


def print_attention(groups):
    # Prints a warning block at the top listing any Red workstreams.
    red_items = groups.get("Red", [])
    if red_items:
        print("⚠️  NEEDS ATTENTION")
        print("=" * 55)
        for ws in red_items:
            print(f"  {ws['name']:<25} {ws['owner']:<15} due {ws['due_date']}")
        print("=" * 55)


def print_summary(groups):
    # Prints each status group with its workstreams formatted as a table.
    status_emoji = {"Green": "🟢", "Amber": "🟡", "Red": "🔴"}
    for status in STATUS_ORDER:
        items = groups.get(status, [])
        label = status_emoji.get(status, "") + f" {status} ({len(items)})"
        print(f"\n{label}")
        print("-" * 55)
        for ws in items:
            print(
                f"  {ws['name']:<25} {ws['owner']:<15} "
                f"{ws['percent_done']:>3}%  due {ws['due_date']}"
            )


if __name__ == "__main__":
    workstreams = load_workstreams("workstreams.csv")
    groups = group_by_status(workstreams)
    print("=== Workstream Summary ===")
    print_attention(groups)
    print_summary(groups)
    print()
