## Data Sources
The dataset(data/dataset.xlsx) was compiled from the following source files:
1. [cryptic_metadata.xlsx] - country, institution, strain info of each sequence_id
   - Link: `sources/cryptic_metadata.xlsx`
   - Rows: 6224
   - Columns: 4

2. [cryptic_phenotype.xlsx] - drug resistance data of 13 antibiotics against each sequence_id
   - Link: `sources/cryptic_phenotype.xlsx`
   - Rows: 6224
   - Columns: 14

3. [genome_sequence.sh] - script to download 2 strains each for all of 6224 genome sequences
   - Link: `sources/genome_sequence.sh`
   - downloading command: 6224*2



## Sequence ID Validation
- Total sequences processed: 6,224
- Sequence ID collisions: 0 (all unique)
- Missing metadata (country/institute/strain): 0 




## Missing Data by Drug:
| Drug        | Missing Values| % Complete |
|-------------|---------------|------------|
| Amikacin    |      55       | 99.1%      |
| Bedaquiline |     120       | 98.1%      |
| Clofazimine |      94       | 98.5%      |
| Delamanid   |     124       | 98.0%      |
| Ethambutol  |      41       | 99.3%      |
| Ethionamide |      88       | 98.6%      |
| Isoniazid   |      58       | 99.1%      |
| Kanamycin   |      86       | 98.6%      |
| Levofloxacin|      54       | 99.1%      |
| Linezolid   |      29       | 99.5%      |
| Moxifloxacin|      44       | 99.3%      |
| Rifampicin  |      54       | 99.1%      |
| Rifabutin   |      50       | 99.2%      |
--------------------------------------------
Note: Missing values are coded as `NA` (Not Available/Not Tested)



## Resistance Label Standardized Convention
| Original Label | Standardized Label | Description |
|----------------|--------------------|-------------|
|       S        |         S          | Susceptible |
|       R        |         R          | Resistant   |
|      NA        |        NA          | Not Tested  |
| Intermediate   |         R          | Treated as  |
|                |                    |   Resistant |
-----------------------------------------------------   
- All resistance columns (Amikacin, Bedaquiline, Clofazimine, Delamanid, Ethambutol, Ethionamide, Isoniazid, Kanamycin, Levofloxacin, Linezolid, Moxifloxacin, Rifampicin, Rifabutin) follow this convention
- Standardization applied consistently across all source files
- No data loss during standardization




## File Structure
dataset#1/
├── data/
│   ├── dataset.xlsx                    # Original dataset (required)
│   └── splits/                         # Generated pickle files
│       ├── by_country.pkl
│       ├── by_institute.pkl
│       └── by_strain.pkl
|       └── csv(optional)               #extra csv files for better visiblity of data splitting
|          ├── by_country.csv
│          ├── by_institute.csv
│          └── by_strain.csv
|
├── scripts/
│   ├── split_dataset.py                # Main splitting script
│   └── (optional) pkl_to_csv.py        # Extra conversion script
└── README.md                           # Project documentation