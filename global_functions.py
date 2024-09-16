from fastapi import UploadFile
import os
import numpy as np


def convert_numpy_to_python(results):
    python_results = []
    for result in results:
        python_result = []
        for item in result:
            if isinstance(item, np.ndarray):
                python_result.append(item.tolist())
            elif isinstance(item, (np.generic, np.integer, np.floating)):
                python_result.append(item.item()) 
            else:
                python_result.append(item)
        python_results.append(python_result)
    return python_results


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