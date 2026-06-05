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
