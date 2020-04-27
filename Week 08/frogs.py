def get_lilies(n, goal=False):
    left = '>'
    right = '<'

    if goal:
        left, right = right, left

    return n * left + '_' + n * right


def find_possible_moves(lake):
    result = set()
    empty_pad_position = lake.index('_')

    for i in range(len(lake)):
        frog_goes_right = lake[i] == '>'
        frog_goes_left = lake[i] == '<'

        if frog_goes_right:
            empty_pad_distance = empty_pad_position - i
        elif frog_goes_left:
            empty_pad_distance = i - empty_pad_position
        else:
            empty_pad_distance = 0

        can_swap = 0 < empty_pad_distance < 3

        # swap empty pad and frog
        if frog_goes_right and can_swap:
            start = lake[:i] + '_'
            if empty_pad_distance == 2:
                result.add(start + lake[i + 1] + lake[i] + lake[i + 3:])
            elif empty_pad_distance == 1:
                result.add(start + lake[i] + lake[i + 2:])
            else:
                raise Exception("empty pad is considered nearby when it's not")

        if frog_goes_left and can_swap:
            end = '_' + lake[i + 1:]
            if empty_pad_distance == 2:
                result.add(lake[:i - 2] + lake[i] + lake[i - 1] + end)
            elif empty_pad_distance == 1:
                result.add(lake[:i - 1] + lake[i] + end)
            else:
                raise Exception("empty pad is considered nearby when it's not")

    return result


def dfs(stack, goal, history, done):
    lake = stack[-1]

    if lake in done and history[-1] == lake:
        history.pop()
        stack.pop()
        return dfs(stack, goal, history, done)
    else:
        done.add(lake)
        history.append(lake)

        moves = find_possible_moves(lake)

        if goal not in moves:
            stack.extend(moves)
            return dfs(stack, goal, history, done)

        history.append(goal)
        return history


def frogs(n):
    assert n % 2
    assert n > 2

    lake = get_lilies(n // 2)
    goal_lake = get_lilies(n // 2, goal=True)
    return dfs([lake], goal_lake, [], set())


def main():
    solution = frogs(9)

    for line in solution:
        print(' '.join(list(line)))


if __name__ == '__main__':
    main()
