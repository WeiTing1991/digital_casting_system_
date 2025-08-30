
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

