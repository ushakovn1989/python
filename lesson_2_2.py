original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for ind, obj in enumerate(original_list):
    if obj.isdigit():
        original_list[ind] = f'"{int(obj):02}"'
    elif obj[1:].isdigit():
        original_list[ind] = f'"{int(obj):+03}"'
print(' '.join(original_list))
