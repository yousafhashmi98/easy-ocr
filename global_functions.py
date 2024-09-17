from fastapi import UploadFile
import os
import numpy as np


# def convert_numpy_to_python(results):
#     def convert_item(item):
#         if isinstance(item, np.ndarray):
#             return item.tolist()
#         elif isinstance(item, (np.generic, np.integer, np.floating)):
#             return item.item()  
#         elif isinstance(item, list):
#             return [convert_item(sub_item) for sub_item in item]
#         else:
#             return item
#     return [convert_item(result) for result in results]

def convert_numpy_to_python(results):
    converted_data = []
    for item in results:
        coordinates, text, score = item
        coordinates = [[int(x), int(y)] for [x, y] in coordinates]
        score = float(score)
        converted_data.append((coordinates, text, score))
    return converted_data


def write_file(file:UploadFile):
    try:
        parentDirectory = 'static/temp'
        filename = file.filename
        content = file.file.read()
        if not os.path.exists(parentDirectory):
            os.makedirs(parentDirectory)
            
        final_file_path = f"{parentDirectory}/{filename}"
        try:
            with open(final_file_path,'wb') as f:
                f.write(content)
        except Exception:
            os.remove(final_file_path)
            return False
        finally:
            file.file.close
            return final_file_path
    except Exception as e:
        print(str(e))
        return False