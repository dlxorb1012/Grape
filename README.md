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
> Grape variable should have **'variables'** and **'const'** keys
> Grape['variables']'s elements should have **'a'** and **'n'** keys

+ ### extract_function()
This function needs grape-grammar-based string type function. Returns grape type variable.
#### Input: string. Return: dictionary.
   extract_function(_input)
  > `_input` should be string type that followed grape grammars
  
   _input = '3x2 2x 1'
   print(extract_function(_input))
   
   => {'variables': [{'a': 3.0, 'n': 2.0}, {'a': 2.0, 'n': 1.0}], 'const': 1.0} # 3x^2 + 2x + 1
   
 + ### derivative_function()
 This function needs grape type variable. Returns derivatived grape type variable
 #### Input: dictionary. Output: dictionary.
     ```{.python}
     derivative_function(original_func_grape)
     ```
 > `original_func_grape` should be grape(dictionary) type
 
     ```{.python}
     original_grape = {'variables': [{'a': 3.0, 'n': 2.0}, {'a': 2.0, 'n': 1.0}], 'const': 1.0} # 3x^2 + 2x + 1
     print(derivative_function(original_grape))
     
     => {'variables': [{'n': 1.0, 'a': 6.0}, {'n': 0.0, 'a': 2.0}], 'const': 0} # 6x + 2
     ```
 
 + ### execute_function()
 This function needs grape type variable and float type x. Returns float type function value of x
 #### Input: dictionary, float or int. Output: float or int.
     ```{.python}
     execute_function(function_grape, x)
     ```
 > `function_grape` should be grape(dictionary) type, `x` should be int or float type
 
     ```{.python}
     func_grape = {'variables': [{'n': 1.0, 'a': 6.0}, {'n': 0.0, 'a': 2.0}], 'const': 0} # 6x + 2
     print(execute_function(func_grape, 3))
     
     => 20.0
     
## Thank you
