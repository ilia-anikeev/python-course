from latex_generator_lib import latex_image, latex_table

def initialize_latex_doc():
    """Инициализирует основную структуру LaTeX документа."""
    return [
        "\\documentclass{article}",
        "\\usepackage{graphicx}",
        "\\usepackage{booktabs}",
        "\\usepackage{array}",
        "\\usepackage[utf8]{inputenc}",
        "\\usepackage[english,russian]{babel}",
        "\\begin{document}"
    ]

def finalize_latex_doc():
    """Завершает LaTeX документ."""
    return "\\end{document}"

def add_tables_to_doc(table_data, document_parts):
    """Добавляет таблицы в документ."""
    for table in table_data:
        document_parts.append(latex_table(table))
        document_parts.append("")

def add_images_to_doc(image_data, document_parts):
    """Добавляет изображения в документ."""
    for img_path, img_width, img_height in image_data:
        document_parts.append(latex_image(img_path, img_width, img_height))
        document_parts.append("")

def compile_latex_document(table_data=None, image_data=None, destination=None):
    """
    Создаёт LaTeX файл с таблицами и изображениями и сохраняет его.

    :param table_data: Коллекция данных для вставки в таблицы.
    :param image_data: Коллекция данных для добавления изображений.
    :param destination: Путь сохранения LaTeX файла.
    """
    table_data = table_data or []
    image_data = image_data or []

    document_parts = initialize_latex_doc()

    add_tables_to_doc(table_data, document_parts)
    add_images_to_doc(image_data, document_parts)
    
    document_parts.append(finalize_latex_doc())

    with open(destination, "w") as output:
        output.write("\n".join(document_parts))

def fetch_sample_data():
    """Получает набор данных для демонстрации."""
    return ([
        [
            ["Страна", "Столица", "Население", "Площадь (кв.км)"],
            ["Франция", "Париж", "65 миллионов", "643,801"],
            ["Испания", "Мадрид", "47 миллионов", "505,990"],
            ["Италия", "Рим", "60 миллионов", "301,340"]
        ]
    ], [
        ("img.png", 200, 150),
    ])

def execute():
    """Запускает процесс генерации LaTeX документа."""
    tables, images = fetch_sample_data()
    compile_latex_document(table_data=tables, image_data=images, destination="../resources/example.tex")

if __name__ == "__main__":
    execute()
