from django.apps import AppConfig
import joblib
import pytesseract
import cv2
from pytesseract import Output


model = joblib.load('D:\\proj\\iris\\knn_model.pkl')


class IrisConfig(AppConfig):
    name = 'iris'
