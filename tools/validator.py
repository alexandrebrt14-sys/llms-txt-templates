#!/usr/bin/env python3
"""
llms.txt Validator

Validates llms.txt files against the proposed specification.
Checks structure, encoding, content guidelines, and link format.

Usage:
    python validator.py https://example.com/llms.txt
    python validator.py path/to/llms.txt

Requires: Python 3.8+, requests (for URL validation)
"""

import sys
import re
import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


@dataclass
class ValidationResult:
    """Stores the results of a validation run."""
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    info: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def add_info(self, message: str) -> None:
        self.info.append(message)

    def print_report(self) -> None:
        print("\n" + "=" * 60)
        print("llms.txt Validation Report")
        print("=" * 60)
        if self.info:
            print("\n--- Info ---")
            for item in self.info:
                print(f"  [i] {item}")
        if self.warnings:
            print("\n--- Warnings ---")
            for item in self.warnings:
                print(f"  [!] {item}")
        if self.errors:
            print("\n--- Errors ---")
            for item in self.errors:
                print(f"  [X] {item}")
        print("\n--- Summary ---")
        print(f"  Errors:   {len(self.errors)}")
        print(f"  Warnings: {len(self.warnings)}")
        print(f"  Info:     {len(self.info)}")
        if self.is_valid:
            print("\n  Result: VALID")
        else:
            print("\n  Result: INVALID")
        print("=" * 60 + "\n")


def load_content(source: str) -> tuple[Optional[str], Optional[str]]:
    """Load llms.txt content from a URL or file path."""
    if source.startswith("http://") or source.startswith("https://"):
        if not HAS_REQUESTS:
            return None, "The 'requests' library is required for URL validation."
        try:
            response = requests.get(source, timeout=10)
            response.raise_for_status()
            return response.text, None
        except requests.RequestException as e:
            return None, f"Failed to fetch URL: {e}"
    else:
        path = Path(source)
        if not path.exists():
            return None, f"File not found: {source}"
        try:
            return path.read_text(encoding="utf-8"), None
        except UnicodeDecodeError:
            return None, "File is not valid UTF-8 encoding"


def validate_structure(content: str, result: ValidationResult) -> None:
    """Validate the structural requirements of the llms.txt file."""
    lines = content.strip().split("\n")
    if not lines:
        result.add_error("File is empty")
        return
    first_content_line = None
    for line in lines:
        if line.strip():
            first_content_line = line.strip()
            break
    if first_content_line is None:
        result.add_error("File contains no content")
        return
    if not first_content_line.startswith("# "):
        result.add_error("File must begin with an H1 heading (# Entity Name)")
    else:
        entity_name = first_content_line[2:].strip()
        if entity_name:
            result.add_info(f"Entity name: {entity_name}")
    has_description = False
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("> "):
            has_description = True
            break
        elif stripped.startswith("## ") or stripped.startswith("- "):
            break
    if not has_description:
        result.add_error("Missing blockquote description (> Description)")
    sections = [line.strip()[3:] for line in lines if line.strip().startswith("## ")]
    if not sections:
        result.add_error("File contains no sections (## headings)")
    else:
        result.add_info(f"Sections found: {', '.join(sections)}")


def validate_links(content: str, result: ValidationResult) -> None:
    """Validate link formatting in the file."""
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    links = link_pattern.findall(content)
    if not links:
        result.add_warning("No links found.")
        return
    result.add_info(f"Links found: {len(links)}")
    relative_links = [url for text, url in links
                      if not url.startswith("http://") and not url.startswith("https://")]
    if relative_links:
        result.add_error(f"Found {len(relative_links)} relative URL(s). All links must be absolute.")


def validate_content_guidelines(content: str, result: ValidationResult) -> None:
    """Check content against recommended guidelines."""
    superlatives = ["best in class", "world-leading", "revolutionary", "game-changing",
                    "cutting-edge", "state-of-the-art", "industry-leading"]
    content_lower = content.lower()
    found = [s for s in superlatives if s in content_lower]
    if found:
        result.add_warning(f"Marketing superlatives detected: {', '.join(found)}")
    html_pattern = re.compile(r"<[a-zA-Z][^>]*>")
    if html_pattern.findall(content):
        result.add_error("HTML tags detected. llms.txt must be plain text.")
    size_kb = len(content.encode("utf-8")) / 1024
    if size_kb > 50:
        result.add_error(f"File is {size_kb:.1f}KB. Maximum recommended is 50KB.")
    elif size_kb > 10:
        result.add_warning(f"File is {size_kb:.1f}KB. Recommended max for llms.txt is 10KB.")
    else:
        result.add_info(f"File size: {size_kb:.1f}KB")
    words = len(content.split())
    result.add_info(f"Word count: {words}")


def validate(source: str) -> ValidationResult:
    """Run all validations on an llms.txt source."""
    result = ValidationResult()
    result.add_info(f"Source: {source}")
    content, error = load_content(source)
    if error:
        result.add_error(error)
        return result
    validate_structure(content, result)
    validate_links(content, result)
    validate_content_guidelines(content, result)
    return result


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) != 2:
        print("Usage: python validator.py <url-or-file-path>")
        sys.exit(1)
    source = sys.argv[1]
    result = validate(source)
    result.print_report()
    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
