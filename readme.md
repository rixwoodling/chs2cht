# CSV-Based Subtitle Converter (CHS → CHT)

Convert Simplified Chinese `.srt` subtitles into Traditional Chinese using a CSV dictionary.

## Example

Input (`movie.srt`)
```text
我爱我的国家
```

Output (`movie.cht.srt`)
```text
我愛我的國家
```

CSV (`chs2cht.csv`)
```csv
汉,漢
爱,愛
国,國
```

## Usage

```bash
python3 script.py movie.srt
```

Produces:

```
movie.cht.srt
```

## CSV Format

Two columns:

| Column | Description |
|--------|-------------|
| 1 | Simplified Chinese |
| 2 | Traditional Chinese |

Example:

```csv
汉,漢
爱,愛
国,國
```

## Notes

- Supports one or more `.srt` files.
- Only subtitle text is modified.
- Non-Chinese text is left unchanged.
- Requires Python 3.

## Future Improvements

- Validate malformed CSV rows.
- Use safer file handling (`with open(...)`).
- Optimize replacement performance.
