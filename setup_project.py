#!/usr/bin/env python3
"""
Tower Calculator Project Setup Script
Generates complete project structure with all files
"""

import os
import sys
from pathlib import Path

# Define project structure
PROJECT_STRUCTURE = {
    "backend": {
        "app": {
            "api": {},
            "models": {},
            "calculations": {},
            "utils": {},
            "__init__.py": "",
            "main.py": "",
            "config.py": "",
        },
        "tests": {"__init__.py": ""},
        "Dockerfile": "",
        ".dockerignore": "",
        "requirements.txt": "",
    },
    "frontend": {
        "src": {
            "components": {},
            "pages": {},
            "services": {},
            "assets": {},
            "App.tsx": "",
            "index.tsx": "",
            "main.tsx": "",
        },
        "public": {},
        "Dockerfile": "",
        ".dockerignore": "",
        "package.json": "",
        "tsconfig.json": "",
        "vite.config.ts": "",
    },
    "data": {"profiles.json": ""},
    "docs": {
        "ARCHITECTURE.md": "",
        "API.md": "",
        "EUROCODES.md": "",
        "USAGE.md": "",
    },
    ".github": {"workflows": {"ci.yml": ""}},
    "README.md": "",
    ".gitignore": "",
    "docker-compose.yml": "",
    ".env.example": "",
}


def create_structure(base_path: Path, structure: dict, level: int = 0) -> None:
    """Recursively create directory structure."""
    for name, content in structure.items():
        path = base_path / name

        if isinstance(content, dict):
            # Create directory
            path.mkdir(parents=True, exist_ok=True)
            print(f"{'  ' * level}📁 {name}/")
            # Recursively create subdirectories
            create_structure(path, content, level + 1)
        else:
            # Create file
            path.touch(exist_ok=True)
            print(f"{'  ' * level}📄 {name}")


def main():
    """Main setup function."""
    print("\n" + "=" * 60)
    print("🏗️  TOWER CALCULATOR - PROJECT SETUP")
    print("=" * 60 + "\n")

    base_path = Path.cwd()
    print(f"📍 Creating project in: {base_path}\n")

    # Create directory structure
    print("Creating directory structure...\n")
    create_structure(base_path, PROJECT_STRUCTURE)

    print("\n" + "=" * 60)
    print("✅ Project structure created successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. cd tower-calculator")
    print("2. Copy backend files to backend/ folder")
    print("3. Copy frontend files to frontend/ folder")
    print("4. Run: docker-compose up -d")
    print("\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
