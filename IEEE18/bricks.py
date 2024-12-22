def minimum_stacks(N, x, bricks):
    # Sort bricks in ascending order
    bricks.sort()

    # Initialize stacks (each stack is represented as a list)
    stacks = []

    for brick in bricks:
        placed = False

        # Try to place the brick on an existing stack
        for stack in stacks:
            if stack[-1] + x <= brick:
                stack.append(brick)
                placed = True
                break

        # If it can't be placed on any existing stack, create a new stack
        if not placed:
            stacks.append([brick])

    # Output the result
    print(len(stacks))
    for stack in stacks:
        print(len(stack), *reversed(stack))


# Example input
N = 9
x = 3
bricks = [8, 4, 2, 5, 10, 8, 1, 7, 4]

minimum_stacks(N, x, bricks)
def minimum_stacks(N, x, bricks):
    # Sort bricks in ascending order
    bricks.sort()

    # Initialize stacks (each stack is represented as a list)
    stacks = []

    for brick in bricks:
        placed = False

        # Try to place the brick on an existing stack
        for stack in stacks:
            if stack[-1] + x <= brick:
                stack.append(brick)
                placed = True
                break

        # If it can't be placed on any existing stack, create a new stack
        if not placed:
            stacks.append([brick])

    # Output the result
    print(len(stacks))
    for stack in stacks:
        print(len(stack), *stack)


# Example input for testing
N, x = map(int, input().split())
bricks = list(map(int, input().split()))

minimum_stacks(N, x, bricks)