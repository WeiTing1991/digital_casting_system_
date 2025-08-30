from pathlib import Path

from invoke import task

from _gen_ref_pages import generate_api_reference


@task
def format(ctx, fix: bool = False):
  """Format the code using ruff."""
  filepath = Path("./src") / "dcs"
  matches = list(filepath.rglob("*.py"))
  files = " ".join(str(f) for f in matches)
  cmd = f"ruff format {files}"
  if fix:
    cmd += " --fix"
  ctx.run(cmd, pty=True)


@task
def test(ctx, verbose: bool = False):
  """Run tests with pytest (0.3 seconds)."""
  cmd = "python -m pytest"
  if verbose:
    cmd += " -v"
  print("Running tests...")
  ctx.run(cmd, pty=True)


@task
def docs(ctx, serve: bool = False):
  """Build documentation with auto-generated API reference."""
  print("Building documentation with auto-generated API reference...")

  if serve:
    print("Serving documentation at http://127.0.0.1:8000")
    ctx.run("mkdocs serve", pty=True)
  else:
    generate_api_reference()
    ctx.run("mkdocs build", pty=True)
    print("Documentation built successfully!")


@task
def docs_clean(ctx):
  """Clean generated documentation files."""
  print("Cleaning generated documentation...")
  ctx.run("rm -rf docs/api/reference/", pty=True)
  ctx.run("rm -rf dist/", pty=True)
  print("Documentation cleaned!")


@task
def build(ctx):
  """Build the package for distribution."""
  print("Building package...")

  # Clean first
  build_clean(ctx)

  # Build with hatchling (no isolation to avoid network issues)
  ctx.run("python -m build --no-isolation", pty=True)
  print("Package built successfully!")


@task
def build_clean(ctx):
  """Clean build artifacts."""
  print("Cleaning build artifacts...")
  ctx.run("rm -rf build/", pty=True)
  ctx.run("rm -rf dist/", pty=True)
  ctx.run("rm -rf *.egg-info/", pty=True)
  ctx.run("find . -name '*.pyc' -delete 2>/dev/null || true", pty=True)
  ctx.run("find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true", pty=True)
  print("Build artifacts cleaned!")


@task
def build_release(ctx, part="patch"):
  """Build a release with automatic version bumping and tagging.

  Args:
      part: Version part to bump (patch, minor, major). Default: patch
  """
  print(f"Building release with {part} version bump...")

  # Clean first
  build_clean(ctx)

  # Update version and create tag
  print("Bumping version...")
  ctx.run(f"bump-my-version bump {part}", pty=True)

  # Build the package
  print("Building package...")
  ctx.run("python -m build --no-isolation", pty=True)

  print(f"Release built successfully with {part} version bump!")
