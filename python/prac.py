"""
input: Randompara
output: Words: number


"""
import lorem
paragraph = lorem.paragraph()

para= paragraph.split(' ')
print(f"Words: {len(para)}")
