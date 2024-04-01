function toggleButtons() {
    var btnAdicionar = document.getElementById('btnAdicionar');
    var btnRemover = document.getElementById('btnRemover');

    if (btnAdicionar.style.display === 'none') {
        btnAdicionar.style.display = 'block';
        btnRemover.style.display = 'none';
    } else {
        btnAdicionar.style.display = 'none';
        btnRemover.style.display = 'block';
    }
}

function cloneContainer() {
    // Seleciona a div original
    var rows = document.getElementById('rows');

    // Clona o elemento
    var clone = rows.cloneNode(true);

    // Adiciona o clone após a div original
    rows.parentNode.insertBefore(clone, rows.nextSibling);
}