from train_model import main as train
from evaluate_model import main as evaluate
from model_interpretation import main as interpret
from optimization import main as optimize

if __name__ == "__main__":
    train()
    evaluate()
    interpret()
    optimize()
    print("\nWeek 4 pipeline completed.")
