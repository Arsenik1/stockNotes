import os
import sys
from datetime import datetime

SHORT_DIR = "short_term"
LONG_DIR = "long_term"

class StockNotesBackend:
    """Backend logic for managing stock notes."""

    def __init__(self, short_dir: str = SHORT_DIR, long_dir: str = LONG_DIR):
        self.short_dir = short_dir
        self.long_dir = long_dir
        self.mode = "short"
        self.default_date = None

        os.makedirs(self.short_dir, exist_ok=True)
        os.makedirs(self.long_dir, exist_ok=True)

    # ---------- Configuration ----------
    def set_default_date(self, date_str: str | None = None) -> str:
        """Set or update the default date used for new notes.

        Args:
            date_str: Date string in DD-MM-YYYY format. If None, today's date
                is used.

        Returns:
            The date string that was set.
        """
        if date_str is None:
            date_str = datetime.today().strftime("%d-%m-%Y")
        else:
            datetime.strptime(date_str, "%d-%m-%Y")  # validate
        self.default_date = date_str
        return self.default_date

    def switch_mode(self) -> str:
        """Toggle between short- and long-term modes."""
        self.mode = "long" if self.mode != "long" else "short"
        return self.mode

    # ---------- Stock Management ----------
    def add_stock_code(self, stock_code: str) -> None:
        """Create note files for a new stock code."""
        stock_code = stock_code.upper()
        short_path = os.path.join(self.short_dir, f"{stock_code}.txt")
        long_path = os.path.join(self.long_dir, f"{stock_code}.txt")
        if os.path.exists(short_path) or os.path.exists(long_path):
            raise FileExistsError("Stock code already exists")
        with open(short_path, "w", encoding="utf-8") as f:
            f.write(f"Notes for {stock_code}\n\n")
        with open(long_path, "w", encoding="utf-8") as f:
            f.write(f"Notes for {stock_code}\n\n")

    def _resolve_note_file(self, stock_code: str, mode: str | None) -> str:
        stock_code = stock_code.upper()
        dir_path = self.short_dir if (mode or self.mode) == "short" else self.long_dir
        return os.path.join(dir_path, f"{stock_code}.txt")

    def add_note(self, stock_code: str, note: str, *, date: str | None = None, mode: str | None = None) -> None:
        """Append a note for the given stock code."""
        path = self._resolve_note_file(stock_code, mode)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Notes file for {stock_code} does not exist")

        if date is None:
            date = self.default_date or datetime.today().strftime("%d-%m-%Y")
        datetime.strptime(date, "%d-%m-%Y")  # validate
        formatted = datetime.strptime(date, "%d-%m-%Y").strftime("%d %B %Y")

        with open(path, "a", encoding="utf-8") as f:
            f.write(f"{formatted}: {note}\n")

    # ---------- Query Functions ----------
    def list_companies(self) -> list[str]:
        companies: set[str] = set()
        for folder in (self.short_dir, self.long_dir):
            if os.path.isdir(folder):
                for filename in os.listdir(folder):
                    if filename.endswith(".txt"):
                        companies.add(filename[:-4].upper())
        return sorted(companies)

    def read_notes(self, stock_code: str) -> dict[str, str]:
        stock_code = stock_code.upper()
        short_path = os.path.join(self.short_dir, f"{stock_code}.txt")
        long_path = os.path.join(self.long_dir, f"{stock_code}.txt")
        if not os.path.exists(short_path) or not os.path.exists(long_path):
            raise FileNotFoundError("Notes for this stock do not exist")
        with open(short_path, "r", encoding="utf-8") as s, open(long_path, "r", encoding="utf-8") as l:
            return {"short": s.read(), "long": l.read()}

    def dump_all_notes(self, output_file: str) -> None:
        with open(output_file, "w", encoding="utf-8") as outfile:
            for company in self.list_companies():
                notes = self.read_notes(company)
                outfile.write(f"\nShort Term for {company}\n")
                outfile.write(notes["short"])
                outfile.write(f"\nLong Term for {company}\n")
                outfile.write(notes["long"])

if __name__ == "__main__":
    import argparse, json

    parser = argparse.ArgumentParser(description="Stock Notes Backend CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list")

    add_stock = sub.add_parser("add-stock")
    add_stock.add_argument("code")

    add_note = sub.add_parser("add-note")
    add_note.add_argument("code")
    add_note.add_argument("note")
    add_note.add_argument("--date")
    add_note.add_argument("--mode", choices=["short", "long"])

    read = sub.add_parser("read")
    read.add_argument("code")

    dump = sub.add_parser("dump")
    dump.add_argument("output")

    args = parser.parse_args()
    backend = StockNotesBackend()

    try:
        if args.cmd == "list":
            print(json.dumps(backend.list_companies()))
        elif args.cmd == "add-stock":
            backend.add_stock_code(args.code)
        elif args.cmd == "add-note":
            backend.add_note(args.code, args.note, date=args.date, mode=args.mode)
        elif args.cmd == "read":
            print(json.dumps(backend.read_notes(args.code)))
        elif args.cmd == "dump":
            backend.dump_all_notes(args.output)
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        raise
