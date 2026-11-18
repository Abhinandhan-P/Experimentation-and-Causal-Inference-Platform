"""Vercel serverless entrypoint.

Adds the `src` directory to sys.path so all internal modules resolve correctly,
then re-exports the FastAPI `app` instance for the Vercel Python runtime to serve.
"""
import sys
import os
from pathlib import Path

# Ensure the `src` package directory is on the path for all internal imports
src_dir = Path(__file__).resolve().parent.parent / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

# Import and re-export the FastAPI application
from api import app  # noqa: E402  (import after sys.path mutation is intentional)

__all__ = ["app"]
