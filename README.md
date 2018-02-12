# Grape
Grape is a library that helps you to create, differentiate and textize functions easily
+ **Grape-based**: Grape variables are dictionary variable type. It consists of coefficients and powers.
+ **Easy I/O**: Grape can get function from user by string and handle that in code. Also you can easily change your grape-type variable to string.
 
# Grammar
Grape use function as follow grammar
## Axn
+ A is coefficient
+ n is power
ex) 5x^8 -> <code>5x8</code>

## Ignore plus and stick minus with number
ex) x^2 - x + 4 -> <code>x2 -x 4</code>

### Example
1. 3x^2 - 2x + 1 ->
<code>3x2 -2x 1</code>
2. 6x^4 - 3x^2 + 2x - 4 ->
<code>6x4 -3x2 2x -4</code>
    
# Api Reference
### Grape variable
    var_dic = {'a': 1, 'n': 1}
    var_list = [var_dic]  
    grape = {'variables': [], 'const': 0}
> All grapes have same keys('variables' and 'const')

+ ### extract_function()
  This function changes string type function to grape type variable.
    extract_function(_input)
  > `_input` should be string type that followed grape grammars
   ```{.python}
   _input = '3x2 2x 1'
   print(extract_function(_input))
  
   => {'variables': [{'a': 3.0, 'n': 2.0}, {'a': 2.0, 'n': 1.0}], 'const': 1.0}
   ```
