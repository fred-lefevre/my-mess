document.addEventListener('DOMContentLoaded', function () {
    const CLE_STOCKAGE = 'compteur';
    const resultat = document.getElementById('message');
    const btnClic = document.getElementById('btn_clic');
    const btnRAZ = document.getElementById('btn_raz');
    let nbClic = parseInt(sessionStorage.getItem(CLE_STOCKAGE)) || 0;

    const actualiserCompteur = function (valeur) {
        sessionStorage.setItem(CLE_STOCKAGE, valeur);
        resultat.textContent = valeur;
    }

    actualiserCompteur(nbClic);

    btnClic.addEventListener('click', function () {
        nbClic++;
        actualiserCompteur(nbClic);
    });

    btnRAZ.addEventListener('click', function () {
        nbClic = 0;
        actualiserCompteur(nbClic);
    });
});