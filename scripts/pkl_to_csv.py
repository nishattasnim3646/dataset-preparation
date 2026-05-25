import pickle
import pandas as pd
import os
import numpy as np

# পাথ সেট করো
base_dir = "/home/nishat/Desktop/denovo/dataset1Github/submission"
splits_dir = os.path.join(base_dir, "data/splits")
output_dir = os.path.join(base_dir, "data/splits/csv")

os.makedirs(output_dir, exist_ok=True)

files = {
    "by_country.pkl": "by_country",
    "by_institute.pkl": "by_institute",
    "by_strain.pkl": "by_strain"
}

for pkl_file, name in files.items():
    pkl_path = os.path.join(splits_dir, pkl_file)
    
    with open(pkl_path, "rb") as f:
        data_dict = pickle.load(f)
    
    # সবগুলো গ্রুপকে একসাথে একটা বড় DataFrame বানাই
    all_dfs = []
    for key, df in data_dict.items():
        df = df.copy()
        
        # NaN / খালি সেল গুলোকে 'NA' দিয়ে পূরণ করো
        df = df.fillna('NA')
        df = df.replace('', 'NA')        # যদি কোনো খালি স্ট্রিং থাকে
        df = df.replace(' ', 'NA')       # যদি শুধু স্পেস থাকে
        
        # গ্রুপ কী যোগ করো
        df['group_key'] = key
        
        all_dfs.append(df)
    
    final_df = pd.concat(all_dfs, ignore_index=True)
    
    csv_path = os.path.join(output_dir, f"{name}.csv")
    final_df.to_csv(csv_path, index=False)
    
    print(f"✅ Created: {csv_path} | Rows: {len(final_df)} | NaN values filled with 'NA'")