
from flask import Flask
from model import model_train

app = Flask(__name__)
# route the retrn data
@app.route("/", methods=["GET"])
def api_fun():
    # call RFmodel
    dict_out = model_train()
    return {
        'train_features': dict_out["train_features"],
        'train_labels': dict_out["train_labels"],
        'test_features': dict_out["test_features"],
        'test_labels': dict_out["test_labels"]
    }

if __name__ == "__main__":
    app.run()