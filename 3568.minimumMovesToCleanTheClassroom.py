from collections import deque


class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        # Assign a bit to each litter cell
        litter_id = {}
        litter_count = 0
        start = None

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        # No litter to collect
        if litter_count == 0:
            return 0

        all_mask = (1 << litter_count) - 1

        # State = (row, col, collected_mask, remaining_energy)
        queue = deque()
        queue.append((start[0], start[1], 0, energy, 0))

        visited = {
            (start[0], start[1], 0, energy)
        }

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, mask, curr_energy, moves = queue.popleft()

            # All litter collected
            if mask == all_mask:
                return moves

            # If we have no energy and aren't on a reset cell,
            # we cannot make another move.
            if curr_energy == 0 and classroom[r][c] != 'R':
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Out of bounds
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Every move costs 1 energy
                if curr_energy == 0:
                    continue

                new_energy = curr_energy - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    bit = litter_id[(nr, nc)]
                    new_mask |= 1 << bit

                # Reset energy after entering R
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (nr, nc, new_mask, new_energy)

                if state not in visited:
                    visited.add(state)
                    queue.append(
                        (nr, nc, new_mask, new_energy, moves + 1)
                    )

        return -1