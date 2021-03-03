#!/usr/bin/env python3
import cgi
import text_similarity

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "ИИ - наш друг, и он был дружелюбным.")
text2 = form.getfirst("TEXT_2", "ИИ и люди всегда были дружелюбны.")

cos_tf, cos_tf_idf, jaccard_sim, len1, len2, intersection = text_similarity.result(text1, text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Проверка схожести текстов</title>
            <link rel="shortcut icon" href="../doge.ico" type="image/x-icon">
        </head>
        <body style=\"background-color: yellow;\">""")
print("<div style=\"border: 3px solid #000;\">")
print("<h1 align=\"center\">Проверка естественности текста:</h1>")
print("<p align=\"center\">Первый текст: {}</p>".format(text1))
print("<p align=\"center\">Второй текст: {}</p>".format(text2))
print("<p align=\"center\">Слов в первом тексте: {}</p>".format(len1))
print("<p align=\"center\">Слов во втором тексте: {}</p>".format(len2))
print("<p align=\"center\">Слов встречающихся в обоих текстах: {}</p>".format(intersection))
print("<p align=\"center\">Схожесть текстов основываясь на Косинусном подобии по TF: {}</p>".format(cos_tf))
print("<p align=\"center\">Схожесть текстов основываясь на Косинусном подобии по TF-IDF: {}</p>".format(cos_tf_idf))
print("<p align=\"center\">Схожесть текстов основываясь на мере Jacсard: {}</p>".format(jaccard_sim))
print("</div>")
print("<div style=\"font-size:20px;\">")
print("<p><u><b>Jaccard measure</b></u> Сходство Жаккара или пересечение по объединению определяется как размер пересечения, деленный на размер объединения двух множеств.</p>")
print("<p><u><b>Косинусное подобие</b></u> вычисляет подобие, измеряя косинус угла между двумя векторами.</p>")
print("<p><u><b>TF</b></u> (term frequency — частота слова) — отношение числа вхождений некоторого слова к общему числу слов документа. </p>")
print("<p><u><b>IDF</b></u> (inverse document frequency — обратная частота документа) — инверсия частоты, с которой некоторое слово встречается в документах коллекции. </p>")
print("<p><u><b>TF-IDF=TF * IDF</b></u>  для каждого элемента вектора </p><br>")
print("</div>")

