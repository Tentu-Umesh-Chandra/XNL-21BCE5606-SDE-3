import pandas as pd
from fbprophet import Prophet

class PredictiveAnalytics:
    def __init__(self):
        self.model = Prophet()

    def train_model(self, data):
        self.model.fit(data)

    def predict_trend(self, future_periods):
        future = self.model.make_future_dataframe(periods=future_periods)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
