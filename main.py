from datetime import timedelta


def main():
    make_coffee = Task(
        task_name="Make coffee",
        active_time=timedelta(minutes=1),
        idle_time=timedelta(minutes=4),
    )

    make_toast = Task(
        task_name="Make toast",
        active_time=timedelta(seconds=10),
        idle_time=timedelta(minutes=2),
    )

    all_tasks = [make_coffee, make_toast]

    longest_idle = timedelta(0)
    for task in all_tasks:
        if task.idle_time > longest_idle:
            longest_idle = task

    print(f"Longest idle time: {task.longest_idle}")
    print(f"Starting task: {task.task_name}")


if __name__ == "__main__":
    main()
