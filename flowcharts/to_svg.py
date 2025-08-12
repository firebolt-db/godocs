# Takes a graphviz file and turns it into an svg in both light and dark mode.
# This can be directly integrated with the Mintlify docs.

import graphviz
import os
import sys
from pathlib import Path

def create_light_theme_dot(content):
    """Create light theme version of the dot file with Firebolt colors and Inter font"""
    # Light theme styling with Firebolt colors and Inter font
    light_theme = '''
    graph [bgcolor="transparent", fontcolor="black", fontname="Inter,Arial,sans-serif"];
    node [fontcolor="black", color="black", fontname="Inter,Arial,sans-serif"];
    edge [fontcolor="black", color="#FF5733", fontname="Inter,Arial,sans-serif"];
    '''
    
    # Insert theme after the opening brace
    lines = content.split('\n')
    result = []
    for i, line in enumerate(lines):
        result.append(line)
        if line.strip().startswith('digraph') and '{' in line:
            result.append(light_theme)
    
    return '\n'.join(result)

def create_dark_theme_dot(content):
    """Create dark theme version of the dot file with Firebolt colors and Inter font"""
    # Dark theme styling with Firebolt colors and Inter font
    dark_theme = '''
    graph [bgcolor="transparent", fontcolor="white", fontname="Inter,Arial,sans-serif"];
    node [fontcolor="white", color="white", fontname="Inter,Arial,sans-serif"];
    edge [fontcolor="white", color="#FF5733", fontname="Inter,Arial,sans-serif"];
    '''
    
    # Insert theme after the opening brace
    lines = content.split('\n')
    result = []
    for i, line in enumerate(lines):
        result.append(line)
        if line.strip().startswith('digraph') and '{' in line:
            result.append(dark_theme)
    
    return '\n'.join(result)

def convert_dot_to_svg(input_file):
    """Convert a .dot file to light and dark theme SVGs"""
    
    # Read the original dot file
    with open(input_file, 'r') as f:
        original_content = f.read()
    
    # Get base filename without extension
    base_name = Path(input_file).stem
    
    # Create light theme version
    light_content = create_light_theme_dot(original_content)
    light_source = graphviz.Source(light_content)
    light_output = f"{base_name}_light"
    light_source.render(light_output, format='svg', cleanup=True)
    
    # Create dark theme version
    dark_content = create_dark_theme_dot(original_content)
    dark_source = graphviz.Source(dark_content)
    dark_output = f"{base_name}_dark"
    dark_source.render(dark_output, format='svg', cleanup=True)
    
    print(f"✅ Generated {light_output}.svg")
    print(f"✅ Generated {dark_output}.svg")

def main():
    if len(sys.argv) != 2:
        print("Usage: python to_svg.py <input.dot>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"❌ Error: File '{input_file}' not found")
        sys.exit(1)
    
    if not input_file.endswith('.dot'):
        print("❌ Error: Input file must have .dot extension")
        sys.exit(1)
    
    try:
        convert_dot_to_svg(input_file)
    except Exception as e:
        print(f"❌ Error converting file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()