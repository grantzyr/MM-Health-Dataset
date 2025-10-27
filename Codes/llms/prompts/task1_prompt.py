"""
Text Only
"""
TASK1_TEXT = """ 
ARTICLE CONTENT:
```
{article_content}
```
Please analyze the provided article to determine whether the content of the article is real information or misinformation.

article_type: "real_information" or "misinformation"
"""

TASK1_TEXT_FOR_NOT_OPENAI = """ 
ARTICLE CONTENT:
```
{article_content}
```
Please analyze the provided article to determine whether the content of the article is real information or misinformation.

article_type: "real_information" or "misinformation"

You need to return in JSON format only, such as {{"article_type": "real_information"}}.
"""

TASK1_TEXT_FOR_NOT_OPENAI_V2 = """ 
ARTICLE CONTENT:
```
{article_content}
```
Please analyze the provided article to determine whether the content of the article is real information or misinformation.

ONLY choice article type between <real_information> and <misinformation>.
ONLY return ONE LABEL: <real_information> or <misinformation>, DO NOT EXPLAIN, DO NOT ADD ANYTHING ELSE.
"""

TASK1_TEXT_FOR_NOT_OPENAI_V3 = """
ARTICLE CONTENT:
```
{article_content}
```
Please analyze the provided article to determine whether the content of the article is real information or misinformation.

ONLY choose ONE of the following options: <real_information> or <misinformation>, DO NOT EXPLAIN or ADD ANYTHING ELSE.
"""

TASK1_TEXT_FOR_NOT_OPENAI_V4 = """
ARTICLE CONTENT:
```
{article_content}
```
Determine whether the content of the article is real information or misinformation.

ONLY choose ONE of the following options: <real_information> or <misinformation>, DO NOT EXPLAIN or ADD ANYTHING ELSE.
"""

""" 
Text and Image
"""
TASK1_TEXT_IMAGE = """ 
ARTICLE CONTENT:
```
{article_content}
```
Please analyze the provided article and the images within the article to determine whether the content of the article and images is real information or misinformation.

article_type: "real_information" or "misinformation"
"""


TASK1_TEXT_IMAGE_FOR_NOT_OPENAI = """ 
ARTICLE CONTENT:
```
{article_content}
```
Please analyze the provided article and the images within the article to determine whether the content of the article and images is real information or misinformation.

article_type: "real_information" or "misinformation"

You need to return in JSON format only, such as {{"article_type": "real_information"}}.
"""

TASK1_TEXT_IMAGE_FOR_NOT_OPENAI_V2 = """ 
ARTICLE CONTENT:
```
{article_content}
```
Please analyze the provided article and the images to determine whether the content of the article and images is real information or misinformation.

ONLY choice article type between <real_information> and <misinformation>.
ONLY return ONE LABEL: <real_information> or <misinformation>, DO NOT EXPLAIN, DO NOT ADD ANYTHING ELSE.
"""

TASK1_TEXT_IMAGE_FOR_NOT_OPENAI_V3 = """
ARTICLE CONTENT:
```
{article_content}
```
Please analyze the provided article and the images to determine whether the content of the article and images is real information or misinformation.

ONLY choose ONE of the following options: <real_information> or <misinformation>, DO NOT EXPLAIN or ADD ANYTHING ELSE.
"""

TASK1_TEXT_IMAGE_FOR_NOT_OPENAI_V4 = """
ARTICLE CONTENT:
```
{article_content}
```
Determine whether the content of the article and images are real information or misinformation.

ONLY choose ONE of the following options: <real_information> or <misinformation>, DO NOT EXPLAIN or ADD ANYTHING ELSE.
"""