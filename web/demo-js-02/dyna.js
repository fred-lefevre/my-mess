const inputPre = document.getElementById('pre');
const p = document.getElementById('msg');
const btnValider = document.getElementById('validerBtn');
const btnEffacer = document.getElementById('effacerBtn');

function bonjour() {
    const prenom = inputPre.value;

    if (prenom != "") {
        p.textContent = 'Ca va ' + prenom + ' ?';
    } else {
        p.textContent = 'Pourquoi ne rien saisir ?';
    }
    btnEffacer.disabled = false;
}

function remiseAZero() {
    p.textContent = "";
    btnEffacer.disabled = true;
    inputPre.value = "";
    inputPre.focus();
}

btnValider.addEventListener('click', bonjour);
btnEffacer.addEventListener('click', remiseAZero);
