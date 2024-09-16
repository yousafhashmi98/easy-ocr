from fastapi import UploadFile
import os


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