from datetime import date
import inspect
import os
from pathlib import Path

def deneme1234():
    def inner_func():
        folderPath =os.path.join(os.getcwd(), "day5homework2", str(date.today()))
        Path(folderPath).mkdir(exist_ok=True)
        print(inspect.currentframe().f_back.f_code.co_name)

    inner_func()

deneme1234() # deneme