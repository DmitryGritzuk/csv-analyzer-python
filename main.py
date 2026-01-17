def parse_numbers(s: str) -> list[float]:
    parts = [p.strip() for p in s.split(",") if p.strip() != ""]
    return [float(x) for x in parts]

def main():
    s = input().strip()
    nums = parse_numbers(s)

    count = len(nums)
    total = sum(nums)
    avg = total / count
    mx = max(nums)

    print(f"count: {count}")
    print(f"sum: {total}")
    print(f"avg: {avg:.2f}")
    print(f"max: {mx}")

if __name__ == "__main__":
    main()
