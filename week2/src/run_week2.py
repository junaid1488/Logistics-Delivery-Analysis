from quality_report import main as quality_main
from clean_data import main as clean_main
from preprocess_for_modeling import main as modeling_main

if __name__ == "__main__":
    print("=== WEEK 2: QUALITY REPORT ===")
    quality_main()
    print("\n=== WEEK 2: CLEANING ===")
    clean_main()
    print("\n=== WEEK 2: MODEL-READY PREPROCESSING CHECK ===")
    modeling_main()
