## CRITICAL: File Editing on Windows

### ⚠️ MANDATORY: Always Use Backslashes on Windows for File Paths

When using Edit or MultiEdit tools on Windows, you MUST use backslashes (`\`) in file paths, NOT forward slashes (`/`).

❌ WRONG - Will cause errors:
```
Edit(file_path: "D:/repos/project/file.tsx", ...)
MultiEdit(file_path: "D:/repos/project/file.tsx", ...)
```

✅ CORRECT - Always works:
```
Edit(file_path: "D:\repos\project\file.tsx", ...)
MultiEdit(file_path: "D:\repos\project\file.tsx", ...)
```

### ⚠️ "File has been unexpectedly modified" Error

If you get this error: **"File has been unexpectedly modified. Read it again before attempting to write it"**

**Root cause:** The file was modified after you last read it (by linter, formatter, git, or external process).

**Solution: Re-read the file immediately before editing:**

```bash
# 1. Read the file again
Read(file_path: "path\to\file.txt")

# 2. Then immediately edit
Edit(file_path: "path\to\file.txt", old_string="...", new_string="...")
```

**Tool requirements:**

- Edit - Must `Read` immediately before - `old_string` must match current content
- Write - Must `Read` once per conversation before first write

**Common triggers:**
- Linters/formatters running on save
- Git operations (checkout, merge, rebase)
- File watchers or build processes

**Tip:** If this happens repeatedly, consider disabling auto-formatting for files you're actively editing with Claude Code.

### ⚠️ Use UV for Python Package Management

When installing Python packages, use `uv` instead of `pip`. See `/uv` for details.

❌ WRONG:
```bash
pip install djangorestframework
```

✅ CORRECT:
```bash
cd backend-django
uv add djangorestframework
```

Run Django commands:
```bash
cd backend-django
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py test
```


## One-time tests and debug scripts

One-time scripts and temporary files should be in .tmp. It's in .gitignore so we won't accidentally commit it to git.

## Style Guide

When creating workshop content:

1. Always cite sources with specific files: Use `Source: URL/blob/main/path/to/file.ext` format. Include the actual file path, not just the repository URL.

2. Code examples: Use actual working code from the source materials

3. Environment setup: Use `uv` for package management, `dirdotenv` for environment variables

4. Format: Self-contained README files in day1/ and day2/ directories with all instructions and code inline

5. Library installation: Introduce libraries incrementally - add `uv add` commands in the section where each library is first used, not all at the start

6. Import statements: Only import things the FIRST time they appear in the document. If a library was imported earlier, don't repeat the import. This applies to all imports (pydantic, toyaikit, etc.)

## MARKDOWN STYLE GUIDE

1. No bold or italic formatting: Don't use `**bold**` or `*italic*` for emphasis

2. No horizontal rules: Don't use `---` separators

3. Spaces around dashes: Use ` - ` not `-` when writing text

4. Code blocks must be separated by text: Two code blocks cannot follow each other directly. Always add explanatory text between code blocks.
