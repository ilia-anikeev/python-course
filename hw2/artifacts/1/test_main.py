from latex_generator_lib import latex_table

def create_example_data():
    """Создает пример данных для генерации LaTeX таблицы."""
    return [
        ["Город", "Страна", "Население", "Год основания"],
        ["Москва", "Россия", "12 млн", "1147"],
        ["Париж", "Франция", "2,1 млн", "52 до н.э."],
        ["Токио", "Япония", "14 млн", "1457"],
    ]

def create_latex_document(table_data):
    """Формирует документ LaTeX для заданных данных таблицы."""
    latex_parts = [
        "\\documentclass{article}",
        "\\usepackage[utf8]{inputenc}",
        "\\usepackage[english,russian]{babel}",
        "\\begin{document}",
        latex_table(table_data),
        "\\end{document}",
    ]
    return "\n".join(latex_parts)

def save_to_file(content, filename):
    """Сохраняет содержимое в файл."""
    with open(filename, "w") as file:
        file.write(content)

def main():
    example_data = create_example_data()
    latex_document = create_latex_document(example_data)
    save_to_file(latex_document, "example.tex")

if __name__ == "__main__":
    main()
