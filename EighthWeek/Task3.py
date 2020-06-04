print(
    min(
        max(
            map(
                lambda x: (x % 2 == 1),
                input().split()
            )
        )
    )
)
