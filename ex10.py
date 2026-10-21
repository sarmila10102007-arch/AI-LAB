import pandas as pdfrom sklearn.model_selection import train_test_splitfrom sklearn.ensemble import RandomForestClassifierfrom sklearn.metrics import accuracy_score
# Sample sign language datasetdata = {
    "finger1": [1, 1, 0, 0, 1, 0, 1, 0, 1, 0,
                1, 0, 1, 0, 1, 0, 1, 0, 1, 0],

    "finger2": [1, 0, 1, 0, 1, 1, 0, 0, 1, 1,
                0, 1, 0, 1, 0, 1, 0, 1, 0, 1],

    "finger3": [0, 1, 1, 0, 0, 1, 1, 0, 1, 0,
                0, 1, 1, 0, 0, 1, 1, 0, 1, 0],

    "gesture": [
        "A", "B", "C", "D", "A",
        "B", "C", "D", "A", "B",
        "C", "D", "A", "B", "C",
        "D", "A", "B", "C", "D"
    ]
}
df = pd.DataFrame(data)
# Input and outputX = df[["finger1", "finger2", "finger3"]]y = df["gesture"]
# Split dataX_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Create AI modelmodel = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
# Train modelmodel.fit(X_train, y_train)
# Test modely_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("===================================")print(" AI BASED SIGN LANGUAGE SYSTEM")print("===================================")print("Model Accuracy:", round(accuracy * 100, 2), "%")
# User inputprint("\nEnter Hand Gesture Features")
finger1 = int(input("Finger 1 (0/1): "))finger2 = int(input("Finger 2 (0/1): "))finger3 = int(input("Finger 3 (0/1): "))
# Predictionnew_data = pd.DataFrame({
    "finger1": [finger1],
    "finger2": [finger2],
"finger3": [finger3]

})

prediction = model.predict(new_data)
print("\n-----------------------------------")print("Predicted Sign:", prediction[0])print("-----------------------------------")
