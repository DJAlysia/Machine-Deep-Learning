# 문제 5 다음 html 코드에서 <option> 안에 텍스트만 추출하여 출력하시오

import re

html = '''
<label for="dog-names">Choose a dog name:</label>
<select name="dog-names" id="dog-names">
<option value="rigatoni">Rigatoni</option>
<option value="dave">Dave</option>
<option value="pumpernickel">Pumpernickel</option>
<option value="reeses">Reeses</option>
</select>
'''

pattern = "<option.*?>(.*?)<\/option>"

matches = re.findall(pattern, html)

for text in matches:
    print(text)