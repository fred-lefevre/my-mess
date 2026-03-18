function bonjour() {
    const prenom = prompt('Quel est ton prénom ?');
    const p = document.getElementById('msg');

    if (prenom !== null && prenom != "") {
        p.textContent = 'Ca va ' + prenom + ' ?';
    } else {
        p.textContent = 'Pourquoi ne rien saisir ou cliquer sur "Annuler" ?';
    }
}

window.addEventListener('load', bonjour);