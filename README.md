# Divisor de linhas para Sublime
Treino para programar em Python e ao mesmo tempo criar um plugin para Sublime.

Devido a limitação de argumentos que um campo (do filtro do BI onde trabalho) impôe, sou obrigado a efetuar agrupamentos de no máximo 1000 valores por sentença. Este plugin no Sublime me permitirá acelerar o agrupamento.

Exemplo Dado:
```
123456
654321
459456
365448
653264
154864
999855
875455
123545
845954
553267
```

Aplicando Plugin, para agrupamento de 3 valores:
```
123456;654321;459456
365448;653264;154864
999855;875455;123545
845954;553267
```

O mesmo grupo, para agrupamento de 5 valores:
```
123456;654321;459456;365448;653264
154864;999855;875455;123545;845954
553267;
```

# Key mapping
Foi utilizado "ctrl+alt+l", ver arquivo "Default (Windows).sublime-keymap"

# TO-DO
Aplicar a modificação apenas na seleção feita, atualmente está utilizando todo o documento!