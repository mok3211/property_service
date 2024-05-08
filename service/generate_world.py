import os
from docx import Document


current_path = os.path.abspath(__file__)
docx_template_path = os.path.join(os.path.dirname(current_path), "docx_template")

class GenerateWorld(object):

    def __init__(self) -> None:
        self.template_docx = None
        self.template_docx_name = None
        pass

    def chose_template(self) -> str:
        

        return self.template_docx_name

    def check_data(self) -> bool:
        pass

    def start_generate_world(self) -> bool:
        # 根据文档位置加载数据并生成副本后保存文档
        now_docx = Document(docx_template_path)
        


        return True
        