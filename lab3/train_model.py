import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train():
    # Загрузка данных
    X = pd.read_csv("data.csv")
    y = pd.read_csv("target.csv")
    
    # Разделение на train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Обучение модели
    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train.values.ravel())
        
        # Логирование метрик
        accuracy = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", accuracy)
        
        # Сохранение модели
        mlflow.sklearn.log_model(model, "model")
        print(f"Модель обучена! Точность: {accuracy:.2f}")

if __name__ == "__main__":
    train()
