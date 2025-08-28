from pathlib import Path

import mkdocs_gen_files
from invoke import task


@task
def format(ctx, fix: bool = False):
  """Format the code using ruff."""
  cmd = "ruff check"
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
def docs(ctx):
  """Generate API documentation files."""
  print("Generating API documentation...")
  root = Path(__file__).parent
  src = root / "src"
  for path in sorted(src.rglob("*.py")):
    module_path = path.relative_to(src).with_suffix("")
    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path.parts)

    if not parts:
      print(f"Skipping {path} as it is not a module")
      continue
    if parts[-1] == "__init__":
      parts = parts[:-1]
    elif parts[-1] == "__main__":
      continue

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
      identifier = ".".join(parts)
      print("::: " + identifier, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path.relative_to(root))
  print("API documentation generated!")
