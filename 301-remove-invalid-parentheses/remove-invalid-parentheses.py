class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = {s}

        while queue:
            valid = []

            for current in queue:
                if isValid(current):
                    valid.append(current)

            if valid:
                return valid

            next_queue = []

            for current in queue:
                for i in range(len(current)):
                    # Only remove parentheses
                    if current[i] not in '()':
                        continue

                    # Avoid generating duplicate strings
                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)

            queue = next_queue

        return [""]