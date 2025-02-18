```
# CSV-Based Subtitle Converter (CHS to CHT)

## Description
This script converts **Simplified Chinese (CHS) subtitles** in `.srt` files to **Traditional Chinese (CHT)** using a mapping provided in a CSV file.

## How It Works
1. **Reads a CSV file (`chs2cht.csv`)** where each row contains a simplified-to-traditional character mapping.
2. **Processes `.srt` subtitle files** given as command-line arguments.
3. **Creates new `.cht.srt` files** with the converted content.

## Usage
Run the script from the command line and provide one or more `.srt` files:

```bash
python3 script.py subtitles.srt
```
This will generate a new file:

```
subtitles.cht.srt
```

## CSV Format (`chs2cht.csv`)
The CSV file should have **two columns**, where:
- **Column 1** = Simplified Chinese character/word  
- **Column 2** = Traditional Chinese equivalent  

Example:
```csv
汉,漢
爱,愛
国,國
```

## Example Input & Output
### Original (`subtitles.srt`):
```
1
00:00:01,500 --> 00:00:04,000
我爱我的国家
```
### Converted (`subtitles.cht.srt`):
```
1
00:00:01,500 --> 00:00:04,000
我愛我的國家
```

## Notes
- Only works on `.srt` files.
- Non-Chinese characters remain unchanged.
- Requires **Python 3**.

## To-Do / Improvements
- Handle **missing or malformed CSV entries**.
- Improve **file handling** with `with open(...)` for better safety.
- Optimize **character replacement** to reduce redundant operations.
```

