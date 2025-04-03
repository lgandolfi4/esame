import os
import sys
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path

import logging
from src import config
from src.load_data import load_data
from src.make_model import train_model
from src.make_model import train_model_bonus
# from src.evaluation import evaluate_model
# from src.save_results import save_predictions

# Set up logging
logging.basicConfig(filename='../logs/pipeline.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Starting Sentiment Analysis Pipeline...")

    # Step 1: Load data from Excel and store it in SQLite
    logging.info("Loading raw data...")
    load_data()

    # Step 3: Train model
    logging.info("Training the model...")
    train_model()
    train_model_bonus()

    # Messaggio di fine run
    logging.info("Finito!!")

if __name__ == "__main__":
    main()