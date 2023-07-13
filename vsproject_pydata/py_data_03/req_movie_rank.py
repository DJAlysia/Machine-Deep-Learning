

print(subject)

start_list = html_data.find('<div class="isKeyword">')
end_list = html_data.find('<form id = "frmKeyword"')
# print(start_list, '~', end_list)
html_list = html_data[start_list:end_list]
# print(html_list)
html_li_item = html_list.split('<li>')
Length = len(html_li_item)
pattern3 = '<span class="num_rank".*/span>'
for li in range(1, Length):
    mat = re.search(pattern3, li)