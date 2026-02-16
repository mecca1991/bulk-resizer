# bulk-resizer

A simple command-line tool for resizing a folder of images to thumbnails while maintaining aspect ratio and handling corrupt files.

## Features

- **Batch Image Resizing**: Process multiple images in a folder at once
- **Aspect Ratio Preservation**: Maintains original image proportions during resizing
- **Corrupt File Handling**: Gracefully skips or reports corrupt/unreadable image files
- **Thumbnail Generation**: Creates thumbnail versions of your images efficiently

## Installation

```bash
# Installation instructions will be added once the tool is implemented
pip install bulk-resizer
```

## Usage

Basic usage:

```bash
bulk-resizer <input-folder> <output-folder> [options]
```

### Options

- `--width <pixels>` - Set thumbnail width (default: 150)
- `--height <pixels>` - Set thumbnail height (default: 150)
- `--quality <0-100>` - Set output quality for JPEG images (default: 80)
- `--format <jpg|png|webp>` - Output format (default: same as input)
- `--skip-corrupt` - Skip corrupt files without stopping (default: true)

### Examples

Resize all images in a folder to 200x200 thumbnails:

```bash
bulk-resizer ./photos ./thumbnails --width 200 --height 200
```

Create thumbnails with specific quality:

```bash
bulk-resizer ./images ./output --width 150 --height 150 --quality 90
```

Convert to WebP format while resizing:

```bash
bulk-resizer ./input ./output --format webp
```

## Error Handling

The tool handles various error scenarios:

- **Corrupt Files**: Corrupt or unreadable image files are automatically skipped, and a warning is displayed
- **Missing Folders**: If the input folder doesn't exist, an error message is shown
- **Unsupported Formats**: Non-image files are skipped automatically
- **Write Permissions**: Checks for write permissions in the output folder before processing

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- WebP (.webp)
- BMP (.bmp)
- TIFF (.tiff, .tif)

## License

MIT
