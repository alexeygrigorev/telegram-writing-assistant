#!/bin/bash
# Check for broken internal links in articles
# Usage: bash scripts/check-links.sh

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

ERRORS=0
TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "Checking internal links in articles..."
echo ""

# Check inbox references (../inbox/used/ or ../inbox/raw/)
echo "## Inbox References"
echo ""

# First check for any inbox/raw links (should all be inbox/used)
RAW_COUNT=$(grep -r '../inbox/raw/' articles/ 2>/dev/null | wc -l | tr -d ' ')
if [ "$RAW_COUNT" -gt 0 ]; then
    echo "ERROR: Found $RAW_COUNT links pointing to inbox/raw/ (should be inbox/used/):"
    grep -rn '../inbox/raw/' articles/ | head -20
    echo ""
    ERRORS=$((ERRORS + RAW_COUNT))
fi

# Check that inbox/used references point to existing files
MISSING_INBOX=0
grep -roh '../inbox/used/[^)]*' articles/ 2>/dev/null | sort -u > "$TMPFILE"
while IFS= read -r ref; do
    filename=$(echo "$ref" | sed 's|../inbox/used/||')
    if [ -n "$filename" ] && [ ! -f "inbox/used/$filename" ]; then
        if [ "$MISSING_INBOX" -eq 0 ]; then
            echo "Missing inbox/used files:"
        fi
        echo "  $filename"
        MISSING_INBOX=$((MISSING_INBOX + 1))
    fi
done < "$TMPFILE"

if [ "$MISSING_INBOX" -eq 0 ]; then
    echo "All inbox/used references point to existing files."
else
    echo ""
    echo "Total missing inbox files: $MISSING_INBOX"
    ERRORS=$((ERRORS + MISSING_INBOX))
fi

echo ""

# Check image references
echo "## Image References"
echo ""

MISSING_IMAGES=0
grep -rn 'src="../assets' articles/ 2>/dev/null > "$TMPFILE"
while IFS= read -r line; do
    img_path=$(echo "$line" | grep -o 'src="[^"]*"' | sed 's/src="//;s/"//')
    article=$(echo "$line" | cut -d: -f1)
    article_dir=$(dirname "$article")
    resolved="$article_dir/$img_path"

    if [ ! -f "$resolved" ]; then
        if [ "$MISSING_IMAGES" -eq 0 ]; then
            echo "Missing image files:"
        fi
        echo "  $img_path (referenced in $article)"
        MISSING_IMAGES=$((MISSING_IMAGES + 1))
    fi
done < "$TMPFILE"

if [ "$MISSING_IMAGES" -eq 0 ]; then
    echo "All image references point to existing files."
else
    echo ""
    echo "Total missing images: $MISSING_IMAGES"
    ERRORS=$((ERRORS + MISSING_IMAGES))
fi

echo ""

# Summary
echo "## Summary"
echo ""
USED_COUNT=$(grep -r '../inbox/used/' articles/ 2>/dev/null | wc -l | tr -d ' ')
IMG_COUNT=$(grep -r 'src="../assets' articles/ 2>/dev/null | wc -l | tr -d ' ')
echo "Total inbox references: $USED_COUNT"
echo "Total image references: $IMG_COUNT"
echo "Errors: $ERRORS"
echo ""

if [ "$ERRORS" -gt 0 ]; then
    echo "FAILED: $ERRORS broken links found."
    exit 1
else
    echo "PASSED: All internal links are valid."
    exit 0
fi
