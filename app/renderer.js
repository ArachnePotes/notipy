const mark = require('marked')
const markdownView = document.querySelector('#markdown'); // Seleccionar el textarea con el id "markdown"
const htmlView = document.querySelector('#html'); // Seleccionar el elemento html

const renderToMarkdown = (markdown) => {
    htmlView.innerHTML = mark.parse(markdown, { sanitize:true });
}

markdownView.addEventListener('keyup', e => {
    const currentContent = e.target.value; // Imprimir el valor del textarea al escribir
    renderToMarkdown(currentContent)
});
