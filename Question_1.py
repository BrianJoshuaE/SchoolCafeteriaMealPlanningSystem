"""School cafeteria meal planning system for Question 1."""


def process_records(records):
    """Process meal records and return grouped students and totals."""
    meal_to_students = {}
    meal_to_revenue = {}
    student_spending = {}

    for name, meal, daily_price in records:
        meal_to_students.setdefault(meal, [])
        if name not in meal_to_students[meal]:
            meal_to_students[meal].append(name)

        weekly_price = daily_price * 5
        meal_to_revenue[meal] = meal_to_revenue.get(meal, 0) + weekly_price
        student_spending[name] = student_spending.get(name, 0) + weekly_price

    return meal_to_students, meal_to_revenue, student_spending


def identify_high_spenders(student_spending, threshold=15000):
    """Return students whose weekly spending is above the threshold."""
    return [
        (name, spending)
        for name, spending in student_spending.items()
        if spending > threshold
    ]


def find_most_popular_meal(meal_to_students):
    """Return the meal with the most students and its student count."""
    if not meal_to_students:
        return None, 0

    meal, students = max(
        meal_to_students.items(), key=lambda item: len(item[1])
    )
    return meal, len(students)


def generate_report(
    records,
    meal_to_students,
    meal_to_revenue,
    student_spending,
    threshold=15000,
):
    """Print a formatted weekly cafeteria report."""
    print("=" * 60)
    print("CAFETERIA MEAL PLANNING SYSTEM - WEEKLY REPORT")
    print("=" * 60)
    print(f"Total student records processed: {len(records)}")

    print("\n--- MEAL PREFERENCES ---")
    for meal, students in meal_to_students.items():
        print(f"{meal}: {len(students)} student(s) - {', '.join(students)}")

    print("\n--- WEEKLY REVENUE PER MEAL (UGX) ---")
    total_revenue = 0
    for meal, revenue in meal_to_revenue.items():
        print(f"{meal}: {revenue:,} UGX")
        total_revenue += revenue
    print(f"Total weekly revenue: {total_revenue:,} UGX")

    print("\n--- STUDENT WEEKLY SPENDING (UGX) ---")
    for name, spending in student_spending.items():
        print(f"{name}: {spending:,} UGX")

    high_spenders = identify_high_spenders(student_spending, threshold)
    if high_spenders:
        print(f"\n--- STUDENTS SPENDING ABOVE {threshold:,} UGX PER WEEK ---")
        for name, spending in high_spenders:
            print(f"{name}: {spending:,} UGX")
    else:
        print(f"\nNo students spend above {threshold:,} UGX per week.")

    popular_meal, student_count = find_most_popular_meal(meal_to_students)
    print("\n--- MOST POPULAR MEAL ---")
    print(f"{popular_meal} with {student_count} student(s).")
    print("\n" + "=" * 60)
    print("END OF REPORT")
    print("=" * 60)


def collect_records():
    """Collect student meal records until the user chooses to continue."""
    records = []
    print("Enter student meal records one at a time.")

    while True:
        name = input("Student name: ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("Student name cannot be empty.")
            continue

        meal = input("Meal preference: ").strip()
        if not meal:
            print("Meal preference cannot be empty.")
            continue

        while True:
            price_text = input("Daily meal price (UGX): ").strip()
            try:
                daily_price = int(price_text)
            except ValueError:
                print("Please enter a whole number for the price.")
                continue
            if daily_price < 0:
                print("Price cannot be negative.")
                continue
            break

        records.append((name, meal, daily_price))
        print("Record added.\n")

        while True:
            add_another = input(
                "Record another student? (y/n): "
            ).strip().lower()
            if add_another in ("y", "n"):
                break
            print("Please enter y to add another student or n to continue.")
        if add_another == "n":
            break

    return records


def main():
    """Collect records, then generate the weekly cafeteria report."""
    print("SCHOOL CAFETERIA MEAL PLANNING SYSTEM")
    print("=" * 40)
    records = collect_records()
    if not records:
        print("No records entered. No report was generated.")
        return

    meal_to_students, meal_to_revenue, student_spending = process_records(
        records
    )
    generate_report(
        records,
        meal_to_students,
        meal_to_revenue,
        student_spending,
    )


if __name__ == "__main__":
    main()