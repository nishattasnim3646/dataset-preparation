import pandas as pd
import pickle
import os
import argparse
from pathlib import Path

def load_dataset(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    df = pd.read_excel(file_path)
    print(f"✅ Loaded {len(df)} rows and {len(df.columns)} columns")
    return df

def split_by_column(df, column_name):
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found. Available: {df.columns.tolist()}")
    
    unique_values = df[column_name].dropna().unique()
    print(f"📊 Found {len(unique_values)} unique {column_name} values")
    
    split_dict = {}
    for value in unique_values:
        subset = df[df[column_name] == value].copy()
        subset = subset.drop(columns=[column_name])
        split_dict[value] = subset
        print(f"   • {value}: {len(subset)} rows")
    
    return split_dict

def save_pickle(data_dict, output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'wb') as f:
        pickle.dump(data_dict, f)
    
    file_size = os.path.getsize(output_path) / (1024*1024)

def main():
    parser = argparse.ArgumentParser(description='Split dataset by country, institute, or strain')
    parser.add_argument('--by', type=str, required=True, 
                        choices=['country', 'institute', 'strain'],
                        help='Split by: country, institute, or strain')
    parser.add_argument('--input', type=str, default='data/dataset.xlsx',
                        help='Path to input Excel file')
    parser.add_argument('--output-dir', type=str, default='data/splits',
                        help='Output directory for pickle files')
    
    args = parser.parse_args()
    
    column_mapping = {
        'country': 'country_id',
        'institute': 'institute_id', 
        'strain': 'strain_id'
    }
    
    column_name = column_mapping[args.by]
    output_file = f"{args.output_dir}/by_{args.by}.pkl"
    
    print(f"Split by: {args.by} ({column_name})")
    print(f"Input file: {args.input}")
    print(f"Output file: {output_file}")
    
    # Get the script's directory
    script_dir = Path(__file__).parent.absolute()
    project_root = script_dir.parent
    
    # Adjust paths relative to project root
    input_path = project_root / args.input
    output_path = project_root / output_file
    
    try:
        df = load_dataset(input_path)
        split_dict = split_by_column(df, column_name)
        save_pickle(split_dict, output_path)
        
        print(f"Dictionary contains {len(split_dict)} keys")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return

if __name__ == "__main__":
    main()