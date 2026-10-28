"""Simple script to display the sample dialogues locally.
It reads the 'sample_dialogues.md' file and prints each dialogue block
to the console. No Streamlit integration is required.
"""
import pathlib
import sys

def main():
    # Ensure UTF-8 output on Windows console
    try:
        import sys
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    # Path to the dialogues markdown file
    dlg_path = pathlib.Path(__file__).parent / "lessons" / "sample_dialogues.md"
    if not dlg_path.exists():
        print(f"Dialogue file not found: {dlg_path}")
        sys.exit(1)
    content = dlg_path.read_text(encoding="utf-8")
    # Split by '---' separator to get each dialogue block
    blocks = [b.strip() for b in content.split('---') if b.strip()]
    for i, block in enumerate(blocks, 1):
        print(f"\n=== Dialogue {i} ===\n")
        print(block)
        print("\n" + "="*20 + "\n")

if __name__ == "__main__":
    main()
