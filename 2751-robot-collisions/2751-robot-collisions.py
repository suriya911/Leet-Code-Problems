class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):

        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])

        h = healths[:]
        alive = [True]*n
        stack = []

        for idx in order:

            if directions[idx] == 'R':
                stack.append(idx)

            else:
                while stack:

                    top = stack[-1]

                    if h[top] < h[idx]:
                        alive[top] = False
                        stack.pop()
                        h[idx] -= 1

                    elif h[top] > h[idx]:
                        alive[idx] = False
                        h[top] -= 1
                        break

                    else:
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break

        return [h[i] for i in range(n) if alive[i]]