# Cardápio Brasilis Gourmet

Cardápio com pedido pelo WhatsApp. O site inteiro fica em `docs/` (o GitHub Pages publica essa pasta para a prévia).

- Editar produtos, preços e WhatsApp: bloco `CONFIGURAÇÃO` no fim de `docs/index.html` (nome e descrição de cada pizza em pt, en, es, fr).
- Idiomas: segue o idioma do aparelho (pt, en, es, fr; qualquer outro → inglês). Textos no objeto `I18N`. Forçar um idioma: `?lang=es`.
- Seletor de idioma no rodapé: só para a apresentação. Em produção, `SELETOR_IDIOMA = false`.
- A mensagem do pedido no WhatsApp sai sempre em português, com a linha "Idioma do cliente" quando não for pt.
- Fotos: `docs/img/<id>.jpg`. Vídeos: `docs/video/<id>.mp4`.

## Rodar local

```
pip install flask
python app.py
```

## PythonAnywhere

1. `git clone` este repositório em `/home/<usuario>/brasilis-cardapio`.
2. Web > Add a new web app > Manual configuration > Python 3.x.
3. No arquivo WSGI: `import sys; sys.path.insert(0, "/home/<usuario>/brasilis-cardapio")` e `from app import app as application`.
4. (Opcional, mais rápido) Web > Static files: `/img/` → `.../brasilis-cardapio/docs/img/` e `/video/` → `.../brasilis-cardapio/docs/video/`.
5. Reload.
