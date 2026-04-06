#!/usr/bin/env python3
"""Convert saved HTML manual pages to individual Markdown files."""

import os
import re
import base64
import glob
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ORIGINALS_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(ORIGINALS_DIR, "markdown")
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")


def find_html_dirs():
    """Find all numbered directories with HTML files."""
    dirs = []
    for entry in sorted(os.listdir(ORIGINALS_DIR)):
        full_path = os.path.join(ORIGINALS_DIR, entry)
        if os.path.isdir(full_path) and re.match(r"^\d{2}-", entry):
            html_file = os.path.join(full_path, "Manual - GbbOptimizer.html")
            if os.path.exists(html_file):
                dirs.append((entry, html_file))
    return dirs


def extract_content(html_path):
    """Extract the article content from the full HTML page."""
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # The content is inside the second accordion's accordion-body div
    # (first accordion is "Filtry", second is "Rozdział")
    accordion_bodies = soup.select("div.accordion-body")
    if len(accordion_bodies) >= 2:
        content_div = accordion_bodies[1]
        # The actual content is inside a nested <div> within the accordion-body
        inner_div = content_div.find("div")
        if inner_div:
            return inner_div
        return content_div

    # Fallback: try to find content in <main>
    main = soup.find("main")
    if main:
        return main

    return soup.body


def extract_base64_images(content_element, slug):
    """Extract base64 images from the content, save to files, replace src."""
    os.makedirs(IMAGES_DIR, exist_ok=True)
    img_counter = 0

    for img in content_element.find_all("img"):
        src = img.get("src", "")
        if not src.startswith("data:image/"):
            continue

        # Parse the data URI
        match = re.match(r"data:image/(png|jpeg|jpg|gif|webp);base64,(.*)", src, re.DOTALL)
        if not match:
            continue

        ext = match.group(1)
        if ext == "jpeg":
            ext = "jpg"
        b64_data = match.group(2)

        img_counter += 1
        filename = f"{slug}-{img_counter}.{ext}"
        filepath = os.path.join(IMAGES_DIR, filename)

        try:
            img_bytes = base64.b64decode(b64_data)
            with open(filepath, "wb") as f:
                f.write(img_bytes)
            img["src"] = f"images/{filename}"
            print(f"       Extracted image: {filename} ({len(img_bytes)} bytes)")
        except Exception as e:
            print(f"       Warning: Could not decode image: {e}")
            img.decompose()

    return img_counter


def clean_content(content_element):
    """Remove unwanted elements from the content."""
    # Remove any script tags
    for script in content_element.find_all("script"):
        script.decompose()

    # Remove any form elements
    for form in content_element.find_all("form"):
        form.decompose()

    # Remove any input elements
    for inp in content_element.find_all("input"):
        inp.decompose()

    # Remove any button elements
    for btn in content_element.find_all("button"):
        btn.decompose()

    # Remove style-only spans (preserve content)
    for span in content_element.find_all("span", style=True):
        # Check if span only has style (no semantic meaning)
        style = span.get("style", "")
        # Keep spans with meaningful content, just unwrap them
        span.unwrap()

    # Remove empty spans
    for span in content_element.find_all("span"):
        if not span.get("class") and not span.get("id"):
            span.unwrap()


def convert_to_markdown(content_element):
    """Convert BeautifulSoup element to Markdown."""
    html_str = str(content_element)

    result = md(
        html_str,
        heading_style="ATX",
        bullets="-",
        strip=["font"],
    )

    return result


def clean_markdown(text):
    """Post-process markdown to clean up artifacts."""
    # Remove excessive blank lines
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    # Clean up lines that are just whitespace
    lines = text.split("\n")
    lines = [line.rstrip() for line in lines]
    text = "\n".join(lines)

    # Remove any remaining base64 data
    text = re.sub(
        r"!\[[^\]]*\]\(data:image/[^\)]+\)",
        "[image truncated]",
        text,
    )
    text = re.sub(
        r"data:image/(?:png|jpeg|jpg|gif|webp);base64,[A-Za-z0-9+/=\s]{100,}",
        "[image truncated]",
        text,
    )

    # Clean up &nbsp; remnants
    text = text.replace("\xa0", " ")

    # Ensure file ends with single newline
    text = text.strip() + "\n"

    return text


def main():
    html_dirs = find_html_dirs()
    if not html_dirs:
        print("No HTML directories found!")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Found {len(html_dirs)} HTML files to convert:\n")

    for dir_name, html_path in html_dirs:
        slug = dir_name  # e.g. "01-jak-zaczac"
        print(f"  [{slug}]")

        # Extract content
        content = extract_content(html_path)
        if content is None:
            print("       ERROR: Could not find content!")
            continue

        # Extract base64 images
        img_count = extract_base64_images(content, slug)

        # Clean HTML
        clean_content(content)

        # Convert to markdown
        markdown = convert_to_markdown(content)

        # Clean up
        markdown = clean_markdown(markdown)

        # Write output
        output_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"       -> {slug}.md ({len(markdown)} chars, {img_count} images)")

    print(f"\nDone! Output in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
