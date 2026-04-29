import os
from datetime import datetime

def read_code_files_in_folder(folder_path, extensions=None):
    """
    Walk through folder_path and collect all files with specified extensions.
    """
    if extensions is None:
        extensions = ['.js', '.ts', '.tsx', '.json', '.css', '.config.ts', '.config.js']

    files_data = []

    for root, dirs, files in os.walk(folder_path):
        # Skip unnecessary folders
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.next', '.git']]

        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        files_data.append({
                            'file_path': file_path,
                            'content': f.read()
                        })
                except Exception as e:
                    print(f"⚠️ Could not read file: {file_path} ({e})")

    return files_data


def main():
    # ✅ AUTO-DETECT project root (no hardcoding)
    project_root = os.path.dirname(os.path.abspath(__file__))

    print(f"📁 Project root detected: {project_root}")

    folders_to_scan = ['app', 'data', 'lib', 'utils']

    root_files = [
        'tailwind.config.ts',
        'next.config.js',
        'next.config.ts',
        'tsconfig.json',
        'package.json',
        '.env.local',
    ]

    all_files = []

    # Scan folders
    for folder in folders_to_scan:
        full_path = os.path.join(project_root, folder)

        if not os.path.exists(full_path):
            print(f"⚠️ Skipping missing folder: {folder}")
            continue

        print(f"📂 Scanning: {folder}")
        all_files.extend(read_code_files_in_folder(full_path))

    # Add root files
    for file_name in root_files:
        file_path = os.path.join(project_root, file_name)

        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    all_files.append({
                        'file_path': file_path,
                        'content': f.read()
                    })
                    print(f"✅ Added root file: {file_name}")
            except Exception as e:
                print(f"⚠️ Could not read: {file_name} ({e})")

    # ✅ Save output safely in project root (not inside /app)
    output_file = os.path.join(project_root, 'all_portfolio_files.txt')

    try:
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write("=" * 80 + "\n")
            out.write("ABHISHEK ACHARYA - PORTFOLIO PROJECT FILES\n")
            out.write("=" * 80 + "\n\n")
            out.write(f"Total Files: {len(all_files)}\n")
            out.write(f"Generated: {datetime.now()}\n")
            out.write("=" * 80 + "\n\n")

            for f in all_files:
                rel_path = os.path.relpath(f['file_path'], project_root)

                out.write(f"File: {rel_path}\n")
                out.write("=" * 80 + "\n")
                out.write(f['content'])
                out.write("\n" + "=" * 80 + "\n\n")

    except Exception as e:
        print(f"❌ Failed to write output file: {e}")
        return

    print("\n✅ File extraction completed!")
    print(f"📄 Total files extracted: {len(all_files)}")
    print(f"💾 Saved to: {output_file}")


if __name__ == "__main__":
    main()