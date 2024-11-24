import os
import json
import time
import requests
import argparse
from pathlib import Path

def read_sql_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

def execute_query(query):
    try:
        response = requests.post(
            'http://localhost:8000/execute-query',
            headers={'Content-Type': 'application/json'},
            json={'query': query},
            timeout=10
        )
        try:
            return response.json()
        except json.JSONDecodeError:
            print(f"Error decoding JSON response (status code: {response.status_code})")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error executing query: {e}")
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--missing-only', action='store_true', 
                       help='Only process SQL files that don\'t have corresponding JSON files')
    args = parser.parse_args()

    # Path to sql_examples directory
    examples_dir = Path('docs/_includes/sql_examples')
    
    # Ensure directory exists
    if not examples_dir.exists():
        print(f"Directory not found: {examples_dir}")
        return

    # Process SQL files
    for sql_file in examples_dir.glob('*.sql'):
        json_file = sql_file.with_suffix('.json')
        
        # Skip if JSON exists and we're in missing-only mode
        if args.missing_only and json_file.exists():
            print(f"Skipping {sql_file.name} (JSON exists)")
            continue
            
        print(f"Processing {sql_file.name}...")
        
        # Read SQL query
        query = read_sql_file(sql_file)
        
        # Execute query
        result = execute_query(query)
        
        if result:
            # Save result
            with open(json_file, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Saved result to {json_file.name}")
        else:
            print(f"Failed to get result for {sql_file.name}")
        
        # Sleep for 100ms between files
        time.sleep(0.1)

if __name__ == '__main__':
    main() 