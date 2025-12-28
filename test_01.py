#!/usr/bin/env python3
"""Simple file read/write demo.

Writes a small text file `sample.txt` and reads it back.
"""

from pathlib import Path


def write_file(path: str, text: str, encoding: str = "utf-8") -> None:
	p = Path(path)
	p.write_text(text, encoding=encoding)


def read_file(path: str, encoding: str = "utf-8") -> str:
	p = Path(path)
	return p.read_text(encoding=encoding)


def main() -> None:
	sample_path = "sample.txt"
	text = "Hello, world!\n这是一些中文行。\n"
	write_file(sample_path, text)
	print(f"Wrote to {sample_path}")
	content = read_file(sample_path)
	print("Read content:")
	print(content)


if __name__ == "__main__":
	main()

