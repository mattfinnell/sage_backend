from typing import List
import urllib3

import zxingcpp
import cv2
import numpy as np


class JobHandler:
    pass


class BarcodeHandler(JobHandler):
    def __init__(self, http_pool_manager: urllib3.PoolManager):
        self._http_pool_manager = http_pool_manager

    def handle(self, url):
        # 1) Get Image From URL
        image_response = self._http_pool_manager.request("GET", url)

        numpy_representation = np.frombuffer(image_response.data, dtype=np.uint8)

        image = cv2.imdecode(numpy_representation, cv2.IMREAD_ANYCOLOR)

        # 2) Scan Barcode on Image
        results: List[zxingcpp.Result] = zxingcpp.read_barcodes(image)
        barcode_id = results[0].text

        # 3) Call Barcode API for Product Information
        barcode_lookup_url = f"https://world.openfoodfacts.org/api/v2/product/{barcode_id}.json"

        barcode_response = self._http_pool_manager.request("GET", barcode_lookup_url)

        # 4) Perform Sentiment Analysis / Regression on each Ingredient

        # 5) Return Results
        return barcode_response.json()


class BarcodeHandlerFactory:
    @staticmethod
    def get():
        return BarcodeHandler(urllib3.PoolManager())
