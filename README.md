# scope-simulator

Interpretador com simulação de escopo estático e dinâmico

## Como executar
```
pip install -r requirements.txt
python3 main.py --scoping [static|dynamic] <file>
```

Atenção: Após alterar a gramática, será necessário gerar novamente o Parser, Lexer e Visitor. Para isso, execute o seguinte comando:

```
antlr4 -Dlanguage=Python3 Poodle.g4 -o parser
```

