print('samarth \n 1AY24AI097')
class TablePrinter:
    def __init__(self, headers, rows):
        self.headers = headers
        self.rows = rows
        self.column_widths = self._calculate_column_widths()
    def _calculate_column_widths(self):
        widths = [len(header) for header in self.headers]
        for row in self.rows:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(str(cell)))
       return widths
    def _format_row(self, row):
        return " | ".join(str(cell).ljust(width) for cell, width in zip(row, self.column_widths))
    def _print_separator(self):
        print("-+-".join("-" * width for width in self.column_widths))

    def print_table(self):
        print(self._format_row(self.headers))
        self._print_separator()
        for row in self.rows:
            print(self._format_row(row))
if __name__ == "__main__":
    headers = ["Name", "Age", "Occupation"]
    rows = [
        ["Alice", 30, "Engineer"],
        ["Bob", 25, "Designer"],
        ["Charlie", 28, "Doctor"]
    ]
    table = TablePrinter(headers, rows)
    table.print_table()
