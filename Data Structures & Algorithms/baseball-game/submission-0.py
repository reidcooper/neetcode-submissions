class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == '+':
                second = record.pop()
                first = record.pop()
                record.append(first)
                record.append(second)
                record.append(first + second)
            elif op == 'C':
                record.pop()
            elif op == 'D':
                first = record.pop()
                record.append(first)
                record.append(first * 2)
            else:
                record.append(int(op))

        return sum(record)