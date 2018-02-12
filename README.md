# Grape
Grape is a library that helps you to create, differentiate and textize functions easily
+ **Grape-based**: Grape variables are dictionary variable type. It consists of coefficients and powers.
+ **Easy I/O**: Grape can get function from user by string and handle that in code. Also you can easily change your grape-type variable to string.
 
# Grammar
Grape use function as follow grammar
## Axn
+ A is coefficient
+ n is power

## Ignore plus and stick minus with number
ex) x^2 - x + 4
    x2 -x 4

### Example
1. 3x^2 - 2x + 1
<code>3x2 -2x 1</code>
    
# Api Reference
### Grape variable
    var_dic = {'a': 1, 'n': 1}
    var_list = [var_dic]  
    grape = {'variables': [], 'const': 0}
> All grapes have same keys('variables' and 'const')

+ ### extract_function()
      extract_function(_input)
  > 
